"""Testes determinísticos da biblioteca de referência."""
import math
import unittest
from volatility_reference import (
    OHLC, atr_sma, atr_wilder, closes_from_bars, compare_estimators,
    garman_klass_variance, log_returns, parkinson_variance,
    realized_variance, realized_volatility, rogers_satchell_variance,
    synthetic_gbm_ohlc, true_ranges,
)

class TestReturnsAndRV(unittest.TestCase):
    def test_log_returns_known_values(self):
        result = log_returns([100.0, 110.0, 100.0])
        self.assertAlmostEqual(result[0], math.log(1.1), places=12)
        self.assertAlmostEqual(result[1], math.log(100 / 110), places=12)

    def test_rv_known_values(self):
        expected = math.log(1.1) ** 2 + math.log(100 / 110) ** 2
        self.assertAlmostEqual(realized_variance([100.0, 110.0, 100.0]), expected, places=12)
        self.assertAlmostEqual(realized_volatility([100.0, 110.0, 100.0]), math.sqrt(expected), places=12)

    def test_invalid_prices_fail_closed(self):
        for prices in ([], [100.0], [100.0, 0.0], [100.0, -1.0], [100.0, float("nan")]):
            with self.subTest(prices=prices), self.assertRaises(ValueError):
                realized_variance(prices)

class TestOHLCAndATR(unittest.TestCase):
    def setUp(self):
        self.flat = [OHLC(100.0, 100.0, 100.0, 100.0)] * 20
        self.bars = [
            OHLC(100.0, 103.0, 99.0, 102.0),
            OHLC(102.0, 104.0, 100.0, 101.0),
            OHLC(101.0, 105.0, 100.5, 104.0),
        ]

    def test_flat_series_estimators_zero(self):
        self.assertEqual(parkinson_variance(self.flat), 0.0)
        self.assertEqual(garman_klass_variance(self.flat), 0.0)
        self.assertEqual(rogers_satchell_variance(self.flat), 0.0)
        self.assertEqual(atr_sma(self.flat, 14), 0.0)
        self.assertEqual(realized_variance(closes_from_bars(self.flat)), 0.0)

    def test_true_range_and_atr(self):
        self.assertEqual(true_ranges(self.bars), [4.0, 4.0, 4.5])
        self.assertAlmostEqual(atr_sma(self.bars, 2), 4.25)
        values = atr_wilder(self.bars, 2)
        self.assertEqual(len(values), 2)
        self.assertAlmostEqual(values[0], 4.0)
        self.assertAlmostEqual(values[1], 4.25)

    def test_estimators_finite_on_fixture(self):
        values = compare_estimators(self.bars, atr_period=2)
        for name, value in values.items():
            with self.subTest(metric=name):
                self.assertTrue(math.isfinite(value))
                self.assertGreaterEqual(value, 0.0)

    def test_invalid_ohlc_rejected(self):
        with self.assertRaises(ValueError):
            parkinson_variance([OHLC(100.0, 99.0, 98.0, 100.0)])
        with self.assertRaises(ValueError):
            atr_sma(self.bars, 0)
        with self.assertRaises(ValueError):
            atr_sma(self.bars, 10)

class TestSyntheticReproducibility(unittest.TestCase):
    def test_seed_reproducible(self):
        self.assertEqual(synthetic_gbm_ohlc(count=100, seed=123),
                         synthetic_gbm_ohlc(count=100, seed=123))

    def test_different_seed_changes_series(self):
        self.assertNotEqual(synthetic_gbm_ohlc(count=20, seed=123),
                            synthetic_gbm_ohlc(count=20, seed=456))

    def test_estimators_on_synthetic_data(self):
        bars = synthetic_gbm_ohlc(count=250, seed=20261018, volatility_per_bar=0.005)
        values = compare_estimators(bars, atr_period=14)
        self.assertEqual(values["n_bars"], 250.0)
        for name, value in values.items():
            with self.subTest(metric=name):
                self.assertTrue(math.isfinite(value))
                self.assertGreaterEqual(value, 0.0)

if __name__ == "__main__":
    unittest.main(verbosity=2)

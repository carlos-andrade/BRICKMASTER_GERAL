"""Biblioteca de referência isolada para estimadores de volatilidade."""
from __future__ import annotations
from dataclasses import dataclass
from math import log, sqrt, isfinite, exp
from random import Random
from typing import Sequence

@dataclass(frozen=True)
class OHLC:
    open: float
    high: float
    low: float
    close: float

def _finite_positive(values: Sequence[float], label: str) -> None:
    if not values:
        raise ValueError(f"{label}: série vazia")
    if any(not isfinite(v) or v <= 0 for v in values):
        raise ValueError(f"{label}: todos os preços devem ser finitos e positivos")

def log_returns(prices: Sequence[float]) -> list[float]:
    if len(prices) < 2:
        raise ValueError("São necessários pelo menos dois preços")
    _finite_positive(prices, "preços")
    return [log(prices[i] / prices[i - 1]) for i in range(1, len(prices))]

def realized_variance(prices: Sequence[float]) -> float:
    return sum(r * r for r in log_returns(prices))

def realized_volatility(prices: Sequence[float]) -> float:
    return sqrt(realized_variance(prices))

def sample_stddev(returns: Sequence[float]) -> float:
    if len(returns) < 2 or any(not isfinite(r) for r in returns):
        raise ValueError("São necessários pelo menos dois retornos finitos")
    mean = sum(returns) / len(returns)
    return sqrt(sum((r - mean) ** 2 for r in returns) / (len(returns) - 1))

def _validate_bars(bars: Sequence[OHLC]) -> None:
    if not bars:
        raise ValueError("Série OHLC vazia")
    for i, b in enumerate(bars):
        vals = (b.open, b.high, b.low, b.close)
        if any(not isfinite(v) or v <= 0 for v in vals):
            raise ValueError(f"Barra {i}: OHLC deve ser finito e positivo")
        if b.high < max(b.open, b.close, b.low) or b.low > min(b.open, b.close, b.high):
            raise ValueError(f"Barra {i}: OHLC inconsistente")

def _nonnegative_variance(value: float, estimator: str) -> float:
    if value < 0:
        raise ValueError(f"{estimator}: variância estimada negativa ({value})")
    return value

def parkinson_variance(bars: Sequence[OHLC]) -> float:
    _validate_bars(bars)
    return sum(log(b.high / b.low) ** 2 for b in bars) / (4.0 * len(bars) * log(2.0))

def parkinson_volatility(bars: Sequence[OHLC]) -> float:
    return sqrt(parkinson_variance(bars))

def garman_klass_variance(bars: Sequence[OHLC]) -> float:
    _validate_bars(bars)
    terms = [0.5 * log(b.high / b.low) ** 2
             - (2.0 * log(2.0) - 1.0) * log(b.close / b.open) ** 2 for b in bars]
    return _nonnegative_variance(sum(terms) / len(bars), "Garman-Klass")

def garman_klass_volatility(bars: Sequence[OHLC]) -> float:
    return sqrt(garman_klass_variance(bars))

def rogers_satchell_variance(bars: Sequence[OHLC]) -> float:
    _validate_bars(bars)
    terms = [log(b.high / b.open) * log(b.high / b.close)
             + log(b.low / b.open) * log(b.low / b.close) for b in bars]
    return _nonnegative_variance(sum(terms) / len(bars), "Rogers-Satchell")

def rogers_satchell_volatility(bars: Sequence[OHLC]) -> float:
    return sqrt(rogers_satchell_variance(bars))

def true_ranges(bars: Sequence[OHLC]) -> list[float]:
    _validate_bars(bars)
    out = []
    for i, b in enumerate(bars):
        if i == 0:
            out.append(b.high - b.low)
        else:
            prev = bars[i - 1].close
            out.append(max(b.high - b.low, abs(b.high - prev), abs(b.low - prev)))
    return out

def atr_sma(bars: Sequence[OHLC], period: int) -> float:
    if period < 1 or len(bars) < period:
        raise ValueError("Período ATR inválido ou amostra insuficiente")
    return sum(true_ranges(bars)[-period:]) / period

def atr_wilder(bars: Sequence[OHLC], period: int) -> list[float]:
    if period < 1 or len(bars) < period:
        raise ValueError("Período ATR inválido ou amostra insuficiente")
    trs = true_ranges(bars)
    result = [sum(trs[:period]) / period]
    for tr in trs[period:]:
        result.append(((period - 1) * result[-1] + tr) / period)
    return result

def synthetic_gbm_ohlc(count: int = 500, seed: int = 20261018, start: float = 100.0,
                       annual_drift: float = 0.0, volatility_per_bar: float = 0.01,
                       intrabar_range_scale: float = 1.0) -> list[OHLC]:
    """GBM aproximado para testes determinísticos; extremos intrabar são sintéticos."""
    if count < 2 or start <= 0 or volatility_per_bar < 0 or intrabar_range_scale < 0:
        raise ValueError("Parâmetros sintéticos inválidos")
    rng = Random(seed)
    bars, prev = [], start
    for _ in range(count):
        opening = prev
        close = opening * exp(annual_drift + volatility_per_bar * rng.gauss(0.0, 1.0))
        high_noise = abs(rng.gauss(0.0, volatility_per_bar * intrabar_range_scale))
        low_noise = abs(rng.gauss(0.0, volatility_per_bar * intrabar_range_scale))
        high = max(opening, close) * exp(high_noise)
        low = min(opening, close) * exp(-low_noise)
        bars.append(OHLC(opening, high, low, close))
        prev = close
    return bars

def closes_from_bars(bars: Sequence[OHLC]) -> list[float]:
    _validate_bars(bars)
    return [bars[0].open] + [b.close for b in bars]

def compare_estimators(bars: Sequence[OHLC], atr_period: int = 14) -> dict[str, float]:
    """RV/OHLC estão na escala dos retornos; ATR está em unidades de preço."""
    closes = closes_from_bars(bars)
    rv = realized_variance(closes)
    return {
        "n_bars": float(len(bars)),
        "rv_variance": rv,
        "rv_volatility": sqrt(rv),
        "parkinson_variance": parkinson_variance(bars),
        "parkinson_volatility": parkinson_volatility(bars),
        "garman_klass_variance": garman_klass_variance(bars),
        "garman_klass_volatility": garman_klass_volatility(bars),
        "rogers_satchell_variance": rogers_satchell_variance(bars),
        "rogers_satchell_volatility": rogers_satchell_volatility(bars),
        "atr_sma_price_units": atr_sma(bars, atr_period),
    }

"""Executa comparação reproduzível; os valores são sintéticos, não dados B3."""
import json
from volatility_reference import compare_estimators, synthetic_gbm_ohlc

def main():
    bars = synthetic_gbm_ohlc(
        count=500, seed=20261018, start=100.0,
        drift_per_bar=0.0, volatility_per_bar=0.005,
        intrabar_range_scale=1.0,
    )
    result = compare_estimators(bars, atr_period=14)
    result["seed"] = 20261018
    result["synthetic_only"] = True
    result["units_note"] = "RV/OHLC estimam escala de retorno; ATR é unidade de preço."
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()

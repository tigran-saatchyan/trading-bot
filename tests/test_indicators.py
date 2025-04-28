import numpy as np
import pandas as pd
import pytest

from trading_bot.analysis.indicators.bollinger import BollingerBands
from trading_bot.analysis.indicators.rsi import RSI
from trading_bot.analysis.indicators.sma import SMA


@pytest.fixture
def df_linear():
    idx = pd.date_range("2025-01-01", periods=100, freq="D")
    price = np.linspace(1, 100, 100)
    df = pd.DataFrame(
        {
            "open": price,
            "high": price + 1,
            "low": price - 1,
            "close": price,
            "volume": np.arange(100),
        },
        index=idx,
    )
    return df


def test_sma(df_linear):
    sma = SMA(window=10)
    result = sma.compute(df_linear)
    assert np.isnan(result.iloc[0])
    assert pytest.approx(result.iloc[9], rel=1e-3) == 5.5


def test_rsi_constant(df_linear):
    rsi = RSI(window=14)
    result = rsi.compute(df_linear)
    assert (result.iloc[-1] > 50) and (result.iloc[-1] < 100)


def test_bollinger_width(df_linear):
    bb = BollingerBands(window=20, std_dev=2.0)
    df_bb = bb.compute(df_linear)
    width = df_bb["bb_upper_20"] - df_bb["bb_lower_20"]
    assert pytest.approx(width.iloc[-1], rel=0.2) > 20

import pandas as pd

from trading_bot.data_processing.market_preprocessor import (
    clean_dataframe,
    resample_ohlcv,
)
from trading_bot.data_sources.stocks.yfinance_connector import (
    fetch_history_yfinance,
)


def test_yfinance_connector(monkeypatch):
    # Patch yf.download
    df_sample = pd.DataFrame(
        {
            "Open": [1, 2],
            "High": [1, 2],
            "Low": [1, 2],
            "Close": [1, 2],
            "Volume": [100, 200],
        },
        index=pd.to_datetime(["2025-01-01", "2025-01-02"]),
    )
    monkeypatch.setattr("yfinance.download", lambda *args, **kwargs: df_sample)
    df = fetch_history_yfinance("AAPL", "2025-01-01", "2025-01-03")
    assert df is not None
    assert list(df.columns) == ["open", "high", "low", "close", "volume"]


def test_preprocessor():
    df = pd.DataFrame(
        {
            "open": [1, 2, None],
            "high": [1, 2, 3],
            "low": [1, 2, 3],
            "close": [1, 2, 3],
            "volume": [10, 20, 30],
        },
        index=pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-03"]),
    )
    clean = clean_dataframe(df)
    assert clean.isna().sum().sum() == 0
    resampled = resample_ohlcv(clean, freq="1D")
    assert "volume" in resampled.columns

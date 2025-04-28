import pandas as pd


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Drop NaNs, enforce column types, sort by index."""
    df = df.dropna()
    df[["open", "high", "low", "close"]] = df[["open", "high", "low", "close"]].astype(
        float
    )
    df["volume"] = df["volume"].astype(int)
    return df.sort_index()


def resample_ohlcv(df: pd.DataFrame, freq: str = "1H") -> pd.DataFrame:
    """Resample to given freq with OHLCV aggregation."""
    ohlc = df["close"].resample(freq).ohlc()
    volume = df["volume"].resample(freq).sum().rename("volume")
    return pd.concat([ohlc, volume], axis=1)

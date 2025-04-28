from typing import Optional

import pandas as pd
import yfinance as yf


def fetch_history_yfinance(symbol: str, start: str, end: str) -> Optional[pd.DataFrame]:
    """
    Fetch OHLCV data from yfinance.
    start/end in "YYYY-MM-DD" format.
    """
    try:
        df = yf.download(symbol, start=start, end=end, progress=False)
        if df.empty:
            print(f"Empty data from yfinance for {symbol}")
            return None
        df = df.rename(
            columns={
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume",
            }
        )
        return df
    except Exception as e:
        print(f"yfinance fetch failed for {symbol}: {e}")
        return None

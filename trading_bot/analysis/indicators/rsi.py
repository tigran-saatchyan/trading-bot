import pandas as pd

from .base import Indicator


class RSI(Indicator):
    """
    Relative Strength Index implemented in pure Python.
    """

    def __init__(self, window: int = 14, column: str = "close"):
        self.window = window
        self.column = column

    def _compute(self, df: pd.DataFrame) -> pd.Series:
        price = df[self.column]
        delta = price.diff()
        up = delta.clip(lower=0)
        down = -delta.clip(upper=0)
        ma_up = up.ewm(span=self.window, adjust=False).mean()
        ma_down = down.ewm(span=self.window, adjust=False).mean()
        rs = ma_up / ma_down
        rsi = 100 - (100 / (1 + rs))
        return rsi.rename(f"rsi_{self.window}")

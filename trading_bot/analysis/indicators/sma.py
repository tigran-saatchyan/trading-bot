import pandas as pd

from .base import Indicator


class SMA(Indicator):
    """
    Simple Moving Average.
    """

    def __init__(self, window: int = 20, column: str = "close"):
        self.window = window
        self.column = column

    def _compute(self, df: pd.DataFrame) -> pd.Series:
        return df[self.column].rolling(self.window).mean().rename(f"sma_{self.window}")

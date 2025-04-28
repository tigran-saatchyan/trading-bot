import pandas as pd
import talib

from .base import Indicator


class EMA(Indicator):
    """
    Exponential Moving Average via ta-lib.
    """

    def __init__(self, window: int = 20, column: str = "close"):
        self.window = window
        self.column = column

    def _compute(self, df: pd.DataFrame) -> pd.Series:
        arr = df[self.column].values
        ema_values = talib.EMA(arr, timeperiod=self.window)
        return pd.Series(ema_values, index=df.index, name=f"ema_{self.window}")

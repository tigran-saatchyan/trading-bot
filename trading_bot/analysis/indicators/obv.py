import pandas as pd

from .base import Indicator


class OBV(Indicator):
    """
    On-Balance Volume.
    """

    def _compute(self, df: pd.DataFrame) -> pd.Series:
        close = df["close"]
        vol = df["volume"]
        direction = (
            close.diff().fillna(0).apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
        )
        obv = (direction * vol).cumsum()
        return obv.rename("obv")

import pandas as pd

from .base import Indicator


class BollingerBands(Indicator):
    """
    Bollinger Bands: upper, middle, lower.
    """

    def __init__(self, window: int = 20, std_dev: float = 2.0, column: str = "close"):
        self.window = window
        self.std_dev = std_dev
        self.column = column

    def _compute(self, df: pd.DataFrame) -> pd.DataFrame:
        series = df[self.column]
        sma = series.rolling(self.window).mean()
        std = series.rolling(self.window).std()
        upper = sma + self.std_dev * std
        lower = sma - self.std_dev * std
        return pd.DataFrame(
            {
                f"bb_upper_{self.window}": upper,
                f"bb_middle_{self.window}": sma,
                f"bb_lower_{self.window}": lower,
            },
            index=df.index,
        )

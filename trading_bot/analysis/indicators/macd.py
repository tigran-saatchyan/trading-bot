import pandas as pd

from .base import Indicator


class MACD(Indicator):
    """
    Moving Average Convergence Divergence.
    """

    def __init__(
        self,
        fast: int = 12,
        slow: int = 26,
        signal: int = 9,
        column: str = "close",
    ):
        self.fast = fast
        self.slow = slow
        self.signal = signal
        self.column = column

    def _compute(self, df: pd.DataFrame) -> pd.DataFrame:
        close = df[self.column]
        ema_fast = close.ewm(span=self.fast, adjust=False).mean()
        ema_slow = close.ewm(span=self.slow, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=self.signal, adjust=False).mean()
        hist = macd_line - signal_line
        return pd.DataFrame(
            {
                f"macd_line_{self.fast}_{self.slow}": macd_line,
                f"macd_signal_{self.signal}": signal_line,
                f"macd_hist_{self.fast}_{self.slow}_{self.signal}": hist,
            },
            index=df.index,
        )

from typing import Optional

import pandas as pd

# from alpaca_trade_api.rest import REST, TimeFrame
# from trading_bot.config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL


class AlpacaConnector:
    """Fetch historical data via Alpaca API."""

    def __init__(self):
        # self.client = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL)
        pass

    def fetch_history(
        self, symbol: str, start: str, end: str, timeframe: str = "1Day"
    ) -> Optional[pd.DataFrame]:
        # Implement actual API call here
        return None

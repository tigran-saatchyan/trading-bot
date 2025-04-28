from typing import Optional

import pandas as pd

# from ib_insync import IB, Stock, util


class IBKRConnector:
    """Fetch data with ib_insync."""

    def __init__(self, client_id: int):
        # self.ib = IB()
        # self.ib.connect("127.0.0.1", 7497, clientId=client_id)
        pass

    def fetch_history(
        self, symbol: str, start: str, end: str, bar_size: str = "1 day"
    ) -> Optional[pd.DataFrame]:
        # Implement actual API call here
        return None

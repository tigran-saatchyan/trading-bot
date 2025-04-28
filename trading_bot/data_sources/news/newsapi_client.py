from typing import Dict, List

# import requests
# from trading_bot.config import NEWSAPI_KEY


class NewsApiClient:
    BASE_URL = "https://newsapi.org/v2/everything"

    def fetch_news(self, query: str, from_dt: str, to_dt: str) -> List[Dict]:
        # params = {
        #     "q": query,
        #     "from": from_dt,
        #     "to": to_dt,
        #     "apiKey": NEWSAPI_KEY,
        # }
        # resp = requests.get(self.BASE_URL, params=params, timeout=10)
        # resp.raise_for_status()
        # return resp.json().get("articles", [])
        return []

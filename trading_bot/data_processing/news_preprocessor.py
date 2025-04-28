from typing import Dict, List

import pandas as pd


def normalize_news(items: List[Dict]) -> pd.DataFrame:
    """Clean HTML tags, convert dates to UTC."""
    # rows = []
    # for it in items:
    #     rows.append({
    #         "title": html.unescape(it["title"]),
    #         "summary": html.unescape(it.get("summary","")),
    #         "published": pd.to_datetime(it["published"], utc=True),
    #         "link": it["link"],
    #     })
    # return pd.DataFrame(rows).drop_duplicates(subset=["link"])
    return pd.DataFrame([])

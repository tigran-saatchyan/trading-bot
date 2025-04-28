# import redis
# import json
# from trading_bot.config import REDIS_URL

# r = redis.from_url(REDIS_URL)


def cache_latest(symbol: str, data: dict, ttl: int = 60):
    """Cache latest ticker or price."""
    # r.setex(f"latest:{symbol}", ttl, json.dumps(data))
    pass


def get_latest(symbol: str) -> dict | None:
    # val = r.get(f"latest:{symbol}")
    # return json.loads(val) if val else None
    return None

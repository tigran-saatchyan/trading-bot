import os

from dotenv import load_dotenv

load_dotenv()

# Stocks
YFINANCE_ENABLED = os.getenv("YFINANCE_ENABLED") == "true"
ALPACA_ENABLED = os.getenv("ALPACA_ENABLED") == "true"
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL")

IBKR_ENABLED = os.getenv("IBKR_ENABLED") == "true"
IBKR_CLIENT_ID = os.getenv("IBKR_CLIENT_ID")
IBKR_CLIENT_SECRET = os.getenv("IBKR_CLIENT_SECRET")

# Crypto
CCXT_EXCHANGES = os.getenv("CCXT_EXCHANGES", "").split(",")

# News
RSS_FEEDS = os.getenv("RSS_FEEDS", "").split(",")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

# PostgreSQL
PG_DSN = (
    f"postgresql://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}"
    f"@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}"
)

# Redis
REDIS_URL = f"redis://{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}/{os.getenv('REDIS_DB')}"

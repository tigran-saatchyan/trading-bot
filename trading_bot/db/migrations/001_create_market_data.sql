CREATE TABLE IF NOT EXISTS market_data (
  source VARCHAR(32),
  symbol VARCHAR(16),
  timestamp TIMESTAMP WITH TIME ZONE,
  open NUMERIC, high NUMERIC, low NUMERIC, close NUMERIC, volume BIGINT,
  PRIMARY KEY (source, symbol, timestamp)
); 
# scanX

scanX is a simple momentum scanner that fetches US stock data, filters the universe, and exports watchlists compatible with TradingView.

## Requirements

- Python 3.8+
- The packages listed in `requirements.txt` (`yfinance`).
  Additional packages used by the project include `requests-cache`, `requests-ratelimiter` and `pyrate-limiter`.
  You can install everything with:

```bash
pip install -r requirements.txt
```

## Configuration

All runtime options are stored in `config/config.json`. You can adjust parameters such as
parallel worker count, data sources and thresholds by editing this file.

## Running the app

From the repository root run:

```bash
python main.py
```

The script downloads market data, performs the momentum scan and writes watchlist
files to the `output` directory.

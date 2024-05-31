import json


class Config:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
        self.max_parallel_workers = config['max_parallel_workers']
        self.top_pct_take = config['top_pct_take']
        self.nasdaq_url = config['nasdaq_url']
        self.nyse_url = config['nyse_url']
        self.fetch_period = config['fetch_period']
        self.filter_industries = config['filter_industries']
        self.dollar_volume_threshold = config['dollar_volume_threshold']
        self.price_threshold = config['price_threshold']
        self.adr_threshold = config['adr_threshold']
        self.ignore_tickers = config['ignore_tickers']

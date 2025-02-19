import yfinance as yf
import concurrent.futures
from util.adr import Adr
import time
import requests_cache
from requests import Session, session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass


class ParallelStockDataFetcher:
    def __init__(self, max_workers=5):
        self.max_workers = max_workers

    @staticmethod
    def fetch_data_for_ticker(ticker, period, cached_session):
        try:
            stock = yf.Ticker(ticker, session=cached_session)
            stock_history = stock.history(period=period).iloc[::-1]
            stock_info = stock.info
            adr = Adr.calculate_adr(stock_history)
            return ticker, stock_history, stock_info, adr
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return ticker, None, None, None

    def fetch_data(self, tickers, period):
        # session = requests_cache.CachedSession('yfinance.cache')
        cached_session = CachedLimiterSession(
            limiter=Limiter(RequestRate(2, Duration.SECOND)),
            bucket_class=MemoryQueueBucket,
            backend=SQLiteCache("yfinance.cache"),
            expire_after=36000  # 10h
        )
        cached_session.cache.delete(expired=True)
        cached_session.headers['User-agent'] = 'scanX/1.0'
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(
                executor.map(lambda ticker: self.fetch_data_for_ticker(ticker, period, cached_session), tickers))

        return results

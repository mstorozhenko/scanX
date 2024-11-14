import yfinance as yf
import concurrent.futures
from util.adr import Adr
import time


class ParallelStockDataFetcher:
    def __init__(self, max_workers=5):
        self.max_workers = max_workers

    @staticmethod
    def fetch_data_for_ticker(ticker, period):
        try:
            stock = yf.Ticker(ticker)
            stock_history = stock.history(period=period).iloc[::-1]
            stock_info = stock.info
            time.sleep(0.3) # fix Too many requests
            adr = Adr.calculate_adr(stock_history)
            return ticker, stock_history, stock_info, adr
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return ticker, None, None, None

    def fetch_data(self, tickers, period):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(lambda ticker: self.fetch_data_for_ticker(ticker, period), tickers))

        return results

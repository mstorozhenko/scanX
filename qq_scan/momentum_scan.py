import concurrent.futures
from util.performance import PerformanceCalculator


class MomentumScan:
    def __init__(self, config):
        self.config = config

    def process_ticker(self, ticker, stock_history, stock_info, adr):
        try:
            if stock_history is None or stock_info is None or adr is None:
                return None
            current_price = stock_info.get('currentPrice')
            volume = stock_info.get('averageDailyVolume10Day')
            performance = PerformanceCalculator.calculate_performance(stock_history, current_price)
            if (adr >= self.config.adr_threshold and current_price >= self.config.price_threshold
                    and current_price is not None and volume * current_price > self.config.dollar_volume_threshold):
                # print(f"Adding {ticker} with ADR% {adr:.2f} and price ${current_price:.2f}")
                return ticker, (current_price, performance)
        except Exception as e:
            print(f"Error processing data for {ticker}: {e}")
        return None

    @staticmethod
    def extract_period_data(stock_history, period_days):
        if stock_history is None:
            return None
        return stock_history.head(period_days)

    def get_top_stocks(self, fetched_data, period_days):
        adjusted_data = [(ticker, self.extract_period_data(stock_history, period_days), stock_info, adr)
                         for ticker, stock_history, stock_info, adr in fetched_data]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            processed_results = list(executor.map(lambda result: self.process_ticker(*result), adjusted_data))

        prices = {result[0]: result[1] for result in processed_results if result is not None}

        sorted_prices = sorted(prices.items(), key=lambda x: x[1][1], reverse=True)

        top_percent_index = int(max(1, len(sorted_prices) * (self.config.top_pct_take / 100)))
        top_tickers = sorted_prices[:top_percent_index]

        return top_tickers

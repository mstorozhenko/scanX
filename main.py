from collections import OrderedDict
from qq_scan.momentum_scan import MomentumScan
from network.data_fetch.parallel_stock_data_fetcher import ParallelStockDataFetcher
from watchlist_csv.trading_view_exporter import TradingViewExporter
from universe.universe import Universe
from config.config import Config
from console.console import animated_indicator
import threading
import sys
import time

if __name__ == "__main__":
    start_time = time.time()

    config = Config('./config/config.json')
    tickers = Universe.build_universe(config)

    scan = MomentumScan(config)

    stop_event = threading.Event()
    indicator_thread = threading.Thread(target=animated_indicator, args=(stop_event,))
    indicator_thread.start()

    data_fetcher = ParallelStockDataFetcher(max_workers=config.max_parallel_workers)

    try:
        fetched_data = data_fetcher.fetch_data(tickers, period=config.fetch_period)

        top_stocks_1w = scan.get_top_stocks(fetched_data, period_days=5)
        top_stocks_1m = scan.get_top_stocks(fetched_data, period_days=22)
        top_stocks_3m = scan.get_top_stocks(fetched_data, period_days=67)
        top_stocks_6m = scan.get_top_stocks(fetched_data, period_days=126)

        # export op
        tickers_1w = [ticker for ticker, _ in top_stocks_1w]
        tickers_1m = [ticker for ticker, _ in top_stocks_1m]
        tickers_3m = [ticker for ticker, _ in top_stocks_3m]
        tickers_6m = [ticker for ticker, _ in top_stocks_6m]

        all_periods_tickers = list(OrderedDict.fromkeys(tickers_1w + tickers_1m + tickers_3m + tickers_6m))

        exporter = TradingViewExporter()

        exporter.export_collection("top_stocks_1w", tickers_1w)
        exporter.export_collection("top_stocks_1m", tickers_1m)
        exporter.export_collection("top_stocks_3m", tickers_3m)
        exporter.export_collection("top_stocks_6m", tickers_6m)
        exporter.export_collection("top_stocks_all", all_periods_tickers)
    finally:
        # Stop the animated indicator
        stop_event.set()
        indicator_thread.join()
        sys.stdout.write('\rDone!           \n')
        sys.stdout.flush()

        print("--- %s minutes ---" % ((time.time() - start_time) / 60))

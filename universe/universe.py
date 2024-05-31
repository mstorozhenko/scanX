from network.downloader import Downloader


class Universe:

    @staticmethod
    def build_universe(config):
        nasdaq_data = Downloader.download_data(config.nasdaq_url)
        nyse_data = Downloader.download_data(config.nyse_url)
        all_stocks = nasdaq_data + nyse_data
        filtered_stocks = [stock for stock in all_stocks if
                           stock.price is not None
                           and stock.price >= config.price_threshold
                           and not any(industry in stock.industry for industry in config.filter_industries)
                           and (stock.volume * stock.price) >= config.dollar_volume_threshold
                           and not any(ticker in stock.symbol for ticker in config.ignore_tickers)]
        tickers = [stock.symbol.replace('/', '-').replace('$', '').strip() for stock in filtered_stocks]
        return tickers

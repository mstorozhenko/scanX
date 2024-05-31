import requests
from domain.stock import Stock


class Downloader:

    @staticmethod
    def download_data(url):
        headers = {
            'Sec-Fetch-Site': 'same-site',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://www.nasdaq.com',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'en-GB,en;q=0.9',
            'Sec-Fetch-Mode': 'cors',
            'Host': 'api.nasdaq.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15',
            'Referer': 'https://www.nasdaq.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        json_data = response.json()
        rows = json_data['data']['rows']
        stocks = [Stock.from_json(row) for row in rows]
        return stocks

class Stock:
    def __init__(self, symbol, name, price, net_change, pct_change, market_cap, country, ipo_year, volume, sector,
                 industry):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.net_change = net_change
        self.pct_change = pct_change
        self.market_cap = market_cap
        self.country = country
        self.ipo_year = ipo_year
        self.volume = volume
        self.sector = sector
        self.industry = industry

    @classmethod
    def from_json(cls, json_data):
        return cls(
            symbol=json_data['symbol'],
            name=json_data['name'],
            price=cls._parse_float(json_data['lastsale']),
            net_change=json_data['netchange'],
            pct_change=json_data['pctchange'],
            market_cap=json_data['marketCap'],
            country=json_data['country'],
            ipo_year=json_data['ipoyear'],
            volume=cls._parse_int(json_data['volume']),
            sector=json_data['sector'],
            industry=json_data['industry'],
        )

    def _parse_float(price_str):
        try:
            return float(price_str.replace('$', '').replace(',', ''))
        except ValueError:
            return None

    def _parse_int(num):
        try:
            return int(num)
        except ValueError:
            return None

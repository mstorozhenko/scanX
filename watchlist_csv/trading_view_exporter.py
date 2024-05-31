import os
from datetime import datetime


class TradingViewExporter:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.current_date = datetime.now().strftime("%d-%m-%Y")

    def export_collection(self, filename, tickers):
        filename = f"{filename}_{self.current_date}.txt"
        with open(os.path.join(self.output_dir, filename), 'w') as file:
            file.write(','.join(tickers))

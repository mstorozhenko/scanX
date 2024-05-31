class PerformanceCalculator:
    @staticmethod
    def calculate_performance(hist, current_price):
        try:
            lowest_price = hist['Low'].min()
            # performance = ((current_price - lowest_price) / lowest_price) * 100
            performance = current_price / lowest_price
            return performance
        except Exception as e:
            print(f"Error calculating performance: {e}")
            return None

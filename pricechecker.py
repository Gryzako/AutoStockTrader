class PriceChecker():
    def __init__(self) -> None:
        self.prices = []

    def check_highest_three_times(self, price):
        self.prices.append(price)

        if len(self.prices) > 3:
            self.prices.pop(0)

        if len(self.prices) == 3:
            if self.prices[2] > self.prices[0] and self.prices[2] > self.prices[1] and self.prices[1] > self.prices[0]:
                print('kupuje')
                return True
            
        return False



class PriceChecker():
    def __init__(self, trx) -> None:
        self.prices = []
        self.trx = trx

    def check_highest_three_times(self, price, time):
        self.prices.append(price)
        print(f'no1: {self.prices}')

        if len(self.prices) > 3:
            self.prices.pop(0)


        if len(self.prices) == 3:
            if self.prices[0] < self.prices[1] < self.prices[2]:
                print('Kupuje Long')
                self.trx.makeTransaction('Long', price, time)
                return True
            elif self.prices[0] > self.prices[1] > self.prices[2]:
                print('Kupuje Short')
                self.trx.makeTransaction('Short', price, time)
                return True
     
        return False
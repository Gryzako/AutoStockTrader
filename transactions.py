from datetime import datetime

class Transactions:
    def __init__(self) -> None:
        self.openPositions = {'2024-10-24 22:02:55': '68200.00000000', '2024-10-24 22:03:24': '68207.68000000'}
        self.amountOfProfit = 0.005 
        self.amoutOfLost = 0.004
        self.fee = 0.1

    def makeTransaction(self, price, time):
        self.openPositions[time] = price
        print(self.openPositions)

    def closeTransaction(self, price):
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def monitoringOpenPositions(self, currentPrice):

        key_to_close_position_with_profit = [key for key, value in self.openPositions.items() if float(value) <= currentPrice + (currentPrice * self.amountOfProfit)]
        key_to_close_position_with_lose = [key for key, value in self.openPositions.items() if float(value) >= currentPrice - (currentPrice * self.amoutOfLost)]

        try:   
            for key in key_to_close_position_with_profit:
                del self.openPositions[key]

            for key in key_to_close_position_with_lose:
                del self.openPositions[key]
        except:
            print('nothing to remove')

        print(f'profit: {key_to_close_position_with_profit}')
        print(f'strata: {key_to_close_position_with_lose}')
        


# Example usage:
trx = Transactions()
amount = 68600.00000000
trx.monitoringOpenPositions(amount)
print(trx.openPositions)

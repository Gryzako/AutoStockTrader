from datetime import datetime
import os
import json

class Transactions:
    def __init__(self) -> None:
        self.openLongPositions = {}
        self.openShortPositions = {}
        self.amountOfProfit = 0.00095 
        self.amountOfLost = 0.00085
        self.fee = 0.1
        self.betSize = 5
        self.saldo = 0

        # Ensure 'transactions.json' exists
        if not os.path.isfile('transactions.json'):
            with open("transactions.json", "w") as file:
                json.dump([], file)

    def makeTransaction(self, type, price, time):
        if type == 'Long':
            self.openLongPositions[time] = price
        if type == 'Short':
            self.openShortPositions[time] = price

    def closeTransaction(self, json_file, positions_to_close, currentPrice, trxType):
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found or JSON decoding error. Initializing empty data list.")
            data = []
        for key, value in positions_to_close.items():
            if trxType == 'Long':
                profit_lost = float(currentPrice) - float(value)
                self.saldo += profit_lost
            elif trxType == 'Short':
                profit_lost = float(value) - float(currentPrice) 
                self.saldo += profit_lost
                
            trade_entry = {
                'time_opening': key,
                'price_buy': value,
                'time_closing': formatted_time,
                'price_closing': currentPrice,
                'type of transaction' : trxType,
                'profit': profit_lost
            }
            data.append(trade_entry)

        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)
        

    def monitoringOpenPositions(self, currentPrice):
        print(f'Currently open long positions: {self.openLongPositions}')
        print(f'Currently open short positions: {self.openShortPositions}') 
        print(f'Saldo: {self.saldo}')

        # Ensure currentPrice is a float for calculations
        currentPrice = float(currentPrice)

        # # Long positions: Create dictionaries for positions to close
        key_to_close_long_with_profit = {
            key: value for key, value in self.openLongPositions.items() 
            if float(value) < currentPrice * (1 - self.amountOfProfit)
        }
        
        key_to_close_long_with_lose = {
            key: value for key, value in self.openLongPositions.items() 
            if float(value) > currentPrice * (1 + self.amountOfLost)
        }

        # Short position: Create dictionary for position to close

        key_to_close_short_with_profit = {
            key: value for key, value in self.openShortPositions.items()
            if float(value) > currentPrice * (1 + self.amountOfProfit)
        }

        key_to_close_short_with_loss = {
            key: value for key, value in self.openShortPositions.items()
            if float(value) < currentPrice * (1 - self.amountOfLost)     
        }

        # Remove closed positions from openPositions
        for key in list(key_to_close_long_with_profit.keys()):
            self.openLongPositions.pop(key, None)

        for key in list(key_to_close_long_with_lose.keys()):
            self.openLongPositions.pop(key, None)

        for key in list(key_to_close_short_with_profit.keys()):
            self.openShortPositions.pop(key, None)

        for key in list(key_to_close_short_with_loss.keys()):
            self.openShortPositions.pop(key, None)

        # Close transactions if there are any to close:
        if key_to_close_long_with_profit:
            self.closeTransaction('transactions.json', key_to_close_long_with_profit, currentPrice, 'Long')
        
        if key_to_close_long_with_lose:
            self.closeTransaction('transactions.json', key_to_close_long_with_lose, currentPrice, 'Long')

        if key_to_close_short_with_profit:
            self.closeTransaction('transactions.json', key_to_close_short_with_profit, currentPrice, 'Short')
        
        if key_to_close_short_with_loss:
            self.closeTransaction('transactions.json', key_to_close_short_with_loss, currentPrice, 'Short')         


        


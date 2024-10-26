from datetime import datetime
import os
import json

class Transactions:
    def __init__(self) -> None:
        self.openPositions = {}
        self.amountOfProfit = 0.005 
        self.amountOfLost = 0.004
        self.fee = 0.1

        # Ensure 'transactions.json' exists
        if not os.path.isfile('transactions.json'):
            with open("transactions.json", "w") as file:
                json.dump([], file)

    def makeTransaction(self, price, time):
        self.openPositions[time] = price
        print(self.openPositions)

    def closeTransaction(self, json_file, positions_to_close, currentPrice):
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found or JSON decoding error. Initializing empty data list.")
            data = []

        for key, value in positions_to_close.items():
            profit_lost = currentPrice - float(value)

            trade_entry = {
                'time_opening': key,
                'price_buy': value,
                'time_closing': formatted_time,
                'price_closing': currentPrice,
                'profit': profit_lost
            }

            data.append(trade_entry)

        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

    def monitoringOpenPositions(self, currentPrice):
        print(f'Currently open positions {self.openPositions}')
        # Ensure currentPrice is a float for calculations
        currentPrice = float(currentPrice)

        # Create dictionaries for positions to close
        key_to_close_position_with_profit = {
            key: value for key, value in self.openPositions.items() 
            if float(value) < currentPrice * (1 - self.amountOfProfit)
        }
        
        key_to_close_position_with_lose = {
            key: value for key, value in self.openPositions.items() 
            if float(value) > currentPrice * (1 + self.amountOfLost)
        }

        # Remove closed positions from openPositions
        for key in list(key_to_close_position_with_profit.keys()):
            self.openPositions.pop(key, None)

        for key in list(key_to_close_position_with_lose.keys()):
            self.openPositions.pop(key, None)

        # Close transactions if there are any to close
        if key_to_close_position_with_profit:
            self.closeTransaction('transactions.json', key_to_close_position_with_profit, currentPrice)
        
        if key_to_close_position_with_lose:
            self.closeTransaction('transactions.json', key_to_close_position_with_lose, currentPrice)

        print(f'Positions closed with profit: {key_to_close_position_with_profit}')
        print(f'Positions closed with loss: {key_to_close_position_with_lose}')

        


import requests
import time
from datetime import datetime
from pricechecker import PriceChecker
from transactions import Transactions

checkPrice = PriceChecker()
trx = Transactions()

while True:
    #API
    btcAPI = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    jsonFile = btcAPI.json()
    currentBTCprice = jsonFile['price']
    #Time
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'{formatted_time} - {currentBTCprice}')

    if checkPrice.check_highest_three_times(currentBTCprice):
        trx.makeTransaction(currentBTCprice, formatted_time)
        time.sleep(10)

    time.sleep(3)
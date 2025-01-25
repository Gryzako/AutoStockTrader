Data:
Binance:
24.10.2024 20:31 
fee = 0.1% for buyin and selling.

API: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT


Plan how aplication works.
- Application is runnig 24h/7 and checking BTC/USDT price.
- monitoring growth trend and if detected it will make a transaction.
- Transaction will be close whenever it will bring a profit in defined value.
- transaction will be closed whenever it will bring a lost in defined value.
- results will be stored in the file in the format easy to analyse.

Needs to be done:
- application should detect also trend and open short position when detected.
- Open position should be defined as short / long
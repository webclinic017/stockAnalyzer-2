import finnhub
from finnhubAPIkey import FINNHUB_API_KEY


import finnhub
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

print(finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1590988249))
import datetime
from finnhubAPIkey import FINNHUB_API_KEY
import finnhub
import time
from dbpass import db_password
import psycopg2

finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
finhub_quote_request = finnhub_client.crypto_candles('BINANCE:BTCUSDT', "D", 1262336461, int(time.time()))
print(finhub_quote_request)
print(len(finhub_quote_request['o']))
print(finhub_quote_request['t'])
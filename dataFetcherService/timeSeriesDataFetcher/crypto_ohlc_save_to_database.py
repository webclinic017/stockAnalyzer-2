import datetime
from finnhubAPIkey import FINNHUB_API_KEY
import finnhub
import time
from dbpass import db_password
import psycopg2
import pandas as pd
import numpy as np


# Connect to Database
db_name = 'securitiesmaster'
db_user = 'postgres'
db_pass = db_password
db_host = 'localhost'

conn = psycopg2.connect(dbname= db_name, user= db_user, password= db_pass, host= db_host )
conn.set_session(autocommit=False)
mycursor = conn.cursor()


dfForPiCycle = pd.read_csv('btcHistoricalPrices9.7.21.csv', index_col='Date', thousands=',', parse_dates=True)
dfForPiDate = pd.read_csv('btcHistoricalPrices9.7.21.csv', thousands=',', parse_dates=True)
dfForPiCycle['Date'] = pd.to_datetime(dfForPiDate['Date'])
print(dfForPiCycle)
dfForPiCycle['Close'] = pd.to_numeric(dfForPiCycle['Price'])
dfForPiCycle['Open'] = pd.to_numeric(dfForPiCycle['Open'])
dfForPiCycle['High'] = pd.to_numeric(dfForPiCycle['High'])
dfForPiCycle['Low'] = pd.to_numeric(dfForPiCycle['Low'])
ohlc = [dfForPiCycle['Open'], dfForPiCycle['High'], dfForPiCycle['Low'], dfForPiCycle['Close'],dfForPiCycle['Vol.'], dfForPiCycle['Date']]
ohlcheaders = ['Open', 'High', 'Low', 'Close', 'Volume', 'Date']
ohlcdf = pd.concat(ohlc, axis=1, keys=ohlcheaders)
ohlcdf = ohlcdf.iloc[::-1]
print(ohlcdf)


def insert_crypto_candles(ticker):


    #print(finhub_quote_request)

    opens =ohlcdf['Open']
    highs = ohlcdf['High']
    lows = ohlcdf['Low']
    closes =ohlcdf['Close']
    timestamps = ohlcdf.index
    volumes = ohlcdf['Volume']
    ticker = 'BTCUSDT'
    #timestampcorrect = datetime.date.fromtimestamp()

    for i in range(1, 10000):
        #try:
            ohlc_db_entry = "INSERT INTO cryptoohlc (open, high, low, close, volume, timestamp, ticker) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            open = opens[i]
            high = highs[i]
            low = lows[i]
            close = closes[i]
            volume = volumes[i]
            timestamp = datetime.date.fromtimestamp(timestamps[i])
            ticker = ticker
            print(ticker)
            candle_values = (open, high, low, close, volume, timestamp, ticker)
            mycursor.execute(ohlc_db_entry, candle_values)
            if i % 1000 == 0:
                conn.commit()
                print(mycursor.rowcount, "1000 records inserted.")

        # except Exception:
        #     #print('End of selected timeseries of x stock')
        #     pass
        # else:
        #     pass


conn.commit()

for symbol in ohlcdf:

        insert_crypto_candles(symbol)
    # except Exception:
    #     #print('Done - check records in database (est 50 million)')
    #     pass
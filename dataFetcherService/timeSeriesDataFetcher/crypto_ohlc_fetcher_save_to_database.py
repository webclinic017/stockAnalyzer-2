import datetime
from finnhubAPIkey import FINNHUB_API_KEY
import finnhub
import time
from dbpass import db_password
import psycopg2


# Connect to Database
db_name = 'securitiesmaster'
db_user = 'postgres'
db_pass = db_password
db_host = 'localhost'

conn = psycopg2.connect(dbname= db_name, user= db_user, password= db_pass, host= db_host )
conn.set_session(autocommit=False)
mycursor = conn.cursor()

def insert_candles_to_master(ticker):
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
    finhub_quote_request = finnhub_client.crypto_candles(ticker, "D", 1262336461, int(time.time()))

    #print(finhub_quote_request)

    opens =finhub_quote_request['o']
    highs = finhub_quote_request['h']
    lows = finhub_quote_request['l']
    closes =finhub_quote_request['c']
    status = finhub_quote_request['s']
    timestamps = finhub_quote_request['t']
    volumes = finhub_quote_request['v']
    #timestampcorrect = datetime.date.fromtimestamp()

    for i in range(1, 10000):
        try:
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

        except Exception:
            #print('End of selected timeseries of x stock')
            pass
        else:
            pass


conn.commit()

for symbol in ticker_list:
    try:
        insert_candles_to_master(symbol)
    except Exception:
        #print('Done - check records in database (est 50 million)')
        pass
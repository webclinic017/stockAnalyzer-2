import finnhub
from finnhubAPIkey import FINNHUB_API_KEY
import time
from get_all_tickers import get_tickers as gt
import mysql
import mysql.connector
import pandas as pd
import finnhub
import datetime


# Connect to mySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0595",
    database="securitiesmaster"
)
mycursor = db.cursor()

#See which ticker's data is already stored in securities master
query = "SELECT distinct ticker FROM securitiesmaster.ohlc"
mycursor.execute(query)
records = mycursor.fetchall()

# Get full ticker list from Finhubb and reformat - API KEY NEEDED.
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
get_list_of_tickers = finnhub_client.stock_symbols('US')
tickers = get_list_of_tickers
list_tickers_dicts = list(tickers)
list_tickers = list_tickers_dicts[5]
print(tickers)

ticker_list = []
for i in list_tickers_dicts:
    ticker_list.append(str(i['symbol']))
    print(i)

print('------------------------------')
print(ticker_list)
print(len(ticker_list))

#Remove this second for loop if you have not already added the S&P 500 tickers to your database
# for i in sp500_symbols:
#     ticker_list.remove(i)

print('------------------------------')
print(len(ticker_list))


for i in records:
    try:
        ticker_list.remove(i)
    except Exception:
        pass


def insert_candles_to_master(ticker):
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
    finhub_quote_request = finnhub_client.stock_candles(ticker, "D", 1262336461, int(time.time()))

    print(finhub_quote_request)

    opens =finhub_quote_request['o']
    highs = finhub_quote_request['h']
    lows = finhub_quote_request['l']
    closes =finhub_quote_request['c']
    status = finhub_quote_request['s']
    timestamps = finhub_quote_request['t']
    volumes = finhub_quote_request['v']
    #timestampcorrect = datetime.date.fromtimestamp()

    for i in range(1, 3000):
        try:
            ohlc_db_entry = "INSERT INTO ohlc (open, high, low, close, volume, timestamp, ticker) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            open = opens[i]
            high = highs[i]
            low = lows[i]
            close = closes[i]
            volume = volumes[i]
            timestamp = datetime.date.fromtimestamp(timestamps[i])
            ticker = ticker
            candle_values = (open, high, low, close, volume, timestamp, ticker)
            mycursor.execute(ohlc_db_entry, candle_values)
            db.commit()
        except Exception:
            print('End of selected timeseries of x stock')
            pass
        else:
            pass

        print(mycursor.rowcount, "record inserted.")

for symbol in ticker_list:
    try:
        insert_candles_to_master(symbol)
    except Exception:
        print('Done - check records in database (est 50 million)')


# print(opens)
# print(highs)
# print(lows)
# print(closes)
# print(timestamps)
# print(volumes)

## COMMAND TO DELETE DUPLICATES FROM DATABASE
# DELETE S1 FROM student_contacts AS S1
# INNER JOIN student_contacts AS S2
# WHERE S1.id > S2.id AND S1.timestamp = S2.timestanmp AND S1.ticker = s2.ticker;
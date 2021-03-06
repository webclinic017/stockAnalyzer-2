import finnhub
from finnhubAPIkey import FINNHUB_API_KEY
import time
from dbpass import db_password
import mysql
import mysql.connector
import pandas as pd
import finnhub
import datetime
import psycopg2

# IF USING mySQL, UN COMMENT AND ENTER CREDENTIALS TO CONNECT TO DATABASE
# Connect to mySQL Database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd=db_password,
#     database="securitiesmaster"
# )
# mycursor = db.cursor()


db_name = 'securitiesmaster'
db_user = 'postgres'
db_pass = db_password
db_host = 'localhost'


conn = psycopg2.connect(dbname= db_name, user= db_user, password= db_pass, host= db_host )
conn.set_session(autocommit=False)
mycursor = conn.cursor()

#See which ticker's data is already stored in securities master
query = "SELECT distinct ticker FROM ohlctwo"
mycursor.execute(query)
records = mycursor.fetchall()
# print(records)
# print(type(records))
res = list(map(''.join, records))
# print(res)


print(len(res))

#Get list of S&P500 tickers
# There are 2 tables on the Wikipedia page
# we want the first table
# payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# first_table = payload[0]
# second_table = payload[1]
#
# df = first_table
# symbols = df['Symbol'].values.tolist()
# print(symbols)

# Get full ticker list from Finhubb and reformat - API KEY NEEDED.
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
get_list_of_tickers = finnhub_client.stock_symbols('US')
tickers = get_list_of_tickers
list_tickers_dicts = list(tickers)
list_tickers = list_tickers_dicts[5]
#print(tickers)
print(len(list_tickers))

ticker_list = []
for i in list_tickers_dicts:
    ticker_list.append(str(i['symbol']))
    print(i)

# print('------------------------------')
#print(ticker_list)
print(len(ticker_list))

#Remove this second for loop if you have not already added the S&P 500 tickers to your database
# for i in sp500_symbols:
#     ticker_list.remove(i)

print('------------------------------')
#print(len(symbols))


# for i in res:
#     if i in symbols:
#         symbols.remove(i)

for i in res:
    if i in ticker_list:
        ticker_list.remove(i)


#print(len(symbols))
print(len(ticker_list))

def insert_candles_to_master(ticker):
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
    finhub_quote_request = finnhub_client.stock_candles(ticker, "D", 1262336461, int(time.time()))

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
            ohlc_db_entry = "INSERT INTO ohlctwo (open, high, low, close, volume, timestamp, ticker) VALUES (%s, %s, %s, %s, %s, %s, %s)"
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
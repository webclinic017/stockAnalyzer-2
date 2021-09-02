from dbpass import db_password
import psycopg2
import pandas as pd
import mplfinance as mpf



db_name = 'securitiesmaster'
db_user = 'postgres'
db_pass = db_password
db_host = 'localhost'


def chartOHLC(ticker):
    conn = psycopg2.connect(dbname= db_name, user= db_user, password= db_pass, host= db_host )
    cur = conn.cursor()

    query = " Select * FROM ohlctwo WHERE ticker = '" + ticker + "' "
    cur.execute(query)
    records = cur.fetchall()

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.read_sql_query(query, con=conn)
    df = df.drop(columns=['id'])
    df = df.set_index('timestamp')
    df = df.drop_duplicates(keep='first')
    df = df.sort_index()

    df["open"] = pd.to_numeric(df["open"], downcast="float")
    df["high"] = pd.to_numeric(df["high"], downcast="float")
    df["low"] = pd.to_numeric(df["low"], downcast="float")
    df["close"] = pd.to_numeric(df["close"], downcast="float")
    print(df)
    print(len(df))

    mpf.plot(df, type='candle')


chartOHLC('MSTR')

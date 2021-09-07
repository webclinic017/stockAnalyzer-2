from dbpass import db_password
import psycopg2
import pandas as pd
import mplfinance as mpf
import plotly.graph_objects as go



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

    df['111MA'] = df['close'].rolling(111).mean()
    df['350MA'] = df['close'].rolling(350).mean()
    df['2x350'] = 2 * df['350MA']

    stmav = df['111MA'].round(2)
    test = df['350MA'].round(2)
    ltmav = df['2x350'].round(2)



    figure = go.Figure(
        data=[
            go.Candlestick(
                x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'],

            )
        ]
    )

    figure.add_trace(
        go.Scatter(
            x=df.index,
            y=df['111MA'],
            line=dict(color='#e74c3c'),
            name= '111MA'
        )
    )

    figure.add_trace(
        go.Scatter(
            x=df.index,
            y=df['2x350'],
            line=dict(color='#263238'),
            name='2x350MA'
        )
    )
    figure.update_yaxes(type="log")
    figure.show()

    #mpf.plot(df, type='candle')


chartOHLC('MSTR')

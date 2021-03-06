import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go

#Creating Dataframe for Historical Prices
dfForPiCycle = pd.read_csv('btcPriceHistory1.csv', index_col='Date', thousands=',', parse_dates=True)
dfForPiDate = pd.read_csv('btcPriceHistory1.csv', thousands=',', parse_dates=True)
dfForPiCycle['Date'] = pd.to_datetime(dfForPiDate['Date'])
print(dfForPiCycle)
dfForPiCycle['Close']= pd.to_numeric(dfForPiCycle['Price'])
dfForPiCycle['Open']= pd.to_numeric(dfForPiCycle['Open'])
dfForPiCycle['High']= pd.to_numeric(dfForPiCycle['High'])
dfForPiCycle['Low']= pd.to_numeric(dfForPiCycle['Low'])
ohlc = [dfForPiCycle['Open'], dfForPiCycle['High'], dfForPiCycle['Low'], dfForPiCycle['Close'], dfForPiCycle['Vol.'], dfForPiCycle['Date']]
ohlcheaders= [ 'Open', 'High', 'Low', 'Close', 'Volume', 'Date']
ohlcdf = pd.concat(ohlc, axis=1, keys=ohlcheaders)
ohlcdf = ohlcdf.iloc[::-1]
print(dfForPiCycle)

pd.set_option("display.max_rows", None, "display.max_columns", None)
dfForPiCycleReversed = dfForPiCycle.iloc[::-1]
dfForPiCycle['111MA'] = dfForPiCycleReversed['Close'].rolling(111).mean()
dfForPiCycle['350MA'] = dfForPiCycleReversed['Close'].rolling(350).mean()
dfForPiCycle['2x350'] = 2 * dfForPiCycle['350MA']

stmav = dfForPiCycle['111MA'].round(2)
test = dfForPiCycle['350MA'].round(2)
ltmav = dfForPiCycle['2x350'].round(2)
studiesData = [stmav, test, ltmav]
headers = ['111MA', '350MA', '2x350']
studies = pd.concat(studiesData, axis=1, keys = headers)

df = dfForPiCycle.iloc[::-1]
print(df)

#mpf.plot(df, type='candle' )

figure = go.Figure(
    data=[
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],

        )
    ]
)

figure.add_trace(
    go.Scatter(
        x=df.index,
        y=df['111MA'],
        line=dict(color='#e74c3c',width=1),
        name='111MA'
    )
)

figure.add_trace(
    go.Scatter(
        x=df.index,
        y=df['2x350'],
        line=dict(color='#263238',width=1),
        name='2x350MA'
    )
)

# First Pi-Cycle Cross April 6, 2013
figure.add_shape(type="line",
    x0=1365231600000, y0=35, x1=1365231600000, y1=100000,
    line=dict(color="RoyalBlue",width=1, dash='dash')
)

#Second Pi-Cycle Cross December 3, 2013
figure.add_shape(type="line",
    x0=1386057600000, y0=290, x1=1386057600000, y1=100000,
    line=dict(color="RoyalBlue",width=1, dash='dash')
)

#Third Pi-Cycle Cross December 16, 2017
figure.add_shape(type="line",
    x0=1513411200000, y0=7000, x1=1513411200000, y1=100000,
    line=dict(color="RoyalBlue",width=1, dash='dash')
)

#Fourth Pi-Cycle Cross April 12, 2021
figure.add_shape(type="line",
    x0=1618210800000, y0=46000, x1=1618210800000, y1=100000,
    line=dict(color="RoyalBlue",width=1, dash='dash')
)

figure.update_yaxes(type="log")
figure.show()

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit


dfForPiCycle = pd.read_csv('btcHistoricalPrices9.7.21.csv', index_col='Date', thousands=',', parse_dates=True)
dfForPiDate = pd.read_csv('btcHistoricalPrices9.7.21.csv', thousands=',', parse_dates=True)
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

def funct(x, p1, p2):
    return p1*np.log(x) + p2

xdata = (np.array([x+1 for x in range(len(df))]))
#xHighsData = np.array([x+1 for x in range(len(df))])
ydata = np.log(df['Close'])
popt, pcov = curve_fit(funct, xdata, ydata, p0=(10.0,-10))
fittedydata = funct(xdata, popt[0], popt[1])
df['fittedYdata'] = fittedydata

#log_x_data = np.log(x_data)

log_y_data = np.log(ydata)



#Plotting BTC price
figure = go.Figure(
    data=[
        go.Scatter(
            x=df.index,
            y=df['Close'],
            line=dict(color='#263238',width=1),
            name='Price'

        )
    ]
)

figure.add_trace(
    go.Scatter(
        x=df.index,
        y=df['fittedYdata'],
        line=dict(color='#e74c3c',width=1),
        name='111MA'
    )
)

figure.update_yaxes(type="log")
figure.show()
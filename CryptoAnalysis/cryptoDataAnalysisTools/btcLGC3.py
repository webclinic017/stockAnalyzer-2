import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import plotly.graph_objects as go



data = pd.read_csv('btcHistoricalPrices9.7.21.csv', index_col='Date', thousands=',', parse_dates=True)
data = data.iloc[::-1]
data['Days_Since_Genisis'] = range(len(data))

print(data)
print(type(data))


def reg(t, c0, c1, c2, c3):
    return c0+c1*t-c2*np.exp(-c3*t)

guess = [10000, 0.0000011, 10000, 0.0000011]

n = len(data['Price'])
y = np.empty(n)
for i in range(n):
    y[i] = reg(data['Days_Since_Genisis'][i], guess[0], guess[1], guess[2], guess[3])


xdata = (np.array([x+1 for x in range(len(data))]))
#plt.semilogy(xdata, data['Price'])
plt.plot(xdata, data['Price'])
plt.semilogy(data['Days_Since_Genisis'], y,'r.')
plt.plot(xdata, y,'r.')

plt.show()

t = data['Days_Since_Genisis'].values
price = data['Price'].values
c, cov = curve_fit(reg, t, price, guess)
print(c)

for i in range(n):
    for i in range(n):
        y[i] = reg(data['Days_Since_Genisis'][i], c[0], c[1], c[2], c[3])

plt.plot(xdata, data['Price'])
plt.semilogy(data['Days_Since_Genisis'], y,'r.')
plt.plot(xdata, y,'r.')
plt.show()




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

df = dfForPiCycle.iloc[::-1]

def funct(x, p1, p2):
    return p2*np.log(x) + p1

xdata = (np.array([x+1 for x in range(len(df))]))
#xHighsData = np.array([x+1 for x in range(len(df))])
ydata = np.log(df['Close'])
y = df['Close']
popt, pcov = curve_fit(funct, xdata, y, p0=(0.0002,1000))
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
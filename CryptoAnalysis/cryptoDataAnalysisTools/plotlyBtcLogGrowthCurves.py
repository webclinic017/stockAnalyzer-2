import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


df = pd.read_csv('btcHistoricalPrices9.7.21.csv', index_col='Date', thousands=',', parse_dates=True)
print(df)
dfForPiDate = pd.read_csv('btcHistoricalPrices9.7.21.csv', thousands=',', parse_dates=True)
df['Date'] = pd.to_datetime(df.index)
df['Timestamp'] = df['Date'].dt.timestamp

print(df)
df['Close']= pd.to_numeric(df['Price'])
df['Open']= pd.to_numeric(df['Open'])
df['High']= pd.to_numeric(df['High'])
df['Low']= pd.to_numeric(df['Low'])
df = df.iloc[::-1]
df['Days_Since_Genisis'] = range(len(df))
df = df.iloc[::-1]
# ohlc = [df['Open'], df['High'], df['Low'], df['Close'], df['Vol.'], df['Date']]
# ohlcheaders= [ 'Open', 'High', 'Low', 'Close', 'Volume', 'Date']
# ohlcdf = pd.concat(ohlc, axis=1, keys=ohlcheaders)
# ohlcdf = ohlcdf.iloc[::-1]
print(df)


pd.set_option("display.max_rows", None, "display.max_columns", None)
dfReversed = df.iloc[::-1]
df = df.iloc[::-1]

def funct(x, p1, p2):
    return p1*np.log(x) + p2

xdata = (np.array([x+1 for x in range(len(df))]))
#xHighsData = np.array([x+1 for x in range(len(df))])
#ydata = np.log(df['Close'])
y = df['Close']
popt, pcov = curve_fit(funct, xdata, y, p0=(1.0,12))
fittedydata = funct(xdata, popt[0], popt[1])

p1 = popt[0]
p2 = popt[1]

df['fittedYdata'] = fittedydata

#log_x_data = np.log(x_data)

#log_y_data = np.log(ydata)

curvex = np.linspace(1,len(xdata),1000)
curvey = funct(curvex,p1, p2)
plt.plot(curvex,curvey,'r.', linewidth=5)
plt.show()


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

print(df.head())
highIntercept = 1.06930947
highSlope= 0.00076

lowIntercept= -3.0269716
lowSlope = 0.001329

timeIndex= df['Days_Since_Genisis']
weight = (np.log10(timeIndex + 10) * timeIndex * timeIndex - timeIndex) / 30000
highSlopeCum =  highSlope * timeIndex

highLogDev = np.log(weight) + highIntercept + highSlopeCum if timeIndex > 2 else np.nan

# BOTTOM OF CHANNEL INTERCEPT & SLOPE CALCS
lowSlopeCum = lowSlope * timeIndex
lowLogDev =  np.log(weight) + lowIntercept + lowSlopeCum if timeIndex > 2 else np.nan

# TOTAL CHANNEL LOG RANGE
logRange = highLogDev - lowLogDev



# FIBONACCI LEVELS
fib9098Calc =   (logRange * 0.9098) + logRange
fib8541Calc =   (logRange * 0.8541) + logRange
fib7639Calc =   (logRange * 0.7639) + logRange
fib618Calc =    (logRange * 0.618) + logRange
midCalc =       (logRange * 0.5) + logRange
fib382Calc =    (logRange * 0.382) + logRange
fib2361Calc =   (logRange * 0.2361) + logRange
fib1459Calc =   (logRange * 0.1459) + logRange
fib0902Calc =   (logRange * 0.0902) + logRange

# SCALE LOG VARIABLES TO LINEAR
highDev =       pow(2.718281828459, highLogDev)
fib9098Dev =    pow(2.718281828459, fib9098Calc)
fib8541Dev =    pow(2.718281828459, fib8541Calc)
fib7639Dev =    pow(2.718281828459, fib7639Calc)
fib618Dev =     pow(2.718281828459, fib618Calc)
midDev =        pow(2.718281828459, midCalc)
fib382Dev =     pow(2.718281828459, fib382Calc)
fib2361Dev =    pow(2.718281828459, fib2361Calc)
fib1459Dev =    pow(2.718281828459, fib1459Calc)
fib0902Dev =    pow(2.718281828459, fib0902Calc)
lowDev =        pow(2.718281828459, lowLogDev)




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
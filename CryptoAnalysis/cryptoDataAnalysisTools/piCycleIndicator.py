import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.dates  as mdates
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.axes   as mpl_axes
import matplotlib.figure as mpl_fig
import finplot as fplt

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

dfForPiCycle = dfForPiCycle.iloc[::-1]
print(dfForPiCycle)

mpf.plot(dfForPiCycle, type='candle' )

print('----------------------------------------')

fig, ax = plt.subplots(figsize = (12,6))
mpf.plot(dfForPiCycle, type='candle', returnfig=True)
ax.plot(dfForPiCycle.index, dfForPiCycle['111MA'], color = 'blue')
ax.plot(dfForPiCycle.index, dfForPiCycle['2x350'], color= 'red')
ax.set_yscale('log')


plt.show()

print('----------------------------------------')

ax,ax2 = fplt.create_plot('ticker', rows=2)
candles = ['Open', 'Close', 'High', 'Low']
fplt.candlestick_ochl(candles, ax=ax)
fplt.plot(ohlc['Date'], ohlc['Close'].rolling(25).mean(), ax=ax, legend='ma-25')

#fplt.volume_ocv(ohlcdf[['Open', 'Close', 'Volume']], ax=ax.overlay())

fplt.show()
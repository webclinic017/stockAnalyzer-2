import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import datetime as dt

#Creating Dataframe for Historical Prices
df = pd.read_csv('btcPriceHistory.csv')
df2 = pd.read_csv('btcPriceHistory.csv', index_col='Date')
#df2 = df.iloc[::-1]
df2 = df2[df2['Value'] > 0]
df2 = df2.sort_index()
bitcoinFullPriceHistory = df2.loc['2009-01-03':]

df = df.iloc[::-1]
df = df[df['Value'] > 0]
df['Date'] = pd.to_datetime(df['Date'])
daysSinceGenesis = [i for i in range(len(bitcoinFullPriceHistory))]
df['Days_Since_Genisis'] = range(len(df))
print(df)
#seriesdf = pd.to_datetime(df)


#Create series' for each Epoch (Each Halving Represents the Beginning of a New Epoch)
series1 = df2.loc['2011-08-11':'2012-11-28']
series2 = df2.loc['2012-11-28':'2016-07-09']
series3 = df2.loc['2016-07-09':'2020-05-11']
series4 = df2.loc['2020-05-11':]
bitcoinFullPriceHistory = df2.loc['2009-01-03':]
# print(series1.head())
# print('---------------------')
# print(series2.head())
# print('---------------------')
# print(series3.head())
# print('---------------------')
# print(series4.head())
# print('---------------------')
# print(df2)

epoch_1_high = series1['Value'].max()
epoch_2_high = series2['Value'].max()
epoch_3_high = series3['Value'].max()
epoch_4_high = series4['Value'].max()


print('---------------------')
highs = [epoch_1_high, epoch_2_high, epoch_3_high, epoch_4_high]
print('Highs =' + str(highs))
print('---------------------')


epoch_1_low = series1['Value'].min()
epoch_2_low = series2['Value'].min()
epoch_3_low = series3['Value'].min()
epoch_4_low = series4['Value'].min()


print('---------------------')
lows = [epoch_1_low, epoch_2_low, epoch_3_low, epoch_4_low]
print('Lows =' + str(lows))
print('---------------------')


#regression fitting
def funct(x, p1, p2):
    return p1*np.log(x) + p2

xdata = (np.array([x+1 for x in range(len(bitcoinFullPriceHistory))]))
#xHighsData = np.array([x+1 for x in range(len(df))])
ydata = np.log(df['Value'])
popt, pcov = curve_fit(funct, xdata, ydata, p0=(3.0,-10))
fittedydata = funct(xdata, popt[0], popt[1])

xHighsdata = np.array([x+1 for x in range(len(highs))])
yHighsData = np.log(highs)
hopt, hcov = curve_fit(funct, xHighsdata, yHighsData, p0=(1.0,-5))
fittedyHighdata = funct(xdata, hopt[0], hopt[1])

xLowsdata = np.array([x+1 for x in range(len(lows))])
yLowsData = np.log(lows)
lopt, lcov = curve_fit(funct, xLowsdata, yLowsData, p0=(3.0,-10))
fittedyLowdata = funct(xdata, lopt[0], lopt[1])


plt.style.use('dark_background')
plt.loglog(daysSinceGenesis, df['Value'])

for i in range(-5, 6):
    #plt.plot(df['Date'], np.exp(fittedydata))
    # plt.plot(df['Date'], np.exp(fittedydata + i))
     plt.plot(daysSinceGenesis, np.exp(fittedydata+(i/2)))
    #plt.fill_between(df['Date'], np.exp(fittedydata + i - 1), np.exp(fittedydata + i), alpha = 0.4)


plt.ylim(bottom = 0.02)
plt.xlim(left = 50)
# plt.axvline(dt.datetime(2012, 11, 28))
# plt.axvline(dt.datetime(2016, 7, 9))
# plt.axvline(dt.datetime(2020, 5, 11))

# plt.axvline(dt.datetime(2012, 1, 1))
# plt.axvline(dt.datetime(2014, 1, 1))
# plt.axvline(dt.datetime(2016, 1, 1))
# plt.axvline(dt.datetime(2018, 1, 1))
# plt.axvline(dt.datetime(2020, 1, 1))

# plt.yscale("log")
# plt.xscale("log")

plt.show()

print(df)
print(popt)
print(xdata)
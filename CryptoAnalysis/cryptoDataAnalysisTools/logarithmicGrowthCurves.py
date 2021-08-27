import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv('btcPriceHistory.csv')
df = df.iloc[::-1]
df = df[df['Value'] > 0]
df['Date'] = pd.to_datetime(df['Date'])
#seriesdf = pd.to_datetime(df)

#series1 = seriesdf[:['2012-11-28']]
#print(series1)

print(df)


#regression fitting
def funct(x, p1, p2):
    return p1*np.log(x) + p2

xdata = np.array([x+1 for x in range(len(df))])
xHighsData = np.array([x+1 for x in range(len(df))])
ydata = np.log(df['Value'])

popt, pcov = curve_fit(funct, xdata, ydata, p0=(3.0,-10))

fittedydata = funct(xdata, popt[0], popt[1])


plt.style.use('dark_background')
plt.semilogy(df['Date'], df['Value'])

for i in range(-1, 1):
    plt.plot(df['Date'], np.exp(fittedydata))
    # plt.plot(df['Date'], np.exp(fittedydata + i))
    # plt.plot(df['Date'], np.exp(fittedydata+(i/2)))
    #plt.fill_between(df['Date'], np.exp(fittedydata + i - 1), np.exp(fittedydata + i), alpha = 0.4)


plt.ylim(bottom = 0.2)
plt.axvline(dt.datetime(2012, 11, 28))
plt.axvline(dt.datetime(2016, 7, 9))
plt.axvline(dt.datetime(2020, 5, 11))

# plt.axvline(dt.datetime(2012, 1, 1))
# plt.axvline(dt.datetime(2014, 1, 1))
# plt.axvline(dt.datetime(2016, 1, 1))
# plt.axvline(dt.datetime(2018, 1, 1))
# plt.axvline(dt.datetime(2020, 1, 1))

plt.show()

print(df)
print(popt)
import json
import pandas as pd
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pypfopt
from pypfopt import CLA, plotting
from pypfopt import risk_models
from pypfopt import plotting

from pypfopt import expected_returns
from pypfopt import EfficientFrontier



INVESTMENT = 2000

# PTR = PetroChina Company Limited ADR
# BUD = Anheuser Busch Inbev SA (AB InBev)
# XOM = Exxon Mobil Corporation
# BA = Boeing Co
# CHTR = Charter Communications Inc
# SHOP = Shopify Inc
# NVDA = NVIDIA Corporation
# NKE = Nike Inc

TICKERS =['PTR','BUD', 'XOM', 'BA','CHTR', 'SHOP', 'NVDA', 'NKE']

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

stocks_prices = pd.DataFrame({'A': []})
stocks_info = pd.DataFrame({'A': []})

for i, ticker in enumerate(TICKERS):
    print(i, ticker)
    yticker = yf.Ticker(ticker)

    # Get max history of prices
    historyPrices = yticker.history(period='max')
    # generate features for historical prices, and what we want to predict
    historyPrices['Ticker'] = ticker
    historyPrices['Year'] = historyPrices.index.year
    historyPrices['Month'] = historyPrices.index.month
    historyPrices['Weekday'] = historyPrices.index.weekday
    historyPrices['Date'] = historyPrices.index.date

    # historical returns
    for i in [1, 3, 7, 30, 90, 365]:
        historyPrices['growth_' + str(i) + 'd'] = historyPrices['Close'] / historyPrices['Close'].shift(i)

    # future growth 3 days
    historyPrices['future_growth_3d'] = historyPrices['Close'].shift(-3) / historyPrices['Close']

    # 30d rolling volatility : https://ycharts.com/glossary/terms/rolling_vol_30
    historyPrices['volatility'] = historyPrices['Close'].rolling(30).std() * np.sqrt(252)

    if stocks_prices.empty:
        stocks_prices = historyPrices
    else:
        stocks_prices = pd.concat([stocks_prices, historyPrices], ignore_index=True)



# Check one day
filter_last_date = stocks_prices.Date==stocks_prices.Date.max()
print(stocks_prices.Date.max())
stocks_prices[filter_last_date]


print('-----------------------------------------------------------------------------------------')

# https://medium.com/analytics-vidhya/how-to-create-a-stock-correlation-matrix-in-python-4f32f8cb5b50
df_pivot = stocks_prices.pivot('Date','Ticker','Close').reset_index()
df_pivot.tail(5)

#Calculating Correlation Matrix
# https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/

df_pivot.corr()

def calculateMatrix(df_pivot):
    corr = df_pivot.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=.3, square=True, annot=True, cmap='RdYlGn')

    plt.show()
    plt.savefig("covMatrix.png")

print('-----------------------------------------------------------------------------------------')
calculateMatrix(df_pivot)
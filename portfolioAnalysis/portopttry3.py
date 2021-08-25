import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pypfopt
from pypfopt import risk_models
from pypfopt import plotting

tickers = ["MSFT", "AMZN", "KO", "MA", "COST",
           "LUV", "XOM", "PFE", "JPM", "UNH",
           "ACN", "DIS", "GILD", "F", "TSLA"]


#Retreive historical price data
ohlc = yf.download(tickers, period="max")
prices = ohlc["Adj Close"].dropna(how="all")
print(prices.tail())


#Plot Historical Prices
# prices[prices.index >= "2008-01-01"].plot(figsize=(15,10));
# plt.show()

#Calculating Covariance Matrix
sample_cov = risk_models.sample_cov(prices, frequency=252)
sample_cov
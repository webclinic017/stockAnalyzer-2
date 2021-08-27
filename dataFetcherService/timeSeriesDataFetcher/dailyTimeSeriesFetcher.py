import yfinance as yf
import pandas_datareader as web
import datetime
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def getStockPriceHistory(ticker):
    #Retreive historical price data
    ohlc = yf.download(ticker, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices.tail())

#getStockPriceHistory('AAPL')


def getCryptoPriceHistory(crypto_currency, start, end):
    currency_against = 'USD'
    ohlc = web.DataReader(f'{crypto_currency}-{currency_against}', 'yahoo', start=start, end=end)
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices)


start = '2009/01/01'
end = date.today()

getCryptoPriceHistory('BTC', start, end)
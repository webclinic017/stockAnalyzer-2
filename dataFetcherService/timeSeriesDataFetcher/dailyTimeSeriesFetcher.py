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
    return ohlc, prices

#ohlc, prices = getStockPriceHistory('AAPL')


def getCryptoPriceHistory(crypto_currency, start, end):
    currency_against = 'USD'
    ohlc = web.DataReader(f'{crypto_currency}-{currency_against}', 'yahoo', period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices)
    return ohlc, prices


def getPriceHistory(ticker):
    try:
        ohlc, prices = getStockPriceHistory(ticker)
    except Exception:
        print('Failed to find ticker for stock, trying crypto...')
        try:
            ohlc, prices = getCryptoPriceHistory(ticker)
        except Exception:
            print(' Both stock price history search and crypto price history search failed. Investigate issue.')

    return ohlc, prices

#start = '2009/01/01'
#end = date.today()

#getCryptoPriceHistory('BTC', start, end)
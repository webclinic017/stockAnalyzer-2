import finnhub
import pandas as pd
from finnhubAPIkey import FINNHUB_API_KEY
from dataFetcherService.timeSeriesDataFetcher.dailyTimeSeriesFetcher import getStockPriceHistory
import ta
from ta.utils import dropna
from ta.volatility import *
from ta.momentum import *
from ta.trend import *
from ta.volume import *


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



ohlc, prices = getStockPriceHistory('AAPL')

print(ohlc)
print(prices)





def bollingerBands(ticker):
    #Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc

    # Initialize Bollinger Bands Indicator
    indicator_bb = BollingerBands(close=ohlc["Close"], window=20, window_dev=1, fillna=1)

    # Add Bollinger Bands features
    technicalsDf['bb_bbm'] = indicator_bb.bollinger_mavg()
    technicalsDf['bb_bbh'] = indicator_bb.bollinger_hband()
    technicalsDf['bb_bbl'] = indicator_bb.bollinger_lband()

    # Add Bollinger Band high indicator
    technicalsDf['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

    # Add Bollinger Band low indicator
    technicalsDf['bb_bbli'] = indicator_bb.bollinger_lband_indicator()
    bBandsDf = technicalsDf

    print('----------------------------')
    print(bBandsDf)
    print('----------------------------')
    return bBandsDf

bollingerBands('AAPL')


def sMA(ticker, window):

    # Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc

    # Initialize SMA Indicator
    sma = sma_indicator(close=ohlc["Close"], window=window, fillna=1)

    technicalsDf['sma'] = sma

    smaDf = technicalsDf
    smaSeries = smaDf['sma']


    print('----------------------------')
    print(smaDf)
    print(smaSeries)
    print('----------------------------')
    return smaDf, smaSeries

# sma50 = sMA('AAPL', 50)
# sma100 = sMA('AAPL', 100)
# sma200 = sMA('AAPL', 200)


def eMA(ticker, window):

    # Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc

    # Initialize SMA Indicator
    ema = ema_indicator(close=ohlc["Close"], window=window, fillna=1)

    technicalsDf['ema'] = ema

    emaDf = technicalsDf
    emaSeries = emaDf['ema']


    print('----------------------------')
    print(emaDf)
    print(emaSeries)
    print('----------------------------')
    return emaDf, emaSeries

# ema50 = eMA('AAPL', 50)
# ema100 = eMA('AAPL', 100)
# ema200 = eMA('AAPL', 200)


def rSI(ticker):
    # Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc
    window = 14

    rsiVal = rsi(close=ohlc["Close"], window=window, fillna=1)

    technicalsDf['rsi'] = rsiVal

    rsiDf = technicalsDf
    rsiSeries = rsiDf['rsi']

    print('----------------------------')
    print(rsiDf)
    print(rsiSeries)
    print('----------------------------')
    return rsiDf, rsiSeries

rSI('AAPL')


def cCI(ticker):
    # Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc
    window = 20

    cciVal = cci(high=ohlc["High"], low=ohlc["Low"], close=ohlc["Close"],  window=window, constant=0.015, fillna=1)

    technicalsDf['cci'] = cciVal

    cciDf = technicalsDf
    cciSeries = cciDf['cci']

    print('----------------------------')
    print(cciDf)
    print(cciSeries)
    print('----------------------------')
    return cciDf, cciSeries

cCI('AAPL')

def dMI(ticker):
    # Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc
    window = 20

    adxVal = adx(high=ohlc["High"], low=ohlc["Low"], close=ohlc["Close"],  window=window, fillna=1)
    diPlus = adx_neg(high=ohlc["High"], low=ohlc["Low"], close=ohlc["Close"], window=window, fillna=1)
    diMinus = adx_pos(high=ohlc["High"], low=ohlc["Low"], close=ohlc["Close"], window=window, fillna=1)

    technicalsDf['adxVal'] = adxVal
    technicalsDf['diPlus'] = diPlus
    technicalsDf['diMinus'] = diMinus

    dmiDf = technicalsDf
    adxSeries = dmiDf['adxVal']
    diPlusSeries = dmiDf['diPlus']
    diMinusSeries = dmiDf['diMinus']

    print('----------------------------')
    print(dmiDf)
    print(adxSeries)
    print(diPlusSeries)
    print(diMinusSeries)
    print('----------------------------')
    return dmiDf, adxSeries, diPlusSeries, diMinusSeries

dMI('AAPL')

def keltnerChannels(ticker):
    # Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc
    window = 20

    keltner_mBand = keltner_channel_mband(high=ohlc["High"], low=ohlc["Low"], close=ohlc["Close"],  window=window, window_atr=3, fillna=1, original_version=False)
    keltner_hBand = keltner_channel_hband(high=ohlc["High"], low=ohlc["Low"], close=ohlc["Close"], window=window, window_atr=3, fillna=1, original_version=False)
    keltner_lBand = keltner_channel_lband(high=ohlc["High"], low=ohlc["Low"], close=ohlc["Close"], window=window, window_atr=3, fillna=1, original_version=False)

    technicalsDf['KCmBand'] = keltner_mBand
    technicalsDf['KChBand'] = keltner_hBand
    technicalsDf['KClBand'] = keltner_lBand

    keltnerChannelsDf = technicalsDf
    KCmBanderies = keltnerChannelsDf['KCmBand']
    KClBandSeries = keltnerChannelsDf['KChBand']
    KChBandSeries = keltnerChannelsDf['KClBand']

    print('----------------------------')
    print(keltnerChannelsDf)
    print(KCmBanderies)
    print(KClBandSeries)
    print(KChBandSeries)
    print('----------------------------')
    return keltnerChannelsDf, KCmBanderies, KClBandSeries, KChBandSeries

keltnerChannels('AAPL')





def bollingerBands(ticker):
    # Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc
    window = 20

    bollinger_mBand = bollinger_mavg(close=ohlc["Close"],  window=window, fillna=1)
    bollinger_hBand = bollinger_hband(close=ohlc["Close"], window=window, window_dev=3, fillna=1)
    bollinger_lBand = bollinger_lband( close=ohlc["Close"], window=window, window_dev=3, fillna=1)

    technicalsDf['BBmBand'] = bollinger_mBand
    technicalsDf['BBhBand'] = bollinger_hBand
    technicalsDf['BBlBand'] = bollinger_lBand

    BollingerBandsDf = technicalsDf
    BBmBandSeries = BollingerBandsDf['BBmBand']
    BBhBandSeries = BollingerBandsDf['BBhBand']
    BBlBandSeries = BollingerBandsDf['BBlBand']

    print('----------------------------')
    print(BollingerBandsDf)
    print(BBmBandSeries)
    print(BBhBandSeries)
    print(BBlBandSeries)
    print('----------------------------')
    return BollingerBandsDf, BBmBandSeries, BBhBandSeries, BBlBandSeries

bollingerBands('AAPL')




def vWAP(ticker, window):
    # Get Timeseries Data
    ohlc, prices = getStockPriceHistory(ticker)
    technicalsDf = ohlc

    vwap = volume_weighted_average_price(high=ohlc["High"], low=ohlc["Low"], close=ohlc["Close"], volume=ohlc["Volume"], window=window, fillna=1)

    technicalsDf['VWAP'] = vwap
    vwapDf = technicalsDf
    vwapSeries = vwapDf['VWAP']

    print('----------------------------')
    print(vwapDf)
    print(vwapSeries)

    print('----------------------------')
    return vwapDf, vwapSeries

vWAP('AAPL', 50)
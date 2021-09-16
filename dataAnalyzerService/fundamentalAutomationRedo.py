import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key
import finnhub
from finnhubAPIkey import FINNHUB_API_KEY
from dataAnalyzerService.stockstatcalculations import *
import numpy as np
import time
from datetime import date
import datetime

import yfinance as yf

finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)



def automatefundamentalanalysis(ticker):
    #ticker = request.GET['tickerForFundamentalStats']
    ticker = ticker
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
    finhub_quote_request = finnhub_client.quote(ticker)
    quoteUnformatted = "{:.2f}".format(list(finhub_quote_request.values())[0])
    quoteUnformatted = float(quoteUnformatted)

    # Defining URLs for the Requests
    isUrl = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    bsUrl = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    cfUrl = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key

    # Requests
    isr = requests.get(isUrl)
    bsr = requests.get(bsUrl)
    cfr = requests.get(cfUrl)

    # JSON dicts
    isData = isr.json()
    bsData = bsr.json()
    cfData = cfr.json()

    print(len(isData))
    print(isData)

    print('-------------------------------------------')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    #Consolidating Income Statements to DataFrame
    incomeStatementsDf = pd.DataFrame()
    for i in range(len(isData['quarterlyReports'])):
        current = pd.DataFrame.from_dict(isData['quarterlyReports'][i], orient='index')
        incomeStatementsDf = pd.concat([incomeStatementsDf, current], axis=1)
        # print(current)
        # print(incomeStatementsDf)
    incomeStatements = incomeStatementsDf.iloc[:, ::-1]
    print(incomeStatements)

    #Consolidating Balance Sheets into DataFrame
    balanceSheetsDf = pd.DataFrame()
    for i in range(len(bsData['quarterlyReports'])):
        current = pd.DataFrame.from_dict(bsData['quarterlyReports'][i], orient='index')
        balanceSheetsDf = pd.concat([balanceSheetsDf, current], axis=1)
        # print(current)
        # print(balanceSheetsDf)
    balanceSheets = balanceSheetsDf.iloc[:, ::-1]
    print(balanceSheets)

    # Consolidating CashFlow Statements into DataFrame
    cashFlowsDf = pd.DataFrame()
    for i in range(len(cfData['quarterlyReports'])):
        current = pd.DataFrame.from_dict(cfData['quarterlyReports'][i], orient='index')
        cashFlowsDf = pd.concat([cashFlowsDf, current], axis=1)
        # print(current)
        # print(cashFlowsDf)
    cashFlows = cashFlowsDf.iloc[:, ::-1]
    print(cashFlows)

    #Aggregating Statements
    isAndBsDf = incomeStatements.append(balanceSheets)
    aggregateStatement = isAndBsDf.append(cashFlows)
    aggregateStatement.columns = ['tm19', 'tm18', 'tm17', 'tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10',
                                         'tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']

    #Replacing None with np.Nan vals (prevent conflicts in many calcs)
    aggregateStatement.replace(to_replace=['None'], value=np.nan, inplace=True)
    print(aggregateStatement)
    print(aggregateStatement.shape)

    #Dropping Duplicates
    aggregateStatement = aggregateStatement.iloc[~aggregateStatement.index.duplicated(), :]
    # for i in range(len(aggregateStatement)):
    #     aggregateStatement.drop_duplicates(subset=None, keep='first', inplace=True)

    print(aggregateStatement)
    print(aggregateStatement.shape)

    statementsDates = aggregateStatement.iloc[0]
    print(statementsDates)
    print(type(aggregateStatement.iloc[0][1]))


    ohlc = yf.download(ticker, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")

    statementDatePrices = []

    checkpoint = []

    for i in statementsDates:
        if str(i) in list(prices.keys()):
            checkpoint = prices[str(i)]
        try:
            statementDatePrices.append(prices[str(i)])
        except Exception:
            statementDatePrices.append(checkpoint)

    data = [statementsDates, statementDatePrices]

    intermediate_dictionary = {'statementsDates': statementsDates, 'statementDatePrices': statementDatePrices}
    df = pd.DataFrame(intermediate_dictionary)
    print(df)
    print(statementDatePrices)

    for i in range(len(df['statementDatePrices'])):
        current = df.iloc[int(i)][1]
        current = np.array(current)
        print(current)
        print(i)
        print('-----------')
        empty = []
        if current.size == 0:
            allDates = ohlc.index
            test_date = df.iloc[int(i)]['statementsDates']
            print('Looking for closest date to' + str(test_date) + '...')
            test_date = time.mktime(datetime.datetime.strptime(test_date, '%Y-%m-%d').timetuple())
            cloz_dict = {
                abs(test_date - date.timestamp()) : date for date in allDates
            }
            closestDate = cloz_dict[min(cloz_dict.keys())]
            print(test_date)
            print('Closest Date with Price =' + str(closestDate))
            # cd = closestDate.strftime('%Y-%m-%d')
            # print(cd)
            checkpoint = []
            for i in prices.keys():
                if str(i) == str(closestDate):
                    checkpoint = prices[str(i)]
                    print(checkpoint)
                    continue


            print('-----------')
            print('-----------')
            #print(closestDate)

    #print(ohlc)
    #allDates = ohlc.index
    #print(allDates)
    #print(prices)







automatefundamentalanalysis('AAPL')
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
from stockstatcalculations import *
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



    # print(len(isData))
    # print(isData)

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
    #print(incomeStatements)

    #Consolidating Balance Sheets into DataFrame
    balanceSheetsDf = pd.DataFrame()
    for i in range(len(bsData['quarterlyReports'])):
        current = pd.DataFrame.from_dict(bsData['quarterlyReports'][i], orient='index')
        balanceSheetsDf = pd.concat([balanceSheetsDf, current], axis=1)
        # print(current)
        # print(balanceSheetsDf)
    balanceSheets = balanceSheetsDf.iloc[:, ::-1]
    #print(balanceSheets)

    # Consolidating CashFlow Statements into DataFrame
    cashFlowsDf = pd.DataFrame()
    for i in range(len(cfData['quarterlyReports'])):
        current = pd.DataFrame.from_dict(cfData['quarterlyReports'][i], orient='index')
        cashFlowsDf = pd.concat([cashFlowsDf, current], axis=1)
        # print(current)
        # print(cashFlowsDf)
    cashFlows = cashFlowsDf.iloc[:, ::-1]
    #print(cashFlows)

    #Aggregating Statements
    isAndBsDf = incomeStatements.append(balanceSheets)
    aggregateStatement = isAndBsDf.append(cashFlows)

    if aggregateStatement.shape[1] == 20:
        aggregateStatement.columns = ['tm19', 'tm18', 'tm17', 'tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11','tm10', 'tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 19:
        aggregateStatement.columns = ['tm18', 'tm17', 'tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10','tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 18:
        aggregateStatement.columns = ['tm17', 'tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10', 'tm9','tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 17:
        aggregateStatement.columns = ['tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10', 'tm9', 'tm8', 'tm7','tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 16:
        aggregateStatement.columns = ['tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10', 'tm9', 'tm8', 'tm7', 'tm6','tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 15:
        aggregateStatement.columns = ['tm14', 'tm13', 'tm12', 'tm11', 'tm10', 'tm9', 'tm8', 'tm7', 'tm6', 'tm5','tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 14:
        aggregateStatement.columns = ['tm13', 'tm12', 'tm11', 'tm10', 'tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4','tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 13:
        aggregateStatement.columns = ['tm12', 'tm11', 'tm10', 'tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3','tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 12:
        aggregateStatement.columns = ['tm11', 'tm10', 'tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2','tm1', 't']
    elif aggregateStatement.shape[1] == 11:
        aggregateStatement.columns = ['tm10', 'tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 10:
        aggregateStatement.columns = ['tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 9:
        aggregateStatement.columns = ['tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 8:
        aggregateStatement.columns = ['tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 7:
        aggregateStatement.columns = ['tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 6:
        aggregateStatement.columns = ['tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 5:
        aggregateStatement.columns = ['tm4', 'tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 4:
        aggregateStatement.columns = ['tm3', 'tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 3:
        aggregateStatement.columns = ['tm2', 'tm1', 't']
    elif aggregateStatement.shape[1] == 2:
        aggregateStatement.columns = ['tm1', 't']
    elif aggregateStatement.shape[1] == 1:
        aggregateStatement.columns = ['t']
    else:
        print('Length Mismatch error!')


    # aggregateStatement.columns = ['tm19', 'tm18', 'tm17', 'tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10',
    #                                      'tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']

    #Replacing None with np.Nan vals (prevent conflicts in many calcs)
    aggregateStatement.replace(to_replace=['None'], value=np.nan, inplace=True)
    #print(aggregateStatement)
    print(aggregateStatement.shape)

    #Dropping Duplicates
    aggregateStatement = aggregateStatement.iloc[~aggregateStatement.index.duplicated(), :]
    # for i in range(len(aggregateStatement)):
    #     aggregateStatement.drop_duplicates(subset=None, keep='first', inplace=True)

    #print(aggregateStatement)
    print(aggregateStatement.shape)

    statementsDates = aggregateStatement.iloc[0]
    #print(statementsDates)
    #print(type(aggregateStatement.iloc[0][1]))

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
        #print('-----------')
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
            #print('Test Date' + str(test_date))
            #print('Closest Date with Price =' + str(closestDate))
            cd = closestDate.strftime('%Y-%m-%d')
            #print(cd)
            checkpoint = []
            for i in prices.keys():
                if str(i) == str(closestDate):
                    checkpoint = prices[str(i)]
                    print(checkpoint)
                    for i in range(len(df)):
                        current = df.iloc[int(i)][1]
                        print('Current = ' + str(current))
                        current = np.array(current)
                        if current.size == 0:
                            df.iloc[int(i)][1] = checkpoint
                            break

            #print(statementDatePrices)
    #print(df)
    prices = df['statementDatePrices']
    aggregateStatement = aggregateStatement.append(prices)

    print(aggregateStatement)

    statsColumns = ['tm19', 'tm18', 'tm17', 'tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10', 'tm9', 'tm8', 'tm7',
                    'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    statsRows = ['priceAtTime','trailingPE', 'forwardPE','priceToCashFlow', 'priceToSales', 'priceToBook', 'pEG', 'earningsYield',
                 'grossProfitMargin', 'operatingProfitMargin', 'netProfitMargin', 'ttmgrossProfitMargin',
                 'ttmoperatingProfitMargin', 'ttmnetProfitMargin', 'basicEPS', 'dilutedEPS', 'cashFlowPerShare',
                 'eBITDAperShare', 'divPerShare', 'operatinROA', 'rOA', 'returnOnTotalCapital', 'rOE',
                 'returnOnCommonEquity', 'debtRatio', 'debtToEquity', 'debtToAsset', 'debtToCapital',
                 'financialLeverage', 'currentRatio', 'quickRatio', 'cashRatio', 'deffensiveInterval',
                 'cashConversionCycle', 'interestCoverage', 'fixedChargeCoverage', 'divPayoutRatio', 'retentionRateB',
                 'sustainableGrowthRate', 'inventoryTurnoverRatio', ' daysOfInvOnHand', 'recievablesTurnover',
                 'daysOfSalesOutstanding', 'payableTurnover', 'numDaysofPayables', 'workingCapitalTurnover',
                 'fixedAssetTurnover', 'totalAssetTurnover']

    metricsDf = pd.DataFrame(data=np.nan, columns=statsColumns, index=statsRows)
    print(metricsDf)

    for i in range(len(metricsDf.loc['trailingPE'])):
        currentprice = aggregateStatement.loc['statementDatePrices'][i]


        netIncome = aggregateStatement.loc['netIncome'][int(i)]
        netIncomem1 = aggregateStatement.loc['netIncome'][int(i)]
        netIncomem2 = aggregateStatement.loc['netIncome'][int(i)]
        netIncomem3 = aggregateStatement.loc['netIncome'][int(i)]

        commonStockSharesOutstanding = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]
        commonStockSharesOutstandingm1 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]
        commonStockSharesOutstandingm2 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]
        commonStockSharesOutstandingm3 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]

        # elif i >= 3:
        #     netIncome = aggregateStatement.loc['netIncome'][int(i)]
        #     netIncomem1 = aggregateStatement.loc['netIncome'][int(i-1)]
        #     netIncomem2 = aggregateStatement.loc['netIncome'][int(i-2)]
        #     netIncomem3 = aggregateStatement.loc['netIncome'][int(i-3)]
        #
        #     commonStockSharesOutstanding = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]
        #     commonStockSharesOutstandingm1 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i - 1)]
        #     commonStockSharesOutstandingm2 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i - 2)]
        #     commonStockSharesOutstandingm3 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i - 3)]
        print('NI =' + str(netIncome))
        print('NIm3 =' + str(netIncomem3))



        metricsDf.loc['priceAtTime'][int(i)] = currentprice
        print('Current Price =' + str(currentprice))

        currentTrailingPE = calTrailingPE(currentprice, netIncome,  netIncomem1, netIncomem2, netIncomem3, commonStockSharesOutstanding, commonStockSharesOutstandingm1, commonStockSharesOutstandingm2, commonStockSharesOutstandingm3)

        metricsDf.loc['trailingPE'][int(i)] = currentTrailingPE




        print(metricsDf.loc['trailingPE'][int(i)])

        print(i)


    print(metricsDf)


        #current1= calculatePE(quoteUnformatted, calculateBasicEPS(ttmNetIncome(aggregateStatement.loc['netIncome'][int(i)], aggregateStatement.loc['netIncome'][int(int(i)-1)], aggregateStatement.loc['netIncome'][int(int(i)-2)], aggregateStatement.loc['netIncome'][int(int(i)-3)]), calculatedWeightedAverageSharesOutstanding(aggregateStatement.loc['commonStockSharesOutstanding'][int(i)], aggregateStatement.loc['commonStockSharesOutstanding'][int(i-1)], aggregateStatement.loc['commonStockSharesOutstanding'][int(i-2)], aggregateStatement.loc['commonStockSharesOutstanding'][int(i-3)])))
        #ni = aggregateStatement.loc['netIncome'][int(i)]
        #prefd = ttmPreferedDivs(aggregateStatement.loc['dividendPayoutPreferredStock'][int(i)],aggregateStatement.loc['dividendPayoutPreferredStock'][int(i-1)], aggregateStatement.loc['dividendPayoutPreferredStock'][int(i-2)],aggregateStatement.loc['dividendPayoutPreferredStock'][int(i-3)])
        #print(prefd)
        #print(ni)
        #metricsDf.loc['priceToEarnings'][int(i)] = current1
        #print('current1! = ' + str(current1))


        #print(metricsDf)



automatefundamentalanalysis('AAPL')
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
    statsRows = ['priceAtTime','trailingPE', 'forwardPE','priceToCashFlow', 'priceToSales', 'bookValue','priceToBook', 'pEG', 'earningsYield',
                 'grossProfitMargin', 'operatingProfitMargin', 'netProfitMargin', 'ttmgrossProfitMargin',
                 'ttmoperatingProfitMargin', 'ttmnetProfitMargin', 'ttmEPS','currentBasicEPS', 'dilutedEPS', 'cashFlowPerShare',
                 'tTMeBITDAperShare', 'divPerShare', 'operatingROA', 'rOA', 'returnOnTotalCapital', 'rOE',
                 'returnOnCommonEquity', 'debtRatio', 'debtToEquity', 'debtToAsset', 'debtToCapital',
                 'financialLeverage', 'currentRatio', 'quickRatio', 'cashRatio', 'deffensiveInterval',
                 'cashConversionCycle', 'interestCoverage', 'fixedChargeCoverage', 'divPayoutRatio', 'retentionRateB',
                 'sustainableGrowthRate', 'inventoryTurnoverRatio', 'daysOfInvOnHand', 'recievablesTurnover',
                 'daysOfSalesOutstanding', 'payableTurnover', 'numDaysofPayables', 'workingCapitalTurnover',
                 'fixedAssetTurnover', 'totalAssetTurnover']

    metricsDf = pd.DataFrame(data=np.nan, columns=statsColumns, index=statsRows)
    print(metricsDf)

    for i in reversed(range(len(metricsDf.loc['trailingPE']))):
        currentprice = aggregateStatement.loc['statementDatePrices'][i]

        if int(i) < 3:
            revenue = aggregateStatement.loc['totalRevenue'][int(i)]
            revenuem1 = aggregateStatement.loc['totalRevenue'][int(i)]
            revenuem2 = aggregateStatement.loc['totalRevenue'][int(i)]
            revenuem3 = aggregateStatement.loc['totalRevenue'][int(i)]

            costOfRev = aggregateStatement.loc['costOfRevenue'][int(i)]
            costOfRev = aggregateStatement.loc['costOfRevenue'][int(i)]
            costOfRev = aggregateStatement.loc['costOfRevenue'][int(i)]
            costOfRev = aggregateStatement.loc['costOfRevenue'][int(i)]

            operatingIncome = aggregateStatement.loc['operatingIncome'][int(i)]
            operatingIncomem1 = aggregateStatement.loc['operatingIncome'][int(i)]
            operatingIncomem2 = aggregateStatement.loc['operatingIncome'][int(i)]
            operatingIncomem3 = aggregateStatement.loc['operatingIncome'][int(i)]

            operatingExp = aggregateStatement.loc['operatingExpenses'][int(i)]
            operatingExpm1 = aggregateStatement.loc['operatingExpenses'][int(i)]
            operatingExpm2 = aggregateStatement.loc['operatingExpenses'][int(i)]
            operatingExpm3 = aggregateStatement.loc['operatingExpenses'][int(i)]

            intAndDebtExp = aggregateStatement.loc['interestAndDebtExpense'][int(i)]
            intAndDebtExpm1 = aggregateStatement.loc['interestAndDebtExpense'][int(i)]
            intAndDebtExpm2 = aggregateStatement.loc['interestAndDebtExpense'][int(i)]
            intAndDebtExpm3 = aggregateStatement.loc['interestAndDebtExpense'][int(i)]

            ebit = aggregateStatement.loc['ebit'][int(i)]
            ebitm1 = aggregateStatement.loc['ebit'][int(i)]
            ebitm2 = aggregateStatement.loc['ebit'][int(i)]
            ebitm3 = aggregateStatement.loc['ebit'][int(i)]

            ebitda = aggregateStatement.loc['ebitda'][int(i)]
            ebitdam1 = aggregateStatement.loc['ebitda'][int(i)]
            ebitdam2 = aggregateStatement.loc['ebitda'][int(i)]
            ebitdam3 = aggregateStatement.loc['ebitda'][int(i)]

            netIncome = aggregateStatement.loc['netIncome'][int(i)]
            netIncomem1 = aggregateStatement.loc['netIncome'][int(i)]
            netIncomem2 = aggregateStatement.loc['netIncome'][int(i)]
            netIncomem3 = aggregateStatement.loc['netIncome'][int(i)]

            divPayout = aggregateStatement.loc['dividendPayout'][int(i)]
            divPayoutm1 = aggregateStatement.loc['dividendPayout'][int(i)]
            divPayoutm2 = aggregateStatement.loc['dividendPayout'][int(i)]
            divPayoutm3 = aggregateStatement.loc['dividendPayout'][int(i)]

            cash = aggregateStatement.loc['cashAndCashEquivalentsAtCarryingValue'][int(i)]
            cashm1 = aggregateStatement.loc['cashAndCashEquivalentsAtCarryingValue'][int(i)]
            cashm2 = aggregateStatement.loc['cashAndCashEquivalentsAtCarryingValue'][int(i)]
            cashm3 = aggregateStatement.loc['cashAndCashEquivalentsAtCarryingValue'][int(i)]

            inventory = aggregateStatement.loc['inventory'][int(i)]
            inventorym1 = aggregateStatement.loc['inventory'][int(i)]
            inventorym2 = aggregateStatement.loc['inventory'][int(i)]
            inventorym3 = aggregateStatement.loc['inventory'][int(i)]

            totalAssets = aggregateStatement.loc['totalAssets'][int(i)]
            totalAssetsm1 = aggregateStatement.loc['totalAssets'][int(i)]
            totalAssetsm2 = aggregateStatement.loc['totalAssets'][int(i)]
            totalAssetsm3 = aggregateStatement.loc['totalAssets'][int(i)]

            totalLiabilities = aggregateStatement.loc['totalLiabilities'][int(i)]
            totalLiabilitiesm1 = aggregateStatement.loc['totalLiabilities'][int(i)]
            totalLiabilitiesm2 = aggregateStatement.loc['totalLiabilities'][int(i)]
            totalLiabilitiesm3 = aggregateStatement.loc['totalLiabilities'][int(i)]

            currentAssets = aggregateStatement.loc['totalCurrentAssets'][int(i)]
            currentAssetsm1 = aggregateStatement.loc['totalCurrentAssets'][int(i)]
            currentAssetsm2 = aggregateStatement.loc['totalCurrentAssets'][int(i)]
            currentAssetsm3 = aggregateStatement.loc['totalCurrentAssets'][int(i)]

            currentLiabilities = aggregateStatement.loc['totalCurrentLiabilities'][int(i)]
            currentLiabilitiesm1 = aggregateStatement.loc['totalCurrentLiabilities'][int(i)]
            currentLiabilitiesm2 = aggregateStatement.loc['totalCurrentLiabilities'][int(i)]
            currentLiabilitiesm3 = aggregateStatement.loc['totalCurrentLiabilities'][int(i)]

            totalDebt = aggregateStatement.loc['shortLongTermDebtTotal'][int(i)]
            totalDebtm1 = aggregateStatement.loc['shortLongTermDebtTotal'][int(i)]
            totalDebtm2 = aggregateStatement.loc['shortLongTermDebtTotal'][int(i)]
            totalDebtm3 = aggregateStatement.loc['shortLongTermDebtTotal'][int(i)]

            noncashcharges = aggregateStatement.loc['accumulatedDepreciationAmortizationPPE'][int(i)]
            noncashchargesm1 = aggregateStatement.loc['accumulatedDepreciationAmortizationPPE'][int(i)]
            noncashchargesm2 = aggregateStatement.loc['accumulatedDepreciationAmortizationPPE'][int(i)]
            noncashchargesm3 = aggregateStatement.loc['accumulatedDepreciationAmortizationPPE'][int(i)]

            totalShareholderEquity = aggregateStatement.loc['totalShareholderEquity'][int(i)]
            totalShareholderEquitym1 = aggregateStatement.loc['totalShareholderEquity'][int(i)]
            totalShareholderEquitym2 = aggregateStatement.loc['totalShareholderEquity'][int(i)]
            totalShareholderEquitym3 = aggregateStatement.loc['totalShareholderEquity'][int(i)]

            commonStockSharesOutstanding = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]
            commonStockSharesOutstandingm1 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]
            commonStockSharesOutstandingm2 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]
            commonStockSharesOutstandingm3 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]

        elif int(i) >= 3:
            revenue = aggregateStatement.loc['totalRevenue'][int(i)]
            revenuem1 = aggregateStatement.loc['totalRevenue'][int(i - 1)]
            revenuem2 = aggregateStatement.loc['totalRevenue'][int(i - 2)]
            revenuem3 = aggregateStatement.loc['totalRevenue'][int(i - 3)]

            operatingIncome = aggregateStatement.loc['operatingIncome'][int(i)]
            operatingIncomem1 = aggregateStatement.loc['operatingIncome'][int(i - 1)]
            operatingIncomem2 = aggregateStatement.loc['operatingIncome'][int(i - 2)]
            operatingIncomem3 = aggregateStatement.loc['operatingIncome'][int(i - 3)]

            operatingExp = aggregateStatement.loc['operatingExpenses'][int(i)]
            operatingExpm1 = aggregateStatement.loc['operatingExpenses'][int(i - 1)]
            operatingExpm2 = aggregateStatement.loc['operatingExpenses'][int(i - 2)]
            operatingExpm3 = aggregateStatement.loc['operatingExpenses'][int(i - 3)]

            intAndDebtExp = aggregateStatement.loc['interestAndDebtExpense'][int(i)]
            intAndDebtExpm1 = aggregateStatement.loc['interestAndDebtExpense'][int(i-1)]
            intAndDebtExpm2 = aggregateStatement.loc['interestAndDebtExpense'][int(i-2)]
            intAndDebtExpm3 = aggregateStatement.loc['interestAndDebtExpense'][int(i-3)]

            ebit = aggregateStatement.loc['ebit'][int(i)]
            ebitm1 = aggregateStatement.loc['ebit'][int(i-1)]
            ebitm2 = aggregateStatement.loc['ebit'][int(i-2)]
            ebitm3 = aggregateStatement.loc['ebit'][int(i-3)]

            ebitda = aggregateStatement.loc['ebitda'][int(i)]
            ebitdam1 = aggregateStatement.loc['ebitda'][int(i - 1)]
            ebitdam2 = aggregateStatement.loc['ebitda'][int(i - 2)]
            ebitdam3 = aggregateStatement.loc['ebitda'][int(i - 3)]

            netIncome = aggregateStatement.loc['netIncome'][int(i)]
            netIncomem1 = aggregateStatement.loc['netIncome'][int(i-1)]
            netIncomem2 = aggregateStatement.loc['netIncome'][int(i-2)]
            netIncomem3 = aggregateStatement.loc['netIncome'][int(i-3)]

            costOfRev = aggregateStatement.loc['costOfRevenue'][int(i)]
            costOfRevm1 = aggregateStatement.loc['costOfRevenue'][int(i-1)]
            costOfRevm2 = aggregateStatement.loc['costOfRevenue'][int(i-2)]
            costOfRevm3 = aggregateStatement.loc['costOfRevenue'][int(i-3)]

            divPayout = aggregateStatement.loc['dividendPayout'][int(i)]
            divPayoutm1 = aggregateStatement.loc['dividendPayout'][int(i-1)]
            divPayoutm2 = aggregateStatement.loc['dividendPayout'][int(i-2)]
            divPayoutm3 = aggregateStatement.loc['dividendPayout'][int(i-3)]

            cash = aggregateStatement.loc['cashAndCashEquivalentsAtCarryingValue'][int(i)]
            cashm1 = aggregateStatement.loc['cashAndCashEquivalentsAtCarryingValue'][int(i - 1)]
            cashm2 = aggregateStatement.loc['cashAndCashEquivalentsAtCarryingValue'][int(i - 2)]
            cashm3 = aggregateStatement.loc['cashAndCashEquivalentsAtCarryingValue'][int(i - 3)]

            inventory = aggregateStatement.loc['inventory'][int(i)]
            inventorym1 = aggregateStatement.loc['inventory'][int(i - 1)]
            inventorym2 = aggregateStatement.loc['inventory'][int(i - 2)]
            inventorym3 = aggregateStatement.loc['inventory'][int(i - 3)]

            totalAssets = aggregateStatement.loc['totalAssets'][int(i)]
            totalAssetsm1 = aggregateStatement.loc['totalAssets'][int(i-1)]
            totalAssetsm2 = aggregateStatement.loc['totalAssets'][int(i-2)]
            totalAssetsm3 = aggregateStatement.loc['totalAssets'][int(i-3)]

            totalLiabilities = aggregateStatement.loc['totalLiabilities'][int(i)]
            totalLiabilitiesm1 = aggregateStatement.loc['totalLiabilities'][int(i-1)]
            totalLiabilitiesm2 = aggregateStatement.loc['totalLiabilities'][int(i-2)]
            totalLiabilitiesm3 = aggregateStatement.loc['totalLiabilities'][int(i-3)]

            currentAssets = aggregateStatement.loc['totalCurrentAssets'][int(i)]
            currentAssetsm1 = aggregateStatement.loc['totalCurrentAssets'][int(i-1)]
            currentAssetsm2 = aggregateStatement.loc['totalCurrentAssets'][int(i-2)]
            currentAssetsm3 = aggregateStatement.loc['totalCurrentAssets'][int(i-3)]

            currentLiabilities = aggregateStatement.loc['totalCurrentLiabilities'][int(i)]
            currentLiabilitiesm1 = aggregateStatement.loc['totalCurrentLiabilities'][int(i-1)]
            currentLiabilitiesm2 = aggregateStatement.loc['totalCurrentLiabilities'][int(i-2)]
            currentLiabilitiesm3 = aggregateStatement.loc['totalCurrentLiabilities'][int(i-3)]

            totalDebt = aggregateStatement.loc['shortLongTermDebtTotal'][int(i)]
            totalDebtm1 = aggregateStatement.loc['shortLongTermDebtTotal'][int(i-1)]
            totalDebtm2 = aggregateStatement.loc['shortLongTermDebtTotal'][int(i-2)]
            totalDebtm3 = aggregateStatement.loc['shortLongTermDebtTotal'][int(i-3)]

            noncashcharges = aggregateStatement.loc['accumulatedDepreciationAmortizationPPE'][int(i)]
            noncashchargesm1 = aggregateStatement.loc['accumulatedDepreciationAmortizationPPE'][int(i-1)]
            noncashchargesm2 = aggregateStatement.loc['accumulatedDepreciationAmortizationPPE'][int(i-2)]
            noncashchargesm3 = aggregateStatement.loc['accumulatedDepreciationAmortizationPPE'][int(i-3)]

            totalShareholderEquity = aggregateStatement.loc['totalShareholderEquity'][int(i)]
            totalShareholderEquitym1 = aggregateStatement.loc['totalShareholderEquity'][int(i-1)]
            totalShareholderEquitym2 = aggregateStatement.loc['totalShareholderEquity'][int(i-2)]
            totalShareholderEquitym3 = aggregateStatement.loc['totalShareholderEquity'][int(i-3)]

            commonStockSharesOutstanding = aggregateStatement.loc['commonStockSharesOutstanding'][int(i)]
            commonStockSharesOutstandingm1 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i - 1)]
            commonStockSharesOutstandingm2 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i - 2)]
            commonStockSharesOutstandingm3 = aggregateStatement.loc['commonStockSharesOutstanding'][int(i - 3)]

        print('NI =' + str(netIncome))
        print('NIm3 =' + str(netIncomem3))

        metricsDf.loc['priceAtTime'][int(i)] = currentprice
        print('Current Price =' + str(currentprice))

        currentTrailingPE, earnignsYield, ttmEPS, basicEPS = calTrailingPEandEY(currentprice, netIncome,  netIncomem1, netIncomem2, netIncomem3, commonStockSharesOutstanding, commonStockSharesOutstandingm1, commonStockSharesOutstandingm2, commonStockSharesOutstandingm3)
        currentPcF, ttmOpCFps, cFpS = calPCF(currentprice, operatingIncome, operatingIncomem1, operatingIncomem2, operatingIncomem3, commonStockSharesOutstanding, commonStockSharesOutstandingm1, commonStockSharesOutstandingm2, commonStockSharesOutstandingm3)
        currentpS = calPS(currentprice, revenue, revenuem1, revenuem2, revenuem3, commonStockSharesOutstanding, commonStockSharesOutstandingm1, commonStockSharesOutstandingm2, commonStockSharesOutstandingm3)
        ttmEbitdaPs = calTtmEBITDApS(ebitda, ebitdam1, ebitdam2, ebitdam3, commonStockSharesOutstanding, commonStockSharesOutstandingm1, commonStockSharesOutstandingm2, commonStockSharesOutstandingm3)

        currentBV, currentpB = calpB(currentprice, totalShareholderEquity, commonStockSharesOutstanding)
        gpM, opM, npM = calCurrentMargins(revenue, operatingIncome, netIncome, costOfRev)
        ttmGPM, ttmOPM, ttmNPM = calTtmMargins(revenue, revenuem1, revenuem2, revenuem3, operatingIncome, operatingIncomem1, operatingIncomem2, operatingIncomem3, netIncome, netIncomem1, netIncomem2, netIncomem3, costOfRev, costOfRevm1, costOfRevm2, costOfRevm3)
        divPerShare, divPayoutRatio, retentionRateB = calDivPerShare(divPayout, commonStockSharesOutstanding, netIncome)

        roa, roe, opRoa, opRoe, interestCoverageRatio, fixedChargeCoverageRatio, retentionRateB, sustainableGrowthRate = calReturnOns(netIncome, operatingIncome, totalAssets, totalAssetsm1, totalShareholderEquity, totalShareholderEquitym1, commonStockSharesOutstanding, divPayout)
        debtToAsset, debtToEquity, financialLeverage, debtToCapital, currentRatio, quickRatio, cashRatio = calBsRatios(totalAssets, totalLiabilities, totalDebt, totalShareholderEquity, inventory, currentAssets, currentLiabilities, cash)
        deffensiveInterval = calDefInt(currentAssets, operatingExp, operatingExpm1, operatingExpm2, operatingExpm3, noncashcharges, noncashchargesm1, noncashchargesm2, noncashchargesm3)
        ###!!!!COMPLETECASHCONVCYCLE
        #interestCoverageRatio, fixedChargeCoverageRatio, retentionRateB = calculateInterestCoverageRatio(ebit, intAndDebtExp)
        inventoryTurnoverRatio, daysOfInvOnHand = invRatios(inventory, inventorym1, costOfRev)

        metricsDf.loc['trailingPE'][int(i)] = currentTrailingPE
        metricsDf.loc['priceToCashFlow'][int(i)] = currentPcF
        metricsDf.loc['priceToSales'][int(i)] = currentpS
        metricsDf.loc['priceToBook'][int(i)] = currentpB
        metricsDf.loc['bookValue'][int(i)] = currentBV
        metricsDf.loc['earningsYield'][int(i)] = earnignsYield
        metricsDf.loc['grossProfitMargin'][int(i)] = gpM
        metricsDf.loc['operatingProfitMargin'][int(i)] = opM
        metricsDf.loc['netProfitMargin'][int(i)] = npM
        metricsDf.loc['ttmgrossProfitMargin'][int(i)] = ttmGPM
        metricsDf.loc['ttmoperatingProfitMargin'][int(i)] = ttmOPM
        metricsDf.loc['ttmnetProfitMargin'][int(i)] = ttmNPM

        metricsDf.loc['currentBasicEPS'][int(i)] = basicEPS
        metricsDf.loc['ttmEPS'][int(i)] = ttmEPS

        metricsDf.loc['cashFlowPerShare'][int(i)] = cFpS
        metricsDf.loc['tTMeBITDAperShare'][int(i)] = ttmEbitdaPs
        metricsDf.loc['divPerShare'][int(i)] = divPerShare

        metricsDf.loc['rOA'][int(i)] = roa
        metricsDf.loc['rOE'][int(i)] = roe
        metricsDf.loc['operatingROA'][int(i)] = opRoa

        metricsDf.loc['debtRatio'][int(i)] = debtToAsset
        metricsDf.loc['debtToEquity'][int(i)] = debtToEquity
        metricsDf.loc['financialLeverage'][int(i)] = financialLeverage
        metricsDf.loc['debtToCapital'][int(i)] = debtToCapital
        metricsDf.loc['currentRatio'][int(i)] = currentRatio
        metricsDf.loc['quickRatio'][int(i)] = quickRatio
        metricsDf.loc['cashRatio'][int(i)] = cashRatio

        metricsDf.loc['deffensiveInterval'][int(i)] = deffensiveInterval
        metricsDf.loc['interestCoverage'][int(i)] = interestCoverageRatio
        metricsDf.loc['fixedChargeCoverage'][int(i)] = fixedChargeCoverageRatio
        metricsDf.loc['divPayoutRatio'][int(i)] = divPayoutRatio
        metricsDf.loc['retentionRateB'][int(i)] = retentionRateB
        metricsDf.loc['sustainableGrowthRate'][int(i)] = sustainableGrowthRate

        metricsDf.loc['inventoryTurnoverRatio'][int(i)] = inventoryTurnoverRatio
        metricsDf.loc['daysOfInvOnHand'][int(i)] = daysOfInvOnHand



        continue




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



automatefundamentalanalysis('HD')
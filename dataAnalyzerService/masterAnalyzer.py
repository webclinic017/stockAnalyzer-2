import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key
import finnhub
from finnhubAPIkey import FINNHUB_API_KEY
from dataAnalyzerService.stockstatcalculations import *
import numpy as np



finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

def build_master(ticker):

    #Retrieving current price
    finhub_quote_request = finnhub_client.quote(ticker)
    quote = "${:.2f}".format(list(finhub_quote_request.values())[0])
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

    # creating DataFrame for IncomeStatements
    isy20df = pd.DataFrame.from_dict(isData['quarterlyReports'][0], orient='index')
    isy19df = pd.DataFrame.from_dict(isData['quarterlyReports'][1], orient='index')
    isy18df = pd.DataFrame.from_dict(isData['quarterlyReports'][2], orient='index')
    isy17df = pd.DataFrame.from_dict(isData['quarterlyReports'][3], orient='index')
    isy16df = pd.DataFrame.from_dict(isData['quarterlyReports'][4], orient='index')
    isy15df = pd.DataFrame.from_dict(isData['quarterlyReports'][5], orient='index')
    isy14df = pd.DataFrame.from_dict(isData['quarterlyReports'][6], orient='index')
    isy13df = pd.DataFrame.from_dict(isData['quarterlyReports'][7], orient='index')
    isy12df = pd.DataFrame.from_dict(isData['quarterlyReports'][8], orient='index')
    isy11df = pd.DataFrame.from_dict(isData['quarterlyReports'][9], orient='index')
    isy10df = pd.DataFrame.from_dict(isData['quarterlyReports'][10], orient='index')
    isy9df = pd.DataFrame.from_dict(isData['quarterlyReports'][11], orient='index')
    isy8df = pd.DataFrame.from_dict(isData['quarterlyReports'][12], orient='index')
    isy7df = pd.DataFrame.from_dict(isData['quarterlyReports'][13], orient='index')
    isy6df = pd.DataFrame.from_dict(isData['quarterlyReports'][14], orient='index')
    isy5df = pd.DataFrame.from_dict(isData['quarterlyReports'][15], orient='index')
    isy4df = pd.DataFrame.from_dict(isData['quarterlyReports'][16], orient='index')
    isy3df = pd.DataFrame.from_dict(isData['quarterlyReports'][17], orient='index')
    isy2df = pd.DataFrame.from_dict(isData['quarterlyReports'][18], orient='index')
    isy1df = pd.DataFrame.from_dict(isData['quarterlyReports'][19], orient='index')

    quarterly_income_statement = pd.concat(
        [isy1df, isy2df, isy3df, isy4df, isy5df, isy6df, isy7df, isy8df, isy9df, isy10df, isy11df, isy12df, isy13df, isy14df, isy15df, isy16df, isy17df,
         isy18df, isy19df, isy20df], axis=1)
    # quarterly_income_statement.to_csv('quarterly_income_statements')

    # DataFrame for Quarterly Balance Sheet
    bsy20df = pd.DataFrame.from_dict(bsData['quarterlyReports'][0], orient='index')
    bsy19df = pd.DataFrame.from_dict(bsData['quarterlyReports'][1], orient='index')
    bsy18df = pd.DataFrame.from_dict(bsData['quarterlyReports'][2], orient='index')
    bsy17df = pd.DataFrame.from_dict(bsData['quarterlyReports'][3], orient='index')
    bsy16df = pd.DataFrame.from_dict(bsData['quarterlyReports'][4], orient='index')
    bsy15df = pd.DataFrame.from_dict(bsData['quarterlyReports'][5], orient='index')
    bsy14df = pd.DataFrame.from_dict(bsData['quarterlyReports'][6], orient='index')
    bsy13df = pd.DataFrame.from_dict(bsData['quarterlyReports'][7], orient='index')
    bsy12df = pd.DataFrame.from_dict(bsData['quarterlyReports'][8], orient='index')
    bsy11df = pd.DataFrame.from_dict(bsData['quarterlyReports'][9], orient='index')
    bsy10df = pd.DataFrame.from_dict(bsData['quarterlyReports'][10], orient='index')
    bsy9df = pd.DataFrame.from_dict(bsData['quarterlyReports'][11], orient='index')
    bsy8df = pd.DataFrame.from_dict(bsData['quarterlyReports'][12], orient='index')
    bsy7df = pd.DataFrame.from_dict(bsData['quarterlyReports'][13], orient='index')
    bsy6df = pd.DataFrame.from_dict(bsData['quarterlyReports'][14], orient='index')
    bsy5df = pd.DataFrame.from_dict(bsData['quarterlyReports'][15], orient='index')
    bsy4df = pd.DataFrame.from_dict(bsData['quarterlyReports'][16], orient='index')
    bsy3df = pd.DataFrame.from_dict(bsData['quarterlyReports'][17], orient='index')
    bsy2df = pd.DataFrame.from_dict(bsData['quarterlyReports'][18], orient='index')
    bsy1df = pd.DataFrame.from_dict(bsData['quarterlyReports'][19], orient='index')

    quarterly_balance_sheet = pd.concat(
        [bsy1df, bsy2df, bsy3df, bsy4df, bsy5df, bsy6df, bsy7df, bsy8df, bsy9df, bsy10df, bsy11df, bsy12df, bsy13df, bsy14df, bsy15df, bsy16df, bsy17df,
         bsy18df, bsy19df, bsy20df], axis=1)
    # quarterly_balance_sheet.to_csv('quarterly_balance_sheets')

    # DataFrame for Quarterly Cash Flow Statement
    cfy20df = pd.DataFrame.from_dict(cfData['quarterlyReports'][0], orient='index')
    cfy19df = pd.DataFrame.from_dict(cfData['quarterlyReports'][1], orient='index')
    cfy18df = pd.DataFrame.from_dict(cfData['quarterlyReports'][2], orient='index')
    cfy17df = pd.DataFrame.from_dict(cfData['quarterlyReports'][3], orient='index')
    cfy16df = pd.DataFrame.from_dict(cfData['quarterlyReports'][4], orient='index')
    cfy15df = pd.DataFrame.from_dict(cfData['quarterlyReports'][5], orient='index')
    cfy14df = pd.DataFrame.from_dict(cfData['quarterlyReports'][6], orient='index')
    cfy13df = pd.DataFrame.from_dict(cfData['quarterlyReports'][7], orient='index')
    cfy12df = pd.DataFrame.from_dict(cfData['quarterlyReports'][8], orient='index')
    cfy11df = pd.DataFrame.from_dict(cfData['quarterlyReports'][9], orient='index')
    cfy10df = pd.DataFrame.from_dict(cfData['quarterlyReports'][10], orient='index')
    cfy9df = pd.DataFrame.from_dict(cfData['quarterlyReports'][11], orient='index')
    cfy8df = pd.DataFrame.from_dict(cfData['quarterlyReports'][12], orient='index')
    cfy7df = pd.DataFrame.from_dict(cfData['quarterlyReports'][13], orient='index')
    cfy6df = pd.DataFrame.from_dict(cfData['quarterlyReports'][14], orient='index')
    cfy5df = pd.DataFrame.from_dict(cfData['quarterlyReports'][15], orient='index')
    cfy4df = pd.DataFrame.from_dict(cfData['quarterlyReports'][16], orient='index')
    cfy3df = pd.DataFrame.from_dict(cfData['quarterlyReports'][17], orient='index')
    cfy2df = pd.DataFrame.from_dict(cfData['quarterlyReports'][18], orient='index')
    cfy1df = pd.DataFrame.from_dict(cfData['quarterlyReports'][19], orient='index')

    quarterly_cash_flow_statement = pd.concat(
        [cfy1df, cfy2df, cfy3df, cfy4df, cfy5df, cfy6df, cfy7df, cfy8df, cfy9df, cfy10df, cfy11df, cfy12df, cfy13df, cfy14df, cfy15df, cfy16df, cfy17df,
         cfy18df, cfy19df, cfy20df], axis=1)
    quarterly_cash_flow_statement.drop('netIncome', axis=0)
    # quarterly_cash_flow_statement.to_csv('quarterly_cash_flow_statements')

    isAndBsDf = quarterly_income_statement.append(quarterly_balance_sheet)
    quarterly_statementsDump1 = isAndBsDf.append(quarterly_cash_flow_statement)
    quarterly_statementsDump1.columns = ['tm19', 'tm18', 'tm17', 'tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10', 'tm9', 'tm8', 'tm7', 'tm6', 'tm5', 'tm4', 'tm3', 'tm2', 'tm1', 't']
    quarterly_statementsDump = quarterly_statementsDump1[:-1]
    #quarterly_statementsDump = quarterly_statementsDump1.replace(to_replace=['None'], value=np.nan, inplace=True)

    for i in range(len(quarterly_statementsDump)):
        try:
            quarterly_statementsDump[i].replace('None', np.nan, inplace=True)
        except Exception:
            pass

    # quarterly_statementsDump['t'] = pd.to_numeric(quarterly_statementsDump['t'])
    # quarterly_statementsDump['tm1'] = pd.to_numeric(quarterly_statementsDump['tm1'])
    # quarterly_statementsDump['tm2'] = pd.to_numeric(quarterly_statementsDump['tm2'])
    # quarterly_statementsDump['tm3'] = pd.to_numeric(quarterly_statementsDump['tm3'])
    # quarterly_statementsDump['tm4'] = pd.to_numeric(quarterly_statementsDump['tm4'])
    # quarterly_statementsDump['tm5'] = pd.to_numeric(quarterly_statementsDump['tm5'])
    # quarterly_statementsDump['tm6'] = pd.to_numeric(quarterly_statementsDump['tm6'])
    # quarterly_statementsDump['tm7'] = pd.to_numeric(quarterly_statementsDump['tm7'])
    # quarterly_statementsDump['tm8'] = pd.to_numeric(quarterly_statementsDump['tm8'])
    # quarterly_statementsDump['tm9'] = pd.to_numeric(quarterly_statementsDump['tm9'])
    # quarterly_statementsDump['tm10'] = pd.to_numeric(quarterly_statementsDump['tm10'])
    # quarterly_statementsDump['tm11'] = pd.to_numeric(quarterly_statementsDump['tm11'])
    # quarterly_statementsDump['tm12'] = pd.to_numeric(quarterly_statementsDump['tm12'])
    # quarterly_statementsDump['tm13'] = pd.to_numeric(quarterly_statementsDump['tm13'])
    # quarterly_statementsDump['tm14'] = pd.to_numeric(quarterly_statementsDump['tm14'])
    # quarterly_statementsDump['tm15'] = pd.to_numeric(quarterly_statementsDump['tm15'])
    # quarterly_statementsDump['tm16'] = pd.to_numeric(quarterly_statementsDump['tm16'])
    # quarterly_statementsDump['tm17'] = pd.to_numeric(quarterly_statementsDump['tm17'])
    # quarterly_statementsDump['tm18'] = pd.to_numeric(quarterly_statementsDump['tm18'])
    # quarterly_statementsDump['tm19'] = pd.to_numeric(quarterly_statementsDump['tm19'])
    quarterly_statementsDumpHtml = quarterly_statementsDump1.to_html()
    print('-------------------------------------------')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    print(quarterly_statementsDump)
    # print(quarterly_statementsDumpHtml)
    # print(type(quarterly_statementsDumpHtml))

    ## tm19  VARIABLES
    # Income Statement Variables for tm19
    gross_profit19 = quarterly_statementsDump.loc['grossProfit'][0]
    try:
        gross_profit19 = int(gross_profit19)
    except Exception:
        gross_profit19 = 0
    totalRevenue19 = quarterly_statementsDump.loc['totalRevenue'][0]
    try:
        totalRevenue19 = int(totalRevenue19)
    except Exception:
        totalRevenue19 = 0
    costOfRevenue19 = quarterly_statementsDump.loc['costOfRevenue'][0]
    try:
        costOfRevenue19 = int(costOfRevenue19)
    except Exception:
        costOfRevenue19 = 0
    costofGoodsAndServicesSold19 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][0]
    try:
        costofGoodsAndServicesSold19 = int(costofGoodsAndServicesSold19)
    except Exception:
        costofGoodsAndServicesSold19 = 0
    operatingIncome19 = quarterly_statementsDump.loc['operatingIncome'][0]
    try:
        operatingIncome19 = int(operatingIncome19)
    except Exception:
        operatingIncome19 = 0
    sellingGeneralAndAdministrative19 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][0]
    try:
        sellingGeneralAndAdministrative19 = int(sellingGeneralAndAdministrative19)
    except Exception:
        sellingGeneralAndAdministrative19 = 0
    researchAndDevelopment19 = quarterly_statementsDump.loc['researchAndDevelopment'][0]
    try:
        researchAndDevelopment19 = int(researchAndDevelopment19)
    except Exception:
        researchAndDevelopment19 = 0
    operatingExpenses19 = quarterly_statementsDump.loc['operatingExpenses'][0]
    try:
        operatingExpenses19 = int(operatingExpenses19)
    except Exception:
        operatingExpenses19 = 0
    investmentIncomeNet19 = quarterly_statementsDump.loc['investmentIncomeNet'][0]
    try:
        investmentIncomeNet19 = int(investmentIncomeNet19)
    except Exception:
        investmentIncomeNet19 = 0

    netInterestIncome19 = quarterly_statementsDump.loc['netInterestIncome'][0]
    try:
        netInterestIncome19 = int(netInterestIncome19)
    except Exception:
        netInterestIncome19 = 0
    interestIncome19 = quarterly_statementsDump.loc['interestIncome'][0]
    try:
        interestIncome19 = int(interestIncome19)
    except Exception:
        interestIncome19 = 0
    interestExpense19 = quarterly_statementsDump.loc['interestExpense'][0]
    try:
        interestExpense19 = int(interestExpense19)
    except Exception:
        interestExpense19 = 0
    nonInterestIncome19 = quarterly_statementsDump.loc['nonInterestIncome'][0]
    try:
        nonInterestIncome19 = int(nonInterestIncome19)
    except Exception:
        nonInterestIncome19 = 0
    otherNonOperatingIncome19 = quarterly_statementsDump.loc['otherNonOperatingIncome'][0]
    try:
        otherNonOperatingIncome19 = int(otherNonOperatingIncome19)
    except Exception:
        otherNonOperatingIncome19 = 0
    depreciation19 = quarterly_statementsDump.loc['depreciation'][0]
    try:
        depreciation19 = int(depreciation19)
    except Exception:
        depreciation19 = 0
    depreciationAndAmortization19 = quarterly_statementsDump.loc['depreciationAndAmortization'][0]
    try:
        depreciationAndAmortization19 = int(depreciationAndAmortization19)
    except Exception:
        depreciationAndAmortization19 = 0

    incomeBeforeTax19 = quarterly_statementsDump.loc['incomeBeforeTax'][0]
    try:
        incomeBeforeTax19 = int(incomeBeforeTax19)
    except Exception:
        incomeBeforeTax19 = 0

    incomeTaxExpense19 = quarterly_statementsDump.loc['incomeTaxExpense'][0]
    try:
        incomeTaxExpense19 = int(incomeTaxExpense19)
    except Exception:
        incomeTaxExpense19 = 0
    interestAndDebtExpense19 = quarterly_statementsDump.loc['interestAndDebtExpense'][0]
    try:
        interestAndDebtExpense19 = int(interestAndDebtExpense19)
    except Exception:
        interestAndDebtExpense19 = 0
    netIncomeFromContinuingOperations19 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][0]
    try:
        netIncomeFromContinuingOperations19 = int(netIncomeFromContinuingOperations19)
    except Exception:
        netIncomeFromContinuingOperations19 = 0
    comprehensiveIncomeNetOfTax19 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][0]
    try:
        comprehensiveIncomeNetOfTax19 = int(comprehensiveIncomeNetOfTax19)
    except Exception:
        comprehensiveIncomeNetOfTax19 = 0
    ebit19 = quarterly_statementsDump.loc['ebit'][0]
    try:
        ebit19 = int(ebit19)
    except Exception:
        ebit19 = 0
    ebitda19 = quarterly_statementsDump.loc['ebitda'][0]
    try:
        ebitda19 = int(ebitda19)
    except Exception:
        ebitda19 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 1]

    # Balance Sheet Values for tm19

    totalAssets19 = quarterly_statementsDump.loc['totalAssets'][0]
    try:
        totalAssets19 = int(totalAssets19)
    except Exception:
        totalAssets19 = 0
    totalCurrentAssets19 = quarterly_statementsDump.loc['totalCurrentAssets'][0]
    try:
        totalCurrentAssets19 = int(totalCurrentAssets19)
    except Exception:
        totalCurrentAssets19 = 0
    cashAndCashEquivalentsAtCarryingValue19 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][0]
    try:
        cashAndCashEquivalentsAtCarryingValue19 = int(cashAndCashEquivalentsAtCarryingValue19)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue19 = 0
    cashAndShortTermInvestments19 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][0]
    try:
        cashAndShortTermInvestments19 = int(cashAndShortTermInvestments19)
    except Exception:
        cashAndShortTermInvestments19 = 0
    inventory19 = quarterly_statementsDump.loc['inventory'][0]
    try:
        inventory19 = int(inventory19)
    except Exception:
        inventory19 = 0
    currentNetReceivables19 = quarterly_statementsDump.loc['currentNetReceivables'][0]
    try:
        currentNetReceivables19 = int(currentNetReceivables19)
    except Exception:
        currentNetReceivables19 = 0
    totalNonCurrentAssets19 = quarterly_statementsDump.loc['totalNonCurrentAssets'][0]
    try:
        totalNonCurrentAssets19 = int(totalNonCurrentAssets19)
    except Exception:
        totalNonCurrentAssets19 = 0
    propertyPlantEquipment19 = quarterly_statementsDump.loc['propertyPlantEquipment'][0]
    try:
        propertyPlantEquipment19 = int(propertyPlantEquipment19)
    except Exception:
        propertyPlantEquipment19 = 0
    accumulatedDepreciationAmortizationPPE19 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][0]
    try:
        accumulatedDepreciationAmortizationPPE19 = int(accumulatedDepreciationAmortizationPPE19)
    except Exception:
        accumulatedDepreciationAmortizationPPE19 = 0
    intangibleAssets19 = quarterly_statementsDump.loc['intangibleAssets'][0]
    try:
        intangibleAssets19 = int(intangibleAssets19)
    except Exception:
        intangibleAssets19 = 0
    intangibleAssetsExcludingGoodwill19 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][0]
    try:
        intangibleAssetsExcludingGoodwill19 = int(intangibleAssetsExcludingGoodwill19)
    except Exception:
        intangibleAssetsExcludingGoodwill19 = 0
    goodwill19 = quarterly_statementsDump.loc['goodwill'][0]
    try:
        goodwill19 = int(goodwill19)
    except Exception:
        goodwill19 = 0
    investments19 = quarterly_statementsDump.loc['investments'][0]
    try:
        investments19 = int(investments19)
    except Exception:
        investments19 = 0
    longTermInvestments19 = quarterly_statementsDump.loc['longTermInvestments'][0]
    try:
        longTermInvestments19 = int(longTermInvestments19)
    except Exception:
        longTermInvestments19 = 0
    shortTermInvestments19 = quarterly_statementsDump.loc['shortTermInvestments'][0]
    try:
        shortTermInvestments19 = int(shortTermInvestments19)
    except Exception:
        shortTermInvestments19 = 0
    otherCurrentAssets19 = quarterly_statementsDump.loc['otherCurrentAssets'][0]
    try:
        otherCurrentAssets19 = int(otherCurrentAssets19)
    except Exception:
        otherCurrentAssets19 = 0
    otherNonCurrrentAssets19 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][0]
    try:
        otherNonCurrrentAssets19 = int(otherNonCurrrentAssets19)
    except Exception:
        otherNonCurrrentAssets19 = 0
    totalLiabilities19 = quarterly_statementsDump.loc['totalLiabilities'][0]
    try:
        totalLiabilities19 = int(totalLiabilities19)
    except Exception:
        totalLiabilities19 = 0
    totalCurrentLiabilities19 = quarterly_statementsDump.loc['totalCurrentLiabilities'][0]
    try:
        totalCurrentLiabilities19 = int(totalCurrentLiabilities19)
    except Exception:
        totalCurrentLiabilities19 = 0
    currentAccountsPayable19 = quarterly_statementsDump.loc['currentAccountsPayable'][0]
    try:
        currentAccountsPayable19 = int(currentAccountsPayable19)
    except Exception:
        currentAccountsPayable19 = 0
    deferredRevenue19 = quarterly_statementsDump.loc['deferredRevenue'][0]
    try:
        deferredRevenue19 = int(deferredRevenue19)
    except Exception:
        deferredRevenue19 = 0
    currentDebt19 = quarterly_statementsDump.loc['currentDebt'][0]
    try:
        currentDebt19 = int(currentDebt19)
    except Exception:
        currentDebt19 = 0
    shortTermDebt19 = quarterly_statementsDump.loc['shortTermDebt'][0]
    try:
        shortTermDebt19 = int(shortTermDebt19)
    except Exception:
        shortTermDebt19 = 0
    totalNonCurrentLiabilities19 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][0]
    try:
        totalNonCurrentLiabilities19 = int(totalNonCurrentLiabilities19)
    except Exception:
        totalNonCurrentLiabilities19 = 0
    capitalLeaseObligations19 = quarterly_statementsDump.loc['capitalLeaseObligations'][0]
    try:
        capitalLeaseObligations19 = int(capitalLeaseObligations19)
    except Exception:
        capitalLeaseObligations19 = 0

    longTermDebt19 = quarterly_statementsDump.loc['longTermDebt'][0]
    try:
        longTermDebt19 = int(longTermDebt19)
    except Exception:
        longTermDebt19 = 0
    currentLongTermDebt19 = quarterly_statementsDump.loc['currentLongTermDebt'][0]
    try:
        currentLongTermDebt19 = int(currentLongTermDebt19)
    except Exception:
        currentLongTermDebt19 = 0
    longTermDebtNoncurrent19 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][0]
    try:
        longTermDebtNoncurrent19 = int(longTermDebtNoncurrent19)
    except Exception:
        longTermDebtNoncurrent19 = 0
    shortLongTermDebtTotal19 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][0]
    try:
        shortLongTermDebtTotal19 = int(shortLongTermDebtTotal19)
    except Exception:
        shortLongTermDebtTotal19 = 0
    otherCurrentLiabilities19 = quarterly_statementsDump.loc['otherCurrentLiabilities'][0]
    try:
        otherCurrentLiabilities19 = int(otherCurrentLiabilities19)
    except Exception:
        otherCurrentLiabilities19 = 0
    otherNonCurrentLiabilities19 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][0]
    try:
        otherNonCurrentLiabilities19 = int(otherNonCurrentLiabilities19)
    except Exception:
        otherNonCurrentLiabilities19 = 0
    totalShareholderEquity19 = quarterly_statementsDump.loc['totalShareholderEquity'][0]
    try:
        totalShareholderEquity19 = int(totalShareholderEquity19)
    except Exception:
        totalShareholderEquity19 = 0
    treasuryStock19 = quarterly_statementsDump.loc['treasuryStock'][0]
    try:
        treasuryStock19 = int(treasuryStock19)
    except Exception:
        treasuryStock19 = 0
    retainedEarnings19 = quarterly_statementsDump.loc['retainedEarnings'][0]
    try:
        retainedEarnings19 = int(retainedEarnings19)
    except Exception:
        retainedEarnings19 = 0
    commonStock19 = quarterly_statementsDump.loc['commonStock'][0]
    try:
        commonStock19 = int(commonStock19)
    except Exception:
        commonStock19 = 0
    commonStockSharesOutstanding19 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][0]
    try:
        commonStockSharesOutstanding19 = int(commonStockSharesOutstanding19)
    except Exception:
        commonStockSharesOutstanding19 = 0

    # Cash-Flow Statement values for tm19
    operatingCashflow19 = quarterly_statementsDump.loc['operatingCashflow'][0]
    try:
        operatingCashflow19 = int(operatingCashflow19)
    except Exception:
        operatingCashflow19 = 0
    paymentsForOperatingActivities19 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][0]
    try:
        paymentsForOperatingActivities19 = int(paymentsForOperatingActivities19)
    except Exception:
        paymentsForOperatingActivities19 = 0
    proceedsFromOperatingActivities19 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][0]
    try:
        proceedsFromOperatingActivities19 = int(proceedsFromOperatingActivities19)
    except Exception:
        proceedsFromOperatingActivities19 = 0
    changeInOperatingLiabilities19 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][0]
    try:
        changeInOperatingLiabilities19 = int(changeInOperatingLiabilities19)
    except Exception:
        changeInOperatingLiabilities19 = 0
    changeInOperatingAssets19 = quarterly_statementsDump.loc['changeInOperatingAssets'][0]
    try:
        changeInOperatingAssets19 = int(changeInOperatingAssets19)
    except Exception:
        changeInOperatingAssets19 = 0
    depreciationDepletionAndAmortization19 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][0]
    try:
        depreciationDepletionAndAmortization19 = int(depreciationDepletionAndAmortization19)
    except Exception:
        depreciationDepletionAndAmortization19 = 0
    capitalExpenditures19 = quarterly_statementsDump.loc['capitalExpenditures'][0]
    try:
        capitalExpenditures19 = int(capitalExpenditures19)
    except Exception:
        capitalExpenditures19 = 0
    changeInReceivables19 = quarterly_statementsDump.loc['changeInReceivables'][0]
    try:
        changeInReceivables19 = int(changeInReceivables19)
    except Exception:
        changeInReceivables19 = 0
    changeInInventory19 = quarterly_statementsDump.loc['changeInInventory'][0]
    try:
        changeInInventory19 = int(changeInInventory19)
    except Exception:
        changeInInventory19 = 0
    profitLoss19 = quarterly_statementsDump.loc['profitLoss'][0]
    try:
        profitLoss19 = int(profitLoss19)
    except Exception:
        profitLoss19 = 0
    cashflowFromInvestment19 = quarterly_statementsDump.loc['cashflowFromInvestment'][0]
    try:
        cashflowFromInvestment19 = int(cashflowFromInvestment19)
    except Exception:
        cashflowFromInvestment19 = 0
    cashflowFromFinancing19 = quarterly_statementsDump.loc['cashflowFromFinancing'][0]
    try:
        cashflowFromFinancing19 = int(cashflowFromFinancing19)
    except Exception:
        cashflowFromFinancing19 = 0
    proceedsFromRepaymentsOfShortTermDebt19 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][0]
    try:
        proceedsFromRepaymentsOfShortTermDebt19 = int(proceedsFromRepaymentsOfShortTermDebt19)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt19 = 0
    paymentsForRepurchaseOfCommonStock19 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][0]
    try:
        paymentsForRepurchaseOfCommonStock19 = int(paymentsForRepurchaseOfCommonStock19)
    except Exception:
        paymentsForRepurchaseOfCommonStock19 = 0
    paymentsForRepurchaseOfEquity19 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][0]
    try:
        paymentsForRepurchaseOfEquity19 = int(paymentsForRepurchaseOfEquity19)
    except Exception:
        paymentsForRepurchaseOfEquity19 = 0
    paymentsForRepurchaseOfPreferredStock19 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][0]
    try:
        paymentsForRepurchaseOfPreferredStock19 = int(paymentsForRepurchaseOfPreferredStock19)
    except Exception:
        paymentsForRepurchaseOfPreferredStock19 = 0
    dividendPayout19 = quarterly_statementsDump.loc['dividendPayout'][0]
    try:
        dividendPayout19 = int(dividendPayout19)
    except Exception:
        dividendPayout19 = 0
    dividendPayoutCommonStock19 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][0]
    try:
        dividendPayoutCommonStock19 = int(dividendPayoutCommonStock19)
    except Exception:
        dividendPayoutCommonStock19 = 0
    dividendPayoutPreferredStock19 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][0]
    try:
        dividendPayoutPreferredStock19 = int(dividendPayoutPreferredStock19)
    except Exception:
        dividendPayoutPreferredStock19 = 0
    proceedsFromIssuanceOfCommonStock19 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][0]
    try:
        proceedsFromIssuanceOfCommonStock19 = int(proceedsFromIssuanceOfCommonStock19)
    except Exception:
        proceedsFromIssuanceOfCommonStock19 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet19 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][0]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet19 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet19)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet19 = 0
    proceedsFromIssuanceOfPreferredStock19 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][0]
    try:
        proceedsFromIssuanceOfPreferredStock19 = int(proceedsFromIssuanceOfPreferredStock19)
    except Exception:
        proceedsFromIssuanceOfPreferredStock19 = 0
    proceedsFromRepurchaseOfEquity19 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][0]
    try:
        proceedsFromRepurchaseOfEquity19 = int(proceedsFromRepurchaseOfEquity19)
    except Exception:
        proceedsFromRepurchaseOfEquity19 = 0
    proceedsFromSaleOfTreasuryStock19 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][0]
    try:
        proceedsFromSaleOfTreasuryStock19 = int(proceedsFromSaleOfTreasuryStock19)
    except Exception:
        proceedsFromSaleOfTreasuryStock19 = 0
    changeInCashAndCashEquivalents19 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][0]
    try:
        changeInCashAndCashEquivalents19 = int(changeInCashAndCashEquivalents19)
    except Exception:
        changeInCashAndCashEquivalents19 = 0
    changeInExchangeRate19 = quarterly_statementsDump.loc['changeInExchangeRate'][0]
    try:
        changeInExchangeRate19 = int(changeInExchangeRate19)
    except Exception:
        changeInExchangeRate19 = 0
    netIncome19 = quarterly_statementsDump.loc['netIncome'][0]
    try:
        netIncome19 = int(netIncome19)
    except Exception:
        netIncome19 = 0

    tTMnetIncome19 = (float(netIncome19) + float(netIncome19) + float(netIncome19) + float(netIncome19))
    try:
        tTMpreferredDivs19 = (int(dividendPayoutPreferredStock19) + int(dividendPayoutPreferredStock19) + int(
            dividendPayoutPreferredStock19) + int(dividendPayoutPreferredStock19))
    except Exception:
        tTMpreferredDivs19 = 0
    weightedAvgCommShrsOutstanding19 = (
            (float(commonStockSharesOutstanding19) + float(commonStockSharesOutstanding19) + float(
                commonStockSharesOutstanding19) + float(commonStockSharesOutstanding19)) / 19)
    quoteUnformatted19 = quoteUnformatted
    marketCap19 = calculateMarketCap(quoteUnformatted19, commonStockSharesOutstanding19)
    basicEPS19 = calculateBasicEPS(tTMnetIncome19, tTMpreferredDivs19, weightedAvgCommShrsOutstanding19)
    pE19 = calculatePE(quoteUnformatted19, basicEPS19)
    pCF19 = calculatePriceToCashFlow(quoteUnformatted19,
                                     calculateOperatingCashFlowPerShare(operatingCashflow19,
                                                                        weightedAvgCommShrsOutstanding19))
    pS19 = calculatePS(quoteUnformatted19, calculateSalesPerShare(totalRevenue19, weightedAvgCommShrsOutstanding19))
    pB19 = calculatePB(quoteUnformatted19,
                       calculateMarketToBookValue(marketCap19, totalAssets19, shortLongTermDebtTotal19,
                                                  preferredStock=0))
    sustainableGrowthRate19 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout19, netIncome19)),
        calculateROE(netIncome19, totalShareholderEquity19))
    pEGRatio19 = calculatePEGRatio(pE19, (sustainableGrowthRate19 * 1900))
    earningsYield19 = calculateEarningsYield(basicEPS19, quoteUnformatted19)
    cashFlowPerShare19 = calculateOperatingCashFlowPerShare(operatingCashflow19, weightedAvgCommShrsOutstanding19)
    ebitdaPerShare19 = calculateEBITDAperShare(ebitda19, weightedAvgCommShrsOutstanding19)
    tTMDividendPayout19 = (
        (float(dividendPayout19) + float(dividendPayout19) + float(dividendPayout19) + float(dividendPayout19)))
    dividendsPerShare19 = calculateDividendsPerShare(tTMDividendPayout19, weightedAvgCommShrsOutstanding19)
    currentQuarterGrossProfitMargin19 = calculateGrossProfitMargin(totalRevenue19, costofGoodsAndServicesSold19)
    tTmTotalRevenue19 = (
    (float(totalRevenue19) + float(totalRevenue19) + float(totalRevenue19) + float(totalRevenue19)))
    tTmCOGS19 = ((float(costofGoodsAndServicesSold19) + float(costofGoodsAndServicesSold19) + float(
        costofGoodsAndServicesSold19) + float(costofGoodsAndServicesSold19)))
    tTMGrossProfitMargin19 = calculateGrossProfitMargin(tTmTotalRevenue19, tTmCOGS19)
    currentQuarterOperatingMargin19 = calculateOperatingMargin(operatingIncome19, totalRevenue19)
    tTMOperatingIncome19 = (
        (float(operatingIncome19) + float(operatingIncome19) + float(operatingIncome19) + float(operatingIncome19)))
    tTMOperatingMargin19 = calculateOperatingMargin(tTMOperatingIncome19, tTmTotalRevenue19)
    currentQuarterPreTaxMargin19 = calculatePreTaxMargin(calculateEBT(ebit19, interestExpense19), totalRevenue19)
    tTMebit19 = ((float(ebit19) + float(ebit19) + float(ebit19) + float(ebit19)))
    tTMInterestExpense19 = (
        (float(interestExpense19) + float(interestExpense19) + float(interestExpense19) + float(interestExpense19)))
    tTMPreTaxMargin19 = calculatePreTaxMargin(calculateEBT(tTMebit19, tTMInterestExpense19), tTmTotalRevenue19)
    currentQuarterNetProfitMargin19 = calculateNetProfitMargin(netIncome19, totalRevenue19)
    tTMNetProfitMargin19 = calculateNetProfitMargin(tTMnetIncome19, tTmTotalRevenue19)
    currentQuarterAvgTotalAssets19 = ((float(totalAssets19) + float(totalAssets19)) / 4)
    currentQuarterOperatingROA19 = (calculateOperatingROA(operatingIncome19, currentQuarterAvgTotalAssets19)) * 4
    tTMAvgTotalAssets19 = (
                (float(totalAssets19) + float(totalAssets19) + float(totalAssets19) + float(totalAssets19)) / 4)
    tTMOperatingROA19 = calculateOperatingROA(tTMOperatingIncome19, tTMAvgTotalAssets19)
    currentQuarterROA19 = (calculateROA(netIncome19, currentQuarterAvgTotalAssets19)) * 4
    tTMROA19 = calculateROA(tTMnetIncome19, tTMAvgTotalAssets19)
    currentQuarterReturnOnTotalCapital19 = (calculateReturnOnTotalCapital(ebit19, shortLongTermDebtTotal19,
                                                                          totalShareholderEquity19)) * 4
    tTMReturnOnTotalCapital19 = calculateReturnOnTotalCapital(tTMebit19, shortLongTermDebtTotal19,
                                                              totalShareholderEquity19)
    currentQuarterROE19 = (calculateROE(netIncome19, totalShareholderEquity19)) * 4
    tTMROE19 = calculateROE(tTMnetIncome19, totalShareholderEquity19)
    currentQuarterAvgCommonEquity19 = ((float(totalShareholderEquity19) + float(totalShareholderEquity19)) / 4)
    currentQuarterReturnOnCommonEquity19 = (calculateReturnOnCommonEquity(netIncome19, dividendPayoutPreferredStock19,
                                                                          currentQuarterAvgCommonEquity19)) * 4
    tTMAvgCommonEquity19 = ((float(totalShareholderEquity19) + float(totalShareholderEquity19) + float(
        totalShareholderEquity19) + float(totalShareholderEquity19)) / 4)
    tTMReturnOnCommonEquity19 = calculateReturnOnCommonEquity(tTMnetIncome19, tTMpreferredDivs19, tTMAvgCommonEquity19)
    debtRatio19 = calculateDebtRatio(totalLiabilities19, totalAssets19)
    debtToEquityRatio19 = calculateDebtToEquity(shortLongTermDebtTotal19, totalShareholderEquity19)
    debtToAssetRatio19 = calculateDebtToAssetRatio(shortLongTermDebtTotal19, totalAssets19)
    debtToCapitalRatio19 = calculateDebtToCapitalRatio(shortLongTermDebtTotal19, totalShareholderEquity19)

    financialLeverage19 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets19,
                                                          currentQuarterAvgCommonEquity19)
    interestCoverage19 = calculateInterestCoverageRatio(operatingCashflow19, interestExpense19, incomeTaxExpense19)
    fixedChargeCoverageRatio19 = calculateFixedChargeCoverage(ebit19, capitalLeaseObligations19, interestExpense19)

    ## tm18  VARIABLES
    # Income Statement Variables for tm18
    gross_profit18 = quarterly_statementsDump.loc['grossProfit'][1]
    try:
        gross_profit18 = int(gross_profit18)
    except Exception:
        gross_profit18 = 0
    totalRevenue18 = quarterly_statementsDump.loc['totalRevenue'][1]
    try:
        totalRevenue18 = int(totalRevenue18)
    except Exception:
        totalRevenue18 = 0
    costOfRevenue18 = quarterly_statementsDump.loc['costOfRevenue'][1]
    try:
        costOfRevenue18 = int(costOfRevenue18)
    except Exception:
        costOfRevenue18 = 0
    costofGoodsAndServicesSold18 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][1]
    try:
        costofGoodsAndServicesSold18 = int(costofGoodsAndServicesSold18)
    except Exception:
        costofGoodsAndServicesSold18 = 0
    operatingIncome18 = quarterly_statementsDump.loc['operatingIncome'][1]
    try:
        operatingIncome18 = int(operatingIncome18)
    except Exception:
        operatingIncome18 = 0
    sellingGeneralAndAdministrative18 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][1]
    try:
        sellingGeneralAndAdministrative18 = int(sellingGeneralAndAdministrative18)
    except Exception:
        sellingGeneralAndAdministrative18 = 0
    researchAndDevelopment18 = quarterly_statementsDump.loc['researchAndDevelopment'][1]
    try:
        researchAndDevelopment18 = int(researchAndDevelopment18)
    except Exception:
        researchAndDevelopment18 = 0
    operatingExpenses18 = quarterly_statementsDump.loc['operatingExpenses'][1]
    try:
        operatingExpenses18 = int(operatingExpenses18)
    except Exception:
        operatingExpenses18 = 0
    investmentIncomeNet18 = quarterly_statementsDump.loc['investmentIncomeNet'][1]
    try:
        investmentIncomeNet18 = int(investmentIncomeNet18)
    except Exception:
        investmentIncomeNet18 = 0

    netInterestIncome18 = quarterly_statementsDump.loc['netInterestIncome'][1]
    try:
        netInterestIncome18 = int(netInterestIncome18)
    except Exception:
        netInterestIncome18 = 0
    interestIncome18 = quarterly_statementsDump.loc['interestIncome'][1]
    try:
        interestIncome18 = int(interestIncome18)
    except Exception:
        interestIncome18 = 0
    interestExpense18 = quarterly_statementsDump.loc['interestExpense'][1]
    try:
        interestExpense18 = int(interestExpense18)
    except Exception:
        interestExpense18 = 0
    nonInterestIncome18 = quarterly_statementsDump.loc['nonInterestIncome'][1]
    try:
        nonInterestIncome18 = int(nonInterestIncome18)
    except Exception:
        nonInterestIncome18 = 0
    otherNonOperatingIncome18 = quarterly_statementsDump.loc['otherNonOperatingIncome'][1]
    try:
        otherNonOperatingIncome18 = int(otherNonOperatingIncome18)
    except Exception:
        otherNonOperatingIncome18 = 0
    depreciation18 = quarterly_statementsDump.loc['depreciation'][1]
    try:
        depreciation18 = int(depreciation18)
    except Exception:
        depreciation18 = 0
    depreciationAndAmortization18 = quarterly_statementsDump.loc['depreciationAndAmortization'][1]
    try:
        depreciationAndAmortization18 = int(depreciationAndAmortization18)
    except Exception:
        depreciationAndAmortization18 = 0

    incomeBeforeTax18 = quarterly_statementsDump.loc['incomeBeforeTax'][1]
    try:
        incomeBeforeTax18 = int(incomeBeforeTax18)
    except Exception:
        incomeBeforeTax18 = 0

    incomeTaxExpense18 = quarterly_statementsDump.loc['incomeTaxExpense'][1]
    try:
        incomeTaxExpense18 = int(incomeTaxExpense18)
    except Exception:
        incomeTaxExpense18 = 0
    interestAndDebtExpense18 = quarterly_statementsDump.loc['interestAndDebtExpense'][1]
    try:
        interestAndDebtExpense18 = int(interestAndDebtExpense18)
    except Exception:
        interestAndDebtExpense18 = 0
    netIncomeFromContinuingOperations18 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][1]
    try:
        netIncomeFromContinuingOperations18 = int(netIncomeFromContinuingOperations18)
    except Exception:
        netIncomeFromContinuingOperations18 = 0
    comprehensiveIncomeNetOfTax18 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][1]
    try:
        comprehensiveIncomeNetOfTax18 = int(comprehensiveIncomeNetOfTax18)
    except Exception:
        comprehensiveIncomeNetOfTax18 = 0
    ebit18 = quarterly_statementsDump.loc['ebit'][1]
    try:
        ebit18 = int(ebit18)
    except Exception:
        ebit18 = 0
    ebitda18 = quarterly_statementsDump.loc['ebitda'][1]
    try:
        ebitda18 = int(ebitda18)
    except Exception:
        ebitda18 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 1]

    # Balance Sheet Values for tm18

    totalAssets18 = quarterly_statementsDump.loc['totalAssets'][1]
    try:
        totalAssets18 = int(totalAssets18)
    except Exception:
        totalAssets18 = 0
    totalCurrentAssets18 = quarterly_statementsDump.loc['totalCurrentAssets'][1]
    try:
        totalCurrentAssets18 = int(totalCurrentAssets18)
    except Exception:
        totalCurrentAssets18 = 0
    cashAndCashEquivalentsAtCarryingValue18 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][1]
    try:
        cashAndCashEquivalentsAtCarryingValue18 = int(cashAndCashEquivalentsAtCarryingValue18)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue18 = 0
    cashAndShortTermInvestments18 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][1]
    try:
        cashAndShortTermInvestments18 = int(cashAndShortTermInvestments18)
    except Exception:
        cashAndShortTermInvestments18 = 0
    inventory18 = quarterly_statementsDump.loc['inventory'][1]
    try:
        inventory18 = int(inventory18)
    except Exception:
        inventory18 = 0
    currentNetReceivables18 = quarterly_statementsDump.loc['currentNetReceivables'][1]
    try:
        currentNetReceivables18 = int(currentNetReceivables18)
    except Exception:
        currentNetReceivables18 = 0
    totalNonCurrentAssets18 = quarterly_statementsDump.loc['totalNonCurrentAssets'][1]
    try:
        totalNonCurrentAssets18 = int(totalNonCurrentAssets18)
    except Exception:
        totalNonCurrentAssets18 = 0
    propertyPlantEquipment18 = quarterly_statementsDump.loc['propertyPlantEquipment'][1]
    try:
        propertyPlantEquipment18 = int(propertyPlantEquipment18)
    except Exception:
        propertyPlantEquipment18 = 0
    accumulatedDepreciationAmortizationPPE18 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][1]
    try:
        accumulatedDepreciationAmortizationPPE18 = int(accumulatedDepreciationAmortizationPPE18)
    except Exception:
        accumulatedDepreciationAmortizationPPE18 = 0
    intangibleAssets18 = quarterly_statementsDump.loc['intangibleAssets'][1]
    try:
        intangibleAssets18 = int(intangibleAssets18)
    except Exception:
        intangibleAssets18 = 0
    intangibleAssetsExcludingGoodwill18 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][1]
    try:
        intangibleAssetsExcludingGoodwill18 = int(intangibleAssetsExcludingGoodwill18)
    except Exception:
        intangibleAssetsExcludingGoodwill18 = 0
    goodwill18 = quarterly_statementsDump.loc['goodwill'][1]
    try:
        goodwill18 = int(goodwill18)
    except Exception:
        goodwill18 = 0
    investments18 = quarterly_statementsDump.loc['investments'][1]
    try:
        investments18 = int(investments18)
    except Exception:
        investments18 = 0
    longTermInvestments18 = quarterly_statementsDump.loc['longTermInvestments'][1]
    try:
        longTermInvestments18 = int(longTermInvestments18)
    except Exception:
        longTermInvestments18 = 0
    shortTermInvestments18 = quarterly_statementsDump.loc['shortTermInvestments'][1]
    try:
        shortTermInvestments18 = int(shortTermInvestments18)
    except Exception:
        shortTermInvestments18 = 0
    otherCurrentAssets18 = quarterly_statementsDump.loc['otherCurrentAssets'][1]
    try:
        otherCurrentAssets18 = int(otherCurrentAssets18)
    except Exception:
        otherCurrentAssets18 = 0
    otherNonCurrrentAssets18 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][1]
    try:
        otherNonCurrrentAssets18 = int(otherNonCurrrentAssets18)
    except Exception:
        otherNonCurrrentAssets18 = 0
    totalLiabilities18 = quarterly_statementsDump.loc['totalLiabilities'][1]
    try:
        totalLiabilities18 = int(totalLiabilities18)
    except Exception:
        totalLiabilities18 = 0
    totalCurrentLiabilities18 = quarterly_statementsDump.loc['totalCurrentLiabilities'][1]
    try:
        totalCurrentLiabilities18 = int(totalCurrentLiabilities18)
    except Exception:
        totalCurrentLiabilities18 = 0
    currentAccountsPayable18 = quarterly_statementsDump.loc['currentAccountsPayable'][1]
    try:
        currentAccountsPayable18 = int(currentAccountsPayable18)
    except Exception:
        currentAccountsPayable18 = 0
    deferredRevenue18 = quarterly_statementsDump.loc['deferredRevenue'][1]
    try:
        deferredRevenue18 = int(deferredRevenue18)
    except Exception:
        deferredRevenue18 = 0
    currentDebt18 = quarterly_statementsDump.loc['currentDebt'][1]
    try:
        currentDebt18 = int(currentDebt18)
    except Exception:
        currentDebt18 = 0
    shortTermDebt18 = quarterly_statementsDump.loc['shortTermDebt'][1]
    try:
        shortTermDebt18 = int(shortTermDebt18)
    except Exception:
        shortTermDebt18 = 0
    totalNonCurrentLiabilities18 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][1]
    try:
        totalNonCurrentLiabilities18 = int(totalNonCurrentLiabilities18)
    except Exception:
        totalNonCurrentLiabilities18 = 0
    capitalLeaseObligations18 = quarterly_statementsDump.loc['capitalLeaseObligations'][1]
    try:
        capitalLeaseObligations18 = int(capitalLeaseObligations18)
    except Exception:
        capitalLeaseObligations18 = 0

    longTermDebt18 = quarterly_statementsDump.loc['longTermDebt'][1]
    try:
        longTermDebt18 = int(longTermDebt18)
    except Exception:
        longTermDebt18 = 0
    currentLongTermDebt18 = quarterly_statementsDump.loc['currentLongTermDebt'][1]
    try:
        currentLongTermDebt18 = int(currentLongTermDebt18)
    except Exception:
        currentLongTermDebt18 = 0
    longTermDebtNoncurrent18 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][1]
    try:
        longTermDebtNoncurrent18 = int(longTermDebtNoncurrent18)
    except Exception:
        longTermDebtNoncurrent18 = 0
    shortLongTermDebtTotal18 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][1]
    try:
        shortLongTermDebtTotal18 = int(shortLongTermDebtTotal18)
    except Exception:
        shortLongTermDebtTotal18 = 0
    otherCurrentLiabilities18 = quarterly_statementsDump.loc['otherCurrentLiabilities'][1]
    try:
        otherCurrentLiabilities18 = int(otherCurrentLiabilities18)
    except Exception:
        otherCurrentLiabilities18 = 0
    otherNonCurrentLiabilities18 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][1]
    try:
        otherNonCurrentLiabilities18 = int(otherNonCurrentLiabilities18)
    except Exception:
        otherNonCurrentLiabilities18 = 0
    totalShareholderEquity18 = quarterly_statementsDump.loc['totalShareholderEquity'][1]
    try:
        totalShareholderEquity18 = int(totalShareholderEquity18)
    except Exception:
        totalShareholderEquity18 = 0
    treasuryStock18 = quarterly_statementsDump.loc['treasuryStock'][1]
    try:
        treasuryStock18 = int(treasuryStock18)
    except Exception:
        treasuryStock18 = 0
    retainedEarnings18 = quarterly_statementsDump.loc['retainedEarnings'][1]
    try:
        retainedEarnings18 = int(retainedEarnings18)
    except Exception:
        retainedEarnings18 = 0
    commonStock18 = quarterly_statementsDump.loc['commonStock'][1]
    try:
        commonStock18 = int(commonStock18)
    except Exception:
        commonStock18 = 0
    commonStockSharesOutstanding18 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][1]
    try:
        commonStockSharesOutstanding18 = int(commonStockSharesOutstanding18)
    except Exception:
        commonStockSharesOutstanding18 = 0

    # Cash-Flow Statement values for tm18
    operatingCashflow18 = quarterly_statementsDump.loc['operatingCashflow'][1]
    try:
        operatingCashflow18 = int(operatingCashflow18)
    except Exception:
        operatingCashflow18 = 0
    paymentsForOperatingActivities18 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][1]
    try:
        paymentsForOperatingActivities18 = int(paymentsForOperatingActivities18)
    except Exception:
        paymentsForOperatingActivities18 = 0
    proceedsFromOperatingActivities18 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][1]
    try:
        proceedsFromOperatingActivities18 = int(proceedsFromOperatingActivities18)
    except Exception:
        proceedsFromOperatingActivities18 = 0
    changeInOperatingLiabilities18 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][1]
    try:
        changeInOperatingLiabilities18 = int(changeInOperatingLiabilities18)
    except Exception:
        changeInOperatingLiabilities18 = 0
    changeInOperatingAssets18 = quarterly_statementsDump.loc['changeInOperatingAssets'][1]
    try:
        changeInOperatingAssets18 = int(changeInOperatingAssets18)
    except Exception:
        changeInOperatingAssets18 = 0
    depreciationDepletionAndAmortization18 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][1]
    try:
        depreciationDepletionAndAmortization18 = int(depreciationDepletionAndAmortization18)
    except Exception:
        depreciationDepletionAndAmortization18 = 0
    capitalExpenditures18 = quarterly_statementsDump.loc['capitalExpenditures'][1]
    try:
        capitalExpenditures18 = int(capitalExpenditures18)
    except Exception:
        capitalExpenditures18 = 0
    changeInReceivables18 = quarterly_statementsDump.loc['changeInReceivables'][1]
    try:
        changeInReceivables18 = int(changeInReceivables18)
    except Exception:
        changeInReceivables18 = 0
    changeInInventory18 = quarterly_statementsDump.loc['changeInInventory'][1]
    try:
        changeInInventory18 = int(changeInInventory18)
    except Exception:
        changeInInventory18 = 0
    profitLoss18 = quarterly_statementsDump.loc['profitLoss'][1]
    try:
        profitLoss18 = int(profitLoss18)
    except Exception:
        profitLoss18 = 0
    cashflowFromInvestment18 = quarterly_statementsDump.loc['cashflowFromInvestment'][1]
    try:
        cashflowFromInvestment18 = int(cashflowFromInvestment18)
    except Exception:
        cashflowFromInvestment18 = 0
    cashflowFromFinancing18 = quarterly_statementsDump.loc['cashflowFromFinancing'][1]
    try:
        cashflowFromFinancing18 = int(cashflowFromFinancing18)
    except Exception:
        cashflowFromFinancing18 = 0
    proceedsFromRepaymentsOfShortTermDebt18 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][1]
    try:
        proceedsFromRepaymentsOfShortTermDebt18 = int(proceedsFromRepaymentsOfShortTermDebt18)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt18 = 0
    paymentsForRepurchaseOfCommonStock18 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][1]
    try:
        paymentsForRepurchaseOfCommonStock18 = int(paymentsForRepurchaseOfCommonStock18)
    except Exception:
        paymentsForRepurchaseOfCommonStock18 = 0
    paymentsForRepurchaseOfEquity18 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][1]
    try:
        paymentsForRepurchaseOfEquity18 = int(paymentsForRepurchaseOfEquity18)
    except Exception:
        paymentsForRepurchaseOfEquity18 = 0
    paymentsForRepurchaseOfPreferredStock18 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][1]
    try:
        paymentsForRepurchaseOfPreferredStock18 = int(paymentsForRepurchaseOfPreferredStock18)
    except Exception:
        paymentsForRepurchaseOfPreferredStock18 = 0
    dividendPayout18 = quarterly_statementsDump.loc['dividendPayout'][1]
    try:
        dividendPayout18 = int(dividendPayout18)
    except Exception:
        dividendPayout18 = 0
    dividendPayoutCommonStock18 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][1]
    try:
        dividendPayoutCommonStock18 = int(dividendPayoutCommonStock18)
    except Exception:
        dividendPayoutCommonStock18 = 0
    dividendPayoutPreferredStock18 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][1]
    try:
        dividendPayoutPreferredStock18 = int(dividendPayoutPreferredStock18)
    except Exception:
        dividendPayoutPreferredStock18 = 0
    proceedsFromIssuanceOfCommonStock18 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][1]
    try:
        proceedsFromIssuanceOfCommonStock18 = int(proceedsFromIssuanceOfCommonStock18)
    except Exception:
        proceedsFromIssuanceOfCommonStock18 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet18 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][1]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet18 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet18)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet18 = 0
    proceedsFromIssuanceOfPreferredStock18 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][1]
    try:
        proceedsFromIssuanceOfPreferredStock18 = int(proceedsFromIssuanceOfPreferredStock18)
    except Exception:
        proceedsFromIssuanceOfPreferredStock18 = 0
    proceedsFromRepurchaseOfEquity18 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][1]
    try:
        proceedsFromRepurchaseOfEquity18 = int(proceedsFromRepurchaseOfEquity18)
    except Exception:
        proceedsFromRepurchaseOfEquity18 = 0
    proceedsFromSaleOfTreasuryStock18 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][1]
    try:
        proceedsFromSaleOfTreasuryStock18 = int(proceedsFromSaleOfTreasuryStock18)
    except Exception:
        proceedsFromSaleOfTreasuryStock18 = 0
    changeInCashAndCashEquivalents18 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][1]
    try:
        changeInCashAndCashEquivalents18 = int(changeInCashAndCashEquivalents18)
    except Exception:
        changeInCashAndCashEquivalents18 = 0
    changeInExchangeRate18 = quarterly_statementsDump.loc['changeInExchangeRate'][1]
    try:
        changeInExchangeRate18 = int(changeInExchangeRate18)
    except Exception:
        changeInExchangeRate18 = 0
    netIncome18 = quarterly_statementsDump.loc['netIncome'][1]
    try:
        netIncome18 = int(netIncome18)
    except Exception:
        netIncome18 = 0

    tTMnetIncome18 = (float(netIncome18) + float(netIncome19) + float(netIncome19) + float(netIncome19))
    try:
        tTMpreferredDivs18 = (int(dividendPayoutPreferredStock18) + int(dividendPayoutPreferredStock19) + int(
            dividendPayoutPreferredStock19) + int(dividendPayoutPreferredStock19))
    except Exception:
        tTMpreferredDivs18 = 0
    weightedAvgCommShrsOutstanding18 = (
            (float(commonStockSharesOutstanding18) + float(commonStockSharesOutstanding19) + float(
                commonStockSharesOutstanding19) + float(commonStockSharesOutstanding19)) / 18)
    quoteUnformatted18 = quoteUnformatted
    marketCap18 = calculateMarketCap(quoteUnformatted18, commonStockSharesOutstanding18)
    basicEPS18 = calculateBasicEPS(tTMnetIncome18, tTMpreferredDivs18, weightedAvgCommShrsOutstanding18)
    pE18 = calculatePE(quoteUnformatted18, basicEPS18)
    pCF18 = calculatePriceToCashFlow(quoteUnformatted18,
                                     calculateOperatingCashFlowPerShare(operatingCashflow18,
                                                                        weightedAvgCommShrsOutstanding18))
    pS18 = calculatePS(quoteUnformatted18, calculateSalesPerShare(totalRevenue18, weightedAvgCommShrsOutstanding18))
    pB18 = calculatePB(quoteUnformatted18,
                       calculateMarketToBookValue(marketCap18, totalAssets18, shortLongTermDebtTotal18,
                                                  preferredStock=0))
    sustainableGrowthRate18 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout18, netIncome18)),
        calculateROE(netIncome18, totalShareholderEquity18))
    pEGRatio18 = calculatePEGRatio(pE18, (sustainableGrowthRate18 * 1800))
    earningsYield18 = calculateEarningsYield(basicEPS18, quoteUnformatted18)
    cashFlowPerShare18 = calculateOperatingCashFlowPerShare(operatingCashflow18, weightedAvgCommShrsOutstanding18)
    ebitdaPerShare18 = calculateEBITDAperShare(ebitda18, weightedAvgCommShrsOutstanding18)
    tTMDividendPayout18 = (
        (float(dividendPayout18) + float(dividendPayout19) + float(dividendPayout19) + float(dividendPayout19)))
    dividendsPerShare18 = calculateDividendsPerShare(tTMDividendPayout18, weightedAvgCommShrsOutstanding18)
    currentQuarterGrossProfitMargin18 = calculateGrossProfitMargin(totalRevenue18, costofGoodsAndServicesSold18)
    tTmTotalRevenue18 = (
    (float(totalRevenue18) + float(totalRevenue19) + float(totalRevenue19) + float(totalRevenue19)))
    tTmCOGS18 = ((float(costofGoodsAndServicesSold18) + float(costofGoodsAndServicesSold19) + float(
        costofGoodsAndServicesSold19) + float(costofGoodsAndServicesSold19)))
    tTMGrossProfitMargin18 = calculateGrossProfitMargin(tTmTotalRevenue18, tTmCOGS18)
    currentQuarterOperatingMargin18 = calculateOperatingMargin(operatingIncome18, totalRevenue18)
    tTMOperatingIncome18 = (
        (float(operatingIncome18) + float(operatingIncome19) + float(operatingIncome19) + float(operatingIncome19)))
    tTMOperatingMargin18 = calculateOperatingMargin(tTMOperatingIncome18, tTmTotalRevenue18)
    currentQuarterPreTaxMargin18 = calculatePreTaxMargin(calculateEBT(ebit18, interestExpense18), totalRevenue18)
    tTMebit18 = ((float(ebit18) + float(ebit19) + float(ebit19) + float(ebit19)))
    tTMInterestExpense18 = (
        (float(interestExpense18) + float(interestExpense19) + float(interestExpense19) + float(interestExpense19)))
    tTMPreTaxMargin18 = calculatePreTaxMargin(calculateEBT(tTMebit18, tTMInterestExpense18), tTmTotalRevenue18)
    currentQuarterNetProfitMargin18 = calculateNetProfitMargin(netIncome18, totalRevenue18)
    tTMNetProfitMargin18 = calculateNetProfitMargin(tTMnetIncome18, tTmTotalRevenue18)
    currentQuarterAvgTotalAssets18 = ((float(totalAssets18) + float(totalAssets19)) / 4)
    currentQuarterOperatingROA18 = (calculateOperatingROA(operatingIncome18, currentQuarterAvgTotalAssets18)) * 4
    tTMAvgTotalAssets18 = (
                (float(totalAssets18) + float(totalAssets19) + float(totalAssets19) + float(totalAssets19)) / 4)
    tTMOperatingROA18 = calculateOperatingROA(tTMOperatingIncome18, tTMAvgTotalAssets18)
    currentQuarterROA18 = (calculateROA(netIncome18, currentQuarterAvgTotalAssets18)) * 4
    tTMROA18 = calculateROA(tTMnetIncome18, tTMAvgTotalAssets18)
    currentQuarterReturnOnTotalCapital18 = (calculateReturnOnTotalCapital(ebit18, shortLongTermDebtTotal18,
                                                                          totalShareholderEquity18)) * 4
    tTMReturnOnTotalCapital18 = calculateReturnOnTotalCapital(tTMebit18, shortLongTermDebtTotal18,
                                                              totalShareholderEquity18)
    currentQuarterROE18 = (calculateROE(netIncome18, totalShareholderEquity18)) * 4
    tTMROE18 = calculateROE(tTMnetIncome18, totalShareholderEquity18)
    currentQuarterAvgCommonEquity18 = ((float(totalShareholderEquity18) + float(totalShareholderEquity18)) / 4)
    currentQuarterReturnOnCommonEquity18 = (calculateReturnOnCommonEquity(netIncome18, dividendPayoutPreferredStock18,
                                                                          currentQuarterAvgCommonEquity18)) * 4
    tTMAvgCommonEquity18 = ((float(totalShareholderEquity18) + float(totalShareholderEquity19) + float(
        totalShareholderEquity19) + float(totalShareholderEquity19)) / 4)
    tTMReturnOnCommonEquity18 = calculateReturnOnCommonEquity(tTMnetIncome18, tTMpreferredDivs18, tTMAvgCommonEquity18)
    debtRatio18 = calculateDebtRatio(totalLiabilities18, totalAssets18)
    debtToEquityRatio18 = calculateDebtToEquity(shortLongTermDebtTotal18, totalShareholderEquity18)
    debtToAssetRatio18 = calculateDebtToAssetRatio(shortLongTermDebtTotal18, totalAssets18)
    debtToCapitalRatio18 = calculateDebtToCapitalRatio(shortLongTermDebtTotal18, totalShareholderEquity18)

    financialLeverage18 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets18,
                                                          currentQuarterAvgCommonEquity18)
    interestCoverage18 = calculateInterestCoverageRatio(operatingCashflow18, interestExpense18, incomeTaxExpense18)
    fixedChargeCoverageRatio18 = calculateFixedChargeCoverage(ebit18, capitalLeaseObligations18, interestExpense18)

    ## tm17  VARIABLES
    # Income Statement Variables for tm17
    gross_profit17 = quarterly_statementsDump.loc['grossProfit'][2]
    try:
        gross_profit17 = int(gross_profit17)
    except Exception:
        gross_profit17 = 0
    totalRevenue17 = quarterly_statementsDump.loc['totalRevenue'][2]
    try:
        totalRevenue17 = int(totalRevenue17)
    except Exception:
        totalRevenue17 = 0
    costOfRevenue17 = quarterly_statementsDump.loc['costOfRevenue'][2]
    try:
        costOfRevenue17 = int(costOfRevenue17)
    except Exception:
        costOfRevenue17 = 0
    costofGoodsAndServicesSold17 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][2]
    try:
        costofGoodsAndServicesSold17 = int(costofGoodsAndServicesSold17)
    except Exception:
        costofGoodsAndServicesSold17 = 0
    operatingIncome17 = quarterly_statementsDump.loc['operatingIncome'][2]
    try:
        operatingIncome17 = int(operatingIncome17)
    except Exception:
        operatingIncome17 = 0
    sellingGeneralAndAdministrative17 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][2]
    try:
        sellingGeneralAndAdministrative17 = int(sellingGeneralAndAdministrative17)
    except Exception:
        sellingGeneralAndAdministrative17 = 0
    researchAndDevelopment17 = quarterly_statementsDump.loc['researchAndDevelopment'][2]
    try:
        researchAndDevelopment17 = int(researchAndDevelopment17)
    except Exception:
        researchAndDevelopment17 = 0
    operatingExpenses17 = quarterly_statementsDump.loc['operatingExpenses'][2]
    try:
        operatingExpenses17 = int(operatingExpenses17)
    except Exception:
        operatingExpenses17 = 0
    investmentIncomeNet17 = quarterly_statementsDump.loc['investmentIncomeNet'][2]
    try:
        investmentIncomeNet17 = int(investmentIncomeNet17)
    except Exception:
        investmentIncomeNet17 = 0

    netInterestIncome17 = quarterly_statementsDump.loc['netInterestIncome'][2]
    try:
        netInterestIncome17 = int(netInterestIncome17)
    except Exception:
        netInterestIncome17 = 0
    interestIncome17 = quarterly_statementsDump.loc['interestIncome'][2]
    try:
        interestIncome17 = int(interestIncome17)
    except Exception:
        interestIncome17 = 0
    interestExpense17 = quarterly_statementsDump.loc['interestExpense'][2]
    try:
        interestExpense17 = int(interestExpense17)
    except Exception:
        interestExpense17 = 0
    nonInterestIncome17 = quarterly_statementsDump.loc['nonInterestIncome'][2]
    try:
        nonInterestIncome17 = int(nonInterestIncome17)
    except Exception:
        nonInterestIncome17 = 0
    otherNonOperatingIncome17 = quarterly_statementsDump.loc['otherNonOperatingIncome'][2]
    try:
        otherNonOperatingIncome17 = int(otherNonOperatingIncome17)
    except Exception:
        otherNonOperatingIncome17 = 0
    depreciation17 = quarterly_statementsDump.loc['depreciation'][2]
    try:
        depreciation17 = int(depreciation17)
    except Exception:
        depreciation17 = 0
    depreciationAndAmortization17 = quarterly_statementsDump.loc['depreciationAndAmortization'][2]
    try:
        depreciationAndAmortization17 = int(depreciationAndAmortization17)
    except Exception:
        depreciationAndAmortization17 = 0

    incomeBeforeTax17 = quarterly_statementsDump.loc['incomeBeforeTax'][2]
    try:
        incomeBeforeTax17 = int(incomeBeforeTax17)
    except Exception:
        incomeBeforeTax17 = 0

    incomeTaxExpense17 = quarterly_statementsDump.loc['incomeTaxExpense'][2]
    try:
        incomeTaxExpense17 = int(incomeTaxExpense17)
    except Exception:
        incomeTaxExpense17 = 0
    interestAndDebtExpense17 = quarterly_statementsDump.loc['interestAndDebtExpense'][2]
    try:
        interestAndDebtExpense17 = int(interestAndDebtExpense17)
    except Exception:
        interestAndDebtExpense17 = 0
    netIncomeFromContinuingOperations17 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][2]
    try:
        netIncomeFromContinuingOperations17 = int(netIncomeFromContinuingOperations17)
    except Exception:
        netIncomeFromContinuingOperations17 = 0
    comprehensiveIncomeNetOfTax17 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][2]
    try:
        comprehensiveIncomeNetOfTax17 = int(comprehensiveIncomeNetOfTax17)
    except Exception:
        comprehensiveIncomeNetOfTax17 = 0
    ebit17 = quarterly_statementsDump.loc['ebit'][2]
    try:
        ebit17 = int(ebit17)
    except Exception:
        ebit17 = 0
    ebitda17 = quarterly_statementsDump.loc['ebitda'][2]
    try:
        ebitda17 = int(ebitda17)
    except Exception:
        ebitda17 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 2]

    # Balance Sheet Values for tm17

    totalAssets17 = quarterly_statementsDump.loc['totalAssets'][2]
    try:
        totalAssets17 = int(totalAssets17)
    except Exception:
        totalAssets17 = 0
    totalCurrentAssets17 = quarterly_statementsDump.loc['totalCurrentAssets'][2]
    try:
        totalCurrentAssets17 = int(totalCurrentAssets17)
    except Exception:
        totalCurrentAssets17 = 0
    cashAndCashEquivalentsAtCarryingValue17 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][2]
    try:
        cashAndCashEquivalentsAtCarryingValue17 = int(cashAndCashEquivalentsAtCarryingValue17)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue17 = 0
    cashAndShortTermInvestments17 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][2]
    try:
        cashAndShortTermInvestments17 = int(cashAndShortTermInvestments17)
    except Exception:
        cashAndShortTermInvestments17 = 0
    inventory17 = quarterly_statementsDump.loc['inventory'][2]
    try:
        inventory17 = int(inventory17)
    except Exception:
        inventory17 = 0
    currentNetReceivables17 = quarterly_statementsDump.loc['currentNetReceivables'][2]
    try:
        currentNetReceivables17 = int(currentNetReceivables17)
    except Exception:
        currentNetReceivables17 = 0
    totalNonCurrentAssets17 = quarterly_statementsDump.loc['totalNonCurrentAssets'][2]
    try:
        totalNonCurrentAssets17 = int(totalNonCurrentAssets17)
    except Exception:
        totalNonCurrentAssets17 = 0
    propertyPlantEquipment17 = quarterly_statementsDump.loc['propertyPlantEquipment'][2]
    try:
        propertyPlantEquipment17 = int(propertyPlantEquipment17)
    except Exception:
        propertyPlantEquipment17 = 0
    accumulatedDepreciationAmortizationPPE17 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][2]
    try:
        accumulatedDepreciationAmortizationPPE17 = int(accumulatedDepreciationAmortizationPPE17)
    except Exception:
        accumulatedDepreciationAmortizationPPE17 = 0
    intangibleAssets17 = quarterly_statementsDump.loc['intangibleAssets'][2]
    try:
        intangibleAssets17 = int(intangibleAssets17)
    except Exception:
        intangibleAssets17 = 0
    intangibleAssetsExcludingGoodwill17 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][2]
    try:
        intangibleAssetsExcludingGoodwill17 = int(intangibleAssetsExcludingGoodwill17)
    except Exception:
        intangibleAssetsExcludingGoodwill17 = 0
    goodwill17 = quarterly_statementsDump.loc['goodwill'][2]
    try:
        goodwill17 = int(goodwill17)
    except Exception:
        goodwill17 = 0
    investments17 = quarterly_statementsDump.loc['investments'][2]
    try:
        investments17 = int(investments17)
    except Exception:
        investments17 = 0
    longTermInvestments17 = quarterly_statementsDump.loc['longTermInvestments'][2]
    try:
        longTermInvestments17 = int(longTermInvestments17)
    except Exception:
        longTermInvestments17 = 0
    shortTermInvestments17 = quarterly_statementsDump.loc['shortTermInvestments'][2]
    try:
        shortTermInvestments17 = int(shortTermInvestments17)
    except Exception:
        shortTermInvestments17 = 0
    otherCurrentAssets17 = quarterly_statementsDump.loc['otherCurrentAssets'][2]
    try:
        otherCurrentAssets17 = int(otherCurrentAssets17)
    except Exception:
        otherCurrentAssets17 = 0
    otherNonCurrrentAssets17 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][2]
    try:
        otherNonCurrrentAssets17 = int(otherNonCurrrentAssets17)
    except Exception:
        otherNonCurrrentAssets17 = 0
    totalLiabilities17 = quarterly_statementsDump.loc['totalLiabilities'][2]
    try:
        totalLiabilities17 = int(totalLiabilities17)
    except Exception:
        totalLiabilities17 = 0
    totalCurrentLiabilities17 = quarterly_statementsDump.loc['totalCurrentLiabilities'][2]
    try:
        totalCurrentLiabilities17 = int(totalCurrentLiabilities17)
    except Exception:
        totalCurrentLiabilities17 = 0
    currentAccountsPayable17 = quarterly_statementsDump.loc['currentAccountsPayable'][2]
    try:
        currentAccountsPayable17 = int(currentAccountsPayable17)
    except Exception:
        currentAccountsPayable17 = 0
    deferredRevenue17 = quarterly_statementsDump.loc['deferredRevenue'][2]
    try:
        deferredRevenue17 = int(deferredRevenue17)
    except Exception:
        deferredRevenue17 = 0
    currentDebt17 = quarterly_statementsDump.loc['currentDebt'][2]
    try:
        currentDebt17 = int(currentDebt17)
    except Exception:
        currentDebt17 = 0
    shortTermDebt17 = quarterly_statementsDump.loc['shortTermDebt'][2]
    try:
        shortTermDebt17 = int(shortTermDebt17)
    except Exception:
        shortTermDebt17 = 0
    totalNonCurrentLiabilities17 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][2]
    try:
        totalNonCurrentLiabilities17 = int(totalNonCurrentLiabilities17)
    except Exception:
        totalNonCurrentLiabilities17 = 0
    capitalLeaseObligations17 = quarterly_statementsDump.loc['capitalLeaseObligations'][2]
    try:
        capitalLeaseObligations17 = int(capitalLeaseObligations17)
    except Exception:
        capitalLeaseObligations17 = 0

    longTermDebt17 = quarterly_statementsDump.loc['longTermDebt'][2]
    try:
        longTermDebt17 = int(longTermDebt17)
    except Exception:
        longTermDebt17 = 0
    currentLongTermDebt17 = quarterly_statementsDump.loc['currentLongTermDebt'][2]
    try:
        currentLongTermDebt17 = int(currentLongTermDebt17)
    except Exception:
        currentLongTermDebt17 = 0
    longTermDebtNoncurrent17 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][2]
    try:
        longTermDebtNoncurrent17 = int(longTermDebtNoncurrent17)
    except Exception:
        longTermDebtNoncurrent17 = 0
    shortLongTermDebtTotal17 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][2]
    try:
        shortLongTermDebtTotal17 = int(shortLongTermDebtTotal17)
    except Exception:
        shortLongTermDebtTotal17 = 0
    otherCurrentLiabilities17 = quarterly_statementsDump.loc['otherCurrentLiabilities'][2]
    try:
        otherCurrentLiabilities17 = int(otherCurrentLiabilities17)
    except Exception:
        otherCurrentLiabilities17 = 0
    otherNonCurrentLiabilities17 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][2]
    try:
        otherNonCurrentLiabilities17 = int(otherNonCurrentLiabilities17)
    except Exception:
        otherNonCurrentLiabilities17 = 0
    totalShareholderEquity17 = quarterly_statementsDump.loc['totalShareholderEquity'][2]
    try:
        totalShareholderEquity17 = int(totalShareholderEquity17)
    except Exception:
        totalShareholderEquity17 = 0
    treasuryStock17 = quarterly_statementsDump.loc['treasuryStock'][2]
    try:
        treasuryStock17 = int(treasuryStock17)
    except Exception:
        treasuryStock17 = 0
    retainedEarnings17 = quarterly_statementsDump.loc['retainedEarnings'][2]
    try:
        retainedEarnings17 = int(retainedEarnings17)
    except Exception:
        retainedEarnings17 = 0
    commonStock17 = quarterly_statementsDump.loc['commonStock'][2]
    try:
        commonStock17 = int(commonStock17)
    except Exception:
        commonStock17 = 0
    commonStockSharesOutstanding17 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][2]
    try:
        commonStockSharesOutstanding17 = int(commonStockSharesOutstanding17)
    except Exception:
        commonStockSharesOutstanding17 = 0

    # Cash-Flow Statement values for tm17
    operatingCashflow17 = quarterly_statementsDump.loc['operatingCashflow'][2]
    try:
        operatingCashflow17 = int(operatingCashflow17)
    except Exception:
        operatingCashflow17 = 0
    paymentsForOperatingActivities17 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][2]
    try:
        paymentsForOperatingActivities17 = int(paymentsForOperatingActivities17)
    except Exception:
        paymentsForOperatingActivities17 = 0
    proceedsFromOperatingActivities17 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][2]
    try:
        proceedsFromOperatingActivities17 = int(proceedsFromOperatingActivities17)
    except Exception:
        proceedsFromOperatingActivities17 = 0
    changeInOperatingLiabilities17 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][2]
    try:
        changeInOperatingLiabilities17 = int(changeInOperatingLiabilities17)
    except Exception:
        changeInOperatingLiabilities17 = 0
    changeInOperatingAssets17 = quarterly_statementsDump.loc['changeInOperatingAssets'][2]
    try:
        changeInOperatingAssets17 = int(changeInOperatingAssets17)
    except Exception:
        changeInOperatingAssets17 = 0
    depreciationDepletionAndAmortization17 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][2]
    try:
        depreciationDepletionAndAmortization17 = int(depreciationDepletionAndAmortization17)
    except Exception:
        depreciationDepletionAndAmortization17 = 0
    capitalExpenditures17 = quarterly_statementsDump.loc['capitalExpenditures'][2]
    try:
        capitalExpenditures17 = int(capitalExpenditures17)
    except Exception:
        capitalExpenditures17 = 0
    changeInReceivables17 = quarterly_statementsDump.loc['changeInReceivables'][2]
    try:
        changeInReceivables17 = int(changeInReceivables17)
    except Exception:
        changeInReceivables17 = 0
    changeInInventory17 = quarterly_statementsDump.loc['changeInInventory'][2]
    try:
        changeInInventory17 = int(changeInInventory17)
    except Exception:
        changeInInventory17 = 0
    profitLoss17 = quarterly_statementsDump.loc['profitLoss'][2]
    try:
        profitLoss17 = int(profitLoss17)
    except Exception:
        profitLoss17 = 0
    cashflowFromInvestment17 = quarterly_statementsDump.loc['cashflowFromInvestment'][2]
    try:
        cashflowFromInvestment17 = int(cashflowFromInvestment17)
    except Exception:
        cashflowFromInvestment17 = 0
    cashflowFromFinancing17 = quarterly_statementsDump.loc['cashflowFromFinancing'][2]
    try:
        cashflowFromFinancing17 = int(cashflowFromFinancing17)
    except Exception:
        cashflowFromFinancing17 = 0
    proceedsFromRepaymentsOfShortTermDebt17 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][2]
    try:
        proceedsFromRepaymentsOfShortTermDebt17 = int(proceedsFromRepaymentsOfShortTermDebt17)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt17 = 0
    paymentsForRepurchaseOfCommonStock17 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][2]
    try:
        paymentsForRepurchaseOfCommonStock17 = int(paymentsForRepurchaseOfCommonStock17)
    except Exception:
        paymentsForRepurchaseOfCommonStock17 = 0
    paymentsForRepurchaseOfEquity17 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][2]
    try:
        paymentsForRepurchaseOfEquity17 = int(paymentsForRepurchaseOfEquity17)
    except Exception:
        paymentsForRepurchaseOfEquity17 = 0
    paymentsForRepurchaseOfPreferredStock17 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][2]
    try:
        paymentsForRepurchaseOfPreferredStock17 = int(paymentsForRepurchaseOfPreferredStock17)
    except Exception:
        paymentsForRepurchaseOfPreferredStock17 = 0
    dividendPayout17 = quarterly_statementsDump.loc['dividendPayout'][2]
    try:
        dividendPayout17 = int(dividendPayout17)
    except Exception:
        dividendPayout17 = 0
    dividendPayoutCommonStock17 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][2]
    try:
        dividendPayoutCommonStock17 = int(dividendPayoutCommonStock17)
    except Exception:
        dividendPayoutCommonStock17 = 0
    dividendPayoutPreferredStock17 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][2]
    try:
        dividendPayoutPreferredStock17 = int(dividendPayoutPreferredStock17)
    except Exception:
        dividendPayoutPreferredStock17 = 0
    proceedsFromIssuanceOfCommonStock17 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][2]
    try:
        proceedsFromIssuanceOfCommonStock17 = int(proceedsFromIssuanceOfCommonStock17)
    except Exception:
        proceedsFromIssuanceOfCommonStock17 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet17 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][2]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet17 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet17)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet17 = 0
    proceedsFromIssuanceOfPreferredStock17 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][2]
    try:
        proceedsFromIssuanceOfPreferredStock17 = int(proceedsFromIssuanceOfPreferredStock17)
    except Exception:
        proceedsFromIssuanceOfPreferredStock17 = 0
    proceedsFromRepurchaseOfEquity17 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][2]
    try:
        proceedsFromRepurchaseOfEquity17 = int(proceedsFromRepurchaseOfEquity17)
    except Exception:
        proceedsFromRepurchaseOfEquity17 = 0
    proceedsFromSaleOfTreasuryStock17 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][2]
    try:
        proceedsFromSaleOfTreasuryStock17 = int(proceedsFromSaleOfTreasuryStock17)
    except Exception:
        proceedsFromSaleOfTreasuryStock17 = 0
    changeInCashAndCashEquivalents17 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][2]
    try:
        changeInCashAndCashEquivalents17 = int(changeInCashAndCashEquivalents17)
    except Exception:
        changeInCashAndCashEquivalents17 = 0
    changeInExchangeRate17 = quarterly_statementsDump.loc['changeInExchangeRate'][2]
    try:
        changeInExchangeRate17 = int(changeInExchangeRate17)
    except Exception:
        changeInExchangeRate17 = 0
    netIncome17 = quarterly_statementsDump.loc['netIncome'][2]
    try:
        netIncome17 = int(netIncome17)
    except Exception:
        netIncome17 = 0

    tTMnetIncome17 = (float(netIncome17) + float(netIncome18) + float(netIncome19) + float(netIncome19))
    try:
        tTMpreferredDivs17 = (int(dividendPayoutPreferredStock17) + int(dividendPayoutPreferredStock18) + int(
            dividendPayoutPreferredStock19) + int(dividendPayoutPreferredStock19))
    except Exception:
        tTMpreferredDivs17 = 0
    weightedAvgCommShrsOutstanding17 = (
            (float(commonStockSharesOutstanding17) + float(commonStockSharesOutstanding18) + float(
                commonStockSharesOutstanding19) + float(commonStockSharesOutstanding19)) / 17)
    quoteUnformatted17 = quoteUnformatted
    marketCap17 = calculateMarketCap(quoteUnformatted17, commonStockSharesOutstanding17)
    basicEPS17 = calculateBasicEPS(tTMnetIncome17, tTMpreferredDivs17, weightedAvgCommShrsOutstanding17)
    pE17 = calculatePE(quoteUnformatted17, basicEPS17)
    pCF17 = calculatePriceToCashFlow(quoteUnformatted17,
                                     calculateOperatingCashFlowPerShare(operatingCashflow17,
                                                                        weightedAvgCommShrsOutstanding17))
    pS17 = calculatePS(quoteUnformatted17, calculateSalesPerShare(totalRevenue17, weightedAvgCommShrsOutstanding17))
    pB17 = calculatePB(quoteUnformatted17,
                       calculateMarketToBookValue(marketCap17, totalAssets17, shortLongTermDebtTotal17,
                                                  preferredStock=0))
    sustainableGrowthRate17 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout17, netIncome17)),
        calculateROE(netIncome17, totalShareholderEquity17))
    pEGRatio17 = calculatePEGRatio(pE17, (sustainableGrowthRate17 * 1700))
    earningsYield17 = calculateEarningsYield(basicEPS17, quoteUnformatted17)
    cashFlowPerShare17 = calculateOperatingCashFlowPerShare(operatingCashflow17, weightedAvgCommShrsOutstanding17)
    ebitdaPerShare17 = calculateEBITDAperShare(ebitda17, weightedAvgCommShrsOutstanding17)
    tTMDividendPayout17 = (
        (float(dividendPayout17) + float(dividendPayout18) + float(dividendPayout19) + float(dividendPayout19)))
    dividendsPerShare17 = calculateDividendsPerShare(tTMDividendPayout17, weightedAvgCommShrsOutstanding17)
    currentQuarterGrossProfitMargin17 = calculateGrossProfitMargin(totalRevenue17, costofGoodsAndServicesSold17)
    tTmTotalRevenue17 = (
    (float(totalRevenue17) + float(totalRevenue18) + float(totalRevenue19) + float(totalRevenue19)))
    tTmCOGS17 = ((float(costofGoodsAndServicesSold17) + float(costofGoodsAndServicesSold18) + float(
        costofGoodsAndServicesSold19) + float(costofGoodsAndServicesSold19)))
    tTMGrossProfitMargin17 = calculateGrossProfitMargin(tTmTotalRevenue17, tTmCOGS17)
    currentQuarterOperatingMargin17 = calculateOperatingMargin(operatingIncome17, totalRevenue17)
    tTMOperatingIncome17 = (
        (float(operatingIncome17) + float(operatingIncome18) + float(operatingIncome19) + float(operatingIncome19)))
    tTMOperatingMargin17 = calculateOperatingMargin(tTMOperatingIncome17, tTmTotalRevenue17)
    currentQuarterPreTaxMargin17 = calculatePreTaxMargin(calculateEBT(ebit17, interestExpense17), totalRevenue17)
    tTMebit17 = ((float(ebit17) + float(ebit18) + float(ebit19) + float(ebit19)))
    tTMInterestExpense17 = (
        (float(interestExpense17) + float(interestExpense18) + float(interestExpense19) + float(interestExpense19)))
    tTMPreTaxMargin17 = calculatePreTaxMargin(calculateEBT(tTMebit17, tTMInterestExpense17), tTmTotalRevenue17)
    currentQuarterNetProfitMargin17 = calculateNetProfitMargin(netIncome17, totalRevenue17)
    tTMNetProfitMargin17 = calculateNetProfitMargin(tTMnetIncome17, tTmTotalRevenue17)
    currentQuarterAvgTotalAssets17 = ((float(totalAssets17) + float(totalAssets18)) / 4)
    currentQuarterOperatingROA17 = (calculateOperatingROA(operatingIncome17, currentQuarterAvgTotalAssets17)) * 4
    tTMAvgTotalAssets17 = (
                (float(totalAssets17) + float(totalAssets18) + float(totalAssets19) + float(totalAssets19)) / 4)
    tTMOperatingROA17 = calculateOperatingROA(tTMOperatingIncome17, tTMAvgTotalAssets17)
    currentQuarterROA17 = (calculateROA(netIncome17, currentQuarterAvgTotalAssets17)) * 4
    tTMROA17 = calculateROA(tTMnetIncome17, tTMAvgTotalAssets17)
    currentQuarterReturnOnTotalCapital17 = (calculateReturnOnTotalCapital(ebit17, shortLongTermDebtTotal17,
                                                                          totalShareholderEquity17)) * 4
    tTMReturnOnTotalCapital17 = calculateReturnOnTotalCapital(tTMebit17, shortLongTermDebtTotal17,
                                                              totalShareholderEquity17)
    currentQuarterROE17 = (calculateROE(netIncome17, totalShareholderEquity17)) * 4
    tTMROE17 = calculateROE(tTMnetIncome17, totalShareholderEquity17)
    currentQuarterAvgCommonEquity17 = ((float(totalShareholderEquity17) + float(totalShareholderEquity17)) / 4)
    currentQuarterReturnOnCommonEquity17 = (calculateReturnOnCommonEquity(netIncome17, dividendPayoutPreferredStock17,
                                                                          currentQuarterAvgCommonEquity17)) * 4
    tTMAvgCommonEquity17 = ((float(totalShareholderEquity17) + float(totalShareholderEquity18) + float(
        totalShareholderEquity19) + float(totalShareholderEquity19)) / 4)
    tTMReturnOnCommonEquity17 = calculateReturnOnCommonEquity(tTMnetIncome17, tTMpreferredDivs17, tTMAvgCommonEquity17)
    debtRatio17 = calculateDebtRatio(totalLiabilities17, totalAssets17)
    debtToEquityRatio17 = calculateDebtToEquity(shortLongTermDebtTotal17, totalShareholderEquity17)
    debtToAssetRatio17 = calculateDebtToAssetRatio(shortLongTermDebtTotal17, totalAssets17)
    debtToCapitalRatio17 = calculateDebtToCapitalRatio(shortLongTermDebtTotal17, totalShareholderEquity17)

    financialLeverage17 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets17,
                                                          currentQuarterAvgCommonEquity17)
    interestCoverage17 = calculateInterestCoverageRatio(operatingCashflow17, interestExpense17, incomeTaxExpense17)
    fixedChargeCoverageRatio17 = calculateFixedChargeCoverage(ebit17, capitalLeaseObligations17, interestExpense17)

    ## tm16  VARIABLES
    # Income Statement Variables for tm16
    gross_profit16 = quarterly_statementsDump.loc['grossProfit'][3]
    try:
        gross_profit16 = int(gross_profit16)
    except Exception:
        gross_profit16 = 0
    totalRevenue16 = quarterly_statementsDump.loc['totalRevenue'][3]
    try:
        totalRevenue16 = int(totalRevenue16)
    except Exception:
        totalRevenue16 = 0
    costOfRevenue16 = quarterly_statementsDump.loc['costOfRevenue'][3]
    try:
        costOfRevenue16 = int(costOfRevenue16)
    except Exception:
        costOfRevenue16 = 0
    costofGoodsAndServicesSold16 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][3]
    try:
        costofGoodsAndServicesSold16 = int(costofGoodsAndServicesSold16)
    except Exception:
        costofGoodsAndServicesSold16 = 0
    operatingIncome16 = quarterly_statementsDump.loc['operatingIncome'][3]
    try:
        operatingIncome16 = int(operatingIncome16)
    except Exception:
        operatingIncome16 = 0
    sellingGeneralAndAdministrative16 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][3]
    try:
        sellingGeneralAndAdministrative16 = int(sellingGeneralAndAdministrative16)
    except Exception:
        sellingGeneralAndAdministrative16 = 0
    researchAndDevelopment16 = quarterly_statementsDump.loc['researchAndDevelopment'][3]
    try:
        researchAndDevelopment16 = int(researchAndDevelopment16)
    except Exception:
        researchAndDevelopment16 = 0
    operatingExpenses16 = quarterly_statementsDump.loc['operatingExpenses'][3]
    try:
        operatingExpenses16 = int(operatingExpenses16)
    except Exception:
        operatingExpenses16 = 0
    investmentIncomeNet16 = quarterly_statementsDump.loc['investmentIncomeNet'][3]
    try:
        investmentIncomeNet16 = int(investmentIncomeNet16)
    except Exception:
        investmentIncomeNet16 = 0

    netInterestIncome16 = quarterly_statementsDump.loc['netInterestIncome'][3]
    try:
        netInterestIncome16 = int(netInterestIncome16)
    except Exception:
        netInterestIncome16 = 0
    interestIncome16 = quarterly_statementsDump.loc['interestIncome'][3]
    try:
        interestIncome16 = int(interestIncome16)
    except Exception:
        interestIncome16 = 0
    interestExpense16 = quarterly_statementsDump.loc['interestExpense'][3]
    try:
        interestExpense16 = int(interestExpense16)
    except Exception:
        interestExpense16 = 0
    nonInterestIncome16 = quarterly_statementsDump.loc['nonInterestIncome'][3]
    try:
        nonInterestIncome16 = int(nonInterestIncome16)
    except Exception:
        nonInterestIncome16 = 0
    otherNonOperatingIncome16 = quarterly_statementsDump.loc['otherNonOperatingIncome'][3]
    try:
        otherNonOperatingIncome16 = int(otherNonOperatingIncome16)
    except Exception:
        otherNonOperatingIncome16 = 0
    depreciation16 = quarterly_statementsDump.loc['depreciation'][3]
    try:
        depreciation16 = int(depreciation16)
    except Exception:
        depreciation16 = 0
    depreciationAndAmortization16 = quarterly_statementsDump.loc['depreciationAndAmortization'][3]
    try:
        depreciationAndAmortization16 = int(depreciationAndAmortization16)
    except Exception:
        depreciationAndAmortization16 = 0

    incomeBeforeTax16 = quarterly_statementsDump.loc['incomeBeforeTax'][3]
    try:
        incomeBeforeTax16 = int(incomeBeforeTax16)
    except Exception:
        incomeBeforeTax16 = 0

    incomeTaxExpense16 = quarterly_statementsDump.loc['incomeTaxExpense'][3]
    try:
        incomeTaxExpense16 = int(incomeTaxExpense16)
    except Exception:
        incomeTaxExpense16 = 0
    interestAndDebtExpense16 = quarterly_statementsDump.loc['interestAndDebtExpense'][3]
    try:
        interestAndDebtExpense16 = int(interestAndDebtExpense16)
    except Exception:
        interestAndDebtExpense16 = 0
    netIncomeFromContinuingOperations16 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][3]
    try:
        netIncomeFromContinuingOperations16 = int(netIncomeFromContinuingOperations16)
    except Exception:
        netIncomeFromContinuingOperations16 = 0
    comprehensiveIncomeNetOfTax16 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][3]
    try:
        comprehensiveIncomeNetOfTax16 = int(comprehensiveIncomeNetOfTax16)
    except Exception:
        comprehensiveIncomeNetOfTax16 = 0
    ebit16 = quarterly_statementsDump.loc['ebit'][3]
    try:
        ebit16 = int(ebit16)
    except Exception:
        ebit16 = 0
    ebitda16 = quarterly_statementsDump.loc['ebitda'][3]
    try:
        ebitda16 = int(ebitda16)
    except Exception:
        ebitda16 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 3]

    # Balance Sheet Values for tm16

    totalAssets16 = quarterly_statementsDump.loc['totalAssets'][3]
    try:
        totalAssets16 = int(totalAssets16)
    except Exception:
        totalAssets16 = 0
    totalCurrentAssets16 = quarterly_statementsDump.loc['totalCurrentAssets'][3]
    try:
        totalCurrentAssets16 = int(totalCurrentAssets16)
    except Exception:
        totalCurrentAssets16 = 0
    cashAndCashEquivalentsAtCarryingValue16 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][3]
    try:
        cashAndCashEquivalentsAtCarryingValue16 = int(cashAndCashEquivalentsAtCarryingValue16)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue16 = 0
    cashAndShortTermInvestments16 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][3]
    try:
        cashAndShortTermInvestments16 = int(cashAndShortTermInvestments16)
    except Exception:
        cashAndShortTermInvestments16 = 0
    inventory16 = quarterly_statementsDump.loc['inventory'][3]
    try:
        inventory16 = int(inventory16)
    except Exception:
        inventory16 = 0
    currentNetReceivables16 = quarterly_statementsDump.loc['currentNetReceivables'][3]
    try:
        currentNetReceivables16 = int(currentNetReceivables16)
    except Exception:
        currentNetReceivables16 = 0
    totalNonCurrentAssets16 = quarterly_statementsDump.loc['totalNonCurrentAssets'][3]
    try:
        totalNonCurrentAssets16 = int(totalNonCurrentAssets16)
    except Exception:
        totalNonCurrentAssets16 = 0
    propertyPlantEquipment16 = quarterly_statementsDump.loc['propertyPlantEquipment'][3]
    try:
        propertyPlantEquipment16 = int(propertyPlantEquipment16)
    except Exception:
        propertyPlantEquipment16 = 0
    accumulatedDepreciationAmortizationPPE16 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][3]
    try:
        accumulatedDepreciationAmortizationPPE16 = int(accumulatedDepreciationAmortizationPPE16)
    except Exception:
        accumulatedDepreciationAmortizationPPE16 = 0
    intangibleAssets16 = quarterly_statementsDump.loc['intangibleAssets'][3]
    try:
        intangibleAssets16 = int(intangibleAssets16)
    except Exception:
        intangibleAssets16 = 0
    intangibleAssetsExcludingGoodwill16 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][3]
    try:
        intangibleAssetsExcludingGoodwill16 = int(intangibleAssetsExcludingGoodwill16)
    except Exception:
        intangibleAssetsExcludingGoodwill16 = 0
    goodwill16 = quarterly_statementsDump.loc['goodwill'][3]
    try:
        goodwill16 = int(goodwill16)
    except Exception:
        goodwill16 = 0
    investments16 = quarterly_statementsDump.loc['investments'][3]
    try:
        investments16 = int(investments16)
    except Exception:
        investments16 = 0
    longTermInvestments16 = quarterly_statementsDump.loc['longTermInvestments'][3]
    try:
        longTermInvestments16 = int(longTermInvestments16)
    except Exception:
        longTermInvestments16 = 0
    shortTermInvestments16 = quarterly_statementsDump.loc['shortTermInvestments'][3]
    try:
        shortTermInvestments16 = int(shortTermInvestments16)
    except Exception:
        shortTermInvestments16 = 0
    otherCurrentAssets16 = quarterly_statementsDump.loc['otherCurrentAssets'][3]
    try:
        otherCurrentAssets16 = int(otherCurrentAssets16)
    except Exception:
        otherCurrentAssets16 = 0
    otherNonCurrrentAssets16 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][3]
    try:
        otherNonCurrrentAssets16 = int(otherNonCurrrentAssets16)
    except Exception:
        otherNonCurrrentAssets16 = 0
    totalLiabilities16 = quarterly_statementsDump.loc['totalLiabilities'][3]
    try:
        totalLiabilities16 = int(totalLiabilities16)
    except Exception:
        totalLiabilities16 = 0
    totalCurrentLiabilities16 = quarterly_statementsDump.loc['totalCurrentLiabilities'][3]
    try:
        totalCurrentLiabilities16 = int(totalCurrentLiabilities16)
    except Exception:
        totalCurrentLiabilities16 = 0
    currentAccountsPayable16 = quarterly_statementsDump.loc['currentAccountsPayable'][3]
    try:
        currentAccountsPayable16 = int(currentAccountsPayable16)
    except Exception:
        currentAccountsPayable16 = 0
    deferredRevenue16 = quarterly_statementsDump.loc['deferredRevenue'][3]
    try:
        deferredRevenue16 = int(deferredRevenue16)
    except Exception:
        deferredRevenue16 = 0
    currentDebt16 = quarterly_statementsDump.loc['currentDebt'][3]
    try:
        currentDebt16 = int(currentDebt16)
    except Exception:
        currentDebt16 = 0
    shortTermDebt16 = quarterly_statementsDump.loc['shortTermDebt'][3]
    try:
        shortTermDebt16 = int(shortTermDebt16)
    except Exception:
        shortTermDebt16 = 0
    totalNonCurrentLiabilities16 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][3]
    try:
        totalNonCurrentLiabilities16 = int(totalNonCurrentLiabilities16)
    except Exception:
        totalNonCurrentLiabilities16 = 0
    capitalLeaseObligations16 = quarterly_statementsDump.loc['capitalLeaseObligations'][3]
    try:
        capitalLeaseObligations16 = int(capitalLeaseObligations16)
    except Exception:
        capitalLeaseObligations16 = 0

    longTermDebt16 = quarterly_statementsDump.loc['longTermDebt'][3]
    try:
        longTermDebt16 = int(longTermDebt16)
    except Exception:
        longTermDebt16 = 0
    currentLongTermDebt16 = quarterly_statementsDump.loc['currentLongTermDebt'][3]
    try:
        currentLongTermDebt16 = int(currentLongTermDebt16)
    except Exception:
        currentLongTermDebt16 = 0
    longTermDebtNoncurrent16 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][3]
    try:
        longTermDebtNoncurrent16 = int(longTermDebtNoncurrent16)
    except Exception:
        longTermDebtNoncurrent16 = 0
    shortLongTermDebtTotal16 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][3]
    try:
        shortLongTermDebtTotal16 = int(shortLongTermDebtTotal16)
    except Exception:
        shortLongTermDebtTotal16 = 0
    otherCurrentLiabilities16 = quarterly_statementsDump.loc['otherCurrentLiabilities'][3]
    try:
        otherCurrentLiabilities16 = int(otherCurrentLiabilities16)
    except Exception:
        otherCurrentLiabilities16 = 0
    otherNonCurrentLiabilities16 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][3]
    try:
        otherNonCurrentLiabilities16 = int(otherNonCurrentLiabilities16)
    except Exception:
        otherNonCurrentLiabilities16 = 0
    totalShareholderEquity16 = quarterly_statementsDump.loc['totalShareholderEquity'][3]
    try:
        totalShareholderEquity16 = int(totalShareholderEquity16)
    except Exception:
        totalShareholderEquity16 = 0
    treasuryStock16 = quarterly_statementsDump.loc['treasuryStock'][3]
    try:
        treasuryStock16 = int(treasuryStock16)
    except Exception:
        treasuryStock16 = 0
    retainedEarnings16 = quarterly_statementsDump.loc['retainedEarnings'][3]
    try:
        retainedEarnings16 = int(retainedEarnings16)
    except Exception:
        retainedEarnings16 = 0
    commonStock16 = quarterly_statementsDump.loc['commonStock'][3]
    try:
        commonStock16 = int(commonStock16)
    except Exception:
        commonStock16 = 0
    commonStockSharesOutstanding16 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][3]
    try:
        commonStockSharesOutstanding16 = int(commonStockSharesOutstanding16)
    except Exception:
        commonStockSharesOutstanding16 = 0

    # Cash-Flow Statement values for tm16
    operatingCashflow16 = quarterly_statementsDump.loc['operatingCashflow'][3]
    try:
        operatingCashflow16 = int(operatingCashflow16)
    except Exception:
        operatingCashflow16 = 0
    paymentsForOperatingActivities16 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][3]
    try:
        paymentsForOperatingActivities16 = int(paymentsForOperatingActivities16)
    except Exception:
        paymentsForOperatingActivities16 = 0
    proceedsFromOperatingActivities16 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][3]
    try:
        proceedsFromOperatingActivities16 = int(proceedsFromOperatingActivities16)
    except Exception:
        proceedsFromOperatingActivities16 = 0
    changeInOperatingLiabilities16 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][3]
    try:
        changeInOperatingLiabilities16 = int(changeInOperatingLiabilities16)
    except Exception:
        changeInOperatingLiabilities16 = 0
    changeInOperatingAssets16 = quarterly_statementsDump.loc['changeInOperatingAssets'][3]
    try:
        changeInOperatingAssets16 = int(changeInOperatingAssets16)
    except Exception:
        changeInOperatingAssets16 = 0
    depreciationDepletionAndAmortization16 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][3]
    try:
        depreciationDepletionAndAmortization16 = int(depreciationDepletionAndAmortization16)
    except Exception:
        depreciationDepletionAndAmortization16 = 0
    capitalExpenditures16 = quarterly_statementsDump.loc['capitalExpenditures'][3]
    try:
        capitalExpenditures16 = int(capitalExpenditures16)
    except Exception:
        capitalExpenditures16 = 0
    changeInReceivables16 = quarterly_statementsDump.loc['changeInReceivables'][3]
    try:
        changeInReceivables16 = int(changeInReceivables16)
    except Exception:
        changeInReceivables16 = 0
    changeInInventory16 = quarterly_statementsDump.loc['changeInInventory'][3]
    try:
        changeInInventory16 = int(changeInInventory16)
    except Exception:
        changeInInventory16 = 0
    profitLoss16 = quarterly_statementsDump.loc['profitLoss'][3]
    try:
        profitLoss16 = int(profitLoss16)
    except Exception:
        profitLoss16 = 0
    cashflowFromInvestment16 = quarterly_statementsDump.loc['cashflowFromInvestment'][3]
    try:
        cashflowFromInvestment16 = int(cashflowFromInvestment16)
    except Exception:
        cashflowFromInvestment16 = 0
    cashflowFromFinancing16 = quarterly_statementsDump.loc['cashflowFromFinancing'][3]
    try:
        cashflowFromFinancing16 = int(cashflowFromFinancing16)
    except Exception:
        cashflowFromFinancing16 = 0
    proceedsFromRepaymentsOfShortTermDebt16 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][3]
    try:
        proceedsFromRepaymentsOfShortTermDebt16 = int(proceedsFromRepaymentsOfShortTermDebt16)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt16 = 0
    paymentsForRepurchaseOfCommonStock16 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][3]
    try:
        paymentsForRepurchaseOfCommonStock16 = int(paymentsForRepurchaseOfCommonStock16)
    except Exception:
        paymentsForRepurchaseOfCommonStock16 = 0
    paymentsForRepurchaseOfEquity16 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][3]
    try:
        paymentsForRepurchaseOfEquity16 = int(paymentsForRepurchaseOfEquity16)
    except Exception:
        paymentsForRepurchaseOfEquity16 = 0
    paymentsForRepurchaseOfPreferredStock16 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][3]
    try:
        paymentsForRepurchaseOfPreferredStock16 = int(paymentsForRepurchaseOfPreferredStock16)
    except Exception:
        paymentsForRepurchaseOfPreferredStock16 = 0
    dividendPayout16 = quarterly_statementsDump.loc['dividendPayout'][3]
    try:
        dividendPayout16 = int(dividendPayout16)
    except Exception:
        dividendPayout16 = 0
    dividendPayoutCommonStock16 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][3]
    try:
        dividendPayoutCommonStock16 = int(dividendPayoutCommonStock16)
    except Exception:
        dividendPayoutCommonStock16 = 0
    dividendPayoutPreferredStock16 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][3]
    try:
        dividendPayoutPreferredStock16 = int(dividendPayoutPreferredStock16)
    except Exception:
        dividendPayoutPreferredStock16 = 0
    proceedsFromIssuanceOfCommonStock16 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][3]
    try:
        proceedsFromIssuanceOfCommonStock16 = int(proceedsFromIssuanceOfCommonStock16)
    except Exception:
        proceedsFromIssuanceOfCommonStock16 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet16 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][3]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet16 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet16)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet16 = 0
    proceedsFromIssuanceOfPreferredStock16 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][3]
    try:
        proceedsFromIssuanceOfPreferredStock16 = int(proceedsFromIssuanceOfPreferredStock16)
    except Exception:
        proceedsFromIssuanceOfPreferredStock16 = 0
    proceedsFromRepurchaseOfEquity16 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][3]
    try:
        proceedsFromRepurchaseOfEquity16 = int(proceedsFromRepurchaseOfEquity16)
    except Exception:
        proceedsFromRepurchaseOfEquity16 = 0
    proceedsFromSaleOfTreasuryStock16 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][3]
    try:
        proceedsFromSaleOfTreasuryStock16 = int(proceedsFromSaleOfTreasuryStock16)
    except Exception:
        proceedsFromSaleOfTreasuryStock16 = 0
    changeInCashAndCashEquivalents16 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][3]
    try:
        changeInCashAndCashEquivalents16 = int(changeInCashAndCashEquivalents16)
    except Exception:
        changeInCashAndCashEquivalents16 = 0
    changeInExchangeRate16 = quarterly_statementsDump.loc['changeInExchangeRate'][3]
    try:
        changeInExchangeRate16 = int(changeInExchangeRate16)
    except Exception:
        changeInExchangeRate16 = 0
    netIncome16 = quarterly_statementsDump.loc['netIncome'][3]
    try:
        netIncome16 = int(netIncome16)
    except Exception:
        netIncome16 = 0

    tTMnetIncome16 = (float(netIncome16) + float(netIncome17) + float(netIncome18) + float(netIncome19))
    try:
        tTMpreferredDivs16 = (int(dividendPayoutPreferredStock16) + int(dividendPayoutPreferredStock17) + int(
            dividendPayoutPreferredStock18) + int(dividendPayoutPreferredStock19))
    except Exception:
        tTMpreferredDivs16 = 0
    weightedAvgCommShrsOutstanding16 = (
            (float(commonStockSharesOutstanding16) + float(commonStockSharesOutstanding17) + float(
                commonStockSharesOutstanding18) + float(commonStockSharesOutstanding19)) / 16)
    quoteUnformatted16 = quoteUnformatted
    marketCap16 = calculateMarketCap(quoteUnformatted16, commonStockSharesOutstanding16)
    basicEPS16 = calculateBasicEPS(tTMnetIncome16, tTMpreferredDivs16, weightedAvgCommShrsOutstanding16)
    pE16 = calculatePE(quoteUnformatted16, basicEPS16)
    pCF16 = calculatePriceToCashFlow(quoteUnformatted16,
                                     calculateOperatingCashFlowPerShare(operatingCashflow16,
                                                                        weightedAvgCommShrsOutstanding16))
    pS16 = calculatePS(quoteUnformatted16, calculateSalesPerShare(totalRevenue16, weightedAvgCommShrsOutstanding16))
    pB16 = calculatePB(quoteUnformatted16,
                       calculateMarketToBookValue(marketCap16, totalAssets16, shortLongTermDebtTotal16,
                                                  preferredStock=0))
    sustainableGrowthRate16 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout16, netIncome16)),
        calculateROE(netIncome16, totalShareholderEquity16))
    pEGRatio16 = calculatePEGRatio(pE16, (sustainableGrowthRate16 * 1600))
    earningsYield16 = calculateEarningsYield(basicEPS16, quoteUnformatted16)
    cashFlowPerShare16 = calculateOperatingCashFlowPerShare(operatingCashflow16, weightedAvgCommShrsOutstanding16)
    ebitdaPerShare16 = calculateEBITDAperShare(ebitda16, weightedAvgCommShrsOutstanding16)
    tTMDividendPayout16 = (
        (float(dividendPayout16) + float(dividendPayout17) + float(dividendPayout18) + float(dividendPayout19)))
    dividendsPerShare16 = calculateDividendsPerShare(tTMDividendPayout16, weightedAvgCommShrsOutstanding16)
    currentQuarterGrossProfitMargin16 = calculateGrossProfitMargin(totalRevenue16, costofGoodsAndServicesSold16)
    tTmTotalRevenue16 = (
    (float(totalRevenue16) + float(totalRevenue17) + float(totalRevenue18) + float(totalRevenue19)))
    tTmCOGS16 = ((float(costofGoodsAndServicesSold16) + float(costofGoodsAndServicesSold17) + float(
        costofGoodsAndServicesSold18) + float(costofGoodsAndServicesSold19)))
    tTMGrossProfitMargin16 = calculateGrossProfitMargin(tTmTotalRevenue16, tTmCOGS16)
    currentQuarterOperatingMargin16 = calculateOperatingMargin(operatingIncome16, totalRevenue16)
    tTMOperatingIncome16 = (
        (float(operatingIncome16) + float(operatingIncome17) + float(operatingIncome18) + float(operatingIncome19)))
    tTMOperatingMargin16 = calculateOperatingMargin(tTMOperatingIncome16, tTmTotalRevenue16)
    currentQuarterPreTaxMargin16 = calculatePreTaxMargin(calculateEBT(ebit16, interestExpense16), totalRevenue16)
    tTMebit16 = ((float(ebit16) + float(ebit17) + float(ebit18) + float(ebit19)))
    tTMInterestExpense16 = (
        (float(interestExpense16) + float(interestExpense17) + float(interestExpense18) + float(interestExpense19)))
    tTMPreTaxMargin16 = calculatePreTaxMargin(calculateEBT(tTMebit16, tTMInterestExpense16), tTmTotalRevenue16)
    currentQuarterNetProfitMargin16 = calculateNetProfitMargin(netIncome16, totalRevenue16)
    tTMNetProfitMargin16 = calculateNetProfitMargin(tTMnetIncome16, tTmTotalRevenue16)
    currentQuarterAvgTotalAssets16 = ((float(totalAssets16) + float(totalAssets17)) / 4)
    currentQuarterOperatingROA16 = (calculateOperatingROA(operatingIncome16, currentQuarterAvgTotalAssets16)) * 4
    tTMAvgTotalAssets16 = (
                (float(totalAssets16) + float(totalAssets17) + float(totalAssets18) + float(totalAssets19)) / 4)
    tTMOperatingROA16 = calculateOperatingROA(tTMOperatingIncome16, tTMAvgTotalAssets16)
    currentQuarterROA16 = (calculateROA(netIncome16, currentQuarterAvgTotalAssets16)) * 4
    tTMROA16 = calculateROA(tTMnetIncome16, tTMAvgTotalAssets16)
    currentQuarterReturnOnTotalCapital16 = (calculateReturnOnTotalCapital(ebit16, shortLongTermDebtTotal16,
                                                                          totalShareholderEquity16)) * 4
    tTMReturnOnTotalCapital16 = calculateReturnOnTotalCapital(tTMebit16, shortLongTermDebtTotal16,
                                                              totalShareholderEquity16)
    currentQuarterROE16 = (calculateROE(netIncome16, totalShareholderEquity16)) * 4
    tTMROE16 = calculateROE(tTMnetIncome16, totalShareholderEquity16)
    currentQuarterAvgCommonEquity16 = ((float(totalShareholderEquity16) + float(totalShareholderEquity16)) / 4)
    currentQuarterReturnOnCommonEquity16 = (calculateReturnOnCommonEquity(netIncome16, dividendPayoutPreferredStock16,
                                                                          currentQuarterAvgCommonEquity16)) * 4
    tTMAvgCommonEquity16 = ((float(totalShareholderEquity16) + float(totalShareholderEquity17) + float(
        totalShareholderEquity18) + float(totalShareholderEquity19)) / 4)
    tTMReturnOnCommonEquity16 = calculateReturnOnCommonEquity(tTMnetIncome16, tTMpreferredDivs16, tTMAvgCommonEquity16)
    debtRatio16 = calculateDebtRatio(totalLiabilities16, totalAssets16)
    debtToEquityRatio16 = calculateDebtToEquity(shortLongTermDebtTotal16, totalShareholderEquity16)
    debtToAssetRatio16 = calculateDebtToAssetRatio(shortLongTermDebtTotal16, totalAssets16)
    debtToCapitalRatio16 = calculateDebtToCapitalRatio(shortLongTermDebtTotal16, totalShareholderEquity16)

    financialLeverage16 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets16,
                                                          currentQuarterAvgCommonEquity16)
    interestCoverage16 = calculateInterestCoverageRatio(operatingCashflow16, interestExpense16, incomeTaxExpense16)
    fixedChargeCoverageRatio16 = calculateFixedChargeCoverage(ebit16, capitalLeaseObligations16, interestExpense16)

    ## tm15  VARIABLES
    # Income Statement Variables for tm15
    gross_profit15 = quarterly_statementsDump.loc['grossProfit'][4]
    try:
        gross_profit15 = int(gross_profit15)
    except Exception:
        gross_profit15 = 0
    totalRevenue15 = quarterly_statementsDump.loc['totalRevenue'][4]
    try:
        totalRevenue15 = int(totalRevenue15)
    except Exception:
        totalRevenue15 = 0
    costOfRevenue15 = quarterly_statementsDump.loc['costOfRevenue'][4]
    try:
        costOfRevenue15 = int(costOfRevenue15)
    except Exception:
        costOfRevenue15 = 0
    costofGoodsAndServicesSold15 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][4]
    try:
        costofGoodsAndServicesSold15 = int(costofGoodsAndServicesSold15)
    except Exception:
        costofGoodsAndServicesSold15 = 0
    operatingIncome15 = quarterly_statementsDump.loc['operatingIncome'][4]
    try:
        operatingIncome15 = int(operatingIncome15)
    except Exception:
        operatingIncome15 = 0
    sellingGeneralAndAdministrative15 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][4]
    try:
        sellingGeneralAndAdministrative15 = int(sellingGeneralAndAdministrative15)
    except Exception:
        sellingGeneralAndAdministrative15 = 0
    researchAndDevelopment15 = quarterly_statementsDump.loc['researchAndDevelopment'][4]
    try:
        researchAndDevelopment15 = int(researchAndDevelopment15)
    except Exception:
        researchAndDevelopment15 = 0
    operatingExpenses15 = quarterly_statementsDump.loc['operatingExpenses'][4]
    try:
        operatingExpenses15 = int(operatingExpenses15)
    except Exception:
        operatingExpenses15 = 0
    investmentIncomeNet15 = quarterly_statementsDump.loc['investmentIncomeNet'][4]
    try:
        investmentIncomeNet15 = int(investmentIncomeNet15)
    except Exception:
        investmentIncomeNet15 = 0

    netInterestIncome15 = quarterly_statementsDump.loc['netInterestIncome'][4]
    try:
        netInterestIncome15 = int(netInterestIncome15)
    except Exception:
        netInterestIncome15 = 0
    interestIncome15 = quarterly_statementsDump.loc['interestIncome'][4]
    try:
        interestIncome15 = int(interestIncome15)
    except Exception:
        interestIncome15 = 0
    interestExpense15 = quarterly_statementsDump.loc['interestExpense'][4]
    try:
        interestExpense15 = int(interestExpense15)
    except Exception:
        interestExpense15 = 0
    nonInterestIncome15 = quarterly_statementsDump.loc['nonInterestIncome'][4]
    try:
        nonInterestIncome15 = int(nonInterestIncome15)
    except Exception:
        nonInterestIncome15 = 0
    otherNonOperatingIncome15 = quarterly_statementsDump.loc['otherNonOperatingIncome'][4]
    try:
        otherNonOperatingIncome15 = int(otherNonOperatingIncome15)
    except Exception:
        otherNonOperatingIncome15 = 0
    depreciation15 = quarterly_statementsDump.loc['depreciation'][4]
    try:
        depreciation15 = int(depreciation15)
    except Exception:
        depreciation15 = 0
    depreciationAndAmortization15 = quarterly_statementsDump.loc['depreciationAndAmortization'][4]
    try:
        depreciationAndAmortization15 = int(depreciationAndAmortization15)
    except Exception:
        depreciationAndAmortization15 = 0

    incomeBeforeTax15 = quarterly_statementsDump.loc['incomeBeforeTax'][4]
    try:
        incomeBeforeTax15 = int(incomeBeforeTax15)
    except Exception:
        incomeBeforeTax15 = 0

    incomeTaxExpense15 = quarterly_statementsDump.loc['incomeTaxExpense'][4]
    try:
        incomeTaxExpense15 = int(incomeTaxExpense15)
    except Exception:
        incomeTaxExpense15 = 0
    interestAndDebtExpense15 = quarterly_statementsDump.loc['interestAndDebtExpense'][4]
    try:
        interestAndDebtExpense15 = int(interestAndDebtExpense15)
    except Exception:
        interestAndDebtExpense15 = 0
    netIncomeFromContinuingOperations15 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][4]
    try:
        netIncomeFromContinuingOperations15 = int(netIncomeFromContinuingOperations15)
    except Exception:
        netIncomeFromContinuingOperations15 = 0
    comprehensiveIncomeNetOfTax15 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][4]
    try:
        comprehensiveIncomeNetOfTax15 = int(comprehensiveIncomeNetOfTax15)
    except Exception:
        comprehensiveIncomeNetOfTax15 = 0
    ebit15 = quarterly_statementsDump.loc['ebit'][4]
    try:
        ebit15 = int(ebit15)
    except Exception:
        ebit15 = 0
    ebitda15 = quarterly_statementsDump.loc['ebitda'][4]
    try:
        ebitda15 = int(ebitda15)
    except Exception:
        ebitda15 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 4]

    # Balance Sheet Values for tm15

    totalAssets15 = quarterly_statementsDump.loc['totalAssets'][4]
    try:
        totalAssets15 = int(totalAssets15)
    except Exception:
        totalAssets15 = 0
    totalCurrentAssets15 = quarterly_statementsDump.loc['totalCurrentAssets'][4]
    try:
        totalCurrentAssets15 = int(totalCurrentAssets15)
    except Exception:
        totalCurrentAssets15 = 0
    cashAndCashEquivalentsAtCarryingValue15 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][4]
    try:
        cashAndCashEquivalentsAtCarryingValue15 = int(cashAndCashEquivalentsAtCarryingValue15)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue15 = 0
    cashAndShortTermInvestments15 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][4]
    try:
        cashAndShortTermInvestments15 = int(cashAndShortTermInvestments15)
    except Exception:
        cashAndShortTermInvestments15 = 0
    inventory15 = quarterly_statementsDump.loc['inventory'][4]
    try:
        inventory15 = int(inventory15)
    except Exception:
        inventory15 = 0
    currentNetReceivables15 = quarterly_statementsDump.loc['currentNetReceivables'][4]
    try:
        currentNetReceivables15 = int(currentNetReceivables15)
    except Exception:
        currentNetReceivables15 = 0
    totalNonCurrentAssets15 = quarterly_statementsDump.loc['totalNonCurrentAssets'][4]
    try:
        totalNonCurrentAssets15 = int(totalNonCurrentAssets15)
    except Exception:
        totalNonCurrentAssets15 = 0
    propertyPlantEquipment15 = quarterly_statementsDump.loc['propertyPlantEquipment'][4]
    try:
        propertyPlantEquipment15 = int(propertyPlantEquipment15)
    except Exception:
        propertyPlantEquipment15 = 0
    accumulatedDepreciationAmortizationPPE15 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][4]
    try:
        accumulatedDepreciationAmortizationPPE15 = int(accumulatedDepreciationAmortizationPPE15)
    except Exception:
        accumulatedDepreciationAmortizationPPE15 = 0
    intangibleAssets15 = quarterly_statementsDump.loc['intangibleAssets'][4]
    try:
        intangibleAssets15 = int(intangibleAssets15)
    except Exception:
        intangibleAssets15 = 0
    intangibleAssetsExcludingGoodwill15 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][4]
    try:
        intangibleAssetsExcludingGoodwill15 = int(intangibleAssetsExcludingGoodwill15)
    except Exception:
        intangibleAssetsExcludingGoodwill15 = 0
    goodwill15 = quarterly_statementsDump.loc['goodwill'][4]
    try:
        goodwill15 = int(goodwill15)
    except Exception:
        goodwill15 = 0
    investments15 = quarterly_statementsDump.loc['investments'][4]
    try:
        investments15 = int(investments15)
    except Exception:
        investments15 = 0
    longTermInvestments15 = quarterly_statementsDump.loc['longTermInvestments'][4]
    try:
        longTermInvestments15 = int(longTermInvestments15)
    except Exception:
        longTermInvestments15 = 0
    shortTermInvestments15 = quarterly_statementsDump.loc['shortTermInvestments'][4]
    try:
        shortTermInvestments15 = int(shortTermInvestments15)
    except Exception:
        shortTermInvestments15 = 0
    otherCurrentAssets15 = quarterly_statementsDump.loc['otherCurrentAssets'][4]
    try:
        otherCurrentAssets15 = int(otherCurrentAssets15)
    except Exception:
        otherCurrentAssets15 = 0
    otherNonCurrrentAssets15 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][4]
    try:
        otherNonCurrrentAssets15 = int(otherNonCurrrentAssets15)
    except Exception:
        otherNonCurrrentAssets15 = 0
    totalLiabilities15 = quarterly_statementsDump.loc['totalLiabilities'][4]
    try:
        totalLiabilities15 = int(totalLiabilities15)
    except Exception:
        totalLiabilities15 = 0
    totalCurrentLiabilities15 = quarterly_statementsDump.loc['totalCurrentLiabilities'][4]
    try:
        totalCurrentLiabilities15 = int(totalCurrentLiabilities15)
    except Exception:
        totalCurrentLiabilities15 = 0
    currentAccountsPayable15 = quarterly_statementsDump.loc['currentAccountsPayable'][4]
    try:
        currentAccountsPayable15 = int(currentAccountsPayable15)
    except Exception:
        currentAccountsPayable15 = 0
    deferredRevenue15 = quarterly_statementsDump.loc['deferredRevenue'][4]
    try:
        deferredRevenue15 = int(deferredRevenue15)
    except Exception:
        deferredRevenue15 = 0
    currentDebt15 = quarterly_statementsDump.loc['currentDebt'][4]
    try:
        currentDebt15 = int(currentDebt15)
    except Exception:
        currentDebt15 = 0
    shortTermDebt15 = quarterly_statementsDump.loc['shortTermDebt'][4]
    try:
        shortTermDebt15 = int(shortTermDebt15)
    except Exception:
        shortTermDebt15 = 0
    totalNonCurrentLiabilities15 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][4]
    try:
        totalNonCurrentLiabilities15 = int(totalNonCurrentLiabilities15)
    except Exception:
        totalNonCurrentLiabilities15 = 0
    capitalLeaseObligations15 = quarterly_statementsDump.loc['capitalLeaseObligations'][4]
    try:
        capitalLeaseObligations15 = int(capitalLeaseObligations15)
    except Exception:
        capitalLeaseObligations15 = 0

    longTermDebt15 = quarterly_statementsDump.loc['longTermDebt'][4]
    try:
        longTermDebt15 = int(longTermDebt15)
    except Exception:
        longTermDebt15 = 0
    currentLongTermDebt15 = quarterly_statementsDump.loc['currentLongTermDebt'][4]
    try:
        currentLongTermDebt15 = int(currentLongTermDebt15)
    except Exception:
        currentLongTermDebt15 = 0
    longTermDebtNoncurrent15 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][4]
    try:
        longTermDebtNoncurrent15 = int(longTermDebtNoncurrent15)
    except Exception:
        longTermDebtNoncurrent15 = 0
    shortLongTermDebtTotal15 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][4]
    try:
        shortLongTermDebtTotal15 = int(shortLongTermDebtTotal15)
    except Exception:
        shortLongTermDebtTotal15 = 0
    otherCurrentLiabilities15 = quarterly_statementsDump.loc['otherCurrentLiabilities'][4]
    try:
        otherCurrentLiabilities15 = int(otherCurrentLiabilities15)
    except Exception:
        otherCurrentLiabilities15 = 0
    otherNonCurrentLiabilities15 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][4]
    try:
        otherNonCurrentLiabilities15 = int(otherNonCurrentLiabilities15)
    except Exception:
        otherNonCurrentLiabilities15 = 0
    totalShareholderEquity15 = quarterly_statementsDump.loc['totalShareholderEquity'][4]
    try:
        totalShareholderEquity15 = int(totalShareholderEquity15)
    except Exception:
        totalShareholderEquity15 = 0
    treasuryStock15 = quarterly_statementsDump.loc['treasuryStock'][4]
    try:
        treasuryStock15 = int(treasuryStock15)
    except Exception:
        treasuryStock15 = 0
    retainedEarnings15 = quarterly_statementsDump.loc['retainedEarnings'][4]
    try:
        retainedEarnings15 = int(retainedEarnings15)
    except Exception:
        retainedEarnings15 = 0
    commonStock15 = quarterly_statementsDump.loc['commonStock'][4]
    try:
        commonStock15 = int(commonStock15)
    except Exception:
        commonStock15 = 0
    commonStockSharesOutstanding15 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][4]
    try:
        commonStockSharesOutstanding15 = int(commonStockSharesOutstanding15)
    except Exception:
        commonStockSharesOutstanding15 = 0

    # Cash-Flow Statement values for tm15
    operatingCashflow15 = quarterly_statementsDump.loc['operatingCashflow'][4]
    try:
        operatingCashflow15 = int(operatingCashflow15)
    except Exception:
        operatingCashflow15 = 0
    paymentsForOperatingActivities15 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][4]
    try:
        paymentsForOperatingActivities15 = int(paymentsForOperatingActivities15)
    except Exception:
        paymentsForOperatingActivities15 = 0
    proceedsFromOperatingActivities15 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][4]
    try:
        proceedsFromOperatingActivities15 = int(proceedsFromOperatingActivities15)
    except Exception:
        proceedsFromOperatingActivities15 = 0
    changeInOperatingLiabilities15 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][4]
    try:
        changeInOperatingLiabilities15 = int(changeInOperatingLiabilities15)
    except Exception:
        changeInOperatingLiabilities15 = 0
    changeInOperatingAssets15 = quarterly_statementsDump.loc['changeInOperatingAssets'][4]
    try:
        changeInOperatingAssets15 = int(changeInOperatingAssets15)
    except Exception:
        changeInOperatingAssets15 = 0
    depreciationDepletionAndAmortization15 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][4]
    try:
        depreciationDepletionAndAmortization15 = int(depreciationDepletionAndAmortization15)
    except Exception:
        depreciationDepletionAndAmortization15 = 0
    capitalExpenditures15 = quarterly_statementsDump.loc['capitalExpenditures'][4]
    try:
        capitalExpenditures15 = int(capitalExpenditures15)
    except Exception:
        capitalExpenditures15 = 0
    changeInReceivables15 = quarterly_statementsDump.loc['changeInReceivables'][4]
    try:
        changeInReceivables15 = int(changeInReceivables15)
    except Exception:
        changeInReceivables15 = 0
    changeInInventory15 = quarterly_statementsDump.loc['changeInInventory'][4]
    try:
        changeInInventory15 = int(changeInInventory15)
    except Exception:
        changeInInventory15 = 0
    profitLoss15 = quarterly_statementsDump.loc['profitLoss'][4]
    try:
        profitLoss15 = int(profitLoss15)
    except Exception:
        profitLoss15 = 0
    cashflowFromInvestment15 = quarterly_statementsDump.loc['cashflowFromInvestment'][4]
    try:
        cashflowFromInvestment15 = int(cashflowFromInvestment15)
    except Exception:
        cashflowFromInvestment15 = 0
    cashflowFromFinancing15 = quarterly_statementsDump.loc['cashflowFromFinancing'][4]
    try:
        cashflowFromFinancing15 = int(cashflowFromFinancing15)
    except Exception:
        cashflowFromFinancing15 = 0
    proceedsFromRepaymentsOfShortTermDebt15 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][4]
    try:
        proceedsFromRepaymentsOfShortTermDebt15 = int(proceedsFromRepaymentsOfShortTermDebt15)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt15 = 0
    paymentsForRepurchaseOfCommonStock15 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][4]
    try:
        paymentsForRepurchaseOfCommonStock15 = int(paymentsForRepurchaseOfCommonStock15)
    except Exception:
        paymentsForRepurchaseOfCommonStock15 = 0
    paymentsForRepurchaseOfEquity15 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][4]
    try:
        paymentsForRepurchaseOfEquity15 = int(paymentsForRepurchaseOfEquity15)
    except Exception:
        paymentsForRepurchaseOfEquity15 = 0
    paymentsForRepurchaseOfPreferredStock15 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][4]
    try:
        paymentsForRepurchaseOfPreferredStock15 = int(paymentsForRepurchaseOfPreferredStock15)
    except Exception:
        paymentsForRepurchaseOfPreferredStock15 = 0
    dividendPayout15 = quarterly_statementsDump.loc['dividendPayout'][4]
    try:
        dividendPayout15 = int(dividendPayout15)
    except Exception:
        dividendPayout15 = 0
    dividendPayoutCommonStock15 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][4]
    try:
        dividendPayoutCommonStock15 = int(dividendPayoutCommonStock15)
    except Exception:
        dividendPayoutCommonStock15 = 0
    dividendPayoutPreferredStock15 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][4]
    try:
        dividendPayoutPreferredStock15 = int(dividendPayoutPreferredStock15)
    except Exception:
        dividendPayoutPreferredStock15 = 0
    proceedsFromIssuanceOfCommonStock15 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][4]
    try:
        proceedsFromIssuanceOfCommonStock15 = int(proceedsFromIssuanceOfCommonStock15)
    except Exception:
        proceedsFromIssuanceOfCommonStock15 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet15 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][4]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet15 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet15)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet15 = 0
    proceedsFromIssuanceOfPreferredStock15 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][4]
    try:
        proceedsFromIssuanceOfPreferredStock15 = int(proceedsFromIssuanceOfPreferredStock15)
    except Exception:
        proceedsFromIssuanceOfPreferredStock15 = 0
    proceedsFromRepurchaseOfEquity15 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][4]
    try:
        proceedsFromRepurchaseOfEquity15 = int(proceedsFromRepurchaseOfEquity15)
    except Exception:
        proceedsFromRepurchaseOfEquity15 = 0
    proceedsFromSaleOfTreasuryStock15 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][4]
    try:
        proceedsFromSaleOfTreasuryStock15 = int(proceedsFromSaleOfTreasuryStock15)
    except Exception:
        proceedsFromSaleOfTreasuryStock15 = 0
    changeInCashAndCashEquivalents15 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][4]
    try:
        changeInCashAndCashEquivalents15 = int(changeInCashAndCashEquivalents15)
    except Exception:
        changeInCashAndCashEquivalents15 = 0
    changeInExchangeRate15 = quarterly_statementsDump.loc['changeInExchangeRate'][4]
    try:
        changeInExchangeRate15 = int(changeInExchangeRate15)
    except Exception:
        changeInExchangeRate15 = 0
    netIncome15 = quarterly_statementsDump.loc['netIncome'][4]
    try:
        netIncome15 = int(netIncome15)
    except Exception:
        netIncome15 = 0

    tTMnetIncome15 = (float(netIncome15) + float(netIncome16) + float(netIncome17) + float(netIncome18))
    try:
        tTMpreferredDivs15 = (int(dividendPayoutPreferredStock15) + int(dividendPayoutPreferredStock16) + int(
            dividendPayoutPreferredStock17) + int(dividendPayoutPreferredStock18))
    except Exception:
        tTMpreferredDivs15 = 0
    weightedAvgCommShrsOutstanding15 = (
            (float(commonStockSharesOutstanding15) + float(commonStockSharesOutstanding16) + float(
                commonStockSharesOutstanding17) + float(commonStockSharesOutstanding18)) / 15)
    quoteUnformatted15 = quoteUnformatted
    marketCap15 = calculateMarketCap(quoteUnformatted15, commonStockSharesOutstanding15)
    basicEPS15 = calculateBasicEPS(tTMnetIncome15, tTMpreferredDivs15, weightedAvgCommShrsOutstanding15)
    pE15 = calculatePE(quoteUnformatted15, basicEPS15)
    pCF15 = calculatePriceToCashFlow(quoteUnformatted15,
                                     calculateOperatingCashFlowPerShare(operatingCashflow15,
                                                                        weightedAvgCommShrsOutstanding15))
    pS15 = calculatePS(quoteUnformatted15, calculateSalesPerShare(totalRevenue15, weightedAvgCommShrsOutstanding15))
    pB15 = calculatePB(quoteUnformatted15,
                       calculateMarketToBookValue(marketCap15, totalAssets15, shortLongTermDebtTotal15,
                                                  preferredStock=0))
    sustainableGrowthRate15 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout15, netIncome15)),
        calculateROE(netIncome15, totalShareholderEquity15))
    pEGRatio15 = calculatePEGRatio(pE15, (sustainableGrowthRate15 * 1500))
    earningsYield15 = calculateEarningsYield(basicEPS15, quoteUnformatted15)
    cashFlowPerShare15 = calculateOperatingCashFlowPerShare(operatingCashflow15, weightedAvgCommShrsOutstanding15)
    ebitdaPerShare15 = calculateEBITDAperShare(ebitda15, weightedAvgCommShrsOutstanding15)
    tTMDividendPayout15 = (
        (float(dividendPayout15) + float(dividendPayout16) + float(dividendPayout17) + float(dividendPayout18)))
    dividendsPerShare15 = calculateDividendsPerShare(tTMDividendPayout15, weightedAvgCommShrsOutstanding15)
    currentQuarterGrossProfitMargin15 = calculateGrossProfitMargin(totalRevenue15, costofGoodsAndServicesSold15)
    tTmTotalRevenue15 = (
    (float(totalRevenue15) + float(totalRevenue16) + float(totalRevenue17) + float(totalRevenue18)))
    tTmCOGS15 = ((float(costofGoodsAndServicesSold15) + float(costofGoodsAndServicesSold16) + float(
        costofGoodsAndServicesSold17) + float(costofGoodsAndServicesSold18)))
    tTMGrossProfitMargin15 = calculateGrossProfitMargin(tTmTotalRevenue15, tTmCOGS15)
    currentQuarterOperatingMargin15 = calculateOperatingMargin(operatingIncome15, totalRevenue15)
    tTMOperatingIncome15 = (
        (float(operatingIncome15) + float(operatingIncome16) + float(operatingIncome17) + float(operatingIncome18)))
    tTMOperatingMargin15 = calculateOperatingMargin(tTMOperatingIncome15, tTmTotalRevenue15)
    currentQuarterPreTaxMargin15 = calculatePreTaxMargin(calculateEBT(ebit15, interestExpense15), totalRevenue15)
    tTMebit15 = ((float(ebit15) + float(ebit16) + float(ebit17) + float(ebit18)))
    tTMInterestExpense15 = (
        (float(interestExpense15) + float(interestExpense16) + float(interestExpense17) + float(interestExpense18)))
    tTMPreTaxMargin15 = calculatePreTaxMargin(calculateEBT(tTMebit15, tTMInterestExpense15), tTmTotalRevenue15)
    currentQuarterNetProfitMargin15 = calculateNetProfitMargin(netIncome15, totalRevenue15)
    tTMNetProfitMargin15 = calculateNetProfitMargin(tTMnetIncome15, tTmTotalRevenue15)
    currentQuarterAvgTotalAssets15 = ((float(totalAssets15) + float(totalAssets16)) / 4)
    currentQuarterOperatingROA15 = (calculateOperatingROA(operatingIncome15, currentQuarterAvgTotalAssets15)) * 4
    tTMAvgTotalAssets15 = (
                (float(totalAssets15) + float(totalAssets16) + float(totalAssets17) + float(totalAssets18)) / 4)
    tTMOperatingROA15 = calculateOperatingROA(tTMOperatingIncome15, tTMAvgTotalAssets15)
    currentQuarterROA15 = (calculateROA(netIncome15, currentQuarterAvgTotalAssets15)) * 4
    tTMROA15 = calculateROA(tTMnetIncome15, tTMAvgTotalAssets15)
    currentQuarterReturnOnTotalCapital15 = (calculateReturnOnTotalCapital(ebit15, shortLongTermDebtTotal15,
                                                                          totalShareholderEquity15)) * 4
    tTMReturnOnTotalCapital15 = calculateReturnOnTotalCapital(tTMebit15, shortLongTermDebtTotal15,
                                                              totalShareholderEquity15)
    currentQuarterROE15 = (calculateROE(netIncome15, totalShareholderEquity15)) * 4
    tTMROE15 = calculateROE(tTMnetIncome15, totalShareholderEquity15)
    currentQuarterAvgCommonEquity15 = ((float(totalShareholderEquity15) + float(totalShareholderEquity15)) / 4)
    currentQuarterReturnOnCommonEquity15 = (calculateReturnOnCommonEquity(netIncome15, dividendPayoutPreferredStock15,
                                                                          currentQuarterAvgCommonEquity15)) * 4
    tTMAvgCommonEquity15 = ((float(totalShareholderEquity15) + float(totalShareholderEquity16) + float(
        totalShareholderEquity17) + float(totalShareholderEquity18)) / 4)
    tTMReturnOnCommonEquity15 = calculateReturnOnCommonEquity(tTMnetIncome15, tTMpreferredDivs15, tTMAvgCommonEquity15)
    debtRatio15 = calculateDebtRatio(totalLiabilities15, totalAssets15)
    debtToEquityRatio15 = calculateDebtToEquity(shortLongTermDebtTotal15, totalShareholderEquity15)
    debtToAssetRatio15 = calculateDebtToAssetRatio(shortLongTermDebtTotal15, totalAssets15)
    debtToCapitalRatio15 = calculateDebtToCapitalRatio(shortLongTermDebtTotal15, totalShareholderEquity15)

    financialLeverage15 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets15,
                                                          currentQuarterAvgCommonEquity15)
    interestCoverage15 = calculateInterestCoverageRatio(operatingCashflow15, interestExpense15, incomeTaxExpense15)
    fixedChargeCoverageRatio15 = calculateFixedChargeCoverage(ebit15, capitalLeaseObligations15, interestExpense15)

    ## tm14  VARIABLES
    # Income Statement Variables for tm14
    gross_profit14 = quarterly_statementsDump.loc['grossProfit'][5]
    try:
        gross_profit14 = int(gross_profit14)
    except Exception:
        gross_profit14 = 0
    totalRevenue14 = quarterly_statementsDump.loc['totalRevenue'][5]
    try:
        totalRevenue14 = int(totalRevenue14)
    except Exception:
        totalRevenue14 = 0
    costOfRevenue14 = quarterly_statementsDump.loc['costOfRevenue'][5]
    try:
        costOfRevenue14 = int(costOfRevenue14)
    except Exception:
        costOfRevenue14 = 0
    costofGoodsAndServicesSold14 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][5]
    try:
        costofGoodsAndServicesSold14 = int(costofGoodsAndServicesSold14)
    except Exception:
        costofGoodsAndServicesSold14 = 0
    operatingIncome14 = quarterly_statementsDump.loc['operatingIncome'][5]
    try:
        operatingIncome14 = int(operatingIncome14)
    except Exception:
        operatingIncome14 = 0
    sellingGeneralAndAdministrative14 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][5]
    try:
        sellingGeneralAndAdministrative14 = int(sellingGeneralAndAdministrative14)
    except Exception:
        sellingGeneralAndAdministrative14 = 0
    researchAndDevelopment14 = quarterly_statementsDump.loc['researchAndDevelopment'][5]
    try:
        researchAndDevelopment14 = int(researchAndDevelopment14)
    except Exception:
        researchAndDevelopment14 = 0
    operatingExpenses14 = quarterly_statementsDump.loc['operatingExpenses'][5]
    try:
        operatingExpenses14 = int(operatingExpenses14)
    except Exception:
        operatingExpenses14 = 0
    investmentIncomeNet14 = quarterly_statementsDump.loc['investmentIncomeNet'][5]
    try:
        investmentIncomeNet14 = int(investmentIncomeNet14)
    except Exception:
        investmentIncomeNet14 = 0

    netInterestIncome14 = quarterly_statementsDump.loc['netInterestIncome'][5]
    try:
        netInterestIncome14 = int(netInterestIncome14)
    except Exception:
        netInterestIncome14 = 0
    interestIncome14 = quarterly_statementsDump.loc['interestIncome'][5]
    try:
        interestIncome14 = int(interestIncome14)
    except Exception:
        interestIncome14 = 0
    interestExpense14 = quarterly_statementsDump.loc['interestExpense'][5]
    try:
        interestExpense14 = int(interestExpense14)
    except Exception:
        interestExpense14 = 0
    nonInterestIncome14 = quarterly_statementsDump.loc['nonInterestIncome'][5]
    try:
        nonInterestIncome14 = int(nonInterestIncome14)
    except Exception:
        nonInterestIncome14 = 0
    otherNonOperatingIncome14 = quarterly_statementsDump.loc['otherNonOperatingIncome'][5]
    try:
        otherNonOperatingIncome14 = int(otherNonOperatingIncome14)
    except Exception:
        otherNonOperatingIncome14 = 0
    depreciation14 = quarterly_statementsDump.loc['depreciation'][5]
    try:
        depreciation14 = int(depreciation14)
    except Exception:
        depreciation14 = 0
    depreciationAndAmortization14 = quarterly_statementsDump.loc['depreciationAndAmortization'][5]
    try:
        depreciationAndAmortization14 = int(depreciationAndAmortization14)
    except Exception:
        depreciationAndAmortization14 = 0

    incomeBeforeTax14 = quarterly_statementsDump.loc['incomeBeforeTax'][5]
    try:
        incomeBeforeTax14 = int(incomeBeforeTax14)
    except Exception:
        incomeBeforeTax14 = 0

    incomeTaxExpense14 = quarterly_statementsDump.loc['incomeTaxExpense'][5]
    try:
        incomeTaxExpense14 = int(incomeTaxExpense14)
    except Exception:
        incomeTaxExpense14 = 0
    interestAndDebtExpense14 = quarterly_statementsDump.loc['interestAndDebtExpense'][5]
    try:
        interestAndDebtExpense14 = int(interestAndDebtExpense14)
    except Exception:
        interestAndDebtExpense14 = 0
    netIncomeFromContinuingOperations14 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][5]
    try:
        netIncomeFromContinuingOperations14 = int(netIncomeFromContinuingOperations14)
    except Exception:
        netIncomeFromContinuingOperations14 = 0
    comprehensiveIncomeNetOfTax14 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][5]
    try:
        comprehensiveIncomeNetOfTax14 = int(comprehensiveIncomeNetOfTax14)
    except Exception:
        comprehensiveIncomeNetOfTax14 = 0
    ebit14 = quarterly_statementsDump.loc['ebit'][5]
    try:
        ebit14 = int(ebit14)
    except Exception:
        ebit14 = 0
    ebitda14 = quarterly_statementsDump.loc['ebitda'][5]
    try:
        ebitda14 = int(ebitda14)
    except Exception:
        ebitda14 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 5]

    # Balance Sheet Values for tm14

    totalAssets14 = quarterly_statementsDump.loc['totalAssets'][5]
    try:
        totalAssets14 = int(totalAssets14)
    except Exception:
        totalAssets14 = 0
    totalCurrentAssets14 = quarterly_statementsDump.loc['totalCurrentAssets'][5]
    try:
        totalCurrentAssets14 = int(totalCurrentAssets14)
    except Exception:
        totalCurrentAssets14 = 0
    cashAndCashEquivalentsAtCarryingValue14 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][5]
    try:
        cashAndCashEquivalentsAtCarryingValue14 = int(cashAndCashEquivalentsAtCarryingValue14)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue14 = 0
    cashAndShortTermInvestments14 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][5]
    try:
        cashAndShortTermInvestments14 = int(cashAndShortTermInvestments14)
    except Exception:
        cashAndShortTermInvestments14 = 0
    inventory14 = quarterly_statementsDump.loc['inventory'][5]
    try:
        inventory14 = int(inventory14)
    except Exception:
        inventory14 = 0
    currentNetReceivables14 = quarterly_statementsDump.loc['currentNetReceivables'][5]
    try:
        currentNetReceivables14 = int(currentNetReceivables14)
    except Exception:
        currentNetReceivables14 = 0
    totalNonCurrentAssets14 = quarterly_statementsDump.loc['totalNonCurrentAssets'][5]
    try:
        totalNonCurrentAssets14 = int(totalNonCurrentAssets14)
    except Exception:
        totalNonCurrentAssets14 = 0
    propertyPlantEquipment14 = quarterly_statementsDump.loc['propertyPlantEquipment'][5]
    try:
        propertyPlantEquipment14 = int(propertyPlantEquipment14)
    except Exception:
        propertyPlantEquipment14 = 0
    accumulatedDepreciationAmortizationPPE14 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][5]
    try:
        accumulatedDepreciationAmortizationPPE14 = int(accumulatedDepreciationAmortizationPPE14)
    except Exception:
        accumulatedDepreciationAmortizationPPE14 = 0
    intangibleAssets14 = quarterly_statementsDump.loc['intangibleAssets'][5]
    try:
        intangibleAssets14 = int(intangibleAssets14)
    except Exception:
        intangibleAssets14 = 0
    intangibleAssetsExcludingGoodwill14 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][5]
    try:
        intangibleAssetsExcludingGoodwill14 = int(intangibleAssetsExcludingGoodwill14)
    except Exception:
        intangibleAssetsExcludingGoodwill14 = 0
    goodwill14 = quarterly_statementsDump.loc['goodwill'][5]
    try:
        goodwill14 = int(goodwill14)
    except Exception:
        goodwill14 = 0
    investments14 = quarterly_statementsDump.loc['investments'][5]
    try:
        investments14 = int(investments14)
    except Exception:
        investments14 = 0
    longTermInvestments14 = quarterly_statementsDump.loc['longTermInvestments'][5]
    try:
        longTermInvestments14 = int(longTermInvestments14)
    except Exception:
        longTermInvestments14 = 0
    shortTermInvestments14 = quarterly_statementsDump.loc['shortTermInvestments'][5]
    try:
        shortTermInvestments14 = int(shortTermInvestments14)
    except Exception:
        shortTermInvestments14 = 0
    otherCurrentAssets14 = quarterly_statementsDump.loc['otherCurrentAssets'][5]
    try:
        otherCurrentAssets14 = int(otherCurrentAssets14)
    except Exception:
        otherCurrentAssets14 = 0
    otherNonCurrrentAssets14 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][5]
    try:
        otherNonCurrrentAssets14 = int(otherNonCurrrentAssets14)
    except Exception:
        otherNonCurrrentAssets14 = 0
    totalLiabilities14 = quarterly_statementsDump.loc['totalLiabilities'][5]
    try:
        totalLiabilities14 = int(totalLiabilities14)
    except Exception:
        totalLiabilities14 = 0
    totalCurrentLiabilities14 = quarterly_statementsDump.loc['totalCurrentLiabilities'][5]
    try:
        totalCurrentLiabilities14 = int(totalCurrentLiabilities14)
    except Exception:
        totalCurrentLiabilities14 = 0
    currentAccountsPayable14 = quarterly_statementsDump.loc['currentAccountsPayable'][5]
    try:
        currentAccountsPayable14 = int(currentAccountsPayable14)
    except Exception:
        currentAccountsPayable14 = 0
    deferredRevenue14 = quarterly_statementsDump.loc['deferredRevenue'][5]
    try:
        deferredRevenue14 = int(deferredRevenue14)
    except Exception:
        deferredRevenue14 = 0
    currentDebt14 = quarterly_statementsDump.loc['currentDebt'][5]
    try:
        currentDebt14 = int(currentDebt14)
    except Exception:
        currentDebt14 = 0
    shortTermDebt14 = quarterly_statementsDump.loc['shortTermDebt'][5]
    try:
        shortTermDebt14 = int(shortTermDebt14)
    except Exception:
        shortTermDebt14 = 0
    totalNonCurrentLiabilities14 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][5]
    try:
        totalNonCurrentLiabilities14 = int(totalNonCurrentLiabilities14)
    except Exception:
        totalNonCurrentLiabilities14 = 0
    capitalLeaseObligations14 = quarterly_statementsDump.loc['capitalLeaseObligations'][5]
    try:
        capitalLeaseObligations14 = int(capitalLeaseObligations14)
    except Exception:
        capitalLeaseObligations14 = 0

    longTermDebt14 = quarterly_statementsDump.loc['longTermDebt'][5]
    try:
        longTermDebt14 = int(longTermDebt14)
    except Exception:
        longTermDebt14 = 0
    currentLongTermDebt14 = quarterly_statementsDump.loc['currentLongTermDebt'][5]
    try:
        currentLongTermDebt14 = int(currentLongTermDebt14)
    except Exception:
        currentLongTermDebt14 = 0
    longTermDebtNoncurrent14 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][5]
    try:
        longTermDebtNoncurrent14 = int(longTermDebtNoncurrent14)
    except Exception:
        longTermDebtNoncurrent14 = 0
    shortLongTermDebtTotal14 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][5]
    try:
        shortLongTermDebtTotal14 = int(shortLongTermDebtTotal14)
    except Exception:
        shortLongTermDebtTotal14 = 0
    otherCurrentLiabilities14 = quarterly_statementsDump.loc['otherCurrentLiabilities'][5]
    try:
        otherCurrentLiabilities14 = int(otherCurrentLiabilities14)
    except Exception:
        otherCurrentLiabilities14 = 0
    otherNonCurrentLiabilities14 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][5]
    try:
        otherNonCurrentLiabilities14 = int(otherNonCurrentLiabilities14)
    except Exception:
        otherNonCurrentLiabilities14 = 0
    totalShareholderEquity14 = quarterly_statementsDump.loc['totalShareholderEquity'][5]
    try:
        totalShareholderEquity14 = int(totalShareholderEquity14)
    except Exception:
        totalShareholderEquity14 = 0
    treasuryStock14 = quarterly_statementsDump.loc['treasuryStock'][5]
    try:
        treasuryStock14 = int(treasuryStock14)
    except Exception:
        treasuryStock14 = 0
    retainedEarnings14 = quarterly_statementsDump.loc['retainedEarnings'][5]
    try:
        retainedEarnings14 = int(retainedEarnings14)
    except Exception:
        retainedEarnings14 = 0
    commonStock14 = quarterly_statementsDump.loc['commonStock'][5]
    try:
        commonStock14 = int(commonStock14)
    except Exception:
        commonStock14 = 0
    commonStockSharesOutstanding14 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][5]
    try:
        commonStockSharesOutstanding14 = int(commonStockSharesOutstanding14)
    except Exception:
        commonStockSharesOutstanding14 = 0

    # Cash-Flow Statement values for tm14
    operatingCashflow14 = quarterly_statementsDump.loc['operatingCashflow'][5]
    try:
        operatingCashflow14 = int(operatingCashflow14)
    except Exception:
        operatingCashflow14 = 0
    paymentsForOperatingActivities14 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][5]
    try:
        paymentsForOperatingActivities14 = int(paymentsForOperatingActivities14)
    except Exception:
        paymentsForOperatingActivities14 = 0
    proceedsFromOperatingActivities14 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][5]
    try:
        proceedsFromOperatingActivities14 = int(proceedsFromOperatingActivities14)
    except Exception:
        proceedsFromOperatingActivities14 = 0
    changeInOperatingLiabilities14 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][5]
    try:
        changeInOperatingLiabilities14 = int(changeInOperatingLiabilities14)
    except Exception:
        changeInOperatingLiabilities14 = 0
    changeInOperatingAssets14 = quarterly_statementsDump.loc['changeInOperatingAssets'][5]
    try:
        changeInOperatingAssets14 = int(changeInOperatingAssets14)
    except Exception:
        changeInOperatingAssets14 = 0
    depreciationDepletionAndAmortization14 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][5]
    try:
        depreciationDepletionAndAmortization14 = int(depreciationDepletionAndAmortization14)
    except Exception:
        depreciationDepletionAndAmortization14 = 0
    capitalExpenditures14 = quarterly_statementsDump.loc['capitalExpenditures'][5]
    try:
        capitalExpenditures14 = int(capitalExpenditures14)
    except Exception:
        capitalExpenditures14 = 0
    changeInReceivables14 = quarterly_statementsDump.loc['changeInReceivables'][5]
    try:
        changeInReceivables14 = int(changeInReceivables14)
    except Exception:
        changeInReceivables14 = 0
    changeInInventory14 = quarterly_statementsDump.loc['changeInInventory'][5]
    try:
        changeInInventory14 = int(changeInInventory14)
    except Exception:
        changeInInventory14 = 0
    profitLoss14 = quarterly_statementsDump.loc['profitLoss'][5]
    try:
        profitLoss14 = int(profitLoss14)
    except Exception:
        profitLoss14 = 0
    cashflowFromInvestment14 = quarterly_statementsDump.loc['cashflowFromInvestment'][5]
    try:
        cashflowFromInvestment14 = int(cashflowFromInvestment14)
    except Exception:
        cashflowFromInvestment14 = 0
    cashflowFromFinancing14 = quarterly_statementsDump.loc['cashflowFromFinancing'][5]
    try:
        cashflowFromFinancing14 = int(cashflowFromFinancing14)
    except Exception:
        cashflowFromFinancing14 = 0
    proceedsFromRepaymentsOfShortTermDebt14 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][5]
    try:
        proceedsFromRepaymentsOfShortTermDebt14 = int(proceedsFromRepaymentsOfShortTermDebt14)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt14 = 0
    paymentsForRepurchaseOfCommonStock14 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][5]
    try:
        paymentsForRepurchaseOfCommonStock14 = int(paymentsForRepurchaseOfCommonStock14)
    except Exception:
        paymentsForRepurchaseOfCommonStock14 = 0
    paymentsForRepurchaseOfEquity14 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][5]
    try:
        paymentsForRepurchaseOfEquity14 = int(paymentsForRepurchaseOfEquity14)
    except Exception:
        paymentsForRepurchaseOfEquity14 = 0
    paymentsForRepurchaseOfPreferredStock14 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][5]
    try:
        paymentsForRepurchaseOfPreferredStock14 = int(paymentsForRepurchaseOfPreferredStock14)
    except Exception:
        paymentsForRepurchaseOfPreferredStock14 = 0
    dividendPayout14 = quarterly_statementsDump.loc['dividendPayout'][5]
    try:
        dividendPayout14 = int(dividendPayout14)
    except Exception:
        dividendPayout14 = 0
    dividendPayoutCommonStock14 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][5]
    try:
        dividendPayoutCommonStock14 = int(dividendPayoutCommonStock14)
    except Exception:
        dividendPayoutCommonStock14 = 0
    dividendPayoutPreferredStock14 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][5]
    try:
        dividendPayoutPreferredStock14 = int(dividendPayoutPreferredStock14)
    except Exception:
        dividendPayoutPreferredStock14 = 0
    proceedsFromIssuanceOfCommonStock14 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][5]
    try:
        proceedsFromIssuanceOfCommonStock14 = int(proceedsFromIssuanceOfCommonStock14)
    except Exception:
        proceedsFromIssuanceOfCommonStock14 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet14 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][5]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet14 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet14)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet14 = 0
    proceedsFromIssuanceOfPreferredStock14 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][5]
    try:
        proceedsFromIssuanceOfPreferredStock14 = int(proceedsFromIssuanceOfPreferredStock14)
    except Exception:
        proceedsFromIssuanceOfPreferredStock14 = 0
    proceedsFromRepurchaseOfEquity14 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][5]
    try:
        proceedsFromRepurchaseOfEquity14 = int(proceedsFromRepurchaseOfEquity14)
    except Exception:
        proceedsFromRepurchaseOfEquity14 = 0
    proceedsFromSaleOfTreasuryStock14 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][5]
    try:
        proceedsFromSaleOfTreasuryStock14 = int(proceedsFromSaleOfTreasuryStock14)
    except Exception:
        proceedsFromSaleOfTreasuryStock14 = 0
    changeInCashAndCashEquivalents14 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][5]
    try:
        changeInCashAndCashEquivalents14 = int(changeInCashAndCashEquivalents14)
    except Exception:
        changeInCashAndCashEquivalents14 = 0
    changeInExchangeRate14 = quarterly_statementsDump.loc['changeInExchangeRate'][5]
    try:
        changeInExchangeRate14 = int(changeInExchangeRate14)
    except Exception:
        changeInExchangeRate14 = 0
    netIncome14 = quarterly_statementsDump.loc['netIncome'][5]
    try:
        netIncome14 = int(netIncome14)
    except Exception:
        netIncome14 = 0

    tTMnetIncome14 = (float(netIncome14) + float(netIncome15) + float(netIncome16) + float(netIncome17))
    try:
        tTMpreferredDivs14 = (int(dividendPayoutPreferredStock14) + int(dividendPayoutPreferredStock15) + int(
            dividendPayoutPreferredStock16) + int(dividendPayoutPreferredStock17))
    except Exception:
        tTMpreferredDivs14 = 0
    weightedAvgCommShrsOutstanding14 = (
            (float(commonStockSharesOutstanding14) + float(commonStockSharesOutstanding15) + float(
                commonStockSharesOutstanding16) + float(commonStockSharesOutstanding17)) / 14)
    quoteUnformatted14 = quoteUnformatted
    marketCap14 = calculateMarketCap(quoteUnformatted14, commonStockSharesOutstanding14)
    basicEPS14 = calculateBasicEPS(tTMnetIncome14, tTMpreferredDivs14, weightedAvgCommShrsOutstanding14)
    pE14 = calculatePE(quoteUnformatted14, basicEPS14)
    pCF14 = calculatePriceToCashFlow(quoteUnformatted14,
                                     calculateOperatingCashFlowPerShare(operatingCashflow14,
                                                                        weightedAvgCommShrsOutstanding14))
    pS14 = calculatePS(quoteUnformatted14, calculateSalesPerShare(totalRevenue14, weightedAvgCommShrsOutstanding14))
    pB14 = calculatePB(quoteUnformatted14,
                       calculateMarketToBookValue(marketCap14, totalAssets14, shortLongTermDebtTotal14,
                                                  preferredStock=0))
    sustainableGrowthRate14 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout14, netIncome14)),
        calculateROE(netIncome14, totalShareholderEquity14))
    pEGRatio14 = calculatePEGRatio(pE14, (sustainableGrowthRate14 * 1400))
    earningsYield14 = calculateEarningsYield(basicEPS14, quoteUnformatted14)
    cashFlowPerShare14 = calculateOperatingCashFlowPerShare(operatingCashflow14, weightedAvgCommShrsOutstanding14)
    ebitdaPerShare14 = calculateEBITDAperShare(ebitda14, weightedAvgCommShrsOutstanding14)
    tTMDividendPayout14 = (
        (float(dividendPayout14) + float(dividendPayout15) + float(dividendPayout16) + float(dividendPayout17)))
    dividendsPerShare14 = calculateDividendsPerShare(tTMDividendPayout14, weightedAvgCommShrsOutstanding14)
    currentQuarterGrossProfitMargin14 = calculateGrossProfitMargin(totalRevenue14, costofGoodsAndServicesSold14)
    tTmTotalRevenue14 = (
    (float(totalRevenue14) + float(totalRevenue15) + float(totalRevenue16) + float(totalRevenue17)))
    tTmCOGS14 = ((float(costofGoodsAndServicesSold14) + float(costofGoodsAndServicesSold15) + float(
        costofGoodsAndServicesSold16) + float(costofGoodsAndServicesSold17)))
    tTMGrossProfitMargin14 = calculateGrossProfitMargin(tTmTotalRevenue14, tTmCOGS14)
    currentQuarterOperatingMargin14 = calculateOperatingMargin(operatingIncome14, totalRevenue14)
    tTMOperatingIncome14 = (
        (float(operatingIncome14) + float(operatingIncome15) + float(operatingIncome16) + float(operatingIncome17)))
    tTMOperatingMargin14 = calculateOperatingMargin(tTMOperatingIncome14, tTmTotalRevenue14)
    currentQuarterPreTaxMargin14 = calculatePreTaxMargin(calculateEBT(ebit14, interestExpense14), totalRevenue14)
    tTMebit14 = ((float(ebit14) + float(ebit15) + float(ebit16) + float(ebit17)))
    tTMInterestExpense14 = (
        (float(interestExpense14) + float(interestExpense15) + float(interestExpense16) + float(interestExpense17)))
    tTMPreTaxMargin14 = calculatePreTaxMargin(calculateEBT(tTMebit14, tTMInterestExpense14), tTmTotalRevenue14)
    currentQuarterNetProfitMargin14 = calculateNetProfitMargin(netIncome14, totalRevenue14)
    tTMNetProfitMargin14 = calculateNetProfitMargin(tTMnetIncome14, tTmTotalRevenue14)
    currentQuarterAvgTotalAssets14 = ((float(totalAssets14) + float(totalAssets15)) / 4)
    currentQuarterOperatingROA14 = (calculateOperatingROA(operatingIncome14, currentQuarterAvgTotalAssets14)) * 4
    tTMAvgTotalAssets14 = (
                (float(totalAssets14) + float(totalAssets15) + float(totalAssets16) + float(totalAssets17)) / 4)
    tTMOperatingROA14 = calculateOperatingROA(tTMOperatingIncome14, tTMAvgTotalAssets14)
    currentQuarterROA14 = (calculateROA(netIncome14, currentQuarterAvgTotalAssets14)) * 4
    tTMROA14 = calculateROA(tTMnetIncome14, tTMAvgTotalAssets14)
    currentQuarterReturnOnTotalCapital14 = (calculateReturnOnTotalCapital(ebit14, shortLongTermDebtTotal14,
                                                                          totalShareholderEquity14)) * 4
    tTMReturnOnTotalCapital14 = calculateReturnOnTotalCapital(tTMebit14, shortLongTermDebtTotal14,
                                                              totalShareholderEquity14)
    currentQuarterROE14 = (calculateROE(netIncome14, totalShareholderEquity14)) * 4
    tTMROE14 = calculateROE(tTMnetIncome14, totalShareholderEquity14)
    currentQuarterAvgCommonEquity14 = ((float(totalShareholderEquity14) + float(totalShareholderEquity14)) / 4)
    currentQuarterReturnOnCommonEquity14 = (calculateReturnOnCommonEquity(netIncome14, dividendPayoutPreferredStock14,
                                                                          currentQuarterAvgCommonEquity14)) * 4
    tTMAvgCommonEquity14 = ((float(totalShareholderEquity14) + float(totalShareholderEquity15) + float(
        totalShareholderEquity16) + float(totalShareholderEquity17)) / 4)
    tTMReturnOnCommonEquity14 = calculateReturnOnCommonEquity(tTMnetIncome14, tTMpreferredDivs14, tTMAvgCommonEquity14)
    debtRatio14 = calculateDebtRatio(totalLiabilities14, totalAssets14)
    debtToEquityRatio14 = calculateDebtToEquity(shortLongTermDebtTotal14, totalShareholderEquity14)
    debtToAssetRatio14 = calculateDebtToAssetRatio(shortLongTermDebtTotal14, totalAssets14)
    debtToCapitalRatio14 = calculateDebtToCapitalRatio(shortLongTermDebtTotal14, totalShareholderEquity14)

    financialLeverage14 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets14,
                                                          currentQuarterAvgCommonEquity14)
    interestCoverage14 = calculateInterestCoverageRatio(operatingCashflow14, interestExpense14, incomeTaxExpense14)
    fixedChargeCoverageRatio14 = calculateFixedChargeCoverage(ebit14, capitalLeaseObligations14, interestExpense14)

    ## tm13  VARIABLES
    # Income Statement Variables for tm13
    gross_profit13 = quarterly_statementsDump.loc['grossProfit'][6]
    try:
        gross_profit13 = int(gross_profit13)
    except Exception:
        gross_profit13 = 0
    totalRevenue13 = quarterly_statementsDump.loc['totalRevenue'][6]
    try:
        totalRevenue13 = int(totalRevenue13)
    except Exception:
        totalRevenue13 = 0
    costOfRevenue13 = quarterly_statementsDump.loc['costOfRevenue'][6]
    try:
        costOfRevenue13 = int(costOfRevenue13)
    except Exception:
        costOfRevenue13 = 0
    costofGoodsAndServicesSold13 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][6]
    try:
        costofGoodsAndServicesSold13 = int(costofGoodsAndServicesSold13)
    except Exception:
        costofGoodsAndServicesSold13 = 0
    operatingIncome13 = quarterly_statementsDump.loc['operatingIncome'][6]
    try:
        operatingIncome13 = int(operatingIncome13)
    except Exception:
        operatingIncome13 = 0
    sellingGeneralAndAdministrative13 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][6]
    try:
        sellingGeneralAndAdministrative13 = int(sellingGeneralAndAdministrative13)
    except Exception:
        sellingGeneralAndAdministrative13 = 0
    researchAndDevelopment13 = quarterly_statementsDump.loc['researchAndDevelopment'][6]
    try:
        researchAndDevelopment13 = int(researchAndDevelopment13)
    except Exception:
        researchAndDevelopment13 = 0
    operatingExpenses13 = quarterly_statementsDump.loc['operatingExpenses'][6]
    try:
        operatingExpenses13 = int(operatingExpenses13)
    except Exception:
        operatingExpenses13 = 0
    investmentIncomeNet13 = quarterly_statementsDump.loc['investmentIncomeNet'][6]
    try:
        investmentIncomeNet13 = int(investmentIncomeNet13)
    except Exception:
        investmentIncomeNet13 = 0

    netInterestIncome13 = quarterly_statementsDump.loc['netInterestIncome'][6]
    try:
        netInterestIncome13 = int(netInterestIncome13)
    except Exception:
        netInterestIncome13 = 0
    interestIncome13 = quarterly_statementsDump.loc['interestIncome'][6]
    try:
        interestIncome13 = int(interestIncome13)
    except Exception:
        interestIncome13 = 0
    interestExpense13 = quarterly_statementsDump.loc['interestExpense'][6]
    try:
        interestExpense13 = int(interestExpense13)
    except Exception:
        interestExpense13 = 0
    nonInterestIncome13 = quarterly_statementsDump.loc['nonInterestIncome'][6]
    try:
        nonInterestIncome13 = int(nonInterestIncome13)
    except Exception:
        nonInterestIncome13 = 0
    otherNonOperatingIncome13 = quarterly_statementsDump.loc['otherNonOperatingIncome'][6]
    try:
        otherNonOperatingIncome13 = int(otherNonOperatingIncome13)
    except Exception:
        otherNonOperatingIncome13 = 0
    depreciation13 = quarterly_statementsDump.loc['depreciation'][6]
    try:
        depreciation13 = int(depreciation13)
    except Exception:
        depreciation13 = 0
    depreciationAndAmortization13 = quarterly_statementsDump.loc['depreciationAndAmortization'][6]
    try:
        depreciationAndAmortization13 = int(depreciationAndAmortization13)
    except Exception:
        depreciationAndAmortization13 = 0

    incomeBeforeTax13 = quarterly_statementsDump.loc['incomeBeforeTax'][6]
    try:
        incomeBeforeTax13 = int(incomeBeforeTax13)
    except Exception:
        incomeBeforeTax13 = 0

    incomeTaxExpense13 = quarterly_statementsDump.loc['incomeTaxExpense'][6]
    try:
        incomeTaxExpense13 = int(incomeTaxExpense13)
    except Exception:
        incomeTaxExpense13 = 0
    interestAndDebtExpense13 = quarterly_statementsDump.loc['interestAndDebtExpense'][6]
    try:
        interestAndDebtExpense13 = int(interestAndDebtExpense13)
    except Exception:
        interestAndDebtExpense13 = 0
    netIncomeFromContinuingOperations13 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][6]
    try:
        netIncomeFromContinuingOperations13 = int(netIncomeFromContinuingOperations13)
    except Exception:
        netIncomeFromContinuingOperations13 = 0
    comprehensiveIncomeNetOfTax13 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][6]
    try:
        comprehensiveIncomeNetOfTax13 = int(comprehensiveIncomeNetOfTax13)
    except Exception:
        comprehensiveIncomeNetOfTax13 = 0
    ebit13 = quarterly_statementsDump.loc['ebit'][6]
    try:
        ebit13 = int(ebit13)
    except Exception:
        ebit13 = 0
    ebitda13 = quarterly_statementsDump.loc['ebitda'][6]
    try:
        ebitda13 = int(ebitda13)
    except Exception:
        ebitda13 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 6]

    # Balance Sheet Values for tm13

    totalAssets13 = quarterly_statementsDump.loc['totalAssets'][6]
    try:
        totalAssets13 = int(totalAssets13)
    except Exception:
        totalAssets13 = 0
    totalCurrentAssets13 = quarterly_statementsDump.loc['totalCurrentAssets'][6]
    try:
        totalCurrentAssets13 = int(totalCurrentAssets13)
    except Exception:
        totalCurrentAssets13 = 0
    cashAndCashEquivalentsAtCarryingValue13 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][6]
    try:
        cashAndCashEquivalentsAtCarryingValue13 = int(cashAndCashEquivalentsAtCarryingValue13)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue13 = 0
    cashAndShortTermInvestments13 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][6]
    try:
        cashAndShortTermInvestments13 = int(cashAndShortTermInvestments13)
    except Exception:
        cashAndShortTermInvestments13 = 0
    inventory13 = quarterly_statementsDump.loc['inventory'][6]
    try:
        inventory13 = int(inventory13)
    except Exception:
        inventory13 = 0
    currentNetReceivables13 = quarterly_statementsDump.loc['currentNetReceivables'][6]
    try:
        currentNetReceivables13 = int(currentNetReceivables13)
    except Exception:
        currentNetReceivables13 = 0
    totalNonCurrentAssets13 = quarterly_statementsDump.loc['totalNonCurrentAssets'][6]
    try:
        totalNonCurrentAssets13 = int(totalNonCurrentAssets13)
    except Exception:
        totalNonCurrentAssets13 = 0
    propertyPlantEquipment13 = quarterly_statementsDump.loc['propertyPlantEquipment'][6]
    try:
        propertyPlantEquipment13 = int(propertyPlantEquipment13)
    except Exception:
        propertyPlantEquipment13 = 0
    accumulatedDepreciationAmortizationPPE13 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][6]
    try:
        accumulatedDepreciationAmortizationPPE13 = int(accumulatedDepreciationAmortizationPPE13)
    except Exception:
        accumulatedDepreciationAmortizationPPE13 = 0
    intangibleAssets13 = quarterly_statementsDump.loc['intangibleAssets'][6]
    try:
        intangibleAssets13 = int(intangibleAssets13)
    except Exception:
        intangibleAssets13 = 0
    intangibleAssetsExcludingGoodwill13 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][6]
    try:
        intangibleAssetsExcludingGoodwill13 = int(intangibleAssetsExcludingGoodwill13)
    except Exception:
        intangibleAssetsExcludingGoodwill13 = 0
    goodwill13 = quarterly_statementsDump.loc['goodwill'][6]
    try:
        goodwill13 = int(goodwill13)
    except Exception:
        goodwill13 = 0
    investments13 = quarterly_statementsDump.loc['investments'][6]
    try:
        investments13 = int(investments13)
    except Exception:
        investments13 = 0
    longTermInvestments13 = quarterly_statementsDump.loc['longTermInvestments'][6]
    try:
        longTermInvestments13 = int(longTermInvestments13)
    except Exception:
        longTermInvestments13 = 0
    shortTermInvestments13 = quarterly_statementsDump.loc['shortTermInvestments'][6]
    try:
        shortTermInvestments13 = int(shortTermInvestments13)
    except Exception:
        shortTermInvestments13 = 0
    otherCurrentAssets13 = quarterly_statementsDump.loc['otherCurrentAssets'][6]
    try:
        otherCurrentAssets13 = int(otherCurrentAssets13)
    except Exception:
        otherCurrentAssets13 = 0
    otherNonCurrrentAssets13 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][6]
    try:
        otherNonCurrrentAssets13 = int(otherNonCurrrentAssets13)
    except Exception:
        otherNonCurrrentAssets13 = 0
    totalLiabilities13 = quarterly_statementsDump.loc['totalLiabilities'][6]
    try:
        totalLiabilities13 = int(totalLiabilities13)
    except Exception:
        totalLiabilities13 = 0
    totalCurrentLiabilities13 = quarterly_statementsDump.loc['totalCurrentLiabilities'][6]
    try:
        totalCurrentLiabilities13 = int(totalCurrentLiabilities13)
    except Exception:
        totalCurrentLiabilities13 = 0
    currentAccountsPayable13 = quarterly_statementsDump.loc['currentAccountsPayable'][6]
    try:
        currentAccountsPayable13 = int(currentAccountsPayable13)
    except Exception:
        currentAccountsPayable13 = 0
    deferredRevenue13 = quarterly_statementsDump.loc['deferredRevenue'][6]
    try:
        deferredRevenue13 = int(deferredRevenue13)
    except Exception:
        deferredRevenue13 = 0
    currentDebt13 = quarterly_statementsDump.loc['currentDebt'][6]
    try:
        currentDebt13 = int(currentDebt13)
    except Exception:
        currentDebt13 = 0
    shortTermDebt13 = quarterly_statementsDump.loc['shortTermDebt'][6]
    try:
        shortTermDebt13 = int(shortTermDebt13)
    except Exception:
        shortTermDebt13 = 0
    totalNonCurrentLiabilities13 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][6]
    try:
        totalNonCurrentLiabilities13 = int(totalNonCurrentLiabilities13)
    except Exception:
        totalNonCurrentLiabilities13 = 0
    capitalLeaseObligations13 = quarterly_statementsDump.loc['capitalLeaseObligations'][6]
    try:
        capitalLeaseObligations13 = int(capitalLeaseObligations13)
    except Exception:
        capitalLeaseObligations13 = 0

    longTermDebt13 = quarterly_statementsDump.loc['longTermDebt'][6]
    try:
        longTermDebt13 = int(longTermDebt13)
    except Exception:
        longTermDebt13 = 0
    currentLongTermDebt13 = quarterly_statementsDump.loc['currentLongTermDebt'][6]
    try:
        currentLongTermDebt13 = int(currentLongTermDebt13)
    except Exception:
        currentLongTermDebt13 = 0
    longTermDebtNoncurrent13 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][6]
    try:
        longTermDebtNoncurrent13 = int(longTermDebtNoncurrent13)
    except Exception:
        longTermDebtNoncurrent13 = 0
    shortLongTermDebtTotal13 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][6]
    try:
        shortLongTermDebtTotal13 = int(shortLongTermDebtTotal13)
    except Exception:
        shortLongTermDebtTotal13 = 0
    otherCurrentLiabilities13 = quarterly_statementsDump.loc['otherCurrentLiabilities'][6]
    try:
        otherCurrentLiabilities13 = int(otherCurrentLiabilities13)
    except Exception:
        otherCurrentLiabilities13 = 0
    otherNonCurrentLiabilities13 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][6]
    try:
        otherNonCurrentLiabilities13 = int(otherNonCurrentLiabilities13)
    except Exception:
        otherNonCurrentLiabilities13 = 0
    totalShareholderEquity13 = quarterly_statementsDump.loc['totalShareholderEquity'][6]
    try:
        totalShareholderEquity13 = int(totalShareholderEquity13)
    except Exception:
        totalShareholderEquity13 = 0
    treasuryStock13 = quarterly_statementsDump.loc['treasuryStock'][6]
    try:
        treasuryStock13 = int(treasuryStock13)
    except Exception:
        treasuryStock13 = 0
    retainedEarnings13 = quarterly_statementsDump.loc['retainedEarnings'][6]
    try:
        retainedEarnings13 = int(retainedEarnings13)
    except Exception:
        retainedEarnings13 = 0
    commonStock13 = quarterly_statementsDump.loc['commonStock'][6]
    try:
        commonStock13 = int(commonStock13)
    except Exception:
        commonStock13 = 0
    commonStockSharesOutstanding13 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][6]
    try:
        commonStockSharesOutstanding13 = int(commonStockSharesOutstanding13)
    except Exception:
        commonStockSharesOutstanding13 = 0

    # Cash-Flow Statement values for tm13
    operatingCashflow13 = quarterly_statementsDump.loc['operatingCashflow'][6]
    try:
        operatingCashflow13 = int(operatingCashflow13)
    except Exception:
        operatingCashflow13 = 0
    paymentsForOperatingActivities13 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][6]
    try:
        paymentsForOperatingActivities13 = int(paymentsForOperatingActivities13)
    except Exception:
        paymentsForOperatingActivities13 = 0
    proceedsFromOperatingActivities13 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][6]
    try:
        proceedsFromOperatingActivities13 = int(proceedsFromOperatingActivities13)
    except Exception:
        proceedsFromOperatingActivities13 = 0
    changeInOperatingLiabilities13 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][6]
    try:
        changeInOperatingLiabilities13 = int(changeInOperatingLiabilities13)
    except Exception:
        changeInOperatingLiabilities13 = 0
    changeInOperatingAssets13 = quarterly_statementsDump.loc['changeInOperatingAssets'][6]
    try:
        changeInOperatingAssets13 = int(changeInOperatingAssets13)
    except Exception:
        changeInOperatingAssets13 = 0
    depreciationDepletionAndAmortization13 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][6]
    try:
        depreciationDepletionAndAmortization13 = int(depreciationDepletionAndAmortization13)
    except Exception:
        depreciationDepletionAndAmortization13 = 0
    capitalExpenditures13 = quarterly_statementsDump.loc['capitalExpenditures'][6]
    try:
        capitalExpenditures13 = int(capitalExpenditures13)
    except Exception:
        capitalExpenditures13 = 0
    changeInReceivables13 = quarterly_statementsDump.loc['changeInReceivables'][6]
    try:
        changeInReceivables13 = int(changeInReceivables13)
    except Exception:
        changeInReceivables13 = 0
    changeInInventory13 = quarterly_statementsDump.loc['changeInInventory'][6]
    try:
        changeInInventory13 = int(changeInInventory13)
    except Exception:
        changeInInventory13 = 0
    profitLoss13 = quarterly_statementsDump.loc['profitLoss'][6]
    try:
        profitLoss13 = int(profitLoss13)
    except Exception:
        profitLoss13 = 0
    cashflowFromInvestment13 = quarterly_statementsDump.loc['cashflowFromInvestment'][6]
    try:
        cashflowFromInvestment13 = int(cashflowFromInvestment13)
    except Exception:
        cashflowFromInvestment13 = 0
    cashflowFromFinancing13 = quarterly_statementsDump.loc['cashflowFromFinancing'][6]
    try:
        cashflowFromFinancing13 = int(cashflowFromFinancing13)
    except Exception:
        cashflowFromFinancing13 = 0
    proceedsFromRepaymentsOfShortTermDebt13 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][6]
    try:
        proceedsFromRepaymentsOfShortTermDebt13 = int(proceedsFromRepaymentsOfShortTermDebt13)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt13 = 0
    paymentsForRepurchaseOfCommonStock13 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][6]
    try:
        paymentsForRepurchaseOfCommonStock13 = int(paymentsForRepurchaseOfCommonStock13)
    except Exception:
        paymentsForRepurchaseOfCommonStock13 = 0
    paymentsForRepurchaseOfEquity13 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][6]
    try:
        paymentsForRepurchaseOfEquity13 = int(paymentsForRepurchaseOfEquity13)
    except Exception:
        paymentsForRepurchaseOfEquity13 = 0
    paymentsForRepurchaseOfPreferredStock13 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][6]
    try:
        paymentsForRepurchaseOfPreferredStock13 = int(paymentsForRepurchaseOfPreferredStock13)
    except Exception:
        paymentsForRepurchaseOfPreferredStock13 = 0
    dividendPayout13 = quarterly_statementsDump.loc['dividendPayout'][6]
    try:
        dividendPayout13 = int(dividendPayout13)
    except Exception:
        dividendPayout13 = 0
    dividendPayoutCommonStock13 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][6]
    try:
        dividendPayoutCommonStock13 = int(dividendPayoutCommonStock13)
    except Exception:
        dividendPayoutCommonStock13 = 0
    dividendPayoutPreferredStock13 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][6]
    try:
        dividendPayoutPreferredStock13 = int(dividendPayoutPreferredStock13)
    except Exception:
        dividendPayoutPreferredStock13 = 0
    proceedsFromIssuanceOfCommonStock13 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][6]
    try:
        proceedsFromIssuanceOfCommonStock13 = int(proceedsFromIssuanceOfCommonStock13)
    except Exception:
        proceedsFromIssuanceOfCommonStock13 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet13 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][6]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet13 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet13)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet13 = 0
    proceedsFromIssuanceOfPreferredStock13 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][6]
    try:
        proceedsFromIssuanceOfPreferredStock13 = int(proceedsFromIssuanceOfPreferredStock13)
    except Exception:
        proceedsFromIssuanceOfPreferredStock13 = 0
    proceedsFromRepurchaseOfEquity13 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][6]
    try:
        proceedsFromRepurchaseOfEquity13 = int(proceedsFromRepurchaseOfEquity13)
    except Exception:
        proceedsFromRepurchaseOfEquity13 = 0
    proceedsFromSaleOfTreasuryStock13 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][6]
    try:
        proceedsFromSaleOfTreasuryStock13 = int(proceedsFromSaleOfTreasuryStock13)
    except Exception:
        proceedsFromSaleOfTreasuryStock13 = 0
    changeInCashAndCashEquivalents13 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][6]
    try:
        changeInCashAndCashEquivalents13 = int(changeInCashAndCashEquivalents13)
    except Exception:
        changeInCashAndCashEquivalents13 = 0
    changeInExchangeRate13 = quarterly_statementsDump.loc['changeInExchangeRate'][6]
    try:
        changeInExchangeRate13 = int(changeInExchangeRate13)
    except Exception:
        changeInExchangeRate13 = 0
    netIncome13 = quarterly_statementsDump.loc['netIncome'][6]
    try:
        netIncome13 = int(netIncome13)
    except Exception:
        netIncome13 = 0

    tTMnetIncome13 = (float(netIncome13) + float(netIncome14) + float(netIncome15) + float(netIncome16))
    try:
        tTMpreferredDivs13 = (int(dividendPayoutPreferredStock13) + int(dividendPayoutPreferredStock14) + int(
            dividendPayoutPreferredStock15) + int(dividendPayoutPreferredStock16))
    except Exception:
        tTMpreferredDivs13 = 0
    weightedAvgCommShrsOutstanding13 = (
            (float(commonStockSharesOutstanding13) + float(commonStockSharesOutstanding14) + float(
                commonStockSharesOutstanding15) + float(commonStockSharesOutstanding16)) / 13)
    quoteUnformatted13 = quoteUnformatted
    marketCap13 = calculateMarketCap(quoteUnformatted13, commonStockSharesOutstanding13)
    basicEPS13 = calculateBasicEPS(tTMnetIncome13, tTMpreferredDivs13, weightedAvgCommShrsOutstanding13)
    pE13 = calculatePE(quoteUnformatted13, basicEPS13)
    pCF13 = calculatePriceToCashFlow(quoteUnformatted13,
                                     calculateOperatingCashFlowPerShare(operatingCashflow13,
                                                                        weightedAvgCommShrsOutstanding13))
    pS13 = calculatePS(quoteUnformatted13, calculateSalesPerShare(totalRevenue13, weightedAvgCommShrsOutstanding13))
    pB13 = calculatePB(quoteUnformatted13,
                       calculateMarketToBookValue(marketCap13, totalAssets13, shortLongTermDebtTotal13,
                                                  preferredStock=0))
    sustainableGrowthRate13 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout13, netIncome13)),
        calculateROE(netIncome13, totalShareholderEquity13))
    pEGRatio13 = calculatePEGRatio(pE13, (sustainableGrowthRate13 * 1300))
    earningsYield13 = calculateEarningsYield(basicEPS13, quoteUnformatted13)
    cashFlowPerShare13 = calculateOperatingCashFlowPerShare(operatingCashflow13, weightedAvgCommShrsOutstanding13)
    ebitdaPerShare13 = calculateEBITDAperShare(ebitda13, weightedAvgCommShrsOutstanding13)
    tTMDividendPayout13 = (
        (float(dividendPayout13) + float(dividendPayout14) + float(dividendPayout15) + float(dividendPayout16)))
    dividendsPerShare13 = calculateDividendsPerShare(tTMDividendPayout13, weightedAvgCommShrsOutstanding13)
    currentQuarterGrossProfitMargin13 = calculateGrossProfitMargin(totalRevenue13, costofGoodsAndServicesSold13)
    tTmTotalRevenue13 = (
    (float(totalRevenue13) + float(totalRevenue14) + float(totalRevenue15) + float(totalRevenue16)))
    tTmCOGS13 = ((float(costofGoodsAndServicesSold13) + float(costofGoodsAndServicesSold14) + float(
        costofGoodsAndServicesSold15) + float(costofGoodsAndServicesSold16)))
    tTMGrossProfitMargin13 = calculateGrossProfitMargin(tTmTotalRevenue13, tTmCOGS13)
    currentQuarterOperatingMargin13 = calculateOperatingMargin(operatingIncome13, totalRevenue13)
    tTMOperatingIncome13 = (
        (float(operatingIncome13) + float(operatingIncome14) + float(operatingIncome15) + float(operatingIncome16)))
    tTMOperatingMargin13 = calculateOperatingMargin(tTMOperatingIncome13, tTmTotalRevenue13)
    currentQuarterPreTaxMargin13 = calculatePreTaxMargin(calculateEBT(ebit13, interestExpense13), totalRevenue13)
    tTMebit13 = ((float(ebit13) + float(ebit14) + float(ebit15) + float(ebit16)))
    tTMInterestExpense13 = (
        (float(interestExpense13) + float(interestExpense14) + float(interestExpense15) + float(interestExpense16)))
    tTMPreTaxMargin13 = calculatePreTaxMargin(calculateEBT(tTMebit13, tTMInterestExpense13), tTmTotalRevenue13)
    currentQuarterNetProfitMargin13 = calculateNetProfitMargin(netIncome13, totalRevenue13)
    tTMNetProfitMargin13 = calculateNetProfitMargin(tTMnetIncome13, tTmTotalRevenue13)
    currentQuarterAvgTotalAssets13 = ((float(totalAssets13) + float(totalAssets14)) / 4)
    currentQuarterOperatingROA13 = (calculateOperatingROA(operatingIncome13, currentQuarterAvgTotalAssets13)) * 4
    tTMAvgTotalAssets13 = (
                (float(totalAssets13) + float(totalAssets14) + float(totalAssets15) + float(totalAssets16)) / 4)
    tTMOperatingROA13 = calculateOperatingROA(tTMOperatingIncome13, tTMAvgTotalAssets13)
    currentQuarterROA13 = (calculateROA(netIncome13, currentQuarterAvgTotalAssets13)) * 4
    tTMROA13 = calculateROA(tTMnetIncome13, tTMAvgTotalAssets13)
    currentQuarterReturnOnTotalCapital13 = (calculateReturnOnTotalCapital(ebit13, shortLongTermDebtTotal13,
                                                                          totalShareholderEquity13)) * 4
    tTMReturnOnTotalCapital13 = calculateReturnOnTotalCapital(tTMebit13, shortLongTermDebtTotal13,
                                                              totalShareholderEquity13)
    currentQuarterROE13 = (calculateROE(netIncome13, totalShareholderEquity13)) * 4
    tTMROE13 = calculateROE(tTMnetIncome13, totalShareholderEquity13)
    currentQuarterAvgCommonEquity13 = ((float(totalShareholderEquity13) + float(totalShareholderEquity13)) / 4)
    currentQuarterReturnOnCommonEquity13 = (calculateReturnOnCommonEquity(netIncome13, dividendPayoutPreferredStock13,
                                                                          currentQuarterAvgCommonEquity13)) * 4
    tTMAvgCommonEquity13 = ((float(totalShareholderEquity13) + float(totalShareholderEquity14) + float(
        totalShareholderEquity15) + float(totalShareholderEquity16)) / 4)
    tTMReturnOnCommonEquity13 = calculateReturnOnCommonEquity(tTMnetIncome13, tTMpreferredDivs13, tTMAvgCommonEquity13)
    debtRatio13 = calculateDebtRatio(totalLiabilities13, totalAssets13)
    debtToEquityRatio13 = calculateDebtToEquity(shortLongTermDebtTotal13, totalShareholderEquity13)
    debtToAssetRatio13 = calculateDebtToAssetRatio(shortLongTermDebtTotal13, totalAssets13)
    debtToCapitalRatio13 = calculateDebtToCapitalRatio(shortLongTermDebtTotal13, totalShareholderEquity13)

    financialLeverage13 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets13,
                                                          currentQuarterAvgCommonEquity13)
    interestCoverage13 = calculateInterestCoverageRatio(operatingCashflow13, interestExpense13, incomeTaxExpense13)
    fixedChargeCoverageRatio13 = calculateFixedChargeCoverage(ebit13, capitalLeaseObligations13, interestExpense13)

    ## tm12  VARIABLES
    # Income Statement Variables for tm12
    gross_profit12 = quarterly_statementsDump.loc['grossProfit'][7]
    try:
        gross_profit12 = int(gross_profit12)
    except Exception:
        gross_profit12 = 0
    totalRevenue12 = quarterly_statementsDump.loc['totalRevenue'][7]
    try:
        totalRevenue12 = int(totalRevenue12)
    except Exception:
        totalRevenue12 = 0
    costOfRevenue12 = quarterly_statementsDump.loc['costOfRevenue'][7]
    try:
        costOfRevenue12 = int(costOfRevenue12)
    except Exception:
        costOfRevenue12 = 0
    costofGoodsAndServicesSold12 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][7]
    try:
        costofGoodsAndServicesSold12 = int(costofGoodsAndServicesSold12)
    except Exception:
        costofGoodsAndServicesSold12 = 0
    operatingIncome12 = quarterly_statementsDump.loc['operatingIncome'][7]
    try:
        operatingIncome12 = int(operatingIncome12)
    except Exception:
        operatingIncome12 = 0
    sellingGeneralAndAdministrative12 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][7]
    try:
        sellingGeneralAndAdministrative12 = int(sellingGeneralAndAdministrative12)
    except Exception:
        sellingGeneralAndAdministrative12 = 0
    researchAndDevelopment12 = quarterly_statementsDump.loc['researchAndDevelopment'][7]
    try:
        researchAndDevelopment12 = int(researchAndDevelopment12)
    except Exception:
        researchAndDevelopment12 = 0
    operatingExpenses12 = quarterly_statementsDump.loc['operatingExpenses'][7]
    try:
        operatingExpenses12 = int(operatingExpenses12)
    except Exception:
        operatingExpenses12 = 0
    investmentIncomeNet12 = quarterly_statementsDump.loc['investmentIncomeNet'][7]
    try:
        investmentIncomeNet12 = int(investmentIncomeNet12)
    except Exception:
        investmentIncomeNet12 = 0

    netInterestIncome12 = quarterly_statementsDump.loc['netInterestIncome'][7]
    try:
        netInterestIncome12 = int(netInterestIncome12)
    except Exception:
        netInterestIncome12 = 0
    interestIncome12 = quarterly_statementsDump.loc['interestIncome'][7]
    try:
        interestIncome12 = int(interestIncome12)
    except Exception:
        interestIncome12 = 0
    interestExpense12 = quarterly_statementsDump.loc['interestExpense'][7]
    try:
        interestExpense12 = int(interestExpense12)
    except Exception:
        interestExpense12 = 0
    nonInterestIncome12 = quarterly_statementsDump.loc['nonInterestIncome'][7]
    try:
        nonInterestIncome12 = int(nonInterestIncome12)
    except Exception:
        nonInterestIncome12 = 0
    otherNonOperatingIncome12 = quarterly_statementsDump.loc['otherNonOperatingIncome'][7]
    try:
        otherNonOperatingIncome12 = int(otherNonOperatingIncome12)
    except Exception:
        otherNonOperatingIncome12 = 0
    depreciation12 = quarterly_statementsDump.loc['depreciation'][7]
    try:
        depreciation12 = int(depreciation12)
    except Exception:
        depreciation12 = 0
    depreciationAndAmortization12 = quarterly_statementsDump.loc['depreciationAndAmortization'][7]
    try:
        depreciationAndAmortization12 = int(depreciationAndAmortization12)
    except Exception:
        depreciationAndAmortization12 = 0

    incomeBeforeTax12 = quarterly_statementsDump.loc['incomeBeforeTax'][7]
    try:
        incomeBeforeTax12 = int(incomeBeforeTax12)
    except Exception:
        incomeBeforeTax12 = 0

    incomeTaxExpense12 = quarterly_statementsDump.loc['incomeTaxExpense'][7]
    try:
        incomeTaxExpense12 = int(incomeTaxExpense12)
    except Exception:
        incomeTaxExpense12 = 0
    interestAndDebtExpense12 = quarterly_statementsDump.loc['interestAndDebtExpense'][7]
    try:
        interestAndDebtExpense12 = int(interestAndDebtExpense12)
    except Exception:
        interestAndDebtExpense12 = 0
    netIncomeFromContinuingOperations12 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][7]
    try:
        netIncomeFromContinuingOperations12 = int(netIncomeFromContinuingOperations12)
    except Exception:
        netIncomeFromContinuingOperations12 = 0
    comprehensiveIncomeNetOfTax12 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][7]
    try:
        comprehensiveIncomeNetOfTax12 = int(comprehensiveIncomeNetOfTax12)
    except Exception:
        comprehensiveIncomeNetOfTax12 = 0
    ebit12 = quarterly_statementsDump.loc['ebit'][7]
    try:
        ebit12 = int(ebit12)
    except Exception:
        ebit12 = 0
    ebitda12 = quarterly_statementsDump.loc['ebitda'][7]
    try:
        ebitda12 = int(ebitda12)
    except Exception:
        ebitda12 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 7]

    # Balance Sheet Values for tm12

    totalAssets12 = quarterly_statementsDump.loc['totalAssets'][7]
    try:
        totalAssets12 = int(totalAssets12)
    except Exception:
        totalAssets12 = 0
    totalCurrentAssets12 = quarterly_statementsDump.loc['totalCurrentAssets'][7]
    try:
        totalCurrentAssets12 = int(totalCurrentAssets12)
    except Exception:
        totalCurrentAssets12 = 0
    cashAndCashEquivalentsAtCarryingValue12 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][7]
    try:
        cashAndCashEquivalentsAtCarryingValue12 = int(cashAndCashEquivalentsAtCarryingValue12)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue12 = 0
    cashAndShortTermInvestments12 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][7]
    try:
        cashAndShortTermInvestments12 = int(cashAndShortTermInvestments12)
    except Exception:
        cashAndShortTermInvestments12 = 0
    inventory12 = quarterly_statementsDump.loc['inventory'][7]
    try:
        inventory12 = int(inventory12)
    except Exception:
        inventory12 = 0
    currentNetReceivables12 = quarterly_statementsDump.loc['currentNetReceivables'][7]
    try:
        currentNetReceivables12 = int(currentNetReceivables12)
    except Exception:
        currentNetReceivables12 = 0
    totalNonCurrentAssets12 = quarterly_statementsDump.loc['totalNonCurrentAssets'][7]
    try:
        totalNonCurrentAssets12 = int(totalNonCurrentAssets12)
    except Exception:
        totalNonCurrentAssets12 = 0
    propertyPlantEquipment12 = quarterly_statementsDump.loc['propertyPlantEquipment'][7]
    try:
        propertyPlantEquipment12 = int(propertyPlantEquipment12)
    except Exception:
        propertyPlantEquipment12 = 0
    accumulatedDepreciationAmortizationPPE12 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][7]
    try:
        accumulatedDepreciationAmortizationPPE12 = int(accumulatedDepreciationAmortizationPPE12)
    except Exception:
        accumulatedDepreciationAmortizationPPE12 = 0
    intangibleAssets12 = quarterly_statementsDump.loc['intangibleAssets'][7]
    try:
        intangibleAssets12 = int(intangibleAssets12)
    except Exception:
        intangibleAssets12 = 0
    intangibleAssetsExcludingGoodwill12 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][7]
    try:
        intangibleAssetsExcludingGoodwill12 = int(intangibleAssetsExcludingGoodwill12)
    except Exception:
        intangibleAssetsExcludingGoodwill12 = 0
    goodwill12 = quarterly_statementsDump.loc['goodwill'][7]
    try:
        goodwill12 = int(goodwill12)
    except Exception:
        goodwill12 = 0
    investments12 = quarterly_statementsDump.loc['investments'][7]
    try:
        investments12 = int(investments12)
    except Exception:
        investments12 = 0
    longTermInvestments12 = quarterly_statementsDump.loc['longTermInvestments'][7]
    try:
        longTermInvestments12 = int(longTermInvestments12)
    except Exception:
        longTermInvestments12 = 0
    shortTermInvestments12 = quarterly_statementsDump.loc['shortTermInvestments'][7]
    try:
        shortTermInvestments12 = int(shortTermInvestments12)
    except Exception:
        shortTermInvestments12 = 0
    otherCurrentAssets12 = quarterly_statementsDump.loc['otherCurrentAssets'][7]
    try:
        otherCurrentAssets12 = int(otherCurrentAssets12)
    except Exception:
        otherCurrentAssets12 = 0
    otherNonCurrrentAssets12 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][7]
    try:
        otherNonCurrrentAssets12 = int(otherNonCurrrentAssets12)
    except Exception:
        otherNonCurrrentAssets12 = 0
    totalLiabilities12 = quarterly_statementsDump.loc['totalLiabilities'][7]
    try:
        totalLiabilities12 = int(totalLiabilities12)
    except Exception:
        totalLiabilities12 = 0
    totalCurrentLiabilities12 = quarterly_statementsDump.loc['totalCurrentLiabilities'][7]
    try:
        totalCurrentLiabilities12 = int(totalCurrentLiabilities12)
    except Exception:
        totalCurrentLiabilities12 = 0
    currentAccountsPayable12 = quarterly_statementsDump.loc['currentAccountsPayable'][7]
    try:
        currentAccountsPayable12 = int(currentAccountsPayable12)
    except Exception:
        currentAccountsPayable12 = 0
    deferredRevenue12 = quarterly_statementsDump.loc['deferredRevenue'][7]
    try:
        deferredRevenue12 = int(deferredRevenue12)
    except Exception:
        deferredRevenue12 = 0
    currentDebt12 = quarterly_statementsDump.loc['currentDebt'][7]
    try:
        currentDebt12 = int(currentDebt12)
    except Exception:
        currentDebt12 = 0
    shortTermDebt12 = quarterly_statementsDump.loc['shortTermDebt'][7]
    try:
        shortTermDebt12 = int(shortTermDebt12)
    except Exception:
        shortTermDebt12 = 0
    totalNonCurrentLiabilities12 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][7]
    try:
        totalNonCurrentLiabilities12 = int(totalNonCurrentLiabilities12)
    except Exception:
        totalNonCurrentLiabilities12 = 0
    capitalLeaseObligations12 = quarterly_statementsDump.loc['capitalLeaseObligations'][7]
    try:
        capitalLeaseObligations12 = int(capitalLeaseObligations12)
    except Exception:
        capitalLeaseObligations12 = 0

    longTermDebt12 = quarterly_statementsDump.loc['longTermDebt'][7]
    try:
        longTermDebt12 = int(longTermDebt12)
    except Exception:
        longTermDebt12 = 0
    currentLongTermDebt12 = quarterly_statementsDump.loc['currentLongTermDebt'][7]
    try:
        currentLongTermDebt12 = int(currentLongTermDebt12)
    except Exception:
        currentLongTermDebt12 = 0
    longTermDebtNoncurrent12 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][7]
    try:
        longTermDebtNoncurrent12 = int(longTermDebtNoncurrent12)
    except Exception:
        longTermDebtNoncurrent12 = 0
    shortLongTermDebtTotal12 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][7]
    try:
        shortLongTermDebtTotal12 = int(shortLongTermDebtTotal12)
    except Exception:
        shortLongTermDebtTotal12 = 0
    otherCurrentLiabilities12 = quarterly_statementsDump.loc['otherCurrentLiabilities'][7]
    try:
        otherCurrentLiabilities12 = int(otherCurrentLiabilities12)
    except Exception:
        otherCurrentLiabilities12 = 0
    otherNonCurrentLiabilities12 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][7]
    try:
        otherNonCurrentLiabilities12 = int(otherNonCurrentLiabilities12)
    except Exception:
        otherNonCurrentLiabilities12 = 0
    totalShareholderEquity12 = quarterly_statementsDump.loc['totalShareholderEquity'][7]
    try:
        totalShareholderEquity12 = int(totalShareholderEquity12)
    except Exception:
        totalShareholderEquity12 = 0
    treasuryStock12 = quarterly_statementsDump.loc['treasuryStock'][7]
    try:
        treasuryStock12 = int(treasuryStock12)
    except Exception:
        treasuryStock12 = 0
    retainedEarnings12 = quarterly_statementsDump.loc['retainedEarnings'][7]
    try:
        retainedEarnings12 = int(retainedEarnings12)
    except Exception:
        retainedEarnings12 = 0
    commonStock12 = quarterly_statementsDump.loc['commonStock'][7]
    try:
        commonStock12 = int(commonStock12)
    except Exception:
        commonStock12 = 0
    commonStockSharesOutstanding12 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][7]
    try:
        commonStockSharesOutstanding12 = int(commonStockSharesOutstanding12)
    except Exception:
        commonStockSharesOutstanding12 = 0

    # Cash-Flow Statement values for tm12
    operatingCashflow12 = quarterly_statementsDump.loc['operatingCashflow'][7]
    try:
        operatingCashflow12 = int(operatingCashflow12)
    except Exception:
        operatingCashflow12 = 0
    paymentsForOperatingActivities12 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][7]
    try:
        paymentsForOperatingActivities12 = int(paymentsForOperatingActivities12)
    except Exception:
        paymentsForOperatingActivities12 = 0
    proceedsFromOperatingActivities12 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][7]
    try:
        proceedsFromOperatingActivities12 = int(proceedsFromOperatingActivities12)
    except Exception:
        proceedsFromOperatingActivities12 = 0
    changeInOperatingLiabilities12 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][7]
    try:
        changeInOperatingLiabilities12 = int(changeInOperatingLiabilities12)
    except Exception:
        changeInOperatingLiabilities12 = 0
    changeInOperatingAssets12 = quarterly_statementsDump.loc['changeInOperatingAssets'][7]
    try:
        changeInOperatingAssets12 = int(changeInOperatingAssets12)
    except Exception:
        changeInOperatingAssets12 = 0
    depreciationDepletionAndAmortization12 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][7]
    try:
        depreciationDepletionAndAmortization12 = int(depreciationDepletionAndAmortization12)
    except Exception:
        depreciationDepletionAndAmortization12 = 0
    capitalExpenditures12 = quarterly_statementsDump.loc['capitalExpenditures'][7]
    try:
        capitalExpenditures12 = int(capitalExpenditures12)
    except Exception:
        capitalExpenditures12 = 0
    changeInReceivables12 = quarterly_statementsDump.loc['changeInReceivables'][7]
    try:
        changeInReceivables12 = int(changeInReceivables12)
    except Exception:
        changeInReceivables12 = 0
    changeInInventory12 = quarterly_statementsDump.loc['changeInInventory'][7]
    try:
        changeInInventory12 = int(changeInInventory12)
    except Exception:
        changeInInventory12 = 0
    profitLoss12 = quarterly_statementsDump.loc['profitLoss'][7]
    try:
        profitLoss12 = int(profitLoss12)
    except Exception:
        profitLoss12 = 0
    cashflowFromInvestment12 = quarterly_statementsDump.loc['cashflowFromInvestment'][7]
    try:
        cashflowFromInvestment12 = int(cashflowFromInvestment12)
    except Exception:
        cashflowFromInvestment12 = 0
    cashflowFromFinancing12 = quarterly_statementsDump.loc['cashflowFromFinancing'][7]
    try:
        cashflowFromFinancing12 = int(cashflowFromFinancing12)
    except Exception:
        cashflowFromFinancing12 = 0
    proceedsFromRepaymentsOfShortTermDebt12 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][7]
    try:
        proceedsFromRepaymentsOfShortTermDebt12 = int(proceedsFromRepaymentsOfShortTermDebt12)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt12 = 0
    paymentsForRepurchaseOfCommonStock12 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][7]
    try:
        paymentsForRepurchaseOfCommonStock12 = int(paymentsForRepurchaseOfCommonStock12)
    except Exception:
        paymentsForRepurchaseOfCommonStock12 = 0
    paymentsForRepurchaseOfEquity12 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][7]
    try:
        paymentsForRepurchaseOfEquity12 = int(paymentsForRepurchaseOfEquity12)
    except Exception:
        paymentsForRepurchaseOfEquity12 = 0
    paymentsForRepurchaseOfPreferredStock12 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][7]
    try:
        paymentsForRepurchaseOfPreferredStock12 = int(paymentsForRepurchaseOfPreferredStock12)
    except Exception:
        paymentsForRepurchaseOfPreferredStock12 = 0
    dividendPayout12 = quarterly_statementsDump.loc['dividendPayout'][7]
    try:
        dividendPayout12 = int(dividendPayout12)
    except Exception:
        dividendPayout12 = 0
    dividendPayoutCommonStock12 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][7]
    try:
        dividendPayoutCommonStock12 = int(dividendPayoutCommonStock12)
    except Exception:
        dividendPayoutCommonStock12 = 0
    dividendPayoutPreferredStock12 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][7]
    try:
        dividendPayoutPreferredStock12 = int(dividendPayoutPreferredStock12)
    except Exception:
        dividendPayoutPreferredStock12 = 0
    proceedsFromIssuanceOfCommonStock12 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][7]
    try:
        proceedsFromIssuanceOfCommonStock12 = int(proceedsFromIssuanceOfCommonStock12)
    except Exception:
        proceedsFromIssuanceOfCommonStock12 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet12 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][7]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet12 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet12)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet12 = 0
    proceedsFromIssuanceOfPreferredStock12 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][7]
    try:
        proceedsFromIssuanceOfPreferredStock12 = int(proceedsFromIssuanceOfPreferredStock12)
    except Exception:
        proceedsFromIssuanceOfPreferredStock12 = 0
    proceedsFromRepurchaseOfEquity12 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][7]
    try:
        proceedsFromRepurchaseOfEquity12 = int(proceedsFromRepurchaseOfEquity12)
    except Exception:
        proceedsFromRepurchaseOfEquity12 = 0
    proceedsFromSaleOfTreasuryStock12 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][7]
    try:
        proceedsFromSaleOfTreasuryStock12 = int(proceedsFromSaleOfTreasuryStock12)
    except Exception:
        proceedsFromSaleOfTreasuryStock12 = 0
    changeInCashAndCashEquivalents12 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][7]
    try:
        changeInCashAndCashEquivalents12 = int(changeInCashAndCashEquivalents12)
    except Exception:
        changeInCashAndCashEquivalents12 = 0
    changeInExchangeRate12 = quarterly_statementsDump.loc['changeInExchangeRate'][7]
    try:
        changeInExchangeRate12 = int(changeInExchangeRate12)
    except Exception:
        changeInExchangeRate12 = 0
    netIncome12 = quarterly_statementsDump.loc['netIncome'][7]
    try:
        netIncome12 = int(netIncome12)
    except Exception:
        netIncome12 = 0

    tTMnetIncome12 = (float(netIncome12) + float(netIncome13) + float(netIncome14) + float(netIncome15))
    try:
        tTMpreferredDivs12 = (int(dividendPayoutPreferredStock12) + int(dividendPayoutPreferredStock13) + int(
            dividendPayoutPreferredStock14) + int(dividendPayoutPreferredStock15))
    except Exception:
        tTMpreferredDivs12 = 0
    weightedAvgCommShrsOutstanding12 = (
            (float(commonStockSharesOutstanding12) + float(commonStockSharesOutstanding13) + float(
                commonStockSharesOutstanding14) + float(commonStockSharesOutstanding15)) / 12)
    quoteUnformatted12 = quoteUnformatted
    marketCap12 = calculateMarketCap(quoteUnformatted12, commonStockSharesOutstanding12)
    basicEPS12 = calculateBasicEPS(tTMnetIncome12, tTMpreferredDivs12, weightedAvgCommShrsOutstanding12)
    pE12 = calculatePE(quoteUnformatted12, basicEPS12)
    pCF12 = calculatePriceToCashFlow(quoteUnformatted12,
                                     calculateOperatingCashFlowPerShare(operatingCashflow12,
                                                                        weightedAvgCommShrsOutstanding12))
    pS12 = calculatePS(quoteUnformatted12, calculateSalesPerShare(totalRevenue12, weightedAvgCommShrsOutstanding12))
    pB12 = calculatePB(quoteUnformatted12,
                       calculateMarketToBookValue(marketCap12, totalAssets12, shortLongTermDebtTotal12,
                                                  preferredStock=0))
    sustainableGrowthRate12 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout12, netIncome12)),
        calculateROE(netIncome12, totalShareholderEquity12))
    pEGRatio12 = calculatePEGRatio(pE12, (sustainableGrowthRate12 * 1200))
    earningsYield12 = calculateEarningsYield(basicEPS12, quoteUnformatted12)
    cashFlowPerShare12 = calculateOperatingCashFlowPerShare(operatingCashflow12, weightedAvgCommShrsOutstanding12)
    ebitdaPerShare12 = calculateEBITDAperShare(ebitda12, weightedAvgCommShrsOutstanding12)
    tTMDividendPayout12 = (
        (float(dividendPayout12) + float(dividendPayout13) + float(dividendPayout14) + float(dividendPayout15)))
    dividendsPerShare12 = calculateDividendsPerShare(tTMDividendPayout12, weightedAvgCommShrsOutstanding12)
    currentQuarterGrossProfitMargin12 = calculateGrossProfitMargin(totalRevenue12, costofGoodsAndServicesSold12)
    tTmTotalRevenue12 = (
    (float(totalRevenue12) + float(totalRevenue13) + float(totalRevenue14) + float(totalRevenue15)))
    tTmCOGS12 = ((float(costofGoodsAndServicesSold12) + float(costofGoodsAndServicesSold13) + float(
        costofGoodsAndServicesSold14) + float(costofGoodsAndServicesSold15)))
    tTMGrossProfitMargin12 = calculateGrossProfitMargin(tTmTotalRevenue12, tTmCOGS12)
    currentQuarterOperatingMargin12 = calculateOperatingMargin(operatingIncome12, totalRevenue12)
    tTMOperatingIncome12 = (
        (float(operatingIncome12) + float(operatingIncome13) + float(operatingIncome14) + float(operatingIncome15)))
    tTMOperatingMargin12 = calculateOperatingMargin(tTMOperatingIncome12, tTmTotalRevenue12)
    currentQuarterPreTaxMargin12 = calculatePreTaxMargin(calculateEBT(ebit12, interestExpense12), totalRevenue12)
    tTMebit12 = ((float(ebit12) + float(ebit13) + float(ebit14) + float(ebit15)))
    tTMInterestExpense12 = (
        (float(interestExpense12) + float(interestExpense13) + float(interestExpense14) + float(interestExpense15)))
    tTMPreTaxMargin12 = calculatePreTaxMargin(calculateEBT(tTMebit12, tTMInterestExpense12), tTmTotalRevenue12)
    currentQuarterNetProfitMargin12 = calculateNetProfitMargin(netIncome12, totalRevenue12)
    tTMNetProfitMargin12 = calculateNetProfitMargin(tTMnetIncome12, tTmTotalRevenue12)
    currentQuarterAvgTotalAssets12 = ((float(totalAssets12) + float(totalAssets13)) / 4)
    currentQuarterOperatingROA12 = (calculateOperatingROA(operatingIncome12, currentQuarterAvgTotalAssets12)) * 4
    tTMAvgTotalAssets12 = (
                (float(totalAssets12) + float(totalAssets13) + float(totalAssets14) + float(totalAssets15)) / 4)
    tTMOperatingROA12 = calculateOperatingROA(tTMOperatingIncome12, tTMAvgTotalAssets12)
    currentQuarterROA12 = (calculateROA(netIncome12, currentQuarterAvgTotalAssets12)) * 4
    tTMROA12 = calculateROA(tTMnetIncome12, tTMAvgTotalAssets12)
    currentQuarterReturnOnTotalCapital12 = (calculateReturnOnTotalCapital(ebit12, shortLongTermDebtTotal12,
                                                                          totalShareholderEquity12)) * 4
    tTMReturnOnTotalCapital12 = calculateReturnOnTotalCapital(tTMebit12, shortLongTermDebtTotal12,
                                                              totalShareholderEquity12)
    currentQuarterROE12 = (calculateROE(netIncome12, totalShareholderEquity12)) * 4
    tTMROE12 = calculateROE(tTMnetIncome12, totalShareholderEquity12)
    currentQuarterAvgCommonEquity12 = ((float(totalShareholderEquity12) + float(totalShareholderEquity12)) / 4)
    currentQuarterReturnOnCommonEquity12 = (calculateReturnOnCommonEquity(netIncome12, dividendPayoutPreferredStock12,
                                                                          currentQuarterAvgCommonEquity12)) * 4
    tTMAvgCommonEquity12 = ((float(totalShareholderEquity12) + float(totalShareholderEquity13) + float(
        totalShareholderEquity14) + float(totalShareholderEquity15)) / 4)
    tTMReturnOnCommonEquity12 = calculateReturnOnCommonEquity(tTMnetIncome12, tTMpreferredDivs12, tTMAvgCommonEquity12)
    debtRatio12 = calculateDebtRatio(totalLiabilities12, totalAssets12)
    debtToEquityRatio12 = calculateDebtToEquity(shortLongTermDebtTotal12, totalShareholderEquity12)
    debtToAssetRatio12 = calculateDebtToAssetRatio(shortLongTermDebtTotal12, totalAssets12)
    debtToCapitalRatio12 = calculateDebtToCapitalRatio(shortLongTermDebtTotal12, totalShareholderEquity12)

    financialLeverage12 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets12,
                                                          currentQuarterAvgCommonEquity12)
    interestCoverage12 = calculateInterestCoverageRatio(operatingCashflow12, interestExpense12, incomeTaxExpense12)
    fixedChargeCoverageRatio12 = calculateFixedChargeCoverage(ebit12, capitalLeaseObligations12, interestExpense12)

    ## tm11  VARIABLES
    # Income Statement Variables for tm11
    gross_profit11 = quarterly_statementsDump.loc['grossProfit'][8]
    try:
        gross_profit11 = int(gross_profit11)
    except Exception:
        gross_profit11 = 0
    totalRevenue11 = quarterly_statementsDump.loc['totalRevenue'][8]
    try:
        totalRevenue11 = int(totalRevenue11)
    except Exception:
        totalRevenue11 = 0
    costOfRevenue11 = quarterly_statementsDump.loc['costOfRevenue'][8]
    try:
        costOfRevenue11 = int(costOfRevenue11)
    except Exception:
        costOfRevenue11 = 0
    costofGoodsAndServicesSold11 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][8]
    try:
        costofGoodsAndServicesSold11 = int(costofGoodsAndServicesSold11)
    except Exception:
        costofGoodsAndServicesSold11 = 0
    operatingIncome11 = quarterly_statementsDump.loc['operatingIncome'][8]
    try:
        operatingIncome11 = int(operatingIncome11)
    except Exception:
        operatingIncome11 = 0
    sellingGeneralAndAdministrative11 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][8]
    try:
        sellingGeneralAndAdministrative11 = int(sellingGeneralAndAdministrative11)
    except Exception:
        sellingGeneralAndAdministrative11 = 0
    researchAndDevelopment11 = quarterly_statementsDump.loc['researchAndDevelopment'][8]
    try:
        researchAndDevelopment11 = int(researchAndDevelopment11)
    except Exception:
        researchAndDevelopment11 = 0
    operatingExpenses11 = quarterly_statementsDump.loc['operatingExpenses'][8]
    try:
        operatingExpenses11 = int(operatingExpenses11)
    except Exception:
        operatingExpenses11 = 0
    investmentIncomeNet11 = quarterly_statementsDump.loc['investmentIncomeNet'][8]
    try:
        investmentIncomeNet11 = int(investmentIncomeNet11)
    except Exception:
        investmentIncomeNet11 = 0

    netInterestIncome11 = quarterly_statementsDump.loc['netInterestIncome'][8]
    try:
        netInterestIncome11 = int(netInterestIncome11)
    except Exception:
        netInterestIncome11 = 0
    interestIncome11 = quarterly_statementsDump.loc['interestIncome'][8]
    try:
        interestIncome11 = int(interestIncome11)
    except Exception:
        interestIncome11 = 0
    interestExpense11 = quarterly_statementsDump.loc['interestExpense'][8]
    try:
        interestExpense11 = int(interestExpense11)
    except Exception:
        interestExpense11 = 0
    nonInterestIncome11 = quarterly_statementsDump.loc['nonInterestIncome'][8]
    try:
        nonInterestIncome11 = int(nonInterestIncome11)
    except Exception:
        nonInterestIncome11 = 0
    otherNonOperatingIncome11 = quarterly_statementsDump.loc['otherNonOperatingIncome'][8]
    try:
        otherNonOperatingIncome11 = int(otherNonOperatingIncome11)
    except Exception:
        otherNonOperatingIncome11 = 0
    depreciation11 = quarterly_statementsDump.loc['depreciation'][8]
    try:
        depreciation11 = int(depreciation11)
    except Exception:
        depreciation11 = 0
    depreciationAndAmortization11 = quarterly_statementsDump.loc['depreciationAndAmortization'][8]
    try:
        depreciationAndAmortization11 = int(depreciationAndAmortization11)
    except Exception:
        depreciationAndAmortization11 = 0

    incomeBeforeTax11 = quarterly_statementsDump.loc['incomeBeforeTax'][8]
    try:
        incomeBeforeTax11 = int(incomeBeforeTax11)
    except Exception:
        incomeBeforeTax11 = 0

    incomeTaxExpense11 = quarterly_statementsDump.loc['incomeTaxExpense'][8]
    try:
        incomeTaxExpense11 = int(incomeTaxExpense11)
    except Exception:
        incomeTaxExpense11 = 0
    interestAndDebtExpense11 = quarterly_statementsDump.loc['interestAndDebtExpense'][8]
    try:
        interestAndDebtExpense11 = int(interestAndDebtExpense11)
    except Exception:
        interestAndDebtExpense11 = 0
    netIncomeFromContinuingOperations11 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][8]
    try:
        netIncomeFromContinuingOperations11 = int(netIncomeFromContinuingOperations11)
    except Exception:
        netIncomeFromContinuingOperations11 = 0
    comprehensiveIncomeNetOfTax11 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][8]
    try:
        comprehensiveIncomeNetOfTax11 = int(comprehensiveIncomeNetOfTax11)
    except Exception:
        comprehensiveIncomeNetOfTax11 = 0
    ebit11 = quarterly_statementsDump.loc['ebit'][8]
    try:
        ebit11 = int(ebit11)
    except Exception:
        ebit11 = 0
    ebitda11 = quarterly_statementsDump.loc['ebitda'][8]
    try:
        ebitda11 = int(ebitda11)
    except Exception:
        ebitda11 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 8]

    # Balance Sheet Values for tm11

    totalAssets11 = quarterly_statementsDump.loc['totalAssets'][8]
    try:
        totalAssets11 = int(totalAssets11)
    except Exception:
        totalAssets11 = 0
    totalCurrentAssets11 = quarterly_statementsDump.loc['totalCurrentAssets'][8]
    try:
        totalCurrentAssets11 = int(totalCurrentAssets11)
    except Exception:
        totalCurrentAssets11 = 0
    cashAndCashEquivalentsAtCarryingValue11 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][8]
    try:
        cashAndCashEquivalentsAtCarryingValue11 = int(cashAndCashEquivalentsAtCarryingValue11)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue11 = 0
    cashAndShortTermInvestments11 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][8]
    try:
        cashAndShortTermInvestments11 = int(cashAndShortTermInvestments11)
    except Exception:
        cashAndShortTermInvestments11 = 0
    inventory11 = quarterly_statementsDump.loc['inventory'][8]
    try:
        inventory11 = int(inventory11)
    except Exception:
        inventory11 = 0
    currentNetReceivables11 = quarterly_statementsDump.loc['currentNetReceivables'][8]
    try:
        currentNetReceivables11 = int(currentNetReceivables11)
    except Exception:
        currentNetReceivables11 = 0
    totalNonCurrentAssets11 = quarterly_statementsDump.loc['totalNonCurrentAssets'][8]
    try:
        totalNonCurrentAssets11 = int(totalNonCurrentAssets11)
    except Exception:
        totalNonCurrentAssets11 = 0
    propertyPlantEquipment11 = quarterly_statementsDump.loc['propertyPlantEquipment'][8]
    try:
        propertyPlantEquipment11 = int(propertyPlantEquipment11)
    except Exception:
        propertyPlantEquipment11 = 0
    accumulatedDepreciationAmortizationPPE11 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][8]
    try:
        accumulatedDepreciationAmortizationPPE11 = int(accumulatedDepreciationAmortizationPPE11)
    except Exception:
        accumulatedDepreciationAmortizationPPE11 = 0
    intangibleAssets11 = quarterly_statementsDump.loc['intangibleAssets'][8]
    try:
        intangibleAssets11 = int(intangibleAssets11)
    except Exception:
        intangibleAssets11 = 0
    intangibleAssetsExcludingGoodwill11 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][8]
    try:
        intangibleAssetsExcludingGoodwill11 = int(intangibleAssetsExcludingGoodwill11)
    except Exception:
        intangibleAssetsExcludingGoodwill11 = 0
    goodwill11 = quarterly_statementsDump.loc['goodwill'][8]
    try:
        goodwill11 = int(goodwill11)
    except Exception:
        goodwill11 = 0
    investments11 = quarterly_statementsDump.loc['investments'][8]
    try:
        investments11 = int(investments11)
    except Exception:
        investments11 = 0
    longTermInvestments11 = quarterly_statementsDump.loc['longTermInvestments'][8]
    try:
        longTermInvestments11 = int(longTermInvestments11)
    except Exception:
        longTermInvestments11 = 0
    shortTermInvestments11 = quarterly_statementsDump.loc['shortTermInvestments'][8]
    try:
        shortTermInvestments11 = int(shortTermInvestments11)
    except Exception:
        shortTermInvestments11 = 0
    otherCurrentAssets11 = quarterly_statementsDump.loc['otherCurrentAssets'][8]
    try:
        otherCurrentAssets11 = int(otherCurrentAssets11)
    except Exception:
        otherCurrentAssets11 = 0
    otherNonCurrrentAssets11 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][8]
    try:
        otherNonCurrrentAssets11 = int(otherNonCurrrentAssets11)
    except Exception:
        otherNonCurrrentAssets11 = 0
    totalLiabilities11 = quarterly_statementsDump.loc['totalLiabilities'][8]
    try:
        totalLiabilities11 = int(totalLiabilities11)
    except Exception:
        totalLiabilities11 = 0
    totalCurrentLiabilities11 = quarterly_statementsDump.loc['totalCurrentLiabilities'][8]
    try:
        totalCurrentLiabilities11 = int(totalCurrentLiabilities11)
    except Exception:
        totalCurrentLiabilities11 = 0
    currentAccountsPayable11 = quarterly_statementsDump.loc['currentAccountsPayable'][8]
    try:
        currentAccountsPayable11 = int(currentAccountsPayable11)
    except Exception:
        currentAccountsPayable11 = 0
    deferredRevenue11 = quarterly_statementsDump.loc['deferredRevenue'][8]
    try:
        deferredRevenue11 = int(deferredRevenue11)
    except Exception:
        deferredRevenue11 = 0
    currentDebt11 = quarterly_statementsDump.loc['currentDebt'][8]
    try:
        currentDebt11 = int(currentDebt11)
    except Exception:
        currentDebt11 = 0
    shortTermDebt11 = quarterly_statementsDump.loc['shortTermDebt'][8]
    try:
        shortTermDebt11 = int(shortTermDebt11)
    except Exception:
        shortTermDebt11 = 0
    totalNonCurrentLiabilities11 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][8]
    try:
        totalNonCurrentLiabilities11 = int(totalNonCurrentLiabilities11)
    except Exception:
        totalNonCurrentLiabilities11 = 0
    capitalLeaseObligations11 = quarterly_statementsDump.loc['capitalLeaseObligations'][8]
    try:
        capitalLeaseObligations11 = int(capitalLeaseObligations11)
    except Exception:
        capitalLeaseObligations11 = 0

    longTermDebt11 = quarterly_statementsDump.loc['longTermDebt'][8]
    try:
        longTermDebt11 = int(longTermDebt11)
    except Exception:
        longTermDebt11 = 0
    currentLongTermDebt11 = quarterly_statementsDump.loc['currentLongTermDebt'][8]
    try:
        currentLongTermDebt11 = int(currentLongTermDebt11)
    except Exception:
        currentLongTermDebt11 = 0
    longTermDebtNoncurrent11 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][8]
    try:
        longTermDebtNoncurrent11 = int(longTermDebtNoncurrent11)
    except Exception:
        longTermDebtNoncurrent11 = 0
    shortLongTermDebtTotal11 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][8]
    try:
        shortLongTermDebtTotal11 = int(shortLongTermDebtTotal11)
    except Exception:
        shortLongTermDebtTotal11 = 0
    otherCurrentLiabilities11 = quarterly_statementsDump.loc['otherCurrentLiabilities'][8]
    try:
        otherCurrentLiabilities11 = int(otherCurrentLiabilities11)
    except Exception:
        otherCurrentLiabilities11 = 0
    otherNonCurrentLiabilities11 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][8]
    try:
        otherNonCurrentLiabilities11 = int(otherNonCurrentLiabilities11)
    except Exception:
        otherNonCurrentLiabilities11 = 0
    totalShareholderEquity11 = quarterly_statementsDump.loc['totalShareholderEquity'][8]
    try:
        totalShareholderEquity11 = int(totalShareholderEquity11)
    except Exception:
        totalShareholderEquity11 = 0
    treasuryStock11 = quarterly_statementsDump.loc['treasuryStock'][8]
    try:
        treasuryStock11 = int(treasuryStock11)
    except Exception:
        treasuryStock11 = 0
    retainedEarnings11 = quarterly_statementsDump.loc['retainedEarnings'][8]
    try:
        retainedEarnings11 = int(retainedEarnings11)
    except Exception:
        retainedEarnings11 = 0
    commonStock11 = quarterly_statementsDump.loc['commonStock'][8]
    try:
        commonStock11 = int(commonStock11)
    except Exception:
        commonStock11 = 0
    commonStockSharesOutstanding11 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][8]
    try:
        commonStockSharesOutstanding11 = int(commonStockSharesOutstanding11)
    except Exception:
        commonStockSharesOutstanding11 = 0

    # Cash-Flow Statement values for tm11
    operatingCashflow11 = quarterly_statementsDump.loc['operatingCashflow'][8]
    try:
        operatingCashflow11 = int(operatingCashflow11)
    except Exception:
        operatingCashflow11 = 0
    paymentsForOperatingActivities11 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][8]
    try:
        paymentsForOperatingActivities11 = int(paymentsForOperatingActivities11)
    except Exception:
        paymentsForOperatingActivities11 = 0
    proceedsFromOperatingActivities11 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][8]
    try:
        proceedsFromOperatingActivities11 = int(proceedsFromOperatingActivities11)
    except Exception:
        proceedsFromOperatingActivities11 = 0
    changeInOperatingLiabilities11 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][8]
    try:
        changeInOperatingLiabilities11 = int(changeInOperatingLiabilities11)
    except Exception:
        changeInOperatingLiabilities11 = 0
    changeInOperatingAssets11 = quarterly_statementsDump.loc['changeInOperatingAssets'][8]
    try:
        changeInOperatingAssets11 = int(changeInOperatingAssets11)
    except Exception:
        changeInOperatingAssets11 = 0
    depreciationDepletionAndAmortization11 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][8]
    try:
        depreciationDepletionAndAmortization11 = int(depreciationDepletionAndAmortization11)
    except Exception:
        depreciationDepletionAndAmortization11 = 0
    capitalExpenditures11 = quarterly_statementsDump.loc['capitalExpenditures'][8]
    try:
        capitalExpenditures11 = int(capitalExpenditures11)
    except Exception:
        capitalExpenditures11 = 0
    changeInReceivables11 = quarterly_statementsDump.loc['changeInReceivables'][8]
    try:
        changeInReceivables11 = int(changeInReceivables11)
    except Exception:
        changeInReceivables11 = 0
    changeInInventory11 = quarterly_statementsDump.loc['changeInInventory'][8]
    try:
        changeInInventory11 = int(changeInInventory11)
    except Exception:
        changeInInventory11 = 0
    profitLoss11 = quarterly_statementsDump.loc['profitLoss'][8]
    try:
        profitLoss11 = int(profitLoss11)
    except Exception:
        profitLoss11 = 0
    cashflowFromInvestment11 = quarterly_statementsDump.loc['cashflowFromInvestment'][8]
    try:
        cashflowFromInvestment11 = int(cashflowFromInvestment11)
    except Exception:
        cashflowFromInvestment11 = 0
    cashflowFromFinancing11 = quarterly_statementsDump.loc['cashflowFromFinancing'][8]
    try:
        cashflowFromFinancing11 = int(cashflowFromFinancing11)
    except Exception:
        cashflowFromFinancing11 = 0
    proceedsFromRepaymentsOfShortTermDebt11 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][8]
    try:
        proceedsFromRepaymentsOfShortTermDebt11 = int(proceedsFromRepaymentsOfShortTermDebt11)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt11 = 0
    paymentsForRepurchaseOfCommonStock11 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][8]
    try:
        paymentsForRepurchaseOfCommonStock11 = int(paymentsForRepurchaseOfCommonStock11)
    except Exception:
        paymentsForRepurchaseOfCommonStock11 = 0
    paymentsForRepurchaseOfEquity11 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][8]
    try:
        paymentsForRepurchaseOfEquity11 = int(paymentsForRepurchaseOfEquity11)
    except Exception:
        paymentsForRepurchaseOfEquity11 = 0
    paymentsForRepurchaseOfPreferredStock11 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][8]
    try:
        paymentsForRepurchaseOfPreferredStock11 = int(paymentsForRepurchaseOfPreferredStock11)
    except Exception:
        paymentsForRepurchaseOfPreferredStock11 = 0
    dividendPayout11 = quarterly_statementsDump.loc['dividendPayout'][8]
    try:
        dividendPayout11 = int(dividendPayout11)
    except Exception:
        dividendPayout11 = 0
    dividendPayoutCommonStock11 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][8]
    try:
        dividendPayoutCommonStock11 = int(dividendPayoutCommonStock11)
    except Exception:
        dividendPayoutCommonStock11 = 0
    dividendPayoutPreferredStock11 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][8]
    try:
        dividendPayoutPreferredStock11 = int(dividendPayoutPreferredStock11)
    except Exception:
        dividendPayoutPreferredStock11 = 0
    proceedsFromIssuanceOfCommonStock11 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][8]
    try:
        proceedsFromIssuanceOfCommonStock11 = int(proceedsFromIssuanceOfCommonStock11)
    except Exception:
        proceedsFromIssuanceOfCommonStock11 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet11 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][8]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet11 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet11)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet11 = 0
    proceedsFromIssuanceOfPreferredStock11 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][8]
    try:
        proceedsFromIssuanceOfPreferredStock11 = int(proceedsFromIssuanceOfPreferredStock11)
    except Exception:
        proceedsFromIssuanceOfPreferredStock11 = 0
    proceedsFromRepurchaseOfEquity11 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][8]
    try:
        proceedsFromRepurchaseOfEquity11 = int(proceedsFromRepurchaseOfEquity11)
    except Exception:
        proceedsFromRepurchaseOfEquity11 = 0
    proceedsFromSaleOfTreasuryStock11 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][8]
    try:
        proceedsFromSaleOfTreasuryStock11 = int(proceedsFromSaleOfTreasuryStock11)
    except Exception:
        proceedsFromSaleOfTreasuryStock11 = 0
    changeInCashAndCashEquivalents11 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][8]
    try:
        changeInCashAndCashEquivalents11 = int(changeInCashAndCashEquivalents11)
    except Exception:
        changeInCashAndCashEquivalents11 = 0
    changeInExchangeRate11 = quarterly_statementsDump.loc['changeInExchangeRate'][8]
    try:
        changeInExchangeRate11 = int(changeInExchangeRate11)
    except Exception:
        changeInExchangeRate11 = 0
    netIncome11 = quarterly_statementsDump.loc['netIncome'][8]
    try:
        netIncome11 = int(netIncome11)
    except Exception:
        netIncome11 = 0

    tTMnetIncome11 = (float(netIncome11) + float(netIncome12) + float(netIncome13) + float(netIncome14))
    try:
        tTMpreferredDivs11 = (int(dividendPayoutPreferredStock11) + int(dividendPayoutPreferredStock12) + int(
            dividendPayoutPreferredStock13) + int(dividendPayoutPreferredStock14))
    except Exception:
        tTMpreferredDivs11 = 0
    weightedAvgCommShrsOutstanding11 = (
            (float(commonStockSharesOutstanding11) + float(commonStockSharesOutstanding12) + float(
                commonStockSharesOutstanding13) + float(commonStockSharesOutstanding14)) / 11)
    quoteUnformatted11 = quoteUnformatted
    marketCap11 = calculateMarketCap(quoteUnformatted11, commonStockSharesOutstanding11)
    basicEPS11 = calculateBasicEPS(tTMnetIncome11, tTMpreferredDivs11, weightedAvgCommShrsOutstanding11)
    pE11 = calculatePE(quoteUnformatted11, basicEPS11)
    pCF11 = calculatePriceToCashFlow(quoteUnformatted11,
                                     calculateOperatingCashFlowPerShare(operatingCashflow11,
                                                                        weightedAvgCommShrsOutstanding11))
    pS11 = calculatePS(quoteUnformatted11, calculateSalesPerShare(totalRevenue11, weightedAvgCommShrsOutstanding11))
    pB11 = calculatePB(quoteUnformatted11,
                       calculateMarketToBookValue(marketCap11, totalAssets11, shortLongTermDebtTotal11,
                                                  preferredStock=0))
    sustainableGrowthRate11 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout11, netIncome11)),
        calculateROE(netIncome11, totalShareholderEquity11))
    pEGRatio11 = calculatePEGRatio(pE11, (sustainableGrowthRate11 * 1100))
    earningsYield11 = calculateEarningsYield(basicEPS11, quoteUnformatted11)
    cashFlowPerShare11 = calculateOperatingCashFlowPerShare(operatingCashflow11, weightedAvgCommShrsOutstanding11)
    ebitdaPerShare11 = calculateEBITDAperShare(ebitda11, weightedAvgCommShrsOutstanding11)
    tTMDividendPayout11 = (
        (float(dividendPayout11) + float(dividendPayout12) + float(dividendPayout13) + float(dividendPayout14)))
    dividendsPerShare11 = calculateDividendsPerShare(tTMDividendPayout11, weightedAvgCommShrsOutstanding11)
    currentQuarterGrossProfitMargin11 = calculateGrossProfitMargin(totalRevenue11, costofGoodsAndServicesSold11)
    tTmTotalRevenue11 = (
    (float(totalRevenue11) + float(totalRevenue12) + float(totalRevenue13) + float(totalRevenue14)))
    tTmCOGS11 = ((float(costofGoodsAndServicesSold11) + float(costofGoodsAndServicesSold12) + float(
        costofGoodsAndServicesSold13) + float(costofGoodsAndServicesSold14)))
    tTMGrossProfitMargin11 = calculateGrossProfitMargin(tTmTotalRevenue11, tTmCOGS11)
    currentQuarterOperatingMargin11 = calculateOperatingMargin(operatingIncome11, totalRevenue11)
    tTMOperatingIncome11 = (
        (float(operatingIncome11) + float(operatingIncome12) + float(operatingIncome13) + float(operatingIncome14)))
    tTMOperatingMargin11 = calculateOperatingMargin(tTMOperatingIncome11, tTmTotalRevenue11)
    currentQuarterPreTaxMargin11 = calculatePreTaxMargin(calculateEBT(ebit11, interestExpense11), totalRevenue11)
    tTMebit11 = ((float(ebit11) + float(ebit12) + float(ebit13) + float(ebit14)))
    tTMInterestExpense11 = (
        (float(interestExpense11) + float(interestExpense12) + float(interestExpense13) + float(interestExpense14)))
    tTMPreTaxMargin11 = calculatePreTaxMargin(calculateEBT(tTMebit11, tTMInterestExpense11), tTmTotalRevenue11)
    currentQuarterNetProfitMargin11 = calculateNetProfitMargin(netIncome11, totalRevenue11)
    tTMNetProfitMargin11 = calculateNetProfitMargin(tTMnetIncome11, tTmTotalRevenue11)
    currentQuarterAvgTotalAssets11 = ((float(totalAssets11) + float(totalAssets12)) / 4)
    currentQuarterOperatingROA11 = (calculateOperatingROA(operatingIncome11, currentQuarterAvgTotalAssets11)) * 4
    tTMAvgTotalAssets11 = (
                (float(totalAssets11) + float(totalAssets12) + float(totalAssets13) + float(totalAssets14)) / 4)
    tTMOperatingROA11 = calculateOperatingROA(tTMOperatingIncome11, tTMAvgTotalAssets11)
    currentQuarterROA11 = (calculateROA(netIncome11, currentQuarterAvgTotalAssets11)) * 4
    tTMROA11 = calculateROA(tTMnetIncome11, tTMAvgTotalAssets11)
    currentQuarterReturnOnTotalCapital11 = (calculateReturnOnTotalCapital(ebit11, shortLongTermDebtTotal11,
                                                                          totalShareholderEquity11)) * 4
    tTMReturnOnTotalCapital11 = calculateReturnOnTotalCapital(tTMebit11, shortLongTermDebtTotal11,
                                                              totalShareholderEquity11)
    currentQuarterROE11 = (calculateROE(netIncome11, totalShareholderEquity11)) * 4
    tTMROE11 = calculateROE(tTMnetIncome11, totalShareholderEquity11)
    currentQuarterAvgCommonEquity11 = ((float(totalShareholderEquity11) + float(totalShareholderEquity11)) / 4)
    currentQuarterReturnOnCommonEquity11 = (calculateReturnOnCommonEquity(netIncome11, dividendPayoutPreferredStock11,
                                                                          currentQuarterAvgCommonEquity11)) * 4
    tTMAvgCommonEquity11 = ((float(totalShareholderEquity11) + float(totalShareholderEquity12) + float(
        totalShareholderEquity13) + float(totalShareholderEquity14)) / 4)
    tTMReturnOnCommonEquity11 = calculateReturnOnCommonEquity(tTMnetIncome11, tTMpreferredDivs11, tTMAvgCommonEquity11)
    debtRatio11 = calculateDebtRatio(totalLiabilities11, totalAssets11)
    debtToEquityRatio11 = calculateDebtToEquity(shortLongTermDebtTotal11, totalShareholderEquity11)
    debtToAssetRatio11 = calculateDebtToAssetRatio(shortLongTermDebtTotal11, totalAssets11)
    debtToCapitalRatio11 = calculateDebtToCapitalRatio(shortLongTermDebtTotal11, totalShareholderEquity11)

    financialLeverage11 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets11,
                                                          currentQuarterAvgCommonEquity11)
    interestCoverage11 = calculateInterestCoverageRatio(operatingCashflow11, interestExpense11, incomeTaxExpense11)
    fixedChargeCoverageRatio11 = calculateFixedChargeCoverage(ebit11, capitalLeaseObligations11, interestExpense11)

    ## tm10  VARIABLES
    # Income Statement Variables for tm10
    gross_profit10 = quarterly_statementsDump.loc['grossProfit'][9]
    try:
        gross_profit10 = int(gross_profit10)
    except Exception:
        gross_profit10 = 0
    totalRevenue10 = quarterly_statementsDump.loc['totalRevenue'][9]
    try:
        totalRevenue10 = int(totalRevenue10)
    except Exception:
        totalRevenue10 = 0
    costOfRevenue10 = quarterly_statementsDump.loc['costOfRevenue'][9]
    try:
        costOfRevenue10 = int(costOfRevenue10)
    except Exception:
        costOfRevenue10 = 0
    costofGoodsAndServicesSold10 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][9]
    try:
        costofGoodsAndServicesSold10 = int(costofGoodsAndServicesSold10)
    except Exception:
        costofGoodsAndServicesSold10 = 0
    operatingIncome10 = quarterly_statementsDump.loc['operatingIncome'][9]
    try:
        operatingIncome10 = int(operatingIncome10)
    except Exception:
        operatingIncome10 = 0
    sellingGeneralAndAdministrative10 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][9]
    try:
        sellingGeneralAndAdministrative10 = int(sellingGeneralAndAdministrative10)
    except Exception:
        sellingGeneralAndAdministrative10 = 0
    researchAndDevelopment10 = quarterly_statementsDump.loc['researchAndDevelopment'][9]
    try:
        researchAndDevelopment10 = int(researchAndDevelopment10)
    except Exception:
        researchAndDevelopment10 = 0
    operatingExpenses10 = quarterly_statementsDump.loc['operatingExpenses'][9]
    try:
        operatingExpenses10 = int(operatingExpenses10)
    except Exception:
        operatingExpenses10 = 0
    investmentIncomeNet10 = quarterly_statementsDump.loc['investmentIncomeNet'][9]
    try:
        investmentIncomeNet10 = int(investmentIncomeNet10)
    except Exception:
        investmentIncomeNet10 = 0

    netInterestIncome10 = quarterly_statementsDump.loc['netInterestIncome'][9]
    try:
        netInterestIncome10 = int(netInterestIncome10)
    except Exception:
        netInterestIncome10 = 0
    interestIncome10 = quarterly_statementsDump.loc['interestIncome'][9]
    try:
        interestIncome10 = int(interestIncome10)
    except Exception:
        interestIncome10 = 0
    interestExpense10 = quarterly_statementsDump.loc['interestExpense'][9]
    try:
        interestExpense10 = int(interestExpense10)
    except Exception:
        interestExpense10 = 0
    nonInterestIncome10 = quarterly_statementsDump.loc['nonInterestIncome'][9]
    try:
        nonInterestIncome10 = int(nonInterestIncome10)
    except Exception:
        nonInterestIncome10 = 0
    otherNonOperatingIncome10 = quarterly_statementsDump.loc['otherNonOperatingIncome'][9]
    try:
        otherNonOperatingIncome10 = int(otherNonOperatingIncome10)
    except Exception:
        otherNonOperatingIncome10 = 0
    depreciation10 = quarterly_statementsDump.loc['depreciation'][9]
    try:
        depreciation10 = int(depreciation10)
    except Exception:
        depreciation10 = 0
    depreciationAndAmortization10 = quarterly_statementsDump.loc['depreciationAndAmortization'][9]
    try:
        depreciationAndAmortization10 = int(depreciationAndAmortization10)
    except Exception:
        depreciationAndAmortization10 = 0

    incomeBeforeTax10 = quarterly_statementsDump.loc['incomeBeforeTax'][9]
    try:
        incomeBeforeTax10 = int(incomeBeforeTax10)
    except Exception:
        incomeBeforeTax10 = 0

    incomeTaxExpense10 = quarterly_statementsDump.loc['incomeTaxExpense'][9]
    try:
        incomeTaxExpense10 = int(incomeTaxExpense10)
    except Exception:
        incomeTaxExpense10 = 0
    interestAndDebtExpense10 = quarterly_statementsDump.loc['interestAndDebtExpense'][9]
    try:
        interestAndDebtExpense10 = int(interestAndDebtExpense10)
    except Exception:
        interestAndDebtExpense10 = 0
    netIncomeFromContinuingOperations10 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][9]
    try:
        netIncomeFromContinuingOperations10 = int(netIncomeFromContinuingOperations10)
    except Exception:
        netIncomeFromContinuingOperations10 = 0
    comprehensiveIncomeNetOfTax10 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][9]
    try:
        comprehensiveIncomeNetOfTax10 = int(comprehensiveIncomeNetOfTax10)
    except Exception:
        comprehensiveIncomeNetOfTax10 = 0
    ebit10 = quarterly_statementsDump.loc['ebit'][9]
    try:
        ebit10 = int(ebit10)
    except Exception:
        ebit10 = 0
    ebitda10 = quarterly_statementsDump.loc['ebitda'][9]
    try:
        ebitda10 = int(ebitda10)
    except Exception:
        ebitda10 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 9]

    # Balance Sheet Values for tm10

    totalAssets10 = quarterly_statementsDump.loc['totalAssets'][9]
    try:
        totalAssets10 = int(totalAssets10)
    except Exception:
        totalAssets10 = 0
    totalCurrentAssets10 = quarterly_statementsDump.loc['totalCurrentAssets'][9]
    try:
        totalCurrentAssets10 = int(totalCurrentAssets10)
    except Exception:
        totalCurrentAssets10 = 0
    cashAndCashEquivalentsAtCarryingValue10 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][9]
    try:
        cashAndCashEquivalentsAtCarryingValue10 = int(cashAndCashEquivalentsAtCarryingValue10)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue10 = 0
    cashAndShortTermInvestments10 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][9]
    try:
        cashAndShortTermInvestments10 = int(cashAndShortTermInvestments10)
    except Exception:
        cashAndShortTermInvestments10 = 0
    inventory10 = quarterly_statementsDump.loc['inventory'][9]
    try:
        inventory10 = int(inventory10)
    except Exception:
        inventory10 = 0
    currentNetReceivables10 = quarterly_statementsDump.loc['currentNetReceivables'][9]
    try:
        currentNetReceivables10 = int(currentNetReceivables10)
    except Exception:
        currentNetReceivables10 = 0
    totalNonCurrentAssets10 = quarterly_statementsDump.loc['totalNonCurrentAssets'][9]
    try:
        totalNonCurrentAssets10 = int(totalNonCurrentAssets10)
    except Exception:
        totalNonCurrentAssets10 = 0
    propertyPlantEquipment10 = quarterly_statementsDump.loc['propertyPlantEquipment'][9]
    try:
        propertyPlantEquipment10 = int(propertyPlantEquipment10)
    except Exception:
        propertyPlantEquipment10 = 0
    accumulatedDepreciationAmortizationPPE10 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][9]
    try:
        accumulatedDepreciationAmortizationPPE10 = int(accumulatedDepreciationAmortizationPPE10)
    except Exception:
        accumulatedDepreciationAmortizationPPE10 = 0
    intangibleAssets10 = quarterly_statementsDump.loc['intangibleAssets'][9]
    try:
        intangibleAssets10 = int(intangibleAssets10)
    except Exception:
        intangibleAssets10 = 0
    intangibleAssetsExcludingGoodwill10 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][9]
    try:
        intangibleAssetsExcludingGoodwill10 = int(intangibleAssetsExcludingGoodwill10)
    except Exception:
        intangibleAssetsExcludingGoodwill10 = 0
    goodwill10 = quarterly_statementsDump.loc['goodwill'][9]
    try:
        goodwill10 = int(goodwill10)
    except Exception:
        goodwill10 = 0
    investments10 = quarterly_statementsDump.loc['investments'][9]
    try:
        investments10 = int(investments10)
    except Exception:
        investments10 = 0
    longTermInvestments10 = quarterly_statementsDump.loc['longTermInvestments'][9]
    try:
        longTermInvestments10 = int(longTermInvestments10)
    except Exception:
        longTermInvestments10 = 0
    shortTermInvestments10 = quarterly_statementsDump.loc['shortTermInvestments'][9]
    try:
        shortTermInvestments10 = int(shortTermInvestments10)
    except Exception:
        shortTermInvestments10 = 0
    otherCurrentAssets10 = quarterly_statementsDump.loc['otherCurrentAssets'][9]
    try:
        otherCurrentAssets10 = int(otherCurrentAssets10)
    except Exception:
        otherCurrentAssets10 = 0
    otherNonCurrrentAssets10 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][9]
    try:
        otherNonCurrrentAssets10 = int(otherNonCurrrentAssets10)
    except Exception:
        otherNonCurrrentAssets10 = 0
    totalLiabilities10 = quarterly_statementsDump.loc['totalLiabilities'][9]
    try:
        totalLiabilities10 = int(totalLiabilities10)
    except Exception:
        totalLiabilities10 = 0
    totalCurrentLiabilities10 = quarterly_statementsDump.loc['totalCurrentLiabilities'][9]
    try:
        totalCurrentLiabilities10 = int(totalCurrentLiabilities10)
    except Exception:
        totalCurrentLiabilities10 = 0
    currentAccountsPayable10 = quarterly_statementsDump.loc['currentAccountsPayable'][9]
    try:
        currentAccountsPayable10 = int(currentAccountsPayable10)
    except Exception:
        currentAccountsPayable10 = 0
    deferredRevenue10 = quarterly_statementsDump.loc['deferredRevenue'][9]
    try:
        deferredRevenue10 = int(deferredRevenue10)
    except Exception:
        deferredRevenue10 = 0
    currentDebt10 = quarterly_statementsDump.loc['currentDebt'][9]
    try:
        currentDebt10 = int(currentDebt10)
    except Exception:
        currentDebt10 = 0
    shortTermDebt10 = quarterly_statementsDump.loc['shortTermDebt'][9]
    try:
        shortTermDebt10 = int(shortTermDebt10)
    except Exception:
        shortTermDebt10 = 0
    totalNonCurrentLiabilities10 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][9]
    try:
        totalNonCurrentLiabilities10 = int(totalNonCurrentLiabilities10)
    except Exception:
        totalNonCurrentLiabilities10 = 0
    capitalLeaseObligations10 = quarterly_statementsDump.loc['capitalLeaseObligations'][9]
    try:
        capitalLeaseObligations10 = int(capitalLeaseObligations10)
    except Exception:
        capitalLeaseObligations10 = 0

    longTermDebt10 = quarterly_statementsDump.loc['longTermDebt'][9]
    try:
        longTermDebt10 = int(longTermDebt10)
    except Exception:
        longTermDebt10 = 0
    currentLongTermDebt10 = quarterly_statementsDump.loc['currentLongTermDebt'][9]
    try:
        currentLongTermDebt10 = int(currentLongTermDebt10)
    except Exception:
        currentLongTermDebt10 = 0
    longTermDebtNoncurrent10 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][9]
    try:
        longTermDebtNoncurrent10 = int(longTermDebtNoncurrent10)
    except Exception:
        longTermDebtNoncurrent10 = 0
    shortLongTermDebtTotal10 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][9]
    try:
        shortLongTermDebtTotal10 = int(shortLongTermDebtTotal10)
    except Exception:
        shortLongTermDebtTotal10 = 0
    otherCurrentLiabilities10 = quarterly_statementsDump.loc['otherCurrentLiabilities'][9]
    try:
        otherCurrentLiabilities10 = int(otherCurrentLiabilities10)
    except Exception:
        otherCurrentLiabilities10 = 0
    otherNonCurrentLiabilities10 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][9]
    try:
        otherNonCurrentLiabilities10 = int(otherNonCurrentLiabilities10)
    except Exception:
        otherNonCurrentLiabilities10 = 0
    totalShareholderEquity10 = quarterly_statementsDump.loc['totalShareholderEquity'][9]
    try:
        totalShareholderEquity10 = int(totalShareholderEquity10)
    except Exception:
        totalShareholderEquity10 = 0
    treasuryStock10 = quarterly_statementsDump.loc['treasuryStock'][9]
    try:
        treasuryStock10 = int(treasuryStock10)
    except Exception:
        treasuryStock10 = 0
    retainedEarnings10 = quarterly_statementsDump.loc['retainedEarnings'][9]
    try:
        retainedEarnings10 = int(retainedEarnings10)
    except Exception:
        retainedEarnings10 = 0
    commonStock10 = quarterly_statementsDump.loc['commonStock'][9]
    try:
        commonStock10 = int(commonStock10)
    except Exception:
        commonStock10 = 0
    commonStockSharesOutstanding10 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][9]
    try:
        commonStockSharesOutstanding10 = int(commonStockSharesOutstanding10)
    except Exception:
        commonStockSharesOutstanding10 = 0

    # Cash-Flow Statement values for tm10
    operatingCashflow10 = quarterly_statementsDump.loc['operatingCashflow'][9]
    try:
        operatingCashflow10 = int(operatingCashflow10)
    except Exception:
        operatingCashflow10 = 0
    paymentsForOperatingActivities10 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][9]
    try:
        paymentsForOperatingActivities10 = int(paymentsForOperatingActivities10)
    except Exception:
        paymentsForOperatingActivities10 = 0
    proceedsFromOperatingActivities10 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][9]
    try:
        proceedsFromOperatingActivities10 = int(proceedsFromOperatingActivities10)
    except Exception:
        proceedsFromOperatingActivities10 = 0
    changeInOperatingLiabilities10 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][9]
    try:
        changeInOperatingLiabilities10 = int(changeInOperatingLiabilities10)
    except Exception:
        changeInOperatingLiabilities10 = 0
    changeInOperatingAssets10 = quarterly_statementsDump.loc['changeInOperatingAssets'][9]
    try:
        changeInOperatingAssets10 = int(changeInOperatingAssets10)
    except Exception:
        changeInOperatingAssets10 = 0
    depreciationDepletionAndAmortization10 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][9]
    try:
        depreciationDepletionAndAmortization10 = int(depreciationDepletionAndAmortization10)
    except Exception:
        depreciationDepletionAndAmortization10 = 0
    capitalExpenditures10 = quarterly_statementsDump.loc['capitalExpenditures'][9]
    try:
        capitalExpenditures10 = int(capitalExpenditures10)
    except Exception:
        capitalExpenditures10 = 0
    changeInReceivables10 = quarterly_statementsDump.loc['changeInReceivables'][9]
    try:
        changeInReceivables10 = int(changeInReceivables10)
    except Exception:
        changeInReceivables10 = 0
    changeInInventory10 = quarterly_statementsDump.loc['changeInInventory'][9]
    try:
        changeInInventory10 = int(changeInInventory10)
    except Exception:
        changeInInventory10 = 0
    profitLoss10 = quarterly_statementsDump.loc['profitLoss'][9]
    try:
        profitLoss10 = int(profitLoss10)
    except Exception:
        profitLoss10 = 0
    cashflowFromInvestment10 = quarterly_statementsDump.loc['cashflowFromInvestment'][9]
    try:
        cashflowFromInvestment10 = int(cashflowFromInvestment10)
    except Exception:
        cashflowFromInvestment10 = 0
    cashflowFromFinancing10 = quarterly_statementsDump.loc['cashflowFromFinancing'][9]
    try:
        cashflowFromFinancing10 = int(cashflowFromFinancing10)
    except Exception:
        cashflowFromFinancing10 = 0
    proceedsFromRepaymentsOfShortTermDebt10 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][9]
    try:
        proceedsFromRepaymentsOfShortTermDebt10 = int(proceedsFromRepaymentsOfShortTermDebt10)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt10 = 0
    paymentsForRepurchaseOfCommonStock10 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][9]
    try:
        paymentsForRepurchaseOfCommonStock10 = int(paymentsForRepurchaseOfCommonStock10)
    except Exception:
        paymentsForRepurchaseOfCommonStock10 = 0
    paymentsForRepurchaseOfEquity10 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][9]
    try:
        paymentsForRepurchaseOfEquity10 = int(paymentsForRepurchaseOfEquity10)
    except Exception:
        paymentsForRepurchaseOfEquity10 = 0
    paymentsForRepurchaseOfPreferredStock10 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][9]
    try:
        paymentsForRepurchaseOfPreferredStock10 = int(paymentsForRepurchaseOfPreferredStock10)
    except Exception:
        paymentsForRepurchaseOfPreferredStock10 = 0
    dividendPayout10 = quarterly_statementsDump.loc['dividendPayout'][9]
    try:
        dividendPayout10 = int(dividendPayout10)
    except Exception:
        dividendPayout10 = 0
    dividendPayoutCommonStock10 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][9]
    try:
        dividendPayoutCommonStock10 = int(dividendPayoutCommonStock10)
    except Exception:
        dividendPayoutCommonStock10 = 0
    dividendPayoutPreferredStock10 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][9]
    try:
        dividendPayoutPreferredStock10 = int(dividendPayoutPreferredStock10)
    except Exception:
        dividendPayoutPreferredStock10 = 0
    proceedsFromIssuanceOfCommonStock10 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][9]
    try:
        proceedsFromIssuanceOfCommonStock10 = int(proceedsFromIssuanceOfCommonStock10)
    except Exception:
        proceedsFromIssuanceOfCommonStock10 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet10 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][9]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet10 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet10)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet10 = 0
    proceedsFromIssuanceOfPreferredStock10 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][9]
    try:
        proceedsFromIssuanceOfPreferredStock10 = int(proceedsFromIssuanceOfPreferredStock10)
    except Exception:
        proceedsFromIssuanceOfPreferredStock10 = 0
    proceedsFromRepurchaseOfEquity10 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][9]
    try:
        proceedsFromRepurchaseOfEquity10 = int(proceedsFromRepurchaseOfEquity10)
    except Exception:
        proceedsFromRepurchaseOfEquity10 = 0
    proceedsFromSaleOfTreasuryStock10 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][9]
    try:
        proceedsFromSaleOfTreasuryStock10 = int(proceedsFromSaleOfTreasuryStock10)
    except Exception:
        proceedsFromSaleOfTreasuryStock10 = 0
    changeInCashAndCashEquivalents10 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][9]
    try:
        changeInCashAndCashEquivalents10 = int(changeInCashAndCashEquivalents10)
    except Exception:
        changeInCashAndCashEquivalents10 = 0
    changeInExchangeRate10 = quarterly_statementsDump.loc['changeInExchangeRate'][9]
    try:
        changeInExchangeRate10 = int(changeInExchangeRate10)
    except Exception:
        changeInExchangeRate10 = 0
    netIncome10 = quarterly_statementsDump.loc['netIncome'][9]
    try:
        netIncome10 = int(netIncome10)
    except Exception:
        netIncome10 = 0

    tTMnetIncome10 = (float(netIncome10) + float(netIncome10) + float(netIncome12) + float(netIncome13))
    try:
        tTMpreferredDivs10 = (int(dividendPayoutPreferredStock10) + int(dividendPayoutPreferredStock10) + int(
            dividendPayoutPreferredStock12) + int(dividendPayoutPreferredStock13))
    except Exception:
        tTMpreferredDivs10 = 0
    weightedAvgCommShrsOutstanding10 = (
            (float(commonStockSharesOutstanding10) + float(commonStockSharesOutstanding10) + float(
                commonStockSharesOutstanding12) + float(commonStockSharesOutstanding13)) / 10)
    quoteUnformatted10 = quoteUnformatted
    marketCap10 = calculateMarketCap(quoteUnformatted10, commonStockSharesOutstanding10)
    basicEPS10 = calculateBasicEPS(tTMnetIncome10, tTMpreferredDivs10, weightedAvgCommShrsOutstanding10)
    pE10 = calculatePE(quoteUnformatted10, basicEPS10)
    pCF10 = calculatePriceToCashFlow(quoteUnformatted10,
                                     calculateOperatingCashFlowPerShare(operatingCashflow10,
                                                                        weightedAvgCommShrsOutstanding10))
    pS10 = calculatePS(quoteUnformatted10, calculateSalesPerShare(totalRevenue10, weightedAvgCommShrsOutstanding10))
    pB10 = calculatePB(quoteUnformatted10,
                       calculateMarketToBookValue(marketCap10, totalAssets10, shortLongTermDebtTotal10,
                                                  preferredStock=0))
    sustainableGrowthRate10 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout10, netIncome10)),
        calculateROE(netIncome10, totalShareholderEquity10))
    pEGRatio10 = calculatePEGRatio(pE10, (sustainableGrowthRate10 * 1000))
    earningsYield10 = calculateEarningsYield(basicEPS10, quoteUnformatted10)
    cashFlowPerShare10 = calculateOperatingCashFlowPerShare(operatingCashflow10, weightedAvgCommShrsOutstanding10)
    ebitdaPerShare10 = calculateEBITDAperShare(ebitda10, weightedAvgCommShrsOutstanding10)
    tTMDividendPayout10 = (
        (float(dividendPayout10) + float(dividendPayout10) + float(dividendPayout12) + float(dividendPayout13)))
    dividendsPerShare10 = calculateDividendsPerShare(tTMDividendPayout10, weightedAvgCommShrsOutstanding10)
    currentQuarterGrossProfitMargin10 = calculateGrossProfitMargin(totalRevenue10, costofGoodsAndServicesSold10)
    tTmTotalRevenue10 = (
    (float(totalRevenue10) + float(totalRevenue10) + float(totalRevenue12) + float(totalRevenue13)))
    tTmCOGS10 = ((float(costofGoodsAndServicesSold10) + float(costofGoodsAndServicesSold10) + float(
        costofGoodsAndServicesSold12) + float(costofGoodsAndServicesSold13)))
    tTMGrossProfitMargin10 = calculateGrossProfitMargin(tTmTotalRevenue10, tTmCOGS10)
    currentQuarterOperatingMargin10 = calculateOperatingMargin(operatingIncome10, totalRevenue10)
    tTMOperatingIncome10 = (
        (float(operatingIncome10) + float(operatingIncome10) + float(operatingIncome12) + float(operatingIncome13)))
    tTMOperatingMargin10 = calculateOperatingMargin(tTMOperatingIncome10, tTmTotalRevenue10)
    currentQuarterPreTaxMargin10 = calculatePreTaxMargin(calculateEBT(ebit10, interestExpense10), totalRevenue10)
    tTMebit10 = ((float(ebit10) + float(ebit10) + float(ebit12) + float(ebit13)))
    tTMInterestExpense10 = (
        (float(interestExpense10) + float(interestExpense10) + float(interestExpense12) + float(interestExpense13)))
    tTMPreTaxMargin10 = calculatePreTaxMargin(calculateEBT(tTMebit10, tTMInterestExpense10), tTmTotalRevenue10)
    currentQuarterNetProfitMargin10 = calculateNetProfitMargin(netIncome10, totalRevenue10)
    tTMNetProfitMargin10 = calculateNetProfitMargin(tTMnetIncome10, tTmTotalRevenue10)
    currentQuarterAvgTotalAssets10 = ((float(totalAssets10) + float(totalAssets10)) / 4)
    currentQuarterOperatingROA10 = (calculateOperatingROA(operatingIncome10, currentQuarterAvgTotalAssets10)) * 4
    tTMAvgTotalAssets10 = (
                (float(totalAssets10) + float(totalAssets10) + float(totalAssets12) + float(totalAssets13)) / 4)
    tTMOperatingROA10 = calculateOperatingROA(tTMOperatingIncome10, tTMAvgTotalAssets10)
    currentQuarterROA10 = (calculateROA(netIncome10, currentQuarterAvgTotalAssets10)) * 4
    tTMROA10 = calculateROA(tTMnetIncome10, tTMAvgTotalAssets10)
    currentQuarterReturnOnTotalCapital10 = (calculateReturnOnTotalCapital(ebit10, shortLongTermDebtTotal10,
                                                                          totalShareholderEquity10)) * 4
    tTMReturnOnTotalCapital10 = calculateReturnOnTotalCapital(tTMebit10, shortLongTermDebtTotal10,
                                                              totalShareholderEquity10)
    currentQuarterROE10 = (calculateROE(netIncome10, totalShareholderEquity10)) * 4
    tTMROE10 = calculateROE(tTMnetIncome10, totalShareholderEquity10)
    currentQuarterAvgCommonEquity10 = ((float(totalShareholderEquity10) + float(totalShareholderEquity10)) / 4)
    currentQuarterReturnOnCommonEquity10 = (calculateReturnOnCommonEquity(netIncome10, dividendPayoutPreferredStock10,
                                                                          currentQuarterAvgCommonEquity10)) * 4
    tTMAvgCommonEquity10 = ((float(totalShareholderEquity10) + float(totalShareholderEquity10) + float(
        totalShareholderEquity12) + float(totalShareholderEquity13)) / 4)
    tTMReturnOnCommonEquity10 = calculateReturnOnCommonEquity(tTMnetIncome10, tTMpreferredDivs10, tTMAvgCommonEquity10)
    debtRatio10 = calculateDebtRatio(totalLiabilities10, totalAssets10)
    debtToEquityRatio10 = calculateDebtToEquity(shortLongTermDebtTotal10, totalShareholderEquity10)
    debtToAssetRatio10 = calculateDebtToAssetRatio(shortLongTermDebtTotal10, totalAssets10)
    debtToCapitalRatio10 = calculateDebtToCapitalRatio(shortLongTermDebtTotal10, totalShareholderEquity10)

    financialLeverage10 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets10,
                                                          currentQuarterAvgCommonEquity10)
    interestCoverage10 = calculateInterestCoverageRatio(operatingCashflow10, interestExpense10, incomeTaxExpense10)
    fixedChargeCoverageRatio10 = calculateFixedChargeCoverage(ebit10, capitalLeaseObligations10, interestExpense10)

    ## tm9  VARIABLES
    # Income Statement Variables for tm9
    gross_profit9 = quarterly_statementsDump.loc['grossProfit'][10]
    try:
        gross_profit9 = int(gross_profit9)
    except Exception:
        gross_profit9 = 0
    totalRevenue9 = quarterly_statementsDump.loc['totalRevenue'][10]
    try:
        totalRevenue9 = int(totalRevenue9)
    except Exception:
        totalRevenue9 = 0
    costOfRevenue9 = quarterly_statementsDump.loc['costOfRevenue'][10]
    try:
        costOfRevenue9 = int(costOfRevenue9)
    except Exception:
        costOfRevenue9 = 0
    costofGoodsAndServicesSold9 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][10]
    try:
        costofGoodsAndServicesSold9 = int(costofGoodsAndServicesSold9)
    except Exception:
        costofGoodsAndServicesSold9 = 0
    operatingIncome9 = quarterly_statementsDump.loc['operatingIncome'][10]
    try:
        operatingIncome9 = int(operatingIncome9)
    except Exception:
        operatingIncome9 = 0
    sellingGeneralAndAdministrative9 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][10]
    try:
        sellingGeneralAndAdministrative9 = int(sellingGeneralAndAdministrative9)
    except Exception:
        sellingGeneralAndAdministrative9 = 0
    researchAndDevelopment9 = quarterly_statementsDump.loc['researchAndDevelopment'][10]
    try:
        researchAndDevelopment9 = int(researchAndDevelopment9)
    except Exception:
        researchAndDevelopment9 = 0
    operatingExpenses9 = quarterly_statementsDump.loc['operatingExpenses'][10]
    try:
        operatingExpenses9 = int(operatingExpenses9)
    except Exception:
        operatingExpenses9 = 0
    investmentIncomeNet9 = quarterly_statementsDump.loc['investmentIncomeNet'][10]
    try:
        investmentIncomeNet9 = int(investmentIncomeNet9)
    except Exception:
        investmentIncomeNet9 = 0

    netInterestIncome9 = quarterly_statementsDump.loc['netInterestIncome'][10]
    try:
        netInterestIncome9 = int(netInterestIncome9)
    except Exception:
        netInterestIncome9 = 0
    interestIncome9 = quarterly_statementsDump.loc['interestIncome'][10]
    try:
        interestIncome9 = int(interestIncome9)
    except Exception:
        interestIncome9 = 0
    interestExpense9 = quarterly_statementsDump.loc['interestExpense'][10]
    try:
        interestExpense9 = int(interestExpense9)
    except Exception:
        interestExpense9 = 0
    nonInterestIncome9 = quarterly_statementsDump.loc['nonInterestIncome'][10]
    try:
        nonInterestIncome9 = int(nonInterestIncome9)
    except Exception:
        nonInterestIncome9 = 0
    otherNonOperatingIncome9 = quarterly_statementsDump.loc['otherNonOperatingIncome'][10]
    try:
        otherNonOperatingIncome9 = int(otherNonOperatingIncome9)
    except Exception:
        otherNonOperatingIncome9 = 0
    depreciation9 = quarterly_statementsDump.loc['depreciation'][10]
    try:
        depreciation9 = int(depreciation9)
    except Exception:
        depreciation9 = 0
    depreciationAndAmortization9 = quarterly_statementsDump.loc['depreciationAndAmortization'][10]
    try:
        depreciationAndAmortization9 = int(depreciationAndAmortization9)
    except Exception:
        depreciationAndAmortization9 = 0

    incomeBeforeTax9 = quarterly_statementsDump.loc['incomeBeforeTax'][10]
    try:
        incomeBeforeTax9 = int(incomeBeforeTax9)
    except Exception:
        incomeBeforeTax9 = 0

    incomeTaxExpense9 = quarterly_statementsDump.loc['incomeTaxExpense'][10]
    try:
        incomeTaxExpense9 = int(incomeTaxExpense9)
    except Exception:
        incomeTaxExpense9 = 0
    interestAndDebtExpense9 = quarterly_statementsDump.loc['interestAndDebtExpense'][10]
    try:
        interestAndDebtExpense9 = int(interestAndDebtExpense9)
    except Exception:
        interestAndDebtExpense9 = 0
    netIncomeFromContinuingOperations9 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][10]
    try:
        netIncomeFromContinuingOperations9 = int(netIncomeFromContinuingOperations9)
    except Exception:
        netIncomeFromContinuingOperations9 = 0
    comprehensiveIncomeNetOfTax9 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][10]
    try:
        comprehensiveIncomeNetOfTax9 = int(comprehensiveIncomeNetOfTax9)
    except Exception:
        comprehensiveIncomeNetOfTax9 = 0
    ebit9 = quarterly_statementsDump.loc['ebit'][10]
    try:
        ebit9 = int(ebit9)
    except Exception:
        ebit9 = 0
    ebitda9 = quarterly_statementsDump.loc['ebitda'][10]
    try:
        ebitda9 = int(ebitda9)
    except Exception:
        ebitda9 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 10]

    # Balance Sheet Values for tm9

    totalAssets9 = quarterly_statementsDump.loc['totalAssets'][10]
    try:
        totalAssets9 = int(totalAssets9)
    except Exception:
        totalAssets9 = 0
    totalCurrentAssets9 = quarterly_statementsDump.loc['totalCurrentAssets'][10]
    try:
        totalCurrentAssets9 = int(totalCurrentAssets9)
    except Exception:
        totalCurrentAssets9 = 0
    cashAndCashEquivalentsAtCarryingValue9 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][10]
    try:
        cashAndCashEquivalentsAtCarryingValue9 = int(cashAndCashEquivalentsAtCarryingValue9)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue9 = 0
    cashAndShortTermInvestments9 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][10]
    try:
        cashAndShortTermInvestments9 = int(cashAndShortTermInvestments9)
    except Exception:
        cashAndShortTermInvestments9 = 0
    inventory9 = quarterly_statementsDump.loc['inventory'][10]
    try:
        inventory9 = int(inventory9)
    except Exception:
        inventory9 = 0
    currentNetReceivables9 = quarterly_statementsDump.loc['currentNetReceivables'][10]
    try:
        currentNetReceivables9 = int(currentNetReceivables9)
    except Exception:
        currentNetReceivables9 = 0
    totalNonCurrentAssets9 = quarterly_statementsDump.loc['totalNonCurrentAssets'][10]
    try:
        totalNonCurrentAssets9 = int(totalNonCurrentAssets9)
    except Exception:
        totalNonCurrentAssets9 = 0
    propertyPlantEquipment9 = quarterly_statementsDump.loc['propertyPlantEquipment'][10]
    try:
        propertyPlantEquipment9 = int(propertyPlantEquipment9)
    except Exception:
        propertyPlantEquipment9 = 0
    accumulatedDepreciationAmortizationPPE9 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][10]
    try:
        accumulatedDepreciationAmortizationPPE9 = int(accumulatedDepreciationAmortizationPPE9)
    except Exception:
        accumulatedDepreciationAmortizationPPE9 = 0
    intangibleAssets9 = quarterly_statementsDump.loc['intangibleAssets'][10]
    try:
        intangibleAssets9 = int(intangibleAssets9)
    except Exception:
        intangibleAssets9 = 0
    intangibleAssetsExcludingGoodwill9 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][10]
    try:
        intangibleAssetsExcludingGoodwill9 = int(intangibleAssetsExcludingGoodwill9)
    except Exception:
        intangibleAssetsExcludingGoodwill9 = 0
    goodwill9 = quarterly_statementsDump.loc['goodwill'][10]
    try:
        goodwill9 = int(goodwill9)
    except Exception:
        goodwill9 = 0
    investments9 = quarterly_statementsDump.loc['investments'][10]
    try:
        investments9 = int(investments9)
    except Exception:
        investments9 = 0
    longTermInvestments9 = quarterly_statementsDump.loc['longTermInvestments'][10]
    try:
        longTermInvestments9 = int(longTermInvestments9)
    except Exception:
        longTermInvestments9 = 0
    shortTermInvestments9 = quarterly_statementsDump.loc['shortTermInvestments'][10]
    try:
        shortTermInvestments9 = int(shortTermInvestments9)
    except Exception:
        shortTermInvestments9 = 0
    otherCurrentAssets9 = quarterly_statementsDump.loc['otherCurrentAssets'][10]
    try:
        otherCurrentAssets9 = int(otherCurrentAssets9)
    except Exception:
        otherCurrentAssets9 = 0
    otherNonCurrrentAssets9 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][10]
    try:
        otherNonCurrrentAssets9 = int(otherNonCurrrentAssets9)
    except Exception:
        otherNonCurrrentAssets9 = 0
    totalLiabilities9 = quarterly_statementsDump.loc['totalLiabilities'][10]
    try:
        totalLiabilities9 = int(totalLiabilities9)
    except Exception:
        totalLiabilities9 = 0
    totalCurrentLiabilities9 = quarterly_statementsDump.loc['totalCurrentLiabilities'][10]
    try:
        totalCurrentLiabilities9 = int(totalCurrentLiabilities9)
    except Exception:
        totalCurrentLiabilities9 = 0
    currentAccountsPayable9 = quarterly_statementsDump.loc['currentAccountsPayable'][10]
    try:
        currentAccountsPayable9 = int(currentAccountsPayable9)
    except Exception:
        currentAccountsPayable9 = 0
    deferredRevenue9 = quarterly_statementsDump.loc['deferredRevenue'][10]
    try:
        deferredRevenue9 = int(deferredRevenue9)
    except Exception:
        deferredRevenue9 = 0
    currentDebt9 = quarterly_statementsDump.loc['currentDebt'][10]
    try:
        currentDebt9 = int(currentDebt9)
    except Exception:
        currentDebt9 = 0
    shortTermDebt9 = quarterly_statementsDump.loc['shortTermDebt'][10]
    try:
        shortTermDebt9 = int(shortTermDebt9)
    except Exception:
        shortTermDebt9 = 0
    totalNonCurrentLiabilities9 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][10]
    try:
        totalNonCurrentLiabilities9 = int(totalNonCurrentLiabilities9)
    except Exception:
        totalNonCurrentLiabilities9 = 0
    capitalLeaseObligations9 = quarterly_statementsDump.loc['capitalLeaseObligations'][10]
    try:
        capitalLeaseObligations9 = int(capitalLeaseObligations9)
    except Exception:
        capitalLeaseObligations9 = 0

    longTermDebt9 = quarterly_statementsDump.loc['longTermDebt'][10]
    try:
        longTermDebt9 = int(longTermDebt9)
    except Exception:
        longTermDebt9 = 0
    currentLongTermDebt9 = quarterly_statementsDump.loc['currentLongTermDebt'][10]
    try:
        currentLongTermDebt9 = int(currentLongTermDebt9)
    except Exception:
        currentLongTermDebt9 = 0
    longTermDebtNoncurrent9 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][10]
    try:
        longTermDebtNoncurrent9 = int(longTermDebtNoncurrent9)
    except Exception:
        longTermDebtNoncurrent9 = 0
    shortLongTermDebtTotal9 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][10]
    try:
        shortLongTermDebtTotal9 = int(shortLongTermDebtTotal9)
    except Exception:
        shortLongTermDebtTotal9 = 0
    otherCurrentLiabilities9 = quarterly_statementsDump.loc['otherCurrentLiabilities'][10]
    try:
        otherCurrentLiabilities9 = int(otherCurrentLiabilities9)
    except Exception:
        otherCurrentLiabilities9 = 0
    otherNonCurrentLiabilities9 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][10]
    try:
        otherNonCurrentLiabilities9 = int(otherNonCurrentLiabilities9)
    except Exception:
        otherNonCurrentLiabilities9 = 0
    totalShareholderEquity9 = quarterly_statementsDump.loc['totalShareholderEquity'][10]
    try:
        totalShareholderEquity9 = int(totalShareholderEquity9)
    except Exception:
        totalShareholderEquity9 = 0
    treasuryStock9 = quarterly_statementsDump.loc['treasuryStock'][10]
    try:
        treasuryStock9 = int(treasuryStock9)
    except Exception:
        treasuryStock9 = 0
    retainedEarnings9 = quarterly_statementsDump.loc['retainedEarnings'][10]
    try:
        retainedEarnings9 = int(retainedEarnings9)
    except Exception:
        retainedEarnings9 = 0
    commonStock9 = quarterly_statementsDump.loc['commonStock'][10]
    try:
        commonStock9 = int(commonStock9)
    except Exception:
        commonStock9 = 0
    commonStockSharesOutstanding9 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][10]
    try:
        commonStockSharesOutstanding9 = int(commonStockSharesOutstanding9)
    except Exception:
        commonStockSharesOutstanding9 = 0

    # Cash-Flow Statement values for tm9
    operatingCashflow9 = quarterly_statementsDump.loc['operatingCashflow'][10]
    try:
        operatingCashflow9 = int(operatingCashflow9)
    except Exception:
        operatingCashflow9 = 0
    paymentsForOperatingActivities9 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][10]
    try:
        paymentsForOperatingActivities9 = int(paymentsForOperatingActivities9)
    except Exception:
        paymentsForOperatingActivities9 = 0
    proceedsFromOperatingActivities9 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][10]
    try:
        proceedsFromOperatingActivities9 = int(proceedsFromOperatingActivities9)
    except Exception:
        proceedsFromOperatingActivities9 = 0
    changeInOperatingLiabilities9 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][10]
    try:
        changeInOperatingLiabilities9 = int(changeInOperatingLiabilities9)
    except Exception:
        changeInOperatingLiabilities9 = 0
    changeInOperatingAssets9 = quarterly_statementsDump.loc['changeInOperatingAssets'][10]
    try:
        changeInOperatingAssets9 = int(changeInOperatingAssets9)
    except Exception:
        changeInOperatingAssets9 = 0
    depreciationDepletionAndAmortization9 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][10]
    try:
        depreciationDepletionAndAmortization9 = int(depreciationDepletionAndAmortization9)
    except Exception:
        depreciationDepletionAndAmortization9 = 0
    capitalExpenditures9 = quarterly_statementsDump.loc['capitalExpenditures'][10]
    try:
        capitalExpenditures9 = int(capitalExpenditures9)
    except Exception:
        capitalExpenditures9 = 0
    changeInReceivables9 = quarterly_statementsDump.loc['changeInReceivables'][10]
    try:
        changeInReceivables9 = int(changeInReceivables9)
    except Exception:
        changeInReceivables9 = 0
    changeInInventory9 = quarterly_statementsDump.loc['changeInInventory'][10]
    try:
        changeInInventory9 = int(changeInInventory9)
    except Exception:
        changeInInventory9 = 0
    profitLoss9 = quarterly_statementsDump.loc['profitLoss'][10]
    try:
        profitLoss9 = int(profitLoss9)
    except Exception:
        profitLoss9 = 0
    cashflowFromInvestment9 = quarterly_statementsDump.loc['cashflowFromInvestment'][10]
    try:
        cashflowFromInvestment9 = int(cashflowFromInvestment9)
    except Exception:
        cashflowFromInvestment9 = 0
    cashflowFromFinancing9 = quarterly_statementsDump.loc['cashflowFromFinancing'][10]
    try:
        cashflowFromFinancing9 = int(cashflowFromFinancing9)
    except Exception:
        cashflowFromFinancing9 = 0
    proceedsFromRepaymentsOfShortTermDebt9 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][10]
    try:
        proceedsFromRepaymentsOfShortTermDebt9 = int(proceedsFromRepaymentsOfShortTermDebt9)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt9 = 0
    paymentsForRepurchaseOfCommonStock9 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][10]
    try:
        paymentsForRepurchaseOfCommonStock9 = int(paymentsForRepurchaseOfCommonStock9)
    except Exception:
        paymentsForRepurchaseOfCommonStock9 = 0
    paymentsForRepurchaseOfEquity9 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][10]
    try:
        paymentsForRepurchaseOfEquity9 = int(paymentsForRepurchaseOfEquity9)
    except Exception:
        paymentsForRepurchaseOfEquity9 = 0
    paymentsForRepurchaseOfPreferredStock9 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][10]
    try:
        paymentsForRepurchaseOfPreferredStock9 = int(paymentsForRepurchaseOfPreferredStock9)
    except Exception:
        paymentsForRepurchaseOfPreferredStock9 = 0
    dividendPayout9 = quarterly_statementsDump.loc['dividendPayout'][10]
    try:
        dividendPayout9 = int(dividendPayout9)
    except Exception:
        dividendPayout9 = 0
    dividendPayoutCommonStock9 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][10]
    try:
        dividendPayoutCommonStock9 = int(dividendPayoutCommonStock9)
    except Exception:
        dividendPayoutCommonStock9 = 0
    dividendPayoutPreferredStock9 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][10]
    try:
        dividendPayoutPreferredStock9 = int(dividendPayoutPreferredStock9)
    except Exception:
        dividendPayoutPreferredStock9 = 0
    proceedsFromIssuanceOfCommonStock9 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][10]
    try:
        proceedsFromIssuanceOfCommonStock9 = int(proceedsFromIssuanceOfCommonStock9)
    except Exception:
        proceedsFromIssuanceOfCommonStock9 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet9 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][10]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet9 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet9)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet9 = 0
    proceedsFromIssuanceOfPreferredStock9 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][10]
    try:
        proceedsFromIssuanceOfPreferredStock9 = int(proceedsFromIssuanceOfPreferredStock9)
    except Exception:
        proceedsFromIssuanceOfPreferredStock9 = 0
    proceedsFromRepurchaseOfEquity9 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][10]
    try:
        proceedsFromRepurchaseOfEquity9 = int(proceedsFromRepurchaseOfEquity9)
    except Exception:
        proceedsFromRepurchaseOfEquity9 = 0
    proceedsFromSaleOfTreasuryStock9 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][10]
    try:
        proceedsFromSaleOfTreasuryStock9 = int(proceedsFromSaleOfTreasuryStock9)
    except Exception:
        proceedsFromSaleOfTreasuryStock9 = 0
    changeInCashAndCashEquivalents9 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][10]
    try:
        changeInCashAndCashEquivalents9 = int(changeInCashAndCashEquivalents9)
    except Exception:
        changeInCashAndCashEquivalents9 = 0
    changeInExchangeRate9 = quarterly_statementsDump.loc['changeInExchangeRate'][10]
    try:
        changeInExchangeRate9 = int(changeInExchangeRate9)
    except Exception:
        changeInExchangeRate9 = 0
    netIncome9 = quarterly_statementsDump.loc['netIncome'][10]
    try:
        netIncome9 = int(netIncome9)
    except Exception:
        netIncome9 = 0

    tTMnetIncome9 = (float(netIncome9) + float(netIncome10) + float(netIncome11) + float(netIncome12))
    try:
        tTMpreferredDivs9 = (int(dividendPayoutPreferredStock9) + int(dividendPayoutPreferredStock10) + int(
            dividendPayoutPreferredStock11) + int(dividendPayoutPreferredStock12))
    except Exception:
        tTMpreferredDivs9 = 0
    weightedAvgCommShrsOutstanding9 = (
            (float(commonStockSharesOutstanding9) + float(commonStockSharesOutstanding10) + float(
                commonStockSharesOutstanding11) + float(commonStockSharesOutstanding12)) / 9)
    quoteUnformatted9 = quoteUnformatted
    marketCap9 = calculateMarketCap(quoteUnformatted9, commonStockSharesOutstanding9)
    basicEPS9 = calculateBasicEPS(tTMnetIncome9, tTMpreferredDivs9, weightedAvgCommShrsOutstanding9)
    pE9 = calculatePE(quoteUnformatted9, basicEPS9)
    pCF9 = calculatePriceToCashFlow(quoteUnformatted9,
                                    calculateOperatingCashFlowPerShare(operatingCashflow9,
                                                                       weightedAvgCommShrsOutstanding9))
    pS9 = calculatePS(quoteUnformatted9, calculateSalesPerShare(totalRevenue9, weightedAvgCommShrsOutstanding9))
    pB9 = calculatePB(quoteUnformatted9,
                      calculateMarketToBookValue(marketCap9, totalAssets9, shortLongTermDebtTotal9, preferredStock=0))
    sustainableGrowthRate9 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout9, netIncome9)),
        calculateROE(netIncome9, totalShareholderEquity9))
    pEGRatio9 = calculatePEGRatio(pE9, (sustainableGrowthRate9 * 900))
    earningsYield9 = calculateEarningsYield(basicEPS9, quoteUnformatted9)
    cashFlowPerShare9 = calculateOperatingCashFlowPerShare(operatingCashflow9, weightedAvgCommShrsOutstanding9)
    ebitdaPerShare9 = calculateEBITDAperShare(ebitda9, weightedAvgCommShrsOutstanding9)
    tTMDividendPayout9 = (
        (float(dividendPayout9) + float(dividendPayout10) + float(dividendPayout11) + float(dividendPayout12)))
    dividendsPerShare9 = calculateDividendsPerShare(tTMDividendPayout9, weightedAvgCommShrsOutstanding9)
    currentQuarterGrossProfitMargin9 = calculateGrossProfitMargin(totalRevenue9, costofGoodsAndServicesSold9)
    tTmTotalRevenue9 = ((float(totalRevenue9) + float(totalRevenue10) + float(totalRevenue11) + float(totalRevenue12)))
    tTmCOGS9 = ((float(costofGoodsAndServicesSold9) + float(costofGoodsAndServicesSold10) + float(
        costofGoodsAndServicesSold11) + float(costofGoodsAndServicesSold12)))
    tTMGrossProfitMargin9 = calculateGrossProfitMargin(tTmTotalRevenue9, tTmCOGS9)
    currentQuarterOperatingMargin9 = calculateOperatingMargin(operatingIncome9, totalRevenue9)
    tTMOperatingIncome9 = (
        (float(operatingIncome9) + float(operatingIncome10) + float(operatingIncome11) + float(operatingIncome12)))
    tTMOperatingMargin9 = calculateOperatingMargin(tTMOperatingIncome9, tTmTotalRevenue9)
    currentQuarterPreTaxMargin9 = calculatePreTaxMargin(calculateEBT(ebit9, interestExpense9), totalRevenue9)
    tTMebit9 = ((float(ebit9) + float(ebit10) + float(ebit11) + float(ebit12)))
    tTMInterestExpense9 = (
        (float(interestExpense9) + float(interestExpense10) + float(interestExpense11) + float(interestExpense12)))
    tTMPreTaxMargin9 = calculatePreTaxMargin(calculateEBT(tTMebit9, tTMInterestExpense9), tTmTotalRevenue9)
    currentQuarterNetProfitMargin9 = calculateNetProfitMargin(netIncome9, totalRevenue9)
    tTMNetProfitMargin9 = calculateNetProfitMargin(tTMnetIncome9, tTmTotalRevenue9)
    currentQuarterAvgTotalAssets9 = ((float(totalAssets9) + float(totalAssets10)) / 4)
    currentQuarterOperatingROA9 = (calculateOperatingROA(operatingIncome9, currentQuarterAvgTotalAssets9)) * 4
    tTMAvgTotalAssets9 = (
                (float(totalAssets9) + float(totalAssets10) + float(totalAssets11) + float(totalAssets12)) / 4)
    tTMOperatingROA9 = calculateOperatingROA(tTMOperatingIncome9, tTMAvgTotalAssets9)
    currentQuarterROA9 = (calculateROA(netIncome9, currentQuarterAvgTotalAssets9)) * 4
    tTMROA9 = calculateROA(tTMnetIncome9, tTMAvgTotalAssets9)
    currentQuarterReturnOnTotalCapital9 = (calculateReturnOnTotalCapital(ebit9, shortLongTermDebtTotal9,
                                                                         totalShareholderEquity9)) * 4
    tTMReturnOnTotalCapital9 = calculateReturnOnTotalCapital(tTMebit9, shortLongTermDebtTotal9, totalShareholderEquity9)
    currentQuarterROE9 = (calculateROE(netIncome9, totalShareholderEquity9)) * 4
    tTMROE9 = calculateROE(tTMnetIncome9, totalShareholderEquity9)
    currentQuarterAvgCommonEquity9 = ((float(totalShareholderEquity9) + float(totalShareholderEquity9)) / 4)
    currentQuarterReturnOnCommonEquity9 = (calculateReturnOnCommonEquity(netIncome9, dividendPayoutPreferredStock9,
                                                                         currentQuarterAvgCommonEquity9)) * 4
    tTMAvgCommonEquity9 = ((float(totalShareholderEquity9) + float(totalShareholderEquity10) + float(
        totalShareholderEquity11) + float(totalShareholderEquity12)) / 4)
    tTMReturnOnCommonEquity9 = calculateReturnOnCommonEquity(tTMnetIncome9, tTMpreferredDivs9, tTMAvgCommonEquity9)
    debtRatio9 = calculateDebtRatio(totalLiabilities9, totalAssets9)
    debtToEquityRatio9 = calculateDebtToEquity(shortLongTermDebtTotal9, totalShareholderEquity9)
    debtToAssetRatio9 = calculateDebtToAssetRatio(shortLongTermDebtTotal9, totalAssets9)
    debtToCapitalRatio9 = calculateDebtToCapitalRatio(shortLongTermDebtTotal9, totalShareholderEquity9)

    financialLeverage9 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets9, currentQuarterAvgCommonEquity9)
    interestCoverage9 = calculateInterestCoverageRatio(operatingCashflow9, interestExpense9, incomeTaxExpense9)
    fixedChargeCoverageRatio9 = calculateFixedChargeCoverage(ebit9, capitalLeaseObligations9, interestExpense9)

    ## tm8  VARIABLES
    # Income Statement Variables for tm8
    gross_profit8 = quarterly_statementsDump.loc['grossProfit'][11]
    try:
        gross_profit8 = int(gross_profit8)
    except Exception:
        gross_profit8 = 0
    totalRevenue8 = quarterly_statementsDump.loc['totalRevenue'][11]
    try:
        totalRevenue8 = int(totalRevenue8)
    except Exception:
        totalRevenue8 = 0
    costOfRevenue8 = quarterly_statementsDump.loc['costOfRevenue'][11]
    try:
        costOfRevenue8 = int(costOfRevenue8)
    except Exception:
        costOfRevenue8 = 0
    costofGoodsAndServicesSold8 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][11]
    try:
        costofGoodsAndServicesSold8 = int(costofGoodsAndServicesSold8)
    except Exception:
        costofGoodsAndServicesSold8 = 0
    operatingIncome8 = quarterly_statementsDump.loc['operatingIncome'][11]
    try:
        operatingIncome8 = int(operatingIncome8)
    except Exception:
        operatingIncome8 = 0
    sellingGeneralAndAdministrative8 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][11]
    try:
        sellingGeneralAndAdministrative8 = int(sellingGeneralAndAdministrative8)
    except Exception:
        sellingGeneralAndAdministrative8 = 0
    researchAndDevelopment8 = quarterly_statementsDump.loc['researchAndDevelopment'][11]
    try:
        researchAndDevelopment8 = int(researchAndDevelopment8)
    except Exception:
        researchAndDevelopment8 = 0
    operatingExpenses8 = quarterly_statementsDump.loc['operatingExpenses'][11]
    try:
        operatingExpenses8 = int(operatingExpenses8)
    except Exception:
        operatingExpenses8 = 0
    investmentIncomeNet8 = quarterly_statementsDump.loc['investmentIncomeNet'][11]
    try:
        investmentIncomeNet8 = int(investmentIncomeNet8)
    except Exception:
        investmentIncomeNet8 = 0

    netInterestIncome8 = quarterly_statementsDump.loc['netInterestIncome'][11]
    try:
        netInterestIncome8 = int(netInterestIncome8)
    except Exception:
        netInterestIncome8 = 0
    interestIncome8 = quarterly_statementsDump.loc['interestIncome'][11]
    try:
        interestIncome8 = int(interestIncome8)
    except Exception:
        interestIncome8 = 0
    interestExpense8 = quarterly_statementsDump.loc['interestExpense'][11]
    try:
        interestExpense8 = int(interestExpense8)
    except Exception:
        interestExpense8 = 0
    nonInterestIncome8 = quarterly_statementsDump.loc['nonInterestIncome'][11]
    try:
        nonInterestIncome8 = int(nonInterestIncome8)
    except Exception:
        nonInterestIncome8 = 0
    otherNonOperatingIncome8 = quarterly_statementsDump.loc['otherNonOperatingIncome'][11]
    try:
        otherNonOperatingIncome8 = int(otherNonOperatingIncome8)
    except Exception:
        otherNonOperatingIncome8 = 0
    depreciation8 = quarterly_statementsDump.loc['depreciation'][11]
    try:
        depreciation8 = int(depreciation8)
    except Exception:
        depreciation8 = 0
    depreciationAndAmortization8 = quarterly_statementsDump.loc['depreciationAndAmortization'][11]
    try:
        depreciationAndAmortization8 = int(depreciationAndAmortization8)
    except Exception:
        depreciationAndAmortization8 = 0

    incomeBeforeTax8 = quarterly_statementsDump.loc['incomeBeforeTax'][11]
    try:
        incomeBeforeTax8 = int(incomeBeforeTax8)
    except Exception:
        incomeBeforeTax8 = 0

    incomeTaxExpense8 = quarterly_statementsDump.loc['incomeTaxExpense'][11]
    try:
        incomeTaxExpense8 = int(incomeTaxExpense8)
    except Exception:
        incomeTaxExpense8 = 0
    interestAndDebtExpense8 = quarterly_statementsDump.loc['interestAndDebtExpense'][11]
    try:
        interestAndDebtExpense8 = int(interestAndDebtExpense8)
    except Exception:
        interestAndDebtExpense8 = 0
    netIncomeFromContinuingOperations8 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][11]
    try:
        netIncomeFromContinuingOperations8 = int(netIncomeFromContinuingOperations8)
    except Exception:
        netIncomeFromContinuingOperations8 = 0
    comprehensiveIncomeNetOfTax8 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][11]
    try:
        comprehensiveIncomeNetOfTax8 = int(comprehensiveIncomeNetOfTax8)
    except Exception:
        comprehensiveIncomeNetOfTax8 = 0
    ebit8 = quarterly_statementsDump.loc['ebit'][11]
    try:
        ebit8 = int(ebit8)
    except Exception:
        ebit8 = 0
    ebitda8 = quarterly_statementsDump.loc['ebitda'][11]
    try:
        ebitda8 = int(ebitda8)
    except Exception:
        ebitda8 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 11]

    # Balance Sheet Values for tm8

    totalAssets8 = quarterly_statementsDump.loc['totalAssets'][11]
    try:
        totalAssets8 = int(totalAssets8)
    except Exception:
        totalAssets8 = 0
    totalCurrentAssets8 = quarterly_statementsDump.loc['totalCurrentAssets'][11]
    try:
        totalCurrentAssets8 = int(totalCurrentAssets8)
    except Exception:
        totalCurrentAssets8 = 0
    cashAndCashEquivalentsAtCarryingValue8 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][11]
    try:
        cashAndCashEquivalentsAtCarryingValue8 = int(cashAndCashEquivalentsAtCarryingValue8)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue8 = 0
    cashAndShortTermInvestments8 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][11]
    try:
        cashAndShortTermInvestments8 = int(cashAndShortTermInvestments8)
    except Exception:
        cashAndShortTermInvestments8 = 0
    inventory8 = quarterly_statementsDump.loc['inventory'][11]
    try:
        inventory8 = int(inventory8)
    except Exception:
        inventory8 = 0
    currentNetReceivables8 = quarterly_statementsDump.loc['currentNetReceivables'][11]
    try:
        currentNetReceivables8 = int(currentNetReceivables8)
    except Exception:
        currentNetReceivables8 = 0
    totalNonCurrentAssets8 = quarterly_statementsDump.loc['totalNonCurrentAssets'][11]
    try:
        totalNonCurrentAssets8 = int(totalNonCurrentAssets8)
    except Exception:
        totalNonCurrentAssets8 = 0
    propertyPlantEquipment8 = quarterly_statementsDump.loc['propertyPlantEquipment'][11]
    try:
        propertyPlantEquipment8 = int(propertyPlantEquipment8)
    except Exception:
        propertyPlantEquipment8 = 0
    accumulatedDepreciationAmortizationPPE8 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][11]
    try:
        accumulatedDepreciationAmortizationPPE8 = int(accumulatedDepreciationAmortizationPPE8)
    except Exception:
        accumulatedDepreciationAmortizationPPE8 = 0
    intangibleAssets8 = quarterly_statementsDump.loc['intangibleAssets'][11]
    try:
        intangibleAssets8 = int(intangibleAssets8)
    except Exception:
        intangibleAssets8 = 0
    intangibleAssetsExcludingGoodwill8 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][11]
    try:
        intangibleAssetsExcludingGoodwill8 = int(intangibleAssetsExcludingGoodwill8)
    except Exception:
        intangibleAssetsExcludingGoodwill8 = 0
    goodwill8 = quarterly_statementsDump.loc['goodwill'][11]
    try:
        goodwill8 = int(goodwill8)
    except Exception:
        goodwill8 = 0
    investments8 = quarterly_statementsDump.loc['investments'][11]
    try:
        investments8 = int(investments8)
    except Exception:
        investments8 = 0
    longTermInvestments8 = quarterly_statementsDump.loc['longTermInvestments'][11]
    try:
        longTermInvestments8 = int(longTermInvestments8)
    except Exception:
        longTermInvestments8 = 0
    shortTermInvestments8 = quarterly_statementsDump.loc['shortTermInvestments'][11]
    try:
        shortTermInvestments8 = int(shortTermInvestments8)
    except Exception:
        shortTermInvestments8 = 0
    otherCurrentAssets8 = quarterly_statementsDump.loc['otherCurrentAssets'][11]
    try:
        otherCurrentAssets8 = int(otherCurrentAssets8)
    except Exception:
        otherCurrentAssets8 = 0
    otherNonCurrrentAssets8 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][11]
    try:
        otherNonCurrrentAssets8 = int(otherNonCurrrentAssets8)
    except Exception:
        otherNonCurrrentAssets8 = 0
    totalLiabilities8 = quarterly_statementsDump.loc['totalLiabilities'][11]
    try:
        totalLiabilities8 = int(totalLiabilities8)
    except Exception:
        totalLiabilities8 = 0
    totalCurrentLiabilities8 = quarterly_statementsDump.loc['totalCurrentLiabilities'][11]
    try:
        totalCurrentLiabilities8 = int(totalCurrentLiabilities8)
    except Exception:
        totalCurrentLiabilities8 = 0
    currentAccountsPayable8 = quarterly_statementsDump.loc['currentAccountsPayable'][11]
    try:
        currentAccountsPayable8 = int(currentAccountsPayable8)
    except Exception:
        currentAccountsPayable8 = 0
    deferredRevenue8 = quarterly_statementsDump.loc['deferredRevenue'][11]
    try:
        deferredRevenue8 = int(deferredRevenue8)
    except Exception:
        deferredRevenue8 = 0
    currentDebt8 = quarterly_statementsDump.loc['currentDebt'][11]
    try:
        currentDebt8 = int(currentDebt8)
    except Exception:
        currentDebt8 = 0
    shortTermDebt8 = quarterly_statementsDump.loc['shortTermDebt'][11]
    try:
        shortTermDebt8 = int(shortTermDebt8)
    except Exception:
        shortTermDebt8 = 0
    totalNonCurrentLiabilities8 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][11]
    try:
        totalNonCurrentLiabilities8 = int(totalNonCurrentLiabilities8)
    except Exception:
        totalNonCurrentLiabilities8 = 0
    capitalLeaseObligations8 = quarterly_statementsDump.loc['capitalLeaseObligations'][11]
    try:
        capitalLeaseObligations8 = int(capitalLeaseObligations8)
    except Exception:
        capitalLeaseObligations8 = 0

    longTermDebt8 = quarterly_statementsDump.loc['longTermDebt'][11]
    try:
        longTermDebt8 = int(longTermDebt8)
    except Exception:
        longTermDebt8 = 0
    currentLongTermDebt8 = quarterly_statementsDump.loc['currentLongTermDebt'][11]
    try:
        currentLongTermDebt8 = int(currentLongTermDebt8)
    except Exception:
        currentLongTermDebt8 = 0
    longTermDebtNoncurrent8 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][11]
    try:
        longTermDebtNoncurrent8 = int(longTermDebtNoncurrent8)
    except Exception:
        longTermDebtNoncurrent8 = 0
    shortLongTermDebtTotal8 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][11]
    try:
        shortLongTermDebtTotal8 = int(shortLongTermDebtTotal8)
    except Exception:
        shortLongTermDebtTotal8 = 0
    otherCurrentLiabilities8 = quarterly_statementsDump.loc['otherCurrentLiabilities'][11]
    try:
        otherCurrentLiabilities8 = int(otherCurrentLiabilities8)
    except Exception:
        otherCurrentLiabilities8 = 0
    otherNonCurrentLiabilities8 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][11]
    try:
        otherNonCurrentLiabilities8 = int(otherNonCurrentLiabilities8)
    except Exception:
        otherNonCurrentLiabilities8 = 0
    totalShareholderEquity8 = quarterly_statementsDump.loc['totalShareholderEquity'][11]
    try:
        totalShareholderEquity8 = int(totalShareholderEquity8)
    except Exception:
        totalShareholderEquity8 = 0
    treasuryStock8 = quarterly_statementsDump.loc['treasuryStock'][11]
    try:
        treasuryStock8 = int(treasuryStock8)
    except Exception:
        treasuryStock8 = 0
    retainedEarnings8 = quarterly_statementsDump.loc['retainedEarnings'][11]
    try:
        retainedEarnings8 = int(retainedEarnings8)
    except Exception:
        retainedEarnings8 = 0
    commonStock8 = quarterly_statementsDump.loc['commonStock'][11]
    try:
        commonStock8 = int(commonStock8)
    except Exception:
        commonStock8 = 0
    commonStockSharesOutstanding8 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][11]
    try:
        commonStockSharesOutstanding8 = int(commonStockSharesOutstanding8)
    except Exception:
        commonStockSharesOutstanding8 = 0

    # Cash-Flow Statement values for tm8
    operatingCashflow8 = quarterly_statementsDump.loc['operatingCashflow'][11]
    try:
        operatingCashflow8 = int(operatingCashflow8)
    except Exception:
        operatingCashflow8 = 0
    paymentsForOperatingActivities8 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][11]
    try:
        paymentsForOperatingActivities8 = int(paymentsForOperatingActivities8)
    except Exception:
        paymentsForOperatingActivities8 = 0
    proceedsFromOperatingActivities8 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][11]
    try:
        proceedsFromOperatingActivities8 = int(proceedsFromOperatingActivities8)
    except Exception:
        proceedsFromOperatingActivities8 = 0
    changeInOperatingLiabilities8 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][11]
    try:
        changeInOperatingLiabilities8 = int(changeInOperatingLiabilities8)
    except Exception:
        changeInOperatingLiabilities8 = 0
    changeInOperatingAssets8 = quarterly_statementsDump.loc['changeInOperatingAssets'][11]
    try:
        changeInOperatingAssets8 = int(changeInOperatingAssets8)
    except Exception:
        changeInOperatingAssets8 = 0
    depreciationDepletionAndAmortization8 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][11]
    try:
        depreciationDepletionAndAmortization8 = int(depreciationDepletionAndAmortization8)
    except Exception:
        depreciationDepletionAndAmortization8 = 0
    capitalExpenditures8 = quarterly_statementsDump.loc['capitalExpenditures'][11]
    try:
        capitalExpenditures8 = int(capitalExpenditures8)
    except Exception:
        capitalExpenditures8 = 0
    changeInReceivables8 = quarterly_statementsDump.loc['changeInReceivables'][11]
    try:
        changeInReceivables8 = int(changeInReceivables8)
    except Exception:
        changeInReceivables8 = 0
    changeInInventory8 = quarterly_statementsDump.loc['changeInInventory'][11]
    try:
        changeInInventory8 = int(changeInInventory8)
    except Exception:
        changeInInventory8 = 0
    profitLoss8 = quarterly_statementsDump.loc['profitLoss'][11]
    try:
        profitLoss8 = int(profitLoss8)
    except Exception:
        profitLoss8 = 0
    cashflowFromInvestment8 = quarterly_statementsDump.loc['cashflowFromInvestment'][11]
    try:
        cashflowFromInvestment8 = int(cashflowFromInvestment8)
    except Exception:
        cashflowFromInvestment8 = 0
    cashflowFromFinancing8 = quarterly_statementsDump.loc['cashflowFromFinancing'][11]
    try:
        cashflowFromFinancing8 = int(cashflowFromFinancing8)
    except Exception:
        cashflowFromFinancing8 = 0
    proceedsFromRepaymentsOfShortTermDebt8 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][11]
    try:
        proceedsFromRepaymentsOfShortTermDebt8 = int(proceedsFromRepaymentsOfShortTermDebt8)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt8 = 0
    paymentsForRepurchaseOfCommonStock8 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][11]
    try:
        paymentsForRepurchaseOfCommonStock8 = int(paymentsForRepurchaseOfCommonStock8)
    except Exception:
        paymentsForRepurchaseOfCommonStock8 = 0
    paymentsForRepurchaseOfEquity8 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][11]
    try:
        paymentsForRepurchaseOfEquity8 = int(paymentsForRepurchaseOfEquity8)
    except Exception:
        paymentsForRepurchaseOfEquity8 = 0
    paymentsForRepurchaseOfPreferredStock8 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][11]
    try:
        paymentsForRepurchaseOfPreferredStock8 = int(paymentsForRepurchaseOfPreferredStock8)
    except Exception:
        paymentsForRepurchaseOfPreferredStock8 = 0
    dividendPayout8 = quarterly_statementsDump.loc['dividendPayout'][11]
    try:
        dividendPayout8 = int(dividendPayout8)
    except Exception:
        dividendPayout8 = 0
    dividendPayoutCommonStock8 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][11]
    try:
        dividendPayoutCommonStock8 = int(dividendPayoutCommonStock8)
    except Exception:
        dividendPayoutCommonStock8 = 0
    dividendPayoutPreferredStock8 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][11]
    try:
        dividendPayoutPreferredStock8 = int(dividendPayoutPreferredStock8)
    except Exception:
        dividendPayoutPreferredStock8 = 0
    proceedsFromIssuanceOfCommonStock8 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][11]
    try:
        proceedsFromIssuanceOfCommonStock8 = int(proceedsFromIssuanceOfCommonStock8)
    except Exception:
        proceedsFromIssuanceOfCommonStock8 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet8 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][11]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet8 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet8)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet8 = 0
    proceedsFromIssuanceOfPreferredStock8 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][11]
    try:
        proceedsFromIssuanceOfPreferredStock8 = int(proceedsFromIssuanceOfPreferredStock8)
    except Exception:
        proceedsFromIssuanceOfPreferredStock8 = 0
    proceedsFromRepurchaseOfEquity8 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][11]
    try:
        proceedsFromRepurchaseOfEquity8 = int(proceedsFromRepurchaseOfEquity8)
    except Exception:
        proceedsFromRepurchaseOfEquity8 = 0
    proceedsFromSaleOfTreasuryStock8 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][11]
    try:
        proceedsFromSaleOfTreasuryStock8 = int(proceedsFromSaleOfTreasuryStock8)
    except Exception:
        proceedsFromSaleOfTreasuryStock8 = 0
    changeInCashAndCashEquivalents8 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][11]
    try:
        changeInCashAndCashEquivalents8 = int(changeInCashAndCashEquivalents8)
    except Exception:
        changeInCashAndCashEquivalents8 = 0
    changeInExchangeRate8 = quarterly_statementsDump.loc['changeInExchangeRate'][11]
    try:
        changeInExchangeRate8 = int(changeInExchangeRate8)
    except Exception:
        changeInExchangeRate8 = 0
    netIncome8 = quarterly_statementsDump.loc['netIncome'][11]
    try:
        netIncome8 = int(netIncome8)
    except Exception:
        netIncome8 = 0

    tTMnetIncome8 = (float(netIncome8) + float(netIncome9) + float(netIncome10) + float(netIncome11))
    try:
        tTMpreferredDivs8 = (int(dividendPayoutPreferredStock8) + int(dividendPayoutPreferredStock9) + int(
            dividendPayoutPreferredStock10) + int(dividendPayoutPreferredStock11))
    except Exception:
        tTMpreferredDivs8 = 0
    weightedAvgCommShrsOutstanding8 = (
            (float(commonStockSharesOutstanding8) + float(commonStockSharesOutstanding9) + float(
                commonStockSharesOutstanding10) + float(commonStockSharesOutstanding11)) / 8)
    quoteUnformatted8 = quoteUnformatted
    marketCap8 = calculateMarketCap(quoteUnformatted8, commonStockSharesOutstanding8)
    basicEPS8 = calculateBasicEPS(tTMnetIncome8, tTMpreferredDivs8, weightedAvgCommShrsOutstanding8)
    pE8 = calculatePE(quoteUnformatted8, basicEPS8)
    pCF8 = calculatePriceToCashFlow(quoteUnformatted8,
                                    calculateOperatingCashFlowPerShare(operatingCashflow8,
                                                                       weightedAvgCommShrsOutstanding8))
    pS8 = calculatePS(quoteUnformatted8, calculateSalesPerShare(totalRevenue8, weightedAvgCommShrsOutstanding8))
    pB8 = calculatePB(quoteUnformatted8,
                      calculateMarketToBookValue(marketCap8, totalAssets8, shortLongTermDebtTotal8, preferredStock=0))
    sustainableGrowthRate8 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout8, netIncome8)),
        calculateROE(netIncome8, totalShareholderEquity8))
    pEGRatio8 = calculatePEGRatio(pE8, (sustainableGrowthRate8 * 800))
    earningsYield8 = calculateEarningsYield(basicEPS8, quoteUnformatted8)
    cashFlowPerShare8 = calculateOperatingCashFlowPerShare(operatingCashflow8, weightedAvgCommShrsOutstanding8)
    ebitdaPerShare8 = calculateEBITDAperShare(ebitda8, weightedAvgCommShrsOutstanding8)
    tTMDividendPayout8 = (
        (float(dividendPayout8) + float(dividendPayout9) + float(dividendPayout10) + float(dividendPayout11)))
    dividendsPerShare8 = calculateDividendsPerShare(tTMDividendPayout8, weightedAvgCommShrsOutstanding8)
    currentQuarterGrossProfitMargin8 = calculateGrossProfitMargin(totalRevenue8, costofGoodsAndServicesSold8)
    tTmTotalRevenue8 = ((float(totalRevenue8) + float(totalRevenue9) + float(totalRevenue10) + float(totalRevenue11)))
    tTmCOGS8 = ((float(costofGoodsAndServicesSold8) + float(costofGoodsAndServicesSold9) + float(
        costofGoodsAndServicesSold10) + float(costofGoodsAndServicesSold11)))
    tTMGrossProfitMargin8 = calculateGrossProfitMargin(tTmTotalRevenue8, tTmCOGS8)
    currentQuarterOperatingMargin8 = calculateOperatingMargin(operatingIncome8, totalRevenue8)
    tTMOperatingIncome8 = (
        (float(operatingIncome8) + float(operatingIncome9) + float(operatingIncome10) + float(operatingIncome11)))
    tTMOperatingMargin8 = calculateOperatingMargin(tTMOperatingIncome8, tTmTotalRevenue8)
    currentQuarterPreTaxMargin8 = calculatePreTaxMargin(calculateEBT(ebit8, interestExpense8), totalRevenue8)
    tTMebit8 = ((float(ebit8) + float(ebit9) + float(ebit10) + float(ebit11)))
    tTMInterestExpense8 = (
        (float(interestExpense8) + float(interestExpense9) + float(interestExpense10) + float(interestExpense11)))
    tTMPreTaxMargin8 = calculatePreTaxMargin(calculateEBT(tTMebit8, tTMInterestExpense8), tTmTotalRevenue8)
    currentQuarterNetProfitMargin8 = calculateNetProfitMargin(netIncome8, totalRevenue8)
    tTMNetProfitMargin8 = calculateNetProfitMargin(tTMnetIncome8, tTmTotalRevenue8)
    currentQuarterAvgTotalAssets8 = ((float(totalAssets8) + float(totalAssets9)) / 4)
    currentQuarterOperatingROA8 = (calculateOperatingROA(operatingIncome8, currentQuarterAvgTotalAssets8)) * 4
    tTMAvgTotalAssets8 = ((float(totalAssets8) + float(totalAssets9) + float(totalAssets10) + float(totalAssets11)) / 4)
    tTMOperatingROA8 = calculateOperatingROA(tTMOperatingIncome8, tTMAvgTotalAssets8)
    currentQuarterROA8 = (calculateROA(netIncome8, currentQuarterAvgTotalAssets8)) * 4
    tTMROA8 = calculateROA(tTMnetIncome8, tTMAvgTotalAssets8)
    currentQuarterReturnOnTotalCapital8 = (calculateReturnOnTotalCapital(ebit8, shortLongTermDebtTotal8,
                                                                         totalShareholderEquity8)) * 4
    tTMReturnOnTotalCapital8 = calculateReturnOnTotalCapital(tTMebit8, shortLongTermDebtTotal8, totalShareholderEquity8)
    currentQuarterROE8 = (calculateROE(netIncome8, totalShareholderEquity8)) * 4
    tTMROE8 = calculateROE(tTMnetIncome8, totalShareholderEquity8)
    currentQuarterAvgCommonEquity8 = ((float(totalShareholderEquity8) + float(totalShareholderEquity8)) / 4)
    currentQuarterReturnOnCommonEquity8 = (calculateReturnOnCommonEquity(netIncome8, dividendPayoutPreferredStock8,
                                                                         currentQuarterAvgCommonEquity8)) * 4
    tTMAvgCommonEquity8 = ((float(totalShareholderEquity8) + float(totalShareholderEquity9) + float(
        totalShareholderEquity10) + float(totalShareholderEquity11)) / 4)
    tTMReturnOnCommonEquity8 = calculateReturnOnCommonEquity(tTMnetIncome8, tTMpreferredDivs8, tTMAvgCommonEquity8)
    debtRatio8 = calculateDebtRatio(totalLiabilities8, totalAssets8)
    debtToEquityRatio8 = calculateDebtToEquity(shortLongTermDebtTotal8, totalShareholderEquity8)
    debtToAssetRatio8 = calculateDebtToAssetRatio(shortLongTermDebtTotal8, totalAssets8)
    debtToCapitalRatio8 = calculateDebtToCapitalRatio(shortLongTermDebtTotal8, totalShareholderEquity8)

    financialLeverage8 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets8, currentQuarterAvgCommonEquity8)
    interestCoverage8 = calculateInterestCoverageRatio(operatingCashflow8, interestExpense8, incomeTaxExpense8)
    fixedChargeCoverageRatio8 = calculateFixedChargeCoverage(ebit8, capitalLeaseObligations8, interestExpense8)

    ## tm7  VARIABLES
    # Income Statement Variables for tm7
    gross_profit7 = quarterly_statementsDump.loc['grossProfit'][12]
    try:
        gross_profit7 = int(gross_profit7)
    except Exception:
        gross_profit7 = 0
    totalRevenue7 = quarterly_statementsDump.loc['totalRevenue'][12]
    try:
        totalRevenue7 = int(totalRevenue7)
    except Exception:
        totalRevenue7 = 0
    costOfRevenue7 = quarterly_statementsDump.loc['costOfRevenue'][12]
    try:
        costOfRevenue7 = int(costOfRevenue7)
    except Exception:
        costOfRevenue7 = 0
    costofGoodsAndServicesSold7 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][12]
    try:
        costofGoodsAndServicesSold7 = int(costofGoodsAndServicesSold7)
    except Exception:
        costofGoodsAndServicesSold7 = 0
    operatingIncome7 = quarterly_statementsDump.loc['operatingIncome'][12]
    try:
        operatingIncome7 = int(operatingIncome7)
    except Exception:
        operatingIncome7 = 0
    sellingGeneralAndAdministrative7 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][12]
    try:
        sellingGeneralAndAdministrative7 = int(sellingGeneralAndAdministrative7)
    except Exception:
        sellingGeneralAndAdministrative7 = 0
    researchAndDevelopment7 = quarterly_statementsDump.loc['researchAndDevelopment'][12]
    try:
        researchAndDevelopment7 = int(researchAndDevelopment7)
    except Exception:
        researchAndDevelopment7 = 0
    operatingExpenses7 = quarterly_statementsDump.loc['operatingExpenses'][12]
    try:
        operatingExpenses7 = int(operatingExpenses7)
    except Exception:
        operatingExpenses7 = 0
    investmentIncomeNet7 = quarterly_statementsDump.loc['investmentIncomeNet'][12]
    try:
        investmentIncomeNet7 = int(investmentIncomeNet7)
    except Exception:
        investmentIncomeNet7 = 0

    netInterestIncome7 = quarterly_statementsDump.loc['netInterestIncome'][12]
    try:
        netInterestIncome7 = int(netInterestIncome7)
    except Exception:
        netInterestIncome7 = 0
    interestIncome7 = quarterly_statementsDump.loc['interestIncome'][12]
    try:
        interestIncome7 = int(interestIncome7)
    except Exception:
        interestIncome7 = 0
    interestExpense7 = quarterly_statementsDump.loc['interestExpense'][12]
    try:
        interestExpense7 = int(interestExpense7)
    except Exception:
        interestExpense7 = 0
    nonInterestIncome7 = quarterly_statementsDump.loc['nonInterestIncome'][12]
    try:
        nonInterestIncome7 = int(nonInterestIncome7)
    except Exception:
        nonInterestIncome7 = 0
    otherNonOperatingIncome7 = quarterly_statementsDump.loc['otherNonOperatingIncome'][12]
    try:
        otherNonOperatingIncome7 = int(otherNonOperatingIncome7)
    except Exception:
        otherNonOperatingIncome7 = 0
    depreciation7 = quarterly_statementsDump.loc['depreciation'][12]
    try:
        depreciation7 = int(depreciation7)
    except Exception:
        depreciation7 = 0
    depreciationAndAmortization7 = quarterly_statementsDump.loc['depreciationAndAmortization'][12]
    try:
        depreciationAndAmortization7 = int(depreciationAndAmortization7)
    except Exception:
        depreciationAndAmortization7 = 0

    incomeBeforeTax7 = quarterly_statementsDump.loc['incomeBeforeTax'][12]
    try:
        incomeBeforeTax7 = int(incomeBeforeTax7)
    except Exception:
        incomeBeforeTax7 = 0

    incomeTaxExpense7 = quarterly_statementsDump.loc['incomeTaxExpense'][12]
    try:
        incomeTaxExpense7 = int(incomeTaxExpense7)
    except Exception:
        incomeTaxExpense7 = 0
    interestAndDebtExpense7 = quarterly_statementsDump.loc['interestAndDebtExpense'][12]
    try:
        interestAndDebtExpense7 = int(interestAndDebtExpense7)
    except Exception:
        interestAndDebtExpense7 = 0
    netIncomeFromContinuingOperations7 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][12]
    try:
        netIncomeFromContinuingOperations7 = int(netIncomeFromContinuingOperations7)
    except Exception:
        netIncomeFromContinuingOperations7 = 0
    comprehensiveIncomeNetOfTax7 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][12]
    try:
        comprehensiveIncomeNetOfTax7 = int(comprehensiveIncomeNetOfTax7)
    except Exception:
        comprehensiveIncomeNetOfTax7 = 0
    ebit7 = quarterly_statementsDump.loc['ebit'][12]
    try:
        ebit7 = int(ebit7)
    except Exception:
        ebit7 = 0
    ebitda7 = quarterly_statementsDump.loc['ebitda'][12]
    try:
        ebitda7 = int(ebitda7)
    except Exception:
        ebitda7 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 12]

    # Balance Sheet Values for tm7

    totalAssets7 = quarterly_statementsDump.loc['totalAssets'][12]
    try:
        totalAssets7 = int(totalAssets7)
    except Exception:
        totalAssets7 = 0
    totalCurrentAssets7 = quarterly_statementsDump.loc['totalCurrentAssets'][12]
    try:
        totalCurrentAssets7 = int(totalCurrentAssets7)
    except Exception:
        totalCurrentAssets7 = 0
    cashAndCashEquivalentsAtCarryingValue7 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][12]
    try:
        cashAndCashEquivalentsAtCarryingValue7 = int(cashAndCashEquivalentsAtCarryingValue7)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue7 = 0
    cashAndShortTermInvestments7 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][12]
    try:
        cashAndShortTermInvestments7 = int(cashAndShortTermInvestments7)
    except Exception:
        cashAndShortTermInvestments7 = 0
    inventory7 = quarterly_statementsDump.loc['inventory'][12]
    try:
        inventory7 = int(inventory7)
    except Exception:
        inventory7 = 0
    currentNetReceivables7 = quarterly_statementsDump.loc['currentNetReceivables'][12]
    try:
        currentNetReceivables7 = int(currentNetReceivables7)
    except Exception:
        currentNetReceivables7 = 0
    totalNonCurrentAssets7 = quarterly_statementsDump.loc['totalNonCurrentAssets'][12]
    try:
        totalNonCurrentAssets7 = int(totalNonCurrentAssets7)
    except Exception:
        totalNonCurrentAssets7 = 0
    propertyPlantEquipment7 = quarterly_statementsDump.loc['propertyPlantEquipment'][12]
    try:
        propertyPlantEquipment7 = int(propertyPlantEquipment7)
    except Exception:
        propertyPlantEquipment7 = 0
    accumulatedDepreciationAmortizationPPE7 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][12]
    try:
        accumulatedDepreciationAmortizationPPE7 = int(accumulatedDepreciationAmortizationPPE7)
    except Exception:
        accumulatedDepreciationAmortizationPPE7 = 0
    intangibleAssets7 = quarterly_statementsDump.loc['intangibleAssets'][12]
    try:
        intangibleAssets7 = int(intangibleAssets7)
    except Exception:
        intangibleAssets7 = 0
    intangibleAssetsExcludingGoodwill7 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][12]
    try:
        intangibleAssetsExcludingGoodwill7 = int(intangibleAssetsExcludingGoodwill7)
    except Exception:
        intangibleAssetsExcludingGoodwill7 = 0
    goodwill7 = quarterly_statementsDump.loc['goodwill'][12]
    try:
        goodwill7 = int(goodwill7)
    except Exception:
        goodwill7 = 0
    investments7 = quarterly_statementsDump.loc['investments'][12]
    try:
        investments7 = int(investments7)
    except Exception:
        investments7 = 0
    longTermInvestments7 = quarterly_statementsDump.loc['longTermInvestments'][12]
    try:
        longTermInvestments7 = int(longTermInvestments7)
    except Exception:
        longTermInvestments7 = 0
    shortTermInvestments7 = quarterly_statementsDump.loc['shortTermInvestments'][12]
    try:
        shortTermInvestments7 = int(shortTermInvestments7)
    except Exception:
        shortTermInvestments7 = 0
    otherCurrentAssets7 = quarterly_statementsDump.loc['otherCurrentAssets'][12]
    try:
        otherCurrentAssets7 = int(otherCurrentAssets7)
    except Exception:
        otherCurrentAssets7 = 0
    otherNonCurrrentAssets7 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][12]
    try:
        otherNonCurrrentAssets7 = int(otherNonCurrrentAssets7)
    except Exception:
        otherNonCurrrentAssets7 = 0
    totalLiabilities7 = quarterly_statementsDump.loc['totalLiabilities'][12]
    try:
        totalLiabilities7 = int(totalLiabilities7)
    except Exception:
        totalLiabilities7 = 0
    totalCurrentLiabilities7 = quarterly_statementsDump.loc['totalCurrentLiabilities'][12]
    try:
        totalCurrentLiabilities7 = int(totalCurrentLiabilities7)
    except Exception:
        totalCurrentLiabilities7 = 0
    currentAccountsPayable7 = quarterly_statementsDump.loc['currentAccountsPayable'][12]
    try:
        currentAccountsPayable7 = int(currentAccountsPayable7)
    except Exception:
        currentAccountsPayable7 = 0
    deferredRevenue7 = quarterly_statementsDump.loc['deferredRevenue'][12]
    try:
        deferredRevenue7 = int(deferredRevenue7)
    except Exception:
        deferredRevenue7 = 0
    currentDebt7 = quarterly_statementsDump.loc['currentDebt'][12]
    try:
        currentDebt7 = int(currentDebt7)
    except Exception:
        currentDebt7 = 0
    shortTermDebt7 = quarterly_statementsDump.loc['shortTermDebt'][12]
    try:
        shortTermDebt7 = int(shortTermDebt7)
    except Exception:
        shortTermDebt7 = 0
    totalNonCurrentLiabilities7 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][12]
    try:
        totalNonCurrentLiabilities7 = int(totalNonCurrentLiabilities7)
    except Exception:
        totalNonCurrentLiabilities7 = 0
    capitalLeaseObligations7 = quarterly_statementsDump.loc['capitalLeaseObligations'][12]
    try:
        capitalLeaseObligations7 = int(capitalLeaseObligations7)
    except Exception:
        capitalLeaseObligations7 = 0

    longTermDebt7 = quarterly_statementsDump.loc['longTermDebt'][12]
    try:
        longTermDebt7 = int(longTermDebt7)
    except Exception:
        longTermDebt7 = 0
    currentLongTermDebt7 = quarterly_statementsDump.loc['currentLongTermDebt'][12]
    try:
        currentLongTermDebt7 = int(currentLongTermDebt7)
    except Exception:
        currentLongTermDebt7 = 0
    longTermDebtNoncurrent7 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][12]
    try:
        longTermDebtNoncurrent7 = int(longTermDebtNoncurrent7)
    except Exception:
        longTermDebtNoncurrent7 = 0
    shortLongTermDebtTotal7 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][12]
    try:
        shortLongTermDebtTotal7 = int(shortLongTermDebtTotal7)
    except Exception:
        shortLongTermDebtTotal7 = 0
    otherCurrentLiabilities7 = quarterly_statementsDump.loc['otherCurrentLiabilities'][12]
    try:
        otherCurrentLiabilities7 = int(otherCurrentLiabilities7)
    except Exception:
        otherCurrentLiabilities7 = 0
    otherNonCurrentLiabilities7 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][12]
    try:
        otherNonCurrentLiabilities7 = int(otherNonCurrentLiabilities7)
    except Exception:
        otherNonCurrentLiabilities7 = 0
    totalShareholderEquity7 = quarterly_statementsDump.loc['totalShareholderEquity'][12]
    try:
        totalShareholderEquity7 = int(totalShareholderEquity7)
    except Exception:
        totalShareholderEquity7 = 0
    treasuryStock7 = quarterly_statementsDump.loc['treasuryStock'][12]
    try:
        treasuryStock7 = int(treasuryStock7)
    except Exception:
        treasuryStock7 = 0
    retainedEarnings7 = quarterly_statementsDump.loc['retainedEarnings'][12]
    try:
        retainedEarnings7 = int(retainedEarnings7)
    except Exception:
        retainedEarnings7 = 0
    commonStock7 = quarterly_statementsDump.loc['commonStock'][12]
    try:
        commonStock7 = int(commonStock7)
    except Exception:
        commonStock7 = 0
    commonStockSharesOutstanding7 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][12]
    try:
        commonStockSharesOutstanding7 = int(commonStockSharesOutstanding7)
    except Exception:
        commonStockSharesOutstanding7 = 0

    # Cash-Flow Statement values for tm7
    operatingCashflow7 = quarterly_statementsDump.loc['operatingCashflow'][12]
    try:
        operatingCashflow7 = int(operatingCashflow7)
    except Exception:
        operatingCashflow7 = 0
    paymentsForOperatingActivities7 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][12]
    try:
        paymentsForOperatingActivities7 = int(paymentsForOperatingActivities7)
    except Exception:
        paymentsForOperatingActivities7 = 0
    proceedsFromOperatingActivities7 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][12]
    try:
        proceedsFromOperatingActivities7 = int(proceedsFromOperatingActivities7)
    except Exception:
        proceedsFromOperatingActivities7 = 0
    changeInOperatingLiabilities7 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][12]
    try:
        changeInOperatingLiabilities7 = int(changeInOperatingLiabilities7)
    except Exception:
        changeInOperatingLiabilities7 = 0
    changeInOperatingAssets7 = quarterly_statementsDump.loc['changeInOperatingAssets'][12]
    try:
        changeInOperatingAssets7 = int(changeInOperatingAssets7)
    except Exception:
        changeInOperatingAssets7 = 0
    depreciationDepletionAndAmortization7 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][12]
    try:
        depreciationDepletionAndAmortization7 = int(depreciationDepletionAndAmortization7)
    except Exception:
        depreciationDepletionAndAmortization7 = 0
    capitalExpenditures7 = quarterly_statementsDump.loc['capitalExpenditures'][12]
    try:
        capitalExpenditures7 = int(capitalExpenditures7)
    except Exception:
        capitalExpenditures7 = 0
    changeInReceivables7 = quarterly_statementsDump.loc['changeInReceivables'][12]
    try:
        changeInReceivables7 = int(changeInReceivables7)
    except Exception:
        changeInReceivables7 = 0
    changeInInventory7 = quarterly_statementsDump.loc['changeInInventory'][12]
    try:
        changeInInventory7 = int(changeInInventory7)
    except Exception:
        changeInInventory7 = 0
    profitLoss7 = quarterly_statementsDump.loc['profitLoss'][12]
    try:
        profitLoss7 = int(profitLoss7)
    except Exception:
        profitLoss7 = 0
    cashflowFromInvestment7 = quarterly_statementsDump.loc['cashflowFromInvestment'][12]
    try:
        cashflowFromInvestment7 = int(cashflowFromInvestment7)
    except Exception:
        cashflowFromInvestment7 = 0
    cashflowFromFinancing7 = quarterly_statementsDump.loc['cashflowFromFinancing'][12]
    try:
        cashflowFromFinancing7 = int(cashflowFromFinancing7)
    except Exception:
        cashflowFromFinancing7 = 0
    proceedsFromRepaymentsOfShortTermDebt7 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][12]
    try:
        proceedsFromRepaymentsOfShortTermDebt7 = int(proceedsFromRepaymentsOfShortTermDebt7)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt7 = 0
    paymentsForRepurchaseOfCommonStock7 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][12]
    try:
        paymentsForRepurchaseOfCommonStock7 = int(paymentsForRepurchaseOfCommonStock7)
    except Exception:
        paymentsForRepurchaseOfCommonStock7 = 0
    paymentsForRepurchaseOfEquity7 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][12]
    try:
        paymentsForRepurchaseOfEquity7 = int(paymentsForRepurchaseOfEquity7)
    except Exception:
        paymentsForRepurchaseOfEquity7 = 0
    paymentsForRepurchaseOfPreferredStock7 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][12]
    try:
        paymentsForRepurchaseOfPreferredStock7 = int(paymentsForRepurchaseOfPreferredStock7)
    except Exception:
        paymentsForRepurchaseOfPreferredStock7 = 0
    dividendPayout7 = quarterly_statementsDump.loc['dividendPayout'][12]
    try:
        dividendPayout7 = int(dividendPayout7)
    except Exception:
        dividendPayout7 = 0
    dividendPayoutCommonStock7 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][12]
    try:
        dividendPayoutCommonStock7 = int(dividendPayoutCommonStock7)
    except Exception:
        dividendPayoutCommonStock7 = 0
    dividendPayoutPreferredStock7 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][12]
    try:
        dividendPayoutPreferredStock7 = int(dividendPayoutPreferredStock7)
    except Exception:
        dividendPayoutPreferredStock7 = 0
    proceedsFromIssuanceOfCommonStock7 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][12]
    try:
        proceedsFromIssuanceOfCommonStock7 = int(proceedsFromIssuanceOfCommonStock7)
    except Exception:
        proceedsFromIssuanceOfCommonStock7 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet7 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][12]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet7 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet7)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet7 = 0
    proceedsFromIssuanceOfPreferredStock7 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][12]
    try:
        proceedsFromIssuanceOfPreferredStock7 = int(proceedsFromIssuanceOfPreferredStock7)
    except Exception:
        proceedsFromIssuanceOfPreferredStock7 = 0
    proceedsFromRepurchaseOfEquity7 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][12]
    try:
        proceedsFromRepurchaseOfEquity7 = int(proceedsFromRepurchaseOfEquity7)
    except Exception:
        proceedsFromRepurchaseOfEquity7 = 0
    proceedsFromSaleOfTreasuryStock7 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][12]
    try:
        proceedsFromSaleOfTreasuryStock7 = int(proceedsFromSaleOfTreasuryStock7)
    except Exception:
        proceedsFromSaleOfTreasuryStock7 = 0
    changeInCashAndCashEquivalents7 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][12]
    try:
        changeInCashAndCashEquivalents7 = int(changeInCashAndCashEquivalents7)
    except Exception:
        changeInCashAndCashEquivalents7 = 0
    changeInExchangeRate7 = quarterly_statementsDump.loc['changeInExchangeRate'][12]
    try:
        changeInExchangeRate7 = int(changeInExchangeRate7)
    except Exception:
        changeInExchangeRate7 = 0
    netIncome7 = quarterly_statementsDump.loc['netIncome'][12]
    try:
        netIncome7 = int(netIncome7)
    except Exception:
        netIncome7 = 0

    tTMnetIncome7 = (float(netIncome7) + float(netIncome8) + float(netIncome9) + float(netIncome10))
    try:
        tTMpreferredDivs7 = (int(dividendPayoutPreferredStock7) + int(dividendPayoutPreferredStock8) + int(
            dividendPayoutPreferredStock9) + int(dividendPayoutPreferredStock10))
    except Exception:
        tTMpreferredDivs7 = 0
    weightedAvgCommShrsOutstanding7 = (
            (float(commonStockSharesOutstanding7) + float(commonStockSharesOutstanding8) + float(
                commonStockSharesOutstanding9) + float(commonStockSharesOutstanding10)) / 7)
    quoteUnformatted7 = quoteUnformatted
    marketCap7 = calculateMarketCap(quoteUnformatted7, commonStockSharesOutstanding7)
    basicEPS7 = calculateBasicEPS(tTMnetIncome7, tTMpreferredDivs7, weightedAvgCommShrsOutstanding7)
    pE7 = calculatePE(quoteUnformatted7, basicEPS7)
    pCF7 = calculatePriceToCashFlow(quoteUnformatted7,
                                    calculateOperatingCashFlowPerShare(operatingCashflow7,
                                                                       weightedAvgCommShrsOutstanding7))
    pS7 = calculatePS(quoteUnformatted7, calculateSalesPerShare(totalRevenue7, weightedAvgCommShrsOutstanding7))
    pB7 = calculatePB(quoteUnformatted7,
                      calculateMarketToBookValue(marketCap7, totalAssets7, shortLongTermDebtTotal7, preferredStock=0))
    sustainableGrowthRate7 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout7, netIncome7)),
        calculateROE(netIncome7, totalShareholderEquity7))
    pEGRatio7 = calculatePEGRatio(pE7, (sustainableGrowthRate7 * 700))
    earningsYield7 = calculateEarningsYield(basicEPS7, quoteUnformatted7)
    cashFlowPerShare7 = calculateOperatingCashFlowPerShare(operatingCashflow7, weightedAvgCommShrsOutstanding7)
    ebitdaPerShare7 = calculateEBITDAperShare(ebitda7, weightedAvgCommShrsOutstanding7)
    tTMDividendPayout7 = (
        (float(dividendPayout7) + float(dividendPayout8) + float(dividendPayout9) + float(dividendPayout10)))
    dividendsPerShare7 = calculateDividendsPerShare(tTMDividendPayout7, weightedAvgCommShrsOutstanding7)
    currentQuarterGrossProfitMargin7 = calculateGrossProfitMargin(totalRevenue7, costofGoodsAndServicesSold7)
    tTmTotalRevenue7 = ((float(totalRevenue7) + float(totalRevenue8) + float(totalRevenue9) + float(totalRevenue10)))
    tTmCOGS7 = ((float(costofGoodsAndServicesSold7) + float(costofGoodsAndServicesSold8) + float(
        costofGoodsAndServicesSold9) + float(costofGoodsAndServicesSold10)))
    tTMGrossProfitMargin7 = calculateGrossProfitMargin(tTmTotalRevenue7, tTmCOGS7)
    currentQuarterOperatingMargin7 = calculateOperatingMargin(operatingIncome7, totalRevenue7)
    tTMOperatingIncome7 = (
        (float(operatingIncome7) + float(operatingIncome8) + float(operatingIncome9) + float(operatingIncome10)))
    tTMOperatingMargin7 = calculateOperatingMargin(tTMOperatingIncome7, tTmTotalRevenue7)
    currentQuarterPreTaxMargin7 = calculatePreTaxMargin(calculateEBT(ebit7, interestExpense7), totalRevenue7)
    tTMebit7 = ((float(ebit7) + float(ebit8) + float(ebit9) + float(ebit10)))
    tTMInterestExpense7 = (
        (float(interestExpense7) + float(interestExpense8) + float(interestExpense9) + float(interestExpense10)))
    tTMPreTaxMargin7 = calculatePreTaxMargin(calculateEBT(tTMebit7, tTMInterestExpense7), tTmTotalRevenue7)
    currentQuarterNetProfitMargin7 = calculateNetProfitMargin(netIncome7, totalRevenue7)
    tTMNetProfitMargin7 = calculateNetProfitMargin(tTMnetIncome7, tTmTotalRevenue7)
    currentQuarterAvgTotalAssets7 = ((float(totalAssets7) + float(totalAssets8)) / 4)
    currentQuarterOperatingROA7 = (calculateOperatingROA(operatingIncome7, currentQuarterAvgTotalAssets7)) * 4
    tTMAvgTotalAssets7 = ((float(totalAssets7) + float(totalAssets8) + float(totalAssets9) + float(totalAssets10)) / 4)
    tTMOperatingROA7 = calculateOperatingROA(tTMOperatingIncome7, tTMAvgTotalAssets7)
    currentQuarterROA7 = (calculateROA(netIncome7, currentQuarterAvgTotalAssets7)) * 4
    tTMROA7 = calculateROA(tTMnetIncome7, tTMAvgTotalAssets7)
    currentQuarterReturnOnTotalCapital7 = (calculateReturnOnTotalCapital(ebit7, shortLongTermDebtTotal7,
                                                                         totalShareholderEquity7)) * 4
    tTMReturnOnTotalCapital7 = calculateReturnOnTotalCapital(tTMebit7, shortLongTermDebtTotal7, totalShareholderEquity7)
    currentQuarterROE7 = (calculateROE(netIncome7, totalShareholderEquity7)) * 4
    tTMROE7 = calculateROE(tTMnetIncome7, totalShareholderEquity7)
    currentQuarterAvgCommonEquity7 = ((float(totalShareholderEquity7) + float(totalShareholderEquity7)) / 4)
    currentQuarterReturnOnCommonEquity7 = (calculateReturnOnCommonEquity(netIncome7, dividendPayoutPreferredStock7,
                                                                         currentQuarterAvgCommonEquity7)) * 4
    tTMAvgCommonEquity7 = ((float(totalShareholderEquity7) + float(totalShareholderEquity8) + float(
        totalShareholderEquity9) + float(totalShareholderEquity10)) / 4)
    tTMReturnOnCommonEquity7 = calculateReturnOnCommonEquity(tTMnetIncome7, tTMpreferredDivs7, tTMAvgCommonEquity7)
    debtRatio7 = calculateDebtRatio(totalLiabilities7, totalAssets7)
    debtToEquityRatio7 = calculateDebtToEquity(shortLongTermDebtTotal7, totalShareholderEquity7)
    debtToAssetRatio7 = calculateDebtToAssetRatio(shortLongTermDebtTotal7, totalAssets7)
    debtToCapitalRatio7 = calculateDebtToCapitalRatio(shortLongTermDebtTotal7, totalShareholderEquity7)

    financialLeverage7 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets7, currentQuarterAvgCommonEquity7)
    interestCoverage7 = calculateInterestCoverageRatio(operatingCashflow7, interestExpense7, incomeTaxExpense7)
    fixedChargeCoverageRatio7 = calculateFixedChargeCoverage(ebit7, capitalLeaseObligations7, interestExpense7)

    ## tm6  VARIABLES
    # Income Statement Variables for tm6
    gross_profit6 = quarterly_statementsDump.loc['grossProfit'][13]
    try:
        gross_profit6 = int(gross_profit6)
    except Exception:
        gross_profit6 = 0
    totalRevenue6 = quarterly_statementsDump.loc['totalRevenue'][13]
    try:
        totalRevenue6 = int(totalRevenue6)
    except Exception:
        totalRevenue6 = 0
    costOfRevenue6 = quarterly_statementsDump.loc['costOfRevenue'][13]
    try:
        costOfRevenue6 = int(costOfRevenue6)
    except Exception:
        costOfRevenue6 = 0
    costofGoodsAndServicesSold6 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][13]
    try:
        costofGoodsAndServicesSold6 = int(costofGoodsAndServicesSold6)
    except Exception:
        costofGoodsAndServicesSold6 = 0
    operatingIncome6 = quarterly_statementsDump.loc['operatingIncome'][13]
    try:
        operatingIncome6 = int(operatingIncome6)
    except Exception:
        operatingIncome6 = 0
    sellingGeneralAndAdministrative6 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][13]
    try:
        sellingGeneralAndAdministrative6 = int(sellingGeneralAndAdministrative6)
    except Exception:
        sellingGeneralAndAdministrative6 = 0
    researchAndDevelopment6 = quarterly_statementsDump.loc['researchAndDevelopment'][13]
    try:
        researchAndDevelopment6 = int(researchAndDevelopment6)
    except Exception:
        researchAndDevelopment6 = 0
    operatingExpenses6 = quarterly_statementsDump.loc['operatingExpenses'][13]
    try:
        operatingExpenses6 = int(operatingExpenses6)
    except Exception:
        operatingExpenses6 = 0
    investmentIncomeNet6 = quarterly_statementsDump.loc['investmentIncomeNet'][13]
    try:
        investmentIncomeNet6 = int(investmentIncomeNet6)
    except Exception:
        investmentIncomeNet6 = 0

    netInterestIncome6 = quarterly_statementsDump.loc['netInterestIncome'][13]
    try:
        netInterestIncome6 = int(netInterestIncome6)
    except Exception:
        netInterestIncome6 = 0
    interestIncome6 = quarterly_statementsDump.loc['interestIncome'][13]
    try:
        interestIncome6 = int(interestIncome6)
    except Exception:
        interestIncome6 = 0
    interestExpense6 = quarterly_statementsDump.loc['interestExpense'][13]
    try:
        interestExpense6 = int(interestExpense6)
    except Exception:
        interestExpense6 = 0
    nonInterestIncome6 = quarterly_statementsDump.loc['nonInterestIncome'][13]
    try:
        nonInterestIncome6 = int(nonInterestIncome6)
    except Exception:
        nonInterestIncome6 = 0
    otherNonOperatingIncome6 = quarterly_statementsDump.loc['otherNonOperatingIncome'][13]
    try:
        otherNonOperatingIncome6 = int(otherNonOperatingIncome6)
    except Exception:
        otherNonOperatingIncome6 = 0
    depreciation6 = quarterly_statementsDump.loc['depreciation'][13]
    try:
        depreciation6 = int(depreciation6)
    except Exception:
        depreciation6 = 0
    depreciationAndAmortization6 = quarterly_statementsDump.loc['depreciationAndAmortization'][13]
    try:
        depreciationAndAmortization6 = int(depreciationAndAmortization6)
    except Exception:
        depreciationAndAmortization6 = 0

    incomeBeforeTax6 = quarterly_statementsDump.loc['incomeBeforeTax'][13]
    try:
        incomeBeforeTax6 = int(incomeBeforeTax6)
    except Exception:
        incomeBeforeTax6 = 0

    incomeTaxExpense6 = quarterly_statementsDump.loc['incomeTaxExpense'][13]
    try:
        incomeTaxExpense6 = int(incomeTaxExpense6)
    except Exception:
        incomeTaxExpense6 = 0
    interestAndDebtExpense6 = quarterly_statementsDump.loc['interestAndDebtExpense'][13]
    try:
        interestAndDebtExpense6 = int(interestAndDebtExpense6)
    except Exception:
        interestAndDebtExpense6 = 0
    netIncomeFromContinuingOperations6 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][13]
    try:
        netIncomeFromContinuingOperations6 = int(netIncomeFromContinuingOperations6)
    except Exception:
        netIncomeFromContinuingOperations6 = 0
    comprehensiveIncomeNetOfTax6 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][13]
    try:
        comprehensiveIncomeNetOfTax6 = int(comprehensiveIncomeNetOfTax6)
    except Exception:
        comprehensiveIncomeNetOfTax6 = 0
    ebit6 = quarterly_statementsDump.loc['ebit'][13]
    try:
        ebit6 = int(ebit6)
    except Exception:
        ebit6 = 0
    ebitda6 = quarterly_statementsDump.loc['ebitda'][13]
    try:
        ebitda6 = int(ebitda6)
    except Exception:
        ebitda6 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 13]

    # Balance Sheet Values for tm6

    totalAssets6 = quarterly_statementsDump.loc['totalAssets'][13]
    try:
        totalAssets6 = int(totalAssets6)
    except Exception:
        totalAssets6 = 0
    totalCurrentAssets6 = quarterly_statementsDump.loc['totalCurrentAssets'][13]
    try:
        totalCurrentAssets6 = int(totalCurrentAssets6)
    except Exception:
        totalCurrentAssets6 = 0
    cashAndCashEquivalentsAtCarryingValue6 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][13]
    try:
        cashAndCashEquivalentsAtCarryingValue6 = int(cashAndCashEquivalentsAtCarryingValue6)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue6 = 0
    cashAndShortTermInvestments6 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][13]
    try:
        cashAndShortTermInvestments6 = int(cashAndShortTermInvestments6)
    except Exception:
        cashAndShortTermInvestments6 = 0
    inventory6 = quarterly_statementsDump.loc['inventory'][13]
    try:
        inventory6 = int(inventory6)
    except Exception:
        inventory6 = 0
    currentNetReceivables6 = quarterly_statementsDump.loc['currentNetReceivables'][13]
    try:
        currentNetReceivables6 = int(currentNetReceivables6)
    except Exception:
        currentNetReceivables6 = 0
    totalNonCurrentAssets6 = quarterly_statementsDump.loc['totalNonCurrentAssets'][13]
    try:
        totalNonCurrentAssets6 = int(totalNonCurrentAssets6)
    except Exception:
        totalNonCurrentAssets6 = 0
    propertyPlantEquipment6 = quarterly_statementsDump.loc['propertyPlantEquipment'][13]
    try:
        propertyPlantEquipment6 = int(propertyPlantEquipment6)
    except Exception:
        propertyPlantEquipment6 = 0
    accumulatedDepreciationAmortizationPPE6 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][13]
    try:
        accumulatedDepreciationAmortizationPPE6 = int(accumulatedDepreciationAmortizationPPE6)
    except Exception:
        accumulatedDepreciationAmortizationPPE6 = 0
    intangibleAssets6 = quarterly_statementsDump.loc['intangibleAssets'][13]
    try:
        intangibleAssets6 = int(intangibleAssets6)
    except Exception:
        intangibleAssets6 = 0
    intangibleAssetsExcludingGoodwill6 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][13]
    try:
        intangibleAssetsExcludingGoodwill6 = int(intangibleAssetsExcludingGoodwill6)
    except Exception:
        intangibleAssetsExcludingGoodwill6 = 0
    goodwill6 = quarterly_statementsDump.loc['goodwill'][13]
    try:
        goodwill6 = int(goodwill6)
    except Exception:
        goodwill6 = 0
    investments6 = quarterly_statementsDump.loc['investments'][13]
    try:
        investments6 = int(investments6)
    except Exception:
        investments6 = 0
    longTermInvestments6 = quarterly_statementsDump.loc['longTermInvestments'][13]
    try:
        longTermInvestments6 = int(longTermInvestments6)
    except Exception:
        longTermInvestments6 = 0
    shortTermInvestments6 = quarterly_statementsDump.loc['shortTermInvestments'][13]
    try:
        shortTermInvestments6 = int(shortTermInvestments6)
    except Exception:
        shortTermInvestments6 = 0
    otherCurrentAssets6 = quarterly_statementsDump.loc['otherCurrentAssets'][13]
    try:
        otherCurrentAssets6 = int(otherCurrentAssets6)
    except Exception:
        otherCurrentAssets6 = 0
    otherNonCurrrentAssets6 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][13]
    try:
        otherNonCurrrentAssets6 = int(otherNonCurrrentAssets6)
    except Exception:
        otherNonCurrrentAssets6 = 0
    totalLiabilities6 = quarterly_statementsDump.loc['totalLiabilities'][13]
    try:
        totalLiabilities6 = int(totalLiabilities6)
    except Exception:
        totalLiabilities6 = 0
    totalCurrentLiabilities6 = quarterly_statementsDump.loc['totalCurrentLiabilities'][13]
    try:
        totalCurrentLiabilities6 = int(totalCurrentLiabilities6)
    except Exception:
        totalCurrentLiabilities6 = 0
    currentAccountsPayable6 = quarterly_statementsDump.loc['currentAccountsPayable'][13]
    try:
        currentAccountsPayable6 = int(currentAccountsPayable6)
    except Exception:
        currentAccountsPayable6 = 0
    deferredRevenue6 = quarterly_statementsDump.loc['deferredRevenue'][13]
    try:
        deferredRevenue6 = int(deferredRevenue6)
    except Exception:
        deferredRevenue6 = 0
    currentDebt6 = quarterly_statementsDump.loc['currentDebt'][13]
    try:
        currentDebt6 = int(currentDebt6)
    except Exception:
        currentDebt6 = 0
    shortTermDebt6 = quarterly_statementsDump.loc['shortTermDebt'][13]
    try:
        shortTermDebt6 = int(shortTermDebt6)
    except Exception:
        shortTermDebt6 = 0
    totalNonCurrentLiabilities6 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][13]
    try:
        totalNonCurrentLiabilities6 = int(totalNonCurrentLiabilities6)
    except Exception:
        totalNonCurrentLiabilities6 = 0
    capitalLeaseObligations6 = quarterly_statementsDump.loc['capitalLeaseObligations'][13]
    try:
        capitalLeaseObligations6 = int(capitalLeaseObligations6)
    except Exception:
        capitalLeaseObligations6 = 0

    longTermDebt6 = quarterly_statementsDump.loc['longTermDebt'][13]
    try:
        longTermDebt6 = int(longTermDebt6)
    except Exception:
        longTermDebt6 = 0
    currentLongTermDebt6 = quarterly_statementsDump.loc['currentLongTermDebt'][13]
    try:
        currentLongTermDebt6 = int(currentLongTermDebt6)
    except Exception:
        currentLongTermDebt6 = 0
    longTermDebtNoncurrent6 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][13]
    try:
        longTermDebtNoncurrent6 = int(longTermDebtNoncurrent6)
    except Exception:
        longTermDebtNoncurrent6 = 0
    shortLongTermDebtTotal6 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][13]
    try:
        shortLongTermDebtTotal6 = int(shortLongTermDebtTotal6)
    except Exception:
        shortLongTermDebtTotal6 = 0
    otherCurrentLiabilities6 = quarterly_statementsDump.loc['otherCurrentLiabilities'][13]
    try:
        otherCurrentLiabilities6 = int(otherCurrentLiabilities6)
    except Exception:
        otherCurrentLiabilities6 = 0
    otherNonCurrentLiabilities6 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][13]
    try:
        otherNonCurrentLiabilities6 = int(otherNonCurrentLiabilities6)
    except Exception:
        otherNonCurrentLiabilities6 = 0
    totalShareholderEquity6 = quarterly_statementsDump.loc['totalShareholderEquity'][13]
    try:
        totalShareholderEquity6 = int(totalShareholderEquity6)
    except Exception:
        totalShareholderEquity6 = 0
    treasuryStock6 = quarterly_statementsDump.loc['treasuryStock'][13]
    try:
        treasuryStock6 = int(treasuryStock6)
    except Exception:
        treasuryStock6 = 0
    retainedEarnings6 = quarterly_statementsDump.loc['retainedEarnings'][13]
    try:
        retainedEarnings6 = int(retainedEarnings6)
    except Exception:
        retainedEarnings6 = 0
    commonStock6 = quarterly_statementsDump.loc['commonStock'][13]
    try:
        commonStock6 = int(commonStock6)
    except Exception:
        commonStock6 = 0
    commonStockSharesOutstanding6 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][13]
    try:
        commonStockSharesOutstanding6 = int(commonStockSharesOutstanding6)
    except Exception:
        commonStockSharesOutstanding6 = 0

    # Cash-Flow Statement values for tm6
    operatingCashflow6 = quarterly_statementsDump.loc['operatingCashflow'][13]
    try:
        operatingCashflow6 = int(operatingCashflow6)
    except Exception:
        operatingCashflow6 = 0
    paymentsForOperatingActivities6 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][13]
    try:
        paymentsForOperatingActivities6 = int(paymentsForOperatingActivities6)
    except Exception:
        paymentsForOperatingActivities6 = 0
    proceedsFromOperatingActivities6 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][13]
    try:
        proceedsFromOperatingActivities6 = int(proceedsFromOperatingActivities6)
    except Exception:
        proceedsFromOperatingActivities6 = 0
    changeInOperatingLiabilities6 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][13]
    try:
        changeInOperatingLiabilities6 = int(changeInOperatingLiabilities6)
    except Exception:
        changeInOperatingLiabilities6 = 0
    changeInOperatingAssets6 = quarterly_statementsDump.loc['changeInOperatingAssets'][13]
    try:
        changeInOperatingAssets6 = int(changeInOperatingAssets6)
    except Exception:
        changeInOperatingAssets6 = 0
    depreciationDepletionAndAmortization6 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][13]
    try:
        depreciationDepletionAndAmortization6 = int(depreciationDepletionAndAmortization6)
    except Exception:
        depreciationDepletionAndAmortization6 = 0
    capitalExpenditures6 = quarterly_statementsDump.loc['capitalExpenditures'][13]
    try:
        capitalExpenditures6 = int(capitalExpenditures6)
    except Exception:
        capitalExpenditures6 = 0
    changeInReceivables6 = quarterly_statementsDump.loc['changeInReceivables'][13]
    try:
        changeInReceivables6 = int(changeInReceivables6)
    except Exception:
        changeInReceivables6 = 0
    changeInInventory6 = quarterly_statementsDump.loc['changeInInventory'][13]
    try:
        changeInInventory6 = int(changeInInventory6)
    except Exception:
        changeInInventory6 = 0
    profitLoss6 = quarterly_statementsDump.loc['profitLoss'][13]
    try:
        profitLoss6 = int(profitLoss6)
    except Exception:
        profitLoss6 = 0
    cashflowFromInvestment6 = quarterly_statementsDump.loc['cashflowFromInvestment'][13]
    try:
        cashflowFromInvestment6 = int(cashflowFromInvestment6)
    except Exception:
        cashflowFromInvestment6 = 0
    cashflowFromFinancing6 = quarterly_statementsDump.loc['cashflowFromFinancing'][13]
    try:
        cashflowFromFinancing6 = int(cashflowFromFinancing6)
    except Exception:
        cashflowFromFinancing6 = 0
    proceedsFromRepaymentsOfShortTermDebt6 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][13]
    try:
        proceedsFromRepaymentsOfShortTermDebt6 = int(proceedsFromRepaymentsOfShortTermDebt6)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt6 = 0
    paymentsForRepurchaseOfCommonStock6 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][13]
    try:
        paymentsForRepurchaseOfCommonStock6 = int(paymentsForRepurchaseOfCommonStock6)
    except Exception:
        paymentsForRepurchaseOfCommonStock6 = 0
    paymentsForRepurchaseOfEquity6 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][13]
    try:
        paymentsForRepurchaseOfEquity6 = int(paymentsForRepurchaseOfEquity6)
    except Exception:
        paymentsForRepurchaseOfEquity6 = 0
    paymentsForRepurchaseOfPreferredStock6 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][13]
    try:
        paymentsForRepurchaseOfPreferredStock6 = int(paymentsForRepurchaseOfPreferredStock6)
    except Exception:
        paymentsForRepurchaseOfPreferredStock6 = 0
    dividendPayout6 = quarterly_statementsDump.loc['dividendPayout'][13]
    try:
        dividendPayout6 = int(dividendPayout6)
    except Exception:
        dividendPayout6 = 0
    dividendPayoutCommonStock6 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][13]
    try:
        dividendPayoutCommonStock6 = int(dividendPayoutCommonStock6)
    except Exception:
        dividendPayoutCommonStock6 = 0
    dividendPayoutPreferredStock6 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][13]
    try:
        dividendPayoutPreferredStock6 = int(dividendPayoutPreferredStock6)
    except Exception:
        dividendPayoutPreferredStock6 = 0
    proceedsFromIssuanceOfCommonStock6 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][13]
    try:
        proceedsFromIssuanceOfCommonStock6 = int(proceedsFromIssuanceOfCommonStock6)
    except Exception:
        proceedsFromIssuanceOfCommonStock6 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet6 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][13]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet6 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet6)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet6 = 0
    proceedsFromIssuanceOfPreferredStock6 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][13]
    try:
        proceedsFromIssuanceOfPreferredStock6 = int(proceedsFromIssuanceOfPreferredStock6)
    except Exception:
        proceedsFromIssuanceOfPreferredStock6 = 0
    proceedsFromRepurchaseOfEquity6 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][13]
    try:
        proceedsFromRepurchaseOfEquity6 = int(proceedsFromRepurchaseOfEquity6)
    except Exception:
        proceedsFromRepurchaseOfEquity6 = 0
    proceedsFromSaleOfTreasuryStock6 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][13]
    try:
        proceedsFromSaleOfTreasuryStock6 = int(proceedsFromSaleOfTreasuryStock6)
    except Exception:
        proceedsFromSaleOfTreasuryStock6 = 0
    changeInCashAndCashEquivalents6 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][13]
    try:
        changeInCashAndCashEquivalents6 = int(changeInCashAndCashEquivalents6)
    except Exception:
        changeInCashAndCashEquivalents6 = 0
    changeInExchangeRate6 = quarterly_statementsDump.loc['changeInExchangeRate'][13]
    try:
        changeInExchangeRate6 = int(changeInExchangeRate6)
    except Exception:
        changeInExchangeRate6 = 0
    netIncome6 = quarterly_statementsDump.loc['netIncome'][13]
    try:
        netIncome6 = int(netIncome6)
    except Exception:
        netIncome6 = 0

    tTMnetIncome6 = (float(netIncome6) + float(netIncome7) + float(netIncome8) + float(netIncome9))
    try:
        tTMpreferredDivs6 = (int(dividendPayoutPreferredStock6) + int(dividendPayoutPreferredStock7) + int(
            dividendPayoutPreferredStock8) + int(dividendPayoutPreferredStock9))
    except Exception:
        tTMpreferredDivs6 = 0
    weightedAvgCommShrsOutstanding6 = (
            (float(commonStockSharesOutstanding6) + float(commonStockSharesOutstanding7) + float(
                commonStockSharesOutstanding8) + float(commonStockSharesOutstanding9)) / 6)
    quoteUnformatted6 = quoteUnformatted
    marketCap6 = calculateMarketCap(quoteUnformatted6, commonStockSharesOutstanding6)
    basicEPS6 = calculateBasicEPS(tTMnetIncome6, tTMpreferredDivs6, weightedAvgCommShrsOutstanding6)
    pE6 = calculatePE(quoteUnformatted6, basicEPS6)
    pCF6 = calculatePriceToCashFlow(quoteUnformatted6,
                                    calculateOperatingCashFlowPerShare(operatingCashflow6,
                                                                       weightedAvgCommShrsOutstanding6))
    pS6 = calculatePS(quoteUnformatted6, calculateSalesPerShare(totalRevenue6, weightedAvgCommShrsOutstanding6))
    pB6 = calculatePB(quoteUnformatted6,
                      calculateMarketToBookValue(marketCap6, totalAssets6, shortLongTermDebtTotal6, preferredStock=0))
    sustainableGrowthRate6 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout6, netIncome6)),
        calculateROE(netIncome6, totalShareholderEquity6))
    pEGRatio6 = calculatePEGRatio(pE6, (sustainableGrowthRate6 * 600))
    earningsYield6 = calculateEarningsYield(basicEPS6, quoteUnformatted6)
    cashFlowPerShare6 = calculateOperatingCashFlowPerShare(operatingCashflow6, weightedAvgCommShrsOutstanding6)
    ebitdaPerShare6 = calculateEBITDAperShare(ebitda6, weightedAvgCommShrsOutstanding6)
    tTMDividendPayout6 = (
        (float(dividendPayout6) + float(dividendPayout7) + float(dividendPayout8) + float(dividendPayout9)))
    dividendsPerShare6 = calculateDividendsPerShare(tTMDividendPayout6, weightedAvgCommShrsOutstanding6)
    currentQuarterGrossProfitMargin6 = calculateGrossProfitMargin(totalRevenue6, costofGoodsAndServicesSold6)
    tTmTotalRevenue6 = ((float(totalRevenue6) + float(totalRevenue7) + float(totalRevenue8) + float(totalRevenue9)))
    tTmCOGS6 = ((float(costofGoodsAndServicesSold6) + float(costofGoodsAndServicesSold7) + float(
        costofGoodsAndServicesSold8) + float(costofGoodsAndServicesSold9)))
    tTMGrossProfitMargin6 = calculateGrossProfitMargin(tTmTotalRevenue6, tTmCOGS6)
    currentQuarterOperatingMargin6 = calculateOperatingMargin(operatingIncome6, totalRevenue6)
    tTMOperatingIncome6 = (
        (float(operatingIncome6) + float(operatingIncome7) + float(operatingIncome8) + float(operatingIncome9)))
    tTMOperatingMargin6 = calculateOperatingMargin(tTMOperatingIncome6, tTmTotalRevenue6)
    currentQuarterPreTaxMargin6 = calculatePreTaxMargin(calculateEBT(ebit6, interestExpense6), totalRevenue6)
    tTMebit6 = ((float(ebit6) + float(ebit7) + float(ebit8) + float(ebit9)))
    tTMInterestExpense6 = (
        (float(interestExpense6) + float(interestExpense7) + float(interestExpense8) + float(interestExpense9)))
    tTMPreTaxMargin6 = calculatePreTaxMargin(calculateEBT(tTMebit6, tTMInterestExpense6), tTmTotalRevenue6)
    currentQuarterNetProfitMargin6 = calculateNetProfitMargin(netIncome6, totalRevenue6)
    tTMNetProfitMargin6 = calculateNetProfitMargin(tTMnetIncome6, tTmTotalRevenue6)
    currentQuarterAvgTotalAssets6 = ((float(totalAssets6) + float(totalAssets7)) / 4)
    currentQuarterOperatingROA6 = (calculateOperatingROA(operatingIncome6, currentQuarterAvgTotalAssets6)) * 4
    tTMAvgTotalAssets6 = ((float(totalAssets6) + float(totalAssets7) + float(totalAssets8) + float(totalAssets9)) / 4)
    tTMOperatingROA6 = calculateOperatingROA(tTMOperatingIncome6, tTMAvgTotalAssets6)
    currentQuarterROA6 = (calculateROA(netIncome6, currentQuarterAvgTotalAssets6)) * 4
    tTMROA6 = calculateROA(tTMnetIncome6, tTMAvgTotalAssets6)
    currentQuarterReturnOnTotalCapital6 = (calculateReturnOnTotalCapital(ebit6, shortLongTermDebtTotal6,
                                                                         totalShareholderEquity6)) * 4
    tTMReturnOnTotalCapital6 = calculateReturnOnTotalCapital(tTMebit6, shortLongTermDebtTotal6, totalShareholderEquity6)
    currentQuarterROE6 = (calculateROE(netIncome6, totalShareholderEquity6)) * 4
    tTMROE6 = calculateROE(tTMnetIncome6, totalShareholderEquity6)
    currentQuarterAvgCommonEquity6 = ((float(totalShareholderEquity6) + float(totalShareholderEquity6)) / 4)
    currentQuarterReturnOnCommonEquity6 = (calculateReturnOnCommonEquity(netIncome6, dividendPayoutPreferredStock6,
                                                                         currentQuarterAvgCommonEquity6)) * 4
    tTMAvgCommonEquity6 = ((float(totalShareholderEquity6) + float(totalShareholderEquity7) + float(
        totalShareholderEquity8) + float(totalShareholderEquity9)) / 4)
    tTMReturnOnCommonEquity6 = calculateReturnOnCommonEquity(tTMnetIncome6, tTMpreferredDivs6, tTMAvgCommonEquity6)
    debtRatio6 = calculateDebtRatio(totalLiabilities6, totalAssets6)
    debtToEquityRatio6 = calculateDebtToEquity(shortLongTermDebtTotal6, totalShareholderEquity6)
    debtToAssetRatio6 = calculateDebtToAssetRatio(shortLongTermDebtTotal6, totalAssets6)
    debtToCapitalRatio6 = calculateDebtToCapitalRatio(shortLongTermDebtTotal6, totalShareholderEquity6)

    financialLeverage6 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets6, currentQuarterAvgCommonEquity6)
    interestCoverage6 = calculateInterestCoverageRatio(operatingCashflow6, interestExpense6, incomeTaxExpense6)
    fixedChargeCoverageRatio6 = calculateFixedChargeCoverage(ebit6, capitalLeaseObligations6, interestExpense6)

    ## tm5  VARIABLES
    # Income Statement Variables for tm5
    gross_profit5 = quarterly_statementsDump.loc['grossProfit'][14]
    try:
        gross_profit5 = int(gross_profit5)
    except Exception:
        gross_profit5 = 0
    totalRevenue5 = quarterly_statementsDump.loc['totalRevenue'][14]
    try:
        totalRevenue5 = int(totalRevenue5)
    except Exception:
        totalRevenue5 = 0
    costOfRevenue5 = quarterly_statementsDump.loc['costOfRevenue'][14]
    try:
        costOfRevenue5 = int(costOfRevenue5)
    except Exception:
        costOfRevenue5 = 0
    costofGoodsAndServicesSold5 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][14]
    try:
        costofGoodsAndServicesSold5 = int(costofGoodsAndServicesSold5)
    except Exception:
        costofGoodsAndServicesSold5 = 0
    operatingIncome5 = quarterly_statementsDump.loc['operatingIncome'][14]
    try:
        operatingIncome5 = int(operatingIncome5)
    except Exception:
        operatingIncome5 = 0
    sellingGeneralAndAdministrative5 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][14]
    try:
        sellingGeneralAndAdministrative5 = int(sellingGeneralAndAdministrative5)
    except Exception:
        sellingGeneralAndAdministrative5 = 0
    researchAndDevelopment5 = quarterly_statementsDump.loc['researchAndDevelopment'][14]
    try:
        researchAndDevelopment5 = int(researchAndDevelopment5)
    except Exception:
        researchAndDevelopment5 = 0
    operatingExpenses5 = quarterly_statementsDump.loc['operatingExpenses'][14]
    try:
        operatingExpenses5 = int(operatingExpenses5)
    except Exception:
        operatingExpenses5 = 0
    investmentIncomeNet5 = quarterly_statementsDump.loc['investmentIncomeNet'][14]
    try:
        investmentIncomeNet5 = int(investmentIncomeNet5)
    except Exception:
        investmentIncomeNet5 = 0

    netInterestIncome5 = quarterly_statementsDump.loc['netInterestIncome'][14]
    try:
        netInterestIncome5 = int(netInterestIncome5)
    except Exception:
        netInterestIncome5 = 0
    interestIncome5 = quarterly_statementsDump.loc['interestIncome'][14]
    try:
        interestIncome5 = int(interestIncome5)
    except Exception:
        interestIncome5 = 0
    interestExpense5 = quarterly_statementsDump.loc['interestExpense'][14]
    try:
        interestExpense5 = int(interestExpense5)
    except Exception:
        interestExpense5 = 0
    nonInterestIncome5 = quarterly_statementsDump.loc['nonInterestIncome'][14]
    try:
        nonInterestIncome5 = int(nonInterestIncome5)
    except Exception:
        nonInterestIncome5 = 0
    otherNonOperatingIncome5 = quarterly_statementsDump.loc['otherNonOperatingIncome'][14]
    try:
        otherNonOperatingIncome5 = int(otherNonOperatingIncome5)
    except Exception:
        otherNonOperatingIncome5 = 0
    depreciation5 = quarterly_statementsDump.loc['depreciation'][14]
    try:
        depreciation5 = int(depreciation5)
    except Exception:
        depreciation5 = 0
    depreciationAndAmortization5 = quarterly_statementsDump.loc['depreciationAndAmortization'][14]
    try:
        depreciationAndAmortization5 = int(depreciationAndAmortization5)
    except Exception:
        depreciationAndAmortization5 = 0

    incomeBeforeTax5 = quarterly_statementsDump.loc['incomeBeforeTax'][14]
    try:
        incomeBeforeTax5 = int(incomeBeforeTax5)
    except Exception:
        incomeBeforeTax5 = 0

    incomeTaxExpense5 = quarterly_statementsDump.loc['incomeTaxExpense'][14]
    try:
        incomeTaxExpense5 = int(incomeTaxExpense5)
    except Exception:
        incomeTaxExpense5 = 0
    interestAndDebtExpense5 = quarterly_statementsDump.loc['interestAndDebtExpense'][14]
    try:
        interestAndDebtExpense5 = int(interestAndDebtExpense5)
    except Exception:
        interestAndDebtExpense5 = 0
    netIncomeFromContinuingOperations5 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][14]
    try:
        netIncomeFromContinuingOperations5 = int(netIncomeFromContinuingOperations5)
    except Exception:
        netIncomeFromContinuingOperations5 = 0
    comprehensiveIncomeNetOfTax5 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][14]
    try:
        comprehensiveIncomeNetOfTax5 = int(comprehensiveIncomeNetOfTax5)
    except Exception:
        comprehensiveIncomeNetOfTax5 = 0
    ebit5 = quarterly_statementsDump.loc['ebit'][14]
    try:
        ebit5 = int(ebit5)
    except Exception:
        ebit5 = 0
    ebitda5 = quarterly_statementsDump.loc['ebitda'][14]
    try:
        ebitda5 = int(ebitda5)
    except Exception:
        ebitda5 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 14]

    # Balance Sheet Values for tm5

    totalAssets5 = quarterly_statementsDump.loc['totalAssets'][14]
    try:
        totalAssets5 = int(totalAssets5)
    except Exception:
        totalAssets5 = 0
    totalCurrentAssets5 = quarterly_statementsDump.loc['totalCurrentAssets'][14]
    try:
        totalCurrentAssets5 = int(totalCurrentAssets5)
    except Exception:
        totalCurrentAssets5 = 0
    cashAndCashEquivalentsAtCarryingValue5 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][14]
    try:
        cashAndCashEquivalentsAtCarryingValue5 = int(cashAndCashEquivalentsAtCarryingValue5)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue5 = 0
    cashAndShortTermInvestments5 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][14]
    try:
        cashAndShortTermInvestments5 = int(cashAndShortTermInvestments5)
    except Exception:
        cashAndShortTermInvestments5 = 0
    inventory5 = quarterly_statementsDump.loc['inventory'][14]
    try:
        inventory5 = int(inventory5)
    except Exception:
        inventory5 = 0
    currentNetReceivables5 = quarterly_statementsDump.loc['currentNetReceivables'][14]
    try:
        currentNetReceivables5 = int(currentNetReceivables5)
    except Exception:
        currentNetReceivables5 = 0
    totalNonCurrentAssets5 = quarterly_statementsDump.loc['totalNonCurrentAssets'][14]
    try:
        totalNonCurrentAssets5 = int(totalNonCurrentAssets5)
    except Exception:
        totalNonCurrentAssets5 = 0
    propertyPlantEquipment5 = quarterly_statementsDump.loc['propertyPlantEquipment'][14]
    try:
        propertyPlantEquipment5 = int(propertyPlantEquipment5)
    except Exception:
        propertyPlantEquipment5 = 0
    accumulatedDepreciationAmortizationPPE5 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][14]
    try:
        accumulatedDepreciationAmortizationPPE5 = int(accumulatedDepreciationAmortizationPPE5)
    except Exception:
        accumulatedDepreciationAmortizationPPE5 = 0
    intangibleAssets5 = quarterly_statementsDump.loc['intangibleAssets'][14]
    try:
        intangibleAssets5 = int(intangibleAssets5)
    except Exception:
        intangibleAssets5 = 0
    intangibleAssetsExcludingGoodwill5 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][14]
    try:
        intangibleAssetsExcludingGoodwill5 = int(intangibleAssetsExcludingGoodwill5)
    except Exception:
        intangibleAssetsExcludingGoodwill5 = 0
    goodwill5 = quarterly_statementsDump.loc['goodwill'][14]
    try:
        goodwill5 = int(goodwill5)
    except Exception:
        goodwill5 = 0
    investments5 = quarterly_statementsDump.loc['investments'][14]
    try:
        investments5 = int(investments5)
    except Exception:
        investments5 = 0
    longTermInvestments5 = quarterly_statementsDump.loc['longTermInvestments'][14]
    try:
        longTermInvestments5 = int(longTermInvestments5)
    except Exception:
        longTermInvestments5 = 0
    shortTermInvestments5 = quarterly_statementsDump.loc['shortTermInvestments'][14]
    try:
        shortTermInvestments5 = int(shortTermInvestments5)
    except Exception:
        shortTermInvestments5 = 0
    otherCurrentAssets5 = quarterly_statementsDump.loc['otherCurrentAssets'][14]
    try:
        otherCurrentAssets5 = int(otherCurrentAssets5)
    except Exception:
        otherCurrentAssets5 = 0
    otherNonCurrrentAssets5 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][14]
    try:
        otherNonCurrrentAssets5 = int(otherNonCurrrentAssets5)
    except Exception:
        otherNonCurrrentAssets5 = 0
    totalLiabilities5 = quarterly_statementsDump.loc['totalLiabilities'][14]
    try:
        totalLiabilities5 = int(totalLiabilities5)
    except Exception:
        totalLiabilities5 = 0
    totalCurrentLiabilities5 = quarterly_statementsDump.loc['totalCurrentLiabilities'][14]
    try:
        totalCurrentLiabilities5 = int(totalCurrentLiabilities5)
    except Exception:
        totalCurrentLiabilities5 = 0
    currentAccountsPayable5 = quarterly_statementsDump.loc['currentAccountsPayable'][14]
    try:
        currentAccountsPayable5 = int(currentAccountsPayable5)
    except Exception:
        currentAccountsPayable5 = 0
    deferredRevenue5 = quarterly_statementsDump.loc['deferredRevenue'][14]
    try:
        deferredRevenue5 = int(deferredRevenue5)
    except Exception:
        deferredRevenue5 = 0
    currentDebt5 = quarterly_statementsDump.loc['currentDebt'][14]
    try:
        currentDebt5 = int(currentDebt5)
    except Exception:
        currentDebt5 = 0
    shortTermDebt5 = quarterly_statementsDump.loc['shortTermDebt'][14]
    try:
        shortTermDebt5 = int(shortTermDebt5)
    except Exception:
        shortTermDebt5 = 0
    totalNonCurrentLiabilities5 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][14]
    try:
        totalNonCurrentLiabilities5 = int(totalNonCurrentLiabilities5)
    except Exception:
        totalNonCurrentLiabilities5 = 0
    capitalLeaseObligations5 = quarterly_statementsDump.loc['capitalLeaseObligations'][14]
    try:
        capitalLeaseObligations5 = int(capitalLeaseObligations5)
    except Exception:
        capitalLeaseObligations5 = 0

    longTermDebt5 = quarterly_statementsDump.loc['longTermDebt'][14]
    try:
        longTermDebt5 = int(longTermDebt5)
    except Exception:
        longTermDebt5 = 0
    currentLongTermDebt5 = quarterly_statementsDump.loc['currentLongTermDebt'][14]
    try:
        currentLongTermDebt5 = int(currentLongTermDebt5)
    except Exception:
        currentLongTermDebt5 = 0
    longTermDebtNoncurrent5 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][14]
    try:
        longTermDebtNoncurrent5 = int(longTermDebtNoncurrent5)
    except Exception:
        longTermDebtNoncurrent5 = 0
    shortLongTermDebtTotal5 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][14]
    try:
        shortLongTermDebtTotal5 = int(shortLongTermDebtTotal5)
    except Exception:
        shortLongTermDebtTotal5 = 0
    otherCurrentLiabilities5 = quarterly_statementsDump.loc['otherCurrentLiabilities'][14]
    try:
        otherCurrentLiabilities5 = int(otherCurrentLiabilities5)
    except Exception:
        otherCurrentLiabilities5 = 0
    otherNonCurrentLiabilities5 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][14]
    try:
        otherNonCurrentLiabilities5 = int(otherNonCurrentLiabilities5)
    except Exception:
        otherNonCurrentLiabilities5 = 0
    totalShareholderEquity5 = quarterly_statementsDump.loc['totalShareholderEquity'][14]
    try:
        totalShareholderEquity5 = int(totalShareholderEquity5)
    except Exception:
        totalShareholderEquity5 = 0
    treasuryStock5 = quarterly_statementsDump.loc['treasuryStock'][14]
    try:
        treasuryStock5 = int(treasuryStock5)
    except Exception:
        treasuryStock5 = 0
    retainedEarnings5 = quarterly_statementsDump.loc['retainedEarnings'][14]
    try:
        retainedEarnings5 = int(retainedEarnings5)
    except Exception:
        retainedEarnings5 = 0
    commonStock5 = quarterly_statementsDump.loc['commonStock'][14]
    try:
        commonStock5 = int(commonStock5)
    except Exception:
        commonStock5 = 0
    commonStockSharesOutstanding5 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][14]
    try:
        commonStockSharesOutstanding5 = int(commonStockSharesOutstanding5)
    except Exception:
        commonStockSharesOutstanding5 = 0

    # Cash-Flow Statement values for tm5
    operatingCashflow5 = quarterly_statementsDump.loc['operatingCashflow'][14]
    try:
        operatingCashflow5 = int(operatingCashflow5)
    except Exception:
        operatingCashflow5 = 0
    paymentsForOperatingActivities5 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][14]
    try:
        paymentsForOperatingActivities5 = int(paymentsForOperatingActivities5)
    except Exception:
        paymentsForOperatingActivities5 = 0
    proceedsFromOperatingActivities5 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][14]
    try:
        proceedsFromOperatingActivities5 = int(proceedsFromOperatingActivities5)
    except Exception:
        proceedsFromOperatingActivities5 = 0
    changeInOperatingLiabilities5 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][14]
    try:
        changeInOperatingLiabilities5 = int(changeInOperatingLiabilities5)
    except Exception:
        changeInOperatingLiabilities5 = 0
    changeInOperatingAssets5 = quarterly_statementsDump.loc['changeInOperatingAssets'][14]
    try:
        changeInOperatingAssets5 = int(changeInOperatingAssets5)
    except Exception:
        changeInOperatingAssets5 = 0
    depreciationDepletionAndAmortization5 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][14]
    try:
        depreciationDepletionAndAmortization5 = int(depreciationDepletionAndAmortization5)
    except Exception:
        depreciationDepletionAndAmortization5 = 0
    capitalExpenditures5 = quarterly_statementsDump.loc['capitalExpenditures'][14]
    try:
        capitalExpenditures5 = int(capitalExpenditures5)
    except Exception:
        capitalExpenditures5 = 0
    changeInReceivables5 = quarterly_statementsDump.loc['changeInReceivables'][14]
    try:
        changeInReceivables5 = int(changeInReceivables5)
    except Exception:
        changeInReceivables5 = 0
    changeInInventory5 = quarterly_statementsDump.loc['changeInInventory'][14]
    try:
        changeInInventory5 = int(changeInInventory5)
    except Exception:
        changeInInventory5 = 0
    profitLoss5 = quarterly_statementsDump.loc['profitLoss'][14]
    try:
        profitLoss5 = int(profitLoss5)
    except Exception:
        profitLoss5 = 0
    cashflowFromInvestment5 = quarterly_statementsDump.loc['cashflowFromInvestment'][14]
    try:
        cashflowFromInvestment5 = int(cashflowFromInvestment5)
    except Exception:
        cashflowFromInvestment5 = 0
    cashflowFromFinancing5 = quarterly_statementsDump.loc['cashflowFromFinancing'][14]
    try:
        cashflowFromFinancing5 = int(cashflowFromFinancing5)
    except Exception:
        cashflowFromFinancing5 = 0
    proceedsFromRepaymentsOfShortTermDebt5 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][14]
    try:
        proceedsFromRepaymentsOfShortTermDebt5 = int(proceedsFromRepaymentsOfShortTermDebt5)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt5 = 0
    paymentsForRepurchaseOfCommonStock5 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][14]
    try:
        paymentsForRepurchaseOfCommonStock5 = int(paymentsForRepurchaseOfCommonStock5)
    except Exception:
        paymentsForRepurchaseOfCommonStock5 = 0
    paymentsForRepurchaseOfEquity5 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][14]
    try:
        paymentsForRepurchaseOfEquity5 = int(paymentsForRepurchaseOfEquity5)
    except Exception:
        paymentsForRepurchaseOfEquity5 = 0
    paymentsForRepurchaseOfPreferredStock5 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][14]
    try:
        paymentsForRepurchaseOfPreferredStock5 = int(paymentsForRepurchaseOfPreferredStock5)
    except Exception:
        paymentsForRepurchaseOfPreferredStock5 = 0
    dividendPayout5 = quarterly_statementsDump.loc['dividendPayout'][14]
    try:
        dividendPayout5 = int(dividendPayout5)
    except Exception:
        dividendPayout5 = 0
    dividendPayoutCommonStock5 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][14]
    try:
        dividendPayoutCommonStock5 = int(dividendPayoutCommonStock5)
    except Exception:
        dividendPayoutCommonStock5 = 0
    dividendPayoutPreferredStock5 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][14]
    try:
        dividendPayoutPreferredStock5 = int(dividendPayoutPreferredStock5)
    except Exception:
        dividendPayoutPreferredStock5 = 0
    proceedsFromIssuanceOfCommonStock5 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][14]
    try:
        proceedsFromIssuanceOfCommonStock5 = int(proceedsFromIssuanceOfCommonStock5)
    except Exception:
        proceedsFromIssuanceOfCommonStock5 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet5 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][14]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet5 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet5)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet5 = 0
    proceedsFromIssuanceOfPreferredStock5 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][14]
    try:
        proceedsFromIssuanceOfPreferredStock5 = int(proceedsFromIssuanceOfPreferredStock5)
    except Exception:
        proceedsFromIssuanceOfPreferredStock5 = 0
    proceedsFromRepurchaseOfEquity5 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][14]
    try:
        proceedsFromRepurchaseOfEquity5 = int(proceedsFromRepurchaseOfEquity5)
    except Exception:
        proceedsFromRepurchaseOfEquity5 = 0
    proceedsFromSaleOfTreasuryStock5 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][14]
    try:
        proceedsFromSaleOfTreasuryStock5 = int(proceedsFromSaleOfTreasuryStock5)
    except Exception:
        proceedsFromSaleOfTreasuryStock5 = 0
    changeInCashAndCashEquivalents5 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][14]
    try:
        changeInCashAndCashEquivalents5 = int(changeInCashAndCashEquivalents5)
    except Exception:
        changeInCashAndCashEquivalents5 = 0
    changeInExchangeRate5 = quarterly_statementsDump.loc['changeInExchangeRate'][14]
    try:
        changeInExchangeRate5 = int(changeInExchangeRate5)
    except Exception:
        changeInExchangeRate5 = 0
    netIncome5 = quarterly_statementsDump.loc['netIncome'][14]
    try:
        netIncome5 = int(netIncome5)
    except Exception:
        netIncome5 = 0

    tTMnetIncome5 = (float(netIncome5) + float(netIncome6) + float(netIncome7) + float(netIncome8))
    try:
        tTMpreferredDivs5 = (int(dividendPayoutPreferredStock5) + int(dividendPayoutPreferredStock6) + int(
            dividendPayoutPreferredStock7) + int(dividendPayoutPreferredStock8))
    except Exception:
        tTMpreferredDivs5 = 0
    weightedAvgCommShrsOutstanding5 = (
            (float(commonStockSharesOutstanding5) + float(commonStockSharesOutstanding6) + float(
                commonStockSharesOutstanding7) + float(commonStockSharesOutstanding8)) / 5)
    quoteUnformatted5 = quoteUnformatted
    marketCap5 = calculateMarketCap(quoteUnformatted5, commonStockSharesOutstanding5)
    basicEPS5 = calculateBasicEPS(tTMnetIncome5, tTMpreferredDivs5, weightedAvgCommShrsOutstanding5)
    pE5 = calculatePE(quoteUnformatted5, basicEPS5)
    pCF5 = calculatePriceToCashFlow(quoteUnformatted5,
                                    calculateOperatingCashFlowPerShare(operatingCashflow5,
                                                                       weightedAvgCommShrsOutstanding5))
    pS5 = calculatePS(quoteUnformatted5, calculateSalesPerShare(totalRevenue5, weightedAvgCommShrsOutstanding5))
    pB5 = calculatePB(quoteUnformatted5,
                      calculateMarketToBookValue(marketCap5, totalAssets5, shortLongTermDebtTotal5, preferredStock=0))
    sustainableGrowthRate5 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout5, netIncome5)),
        calculateROE(netIncome5, totalShareholderEquity5))
    pEGRatio5 = calculatePEGRatio(pE5, (sustainableGrowthRate5 * 500))
    earningsYield5 = calculateEarningsYield(basicEPS5, quoteUnformatted5)
    cashFlowPerShare5 = calculateOperatingCashFlowPerShare(operatingCashflow5, weightedAvgCommShrsOutstanding5)
    ebitdaPerShare5 = calculateEBITDAperShare(ebitda5, weightedAvgCommShrsOutstanding5)
    tTMDividendPayout5 = (
        (float(dividendPayout5) + float(dividendPayout6) + float(dividendPayout7) + float(dividendPayout8)))
    dividendsPerShare5 = calculateDividendsPerShare(tTMDividendPayout5, weightedAvgCommShrsOutstanding5)
    currentQuarterGrossProfitMargin5 = calculateGrossProfitMargin(totalRevenue5, costofGoodsAndServicesSold5)
    tTmTotalRevenue5 = ((float(totalRevenue5) + float(totalRevenue6) + float(totalRevenue7) + float(totalRevenue8)))
    tTmCOGS5 = ((float(costofGoodsAndServicesSold5) + float(costofGoodsAndServicesSold6) + float(
        costofGoodsAndServicesSold7) + float(costofGoodsAndServicesSold8)))
    tTMGrossProfitMargin5 = calculateGrossProfitMargin(tTmTotalRevenue5, tTmCOGS5)
    currentQuarterOperatingMargin5 = calculateOperatingMargin(operatingIncome5, totalRevenue5)
    tTMOperatingIncome5 = (
        (float(operatingIncome5) + float(operatingIncome6) + float(operatingIncome7) + float(operatingIncome8)))
    tTMOperatingMargin5 = calculateOperatingMargin(tTMOperatingIncome5, tTmTotalRevenue5)
    currentQuarterPreTaxMargin5 = calculatePreTaxMargin(calculateEBT(ebit5, interestExpense5), totalRevenue5)
    tTMebit5 = ((float(ebit5) + float(ebit6) + float(ebit7) + float(ebit8)))
    tTMInterestExpense5 = (
        (float(interestExpense5) + float(interestExpense6) + float(interestExpense7) + float(interestExpense8)))
    tTMPreTaxMargin5 = calculatePreTaxMargin(calculateEBT(tTMebit5, tTMInterestExpense5), tTmTotalRevenue5)
    currentQuarterNetProfitMargin5 = calculateNetProfitMargin(netIncome5, totalRevenue5)
    tTMNetProfitMargin5 = calculateNetProfitMargin(tTMnetIncome5, tTmTotalRevenue5)
    currentQuarterAvgTotalAssets5 = ((float(totalAssets5) + float(totalAssets6)) / 4)
    currentQuarterOperatingROA5 = (calculateOperatingROA(operatingIncome5, currentQuarterAvgTotalAssets5)) * 4
    tTMAvgTotalAssets5 = ((float(totalAssets5) + float(totalAssets6) + float(totalAssets7) + float(totalAssets8)) / 4)
    tTMOperatingROA5 = calculateOperatingROA(tTMOperatingIncome5, tTMAvgTotalAssets5)
    currentQuarterROA5 = (calculateROA(netIncome5, currentQuarterAvgTotalAssets5)) * 4
    tTMROA5 = calculateROA(tTMnetIncome5, tTMAvgTotalAssets5)
    currentQuarterReturnOnTotalCapital5 = (calculateReturnOnTotalCapital(ebit5, shortLongTermDebtTotal5,
                                                                         totalShareholderEquity5)) * 4
    tTMReturnOnTotalCapital5 = calculateReturnOnTotalCapital(tTMebit5, shortLongTermDebtTotal5, totalShareholderEquity5)
    currentQuarterROE5 = (calculateROE(netIncome5, totalShareholderEquity5)) * 4
    tTMROE5 = calculateROE(tTMnetIncome5, totalShareholderEquity5)
    currentQuarterAvgCommonEquity5 = ((float(totalShareholderEquity5) + float(totalShareholderEquity5)) / 4)
    currentQuarterReturnOnCommonEquity5 = (calculateReturnOnCommonEquity(netIncome5, dividendPayoutPreferredStock5,
                                                                         currentQuarterAvgCommonEquity5)) * 4
    tTMAvgCommonEquity5 = ((float(totalShareholderEquity5) + float(totalShareholderEquity6) + float(
        totalShareholderEquity7) + float(totalShareholderEquity8)) / 4)
    tTMReturnOnCommonEquity5 = calculateReturnOnCommonEquity(tTMnetIncome5, tTMpreferredDivs5, tTMAvgCommonEquity5)
    debtRatio5 = calculateDebtRatio(totalLiabilities5, totalAssets5)
    debtToEquityRatio5 = calculateDebtToEquity(shortLongTermDebtTotal5, totalShareholderEquity5)
    debtToAssetRatio5 = calculateDebtToAssetRatio(shortLongTermDebtTotal5, totalAssets5)
    debtToCapitalRatio5 = calculateDebtToCapitalRatio(shortLongTermDebtTotal5, totalShareholderEquity5)

    financialLeverage5 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets5, currentQuarterAvgCommonEquity5)
    interestCoverage5 = calculateInterestCoverageRatio(operatingCashflow5, interestExpense5, incomeTaxExpense5)
    fixedChargeCoverageRatio5 = calculateFixedChargeCoverage(ebit5, capitalLeaseObligations5, interestExpense5)

    ## tm4  VARIABLES
    # Income Statement Variables for tm4
    gross_profit4 = quarterly_statementsDump.loc['grossProfit'][15]
    try:
        gross_profit4 = int(gross_profit4)
    except Exception:
        gross_profit4 = 0
    totalRevenue4 = quarterly_statementsDump.loc['totalRevenue'][15]
    try:
        totalRevenue4 = int(totalRevenue4)
    except Exception:
        totalRevenue4 = 0
    costOfRevenue4 = quarterly_statementsDump.loc['costOfRevenue'][15]
    try:
        costOfRevenue4 = int(costOfRevenue4)
    except Exception:
        costOfRevenue4 = 0
    costofGoodsAndServicesSold4 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][15]
    try:
        costofGoodsAndServicesSold4 = int(costofGoodsAndServicesSold4)
    except Exception:
        costofGoodsAndServicesSold4 = 0
    operatingIncome4 = quarterly_statementsDump.loc['operatingIncome'][15]
    try:
        operatingIncome4 = int(operatingIncome4)
    except Exception:
        operatingIncome4 = 0
    sellingGeneralAndAdministrative4 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][15]
    try:
        sellingGeneralAndAdministrative4 = int(sellingGeneralAndAdministrative4)
    except Exception:
        sellingGeneralAndAdministrative4 = 0
    researchAndDevelopment4 = quarterly_statementsDump.loc['researchAndDevelopment'][15]
    try:
        researchAndDevelopment4 = int(researchAndDevelopment4)
    except Exception:
        researchAndDevelopment4 = 0
    operatingExpenses4 = quarterly_statementsDump.loc['operatingExpenses'][15]
    try:
        operatingExpenses4 = int(operatingExpenses4)
    except Exception:
        operatingExpenses4 = 0
    investmentIncomeNet4 = quarterly_statementsDump.loc['investmentIncomeNet'][15]
    try:
        investmentIncomeNet4 = int(investmentIncomeNet4)
    except Exception:
        investmentIncomeNet4 = 0

    netInterestIncome4 = quarterly_statementsDump.loc['netInterestIncome'][15]
    try:
        netInterestIncome4 = int(netInterestIncome4)
    except Exception:
        netInterestIncome4 = 0
    interestIncome4 = quarterly_statementsDump.loc['interestIncome'][15]
    try:
        interestIncome4 = int(interestIncome4)
    except Exception:
        interestIncome4 = 0
    interestExpense4 = quarterly_statementsDump.loc['interestExpense'][15]
    try:
        interestExpense4 = int(interestExpense4)
    except Exception:
        interestExpense4 = 0
    nonInterestIncome4 = quarterly_statementsDump.loc['nonInterestIncome'][15]
    try:
        nonInterestIncome4 = int(nonInterestIncome4)
    except Exception:
        nonInterestIncome4 = 0
    otherNonOperatingIncome4 = quarterly_statementsDump.loc['otherNonOperatingIncome'][15]
    try:
        otherNonOperatingIncome4 = int(otherNonOperatingIncome4)
    except Exception:
        otherNonOperatingIncome4 = 0
    depreciation4 = quarterly_statementsDump.loc['depreciation'][15]
    try:
        depreciation4 = int(depreciation4)
    except Exception:
        depreciation4 = 0
    depreciationAndAmortization4 = quarterly_statementsDump.loc['depreciationAndAmortization'][15]
    try:
        depreciationAndAmortization4 = int(depreciationAndAmortization4)
    except Exception:
        depreciationAndAmortization4 = 0

    incomeBeforeTax4 = quarterly_statementsDump.loc['incomeBeforeTax'][15]
    try:
        incomeBeforeTax4 = int(incomeBeforeTax4)
    except Exception:
        incomeBeforeTax4 = 0

    incomeTaxExpense4 = quarterly_statementsDump.loc['incomeTaxExpense'][15]
    try:
        incomeTaxExpense4 = int(incomeTaxExpense4)
    except Exception:
        incomeTaxExpense4 = 0
    interestAndDebtExpense4 = quarterly_statementsDump.loc['interestAndDebtExpense'][15]
    try:
        interestAndDebtExpense4 = int(interestAndDebtExpense4)
    except Exception:
        interestAndDebtExpense4 = 0
    netIncomeFromContinuingOperations4 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][15]
    try:
        netIncomeFromContinuingOperations4 = int(netIncomeFromContinuingOperations4)
    except Exception:
        netIncomeFromContinuingOperations4 = 0
    comprehensiveIncomeNetOfTax4 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][15]
    try:
        comprehensiveIncomeNetOfTax4 = int(comprehensiveIncomeNetOfTax4)
    except Exception:
        comprehensiveIncomeNetOfTax4 = 0
    ebit4 = quarterly_statementsDump.loc['ebit'][15]
    try:
        ebit4 = int(ebit4)
    except Exception:
        ebit4 = 0
    ebitda4 = quarterly_statementsDump.loc['ebitda'][15]
    try:
        ebitda4 = int(ebitda4)
    except Exception:
        ebitda4 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 15]

    # Balance Sheet Values for tm4

    totalAssets4 = quarterly_statementsDump.loc['totalAssets'][15]
    try:
        totalAssets4 = int(totalAssets4)
    except Exception:
        totalAssets4 = 0
    totalCurrentAssets4 = quarterly_statementsDump.loc['totalCurrentAssets'][15]
    try:
        totalCurrentAssets4 = int(totalCurrentAssets4)
    except Exception:
        totalCurrentAssets4 = 0
    cashAndCashEquivalentsAtCarryingValue4 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][15]
    try:
        cashAndCashEquivalentsAtCarryingValue4 = int(cashAndCashEquivalentsAtCarryingValue4)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue4 = 0
    cashAndShortTermInvestments4 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][15]
    try:
        cashAndShortTermInvestments4 = int(cashAndShortTermInvestments4)
    except Exception:
        cashAndShortTermInvestments4 = 0
    inventory4 = quarterly_statementsDump.loc['inventory'][15]
    try:
        inventory4 = int(inventory4)
    except Exception:
        inventory4 = 0
    currentNetReceivables4 = quarterly_statementsDump.loc['currentNetReceivables'][15]
    try:
        currentNetReceivables4 = int(currentNetReceivables4)
    except Exception:
        currentNetReceivables4 = 0
    totalNonCurrentAssets4 = quarterly_statementsDump.loc['totalNonCurrentAssets'][15]
    try:
        totalNonCurrentAssets4 = int(totalNonCurrentAssets4)
    except Exception:
        totalNonCurrentAssets4 = 0
    propertyPlantEquipment4 = quarterly_statementsDump.loc['propertyPlantEquipment'][15]
    try:
        propertyPlantEquipment4 = int(propertyPlantEquipment4)
    except Exception:
        propertyPlantEquipment4 = 0
    accumulatedDepreciationAmortizationPPE4 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][15]
    try:
        accumulatedDepreciationAmortizationPPE4 = int(accumulatedDepreciationAmortizationPPE4)
    except Exception:
        accumulatedDepreciationAmortizationPPE4 = 0
    intangibleAssets4 = quarterly_statementsDump.loc['intangibleAssets'][15]
    try:
        intangibleAssets4 = int(intangibleAssets4)
    except Exception:
        intangibleAssets4 = 0
    intangibleAssetsExcludingGoodwill4 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][15]
    try:
        intangibleAssetsExcludingGoodwill4 = int(intangibleAssetsExcludingGoodwill4)
    except Exception:
        intangibleAssetsExcludingGoodwill4 = 0
    goodwill4 = quarterly_statementsDump.loc['goodwill'][15]
    try:
        goodwill4 = int(goodwill4)
    except Exception:
        goodwill4 = 0
    investments4 = quarterly_statementsDump.loc['investments'][15]
    try:
        investments4 = int(investments4)
    except Exception:
        investments4 = 0
    longTermInvestments4 = quarterly_statementsDump.loc['longTermInvestments'][15]
    try:
        longTermInvestments4 = int(longTermInvestments4)
    except Exception:
        longTermInvestments4 = 0
    shortTermInvestments4 = quarterly_statementsDump.loc['shortTermInvestments'][15]
    try:
        shortTermInvestments4 = int(shortTermInvestments4)
    except Exception:
        shortTermInvestments4 = 0
    otherCurrentAssets4 = quarterly_statementsDump.loc['otherCurrentAssets'][15]
    try:
        otherCurrentAssets4 = int(otherCurrentAssets4)
    except Exception:
        otherCurrentAssets4 = 0
    otherNonCurrrentAssets4 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][15]
    try:
        otherNonCurrrentAssets4 = int(otherNonCurrrentAssets4)
    except Exception:
        otherNonCurrrentAssets4 = 0
    totalLiabilities4 = quarterly_statementsDump.loc['totalLiabilities'][15]
    try:
        totalLiabilities4 = int(totalLiabilities4)
    except Exception:
        totalLiabilities4 = 0
    totalCurrentLiabilities4 = quarterly_statementsDump.loc['totalCurrentLiabilities'][15]
    try:
        totalCurrentLiabilities4 = int(totalCurrentLiabilities4)
    except Exception:
        totalCurrentLiabilities4 = 0
    currentAccountsPayable4 = quarterly_statementsDump.loc['currentAccountsPayable'][15]
    try:
        currentAccountsPayable4 = int(currentAccountsPayable4)
    except Exception:
        currentAccountsPayable4 = 0
    deferredRevenue4 = quarterly_statementsDump.loc['deferredRevenue'][15]
    try:
        deferredRevenue4 = int(deferredRevenue4)
    except Exception:
        deferredRevenue4 = 0
    currentDebt4 = quarterly_statementsDump.loc['currentDebt'][15]
    try:
        currentDebt4 = int(currentDebt4)
    except Exception:
        currentDebt4 = 0
    shortTermDebt4 = quarterly_statementsDump.loc['shortTermDebt'][15]
    try:
        shortTermDebt4 = int(shortTermDebt4)
    except Exception:
        shortTermDebt4 = 0
    totalNonCurrentLiabilities4 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][15]
    try:
        totalNonCurrentLiabilities4 = int(totalNonCurrentLiabilities4)
    except Exception:
        totalNonCurrentLiabilities4 = 0
    capitalLeaseObligations4 = quarterly_statementsDump.loc['capitalLeaseObligations'][15]
    try:
        capitalLeaseObligations4 = int(capitalLeaseObligations4)
    except Exception:
        capitalLeaseObligations4 = 0

    longTermDebt4 = quarterly_statementsDump.loc['longTermDebt'][15]
    try:
        longTermDebt4 = int(longTermDebt4)
    except Exception:
        longTermDebt4 = 0
    currentLongTermDebt4 = quarterly_statementsDump.loc['currentLongTermDebt'][15]
    try:
        currentLongTermDebt4 = int(currentLongTermDebt4)
    except Exception:
        currentLongTermDebt4 = 0
    longTermDebtNoncurrent4 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][15]
    try:
        longTermDebtNoncurrent4 = int(longTermDebtNoncurrent4)
    except Exception:
        longTermDebtNoncurrent4 = 0
    shortLongTermDebtTotal4 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][15]
    try:
        shortLongTermDebtTotal4 = int(shortLongTermDebtTotal4)
    except Exception:
        shortLongTermDebtTotal4 = 0
    otherCurrentLiabilities4 = quarterly_statementsDump.loc['otherCurrentLiabilities'][15]
    try:
        otherCurrentLiabilities4 = int(otherCurrentLiabilities4)
    except Exception:
        otherCurrentLiabilities4 = 0
    otherNonCurrentLiabilities4 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][15]
    try:
        otherNonCurrentLiabilities4 = int(otherNonCurrentLiabilities4)
    except Exception:
        otherNonCurrentLiabilities4 = 0
    totalShareholderEquity4 = quarterly_statementsDump.loc['totalShareholderEquity'][15]
    try:
        totalShareholderEquity4 = int(totalShareholderEquity4)
    except Exception:
        totalShareholderEquity4 = 0
    treasuryStock4 = quarterly_statementsDump.loc['treasuryStock'][15]
    try:
        treasuryStock4 = int(treasuryStock4)
    except Exception:
        treasuryStock4 = 0
    retainedEarnings4 = quarterly_statementsDump.loc['retainedEarnings'][15]
    try:
        retainedEarnings4 = int(retainedEarnings4)
    except Exception:
        retainedEarnings4 = 0
    commonStock4 = quarterly_statementsDump.loc['commonStock'][15]
    try:
        commonStock4 = int(commonStock4)
    except Exception:
        commonStock4 = 0
    commonStockSharesOutstanding4 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][15]
    try:
        commonStockSharesOutstanding4 = int(commonStockSharesOutstanding4)
    except Exception:
        commonStockSharesOutstanding4 = 0


    # Cash-Flow Statement values for tm4
    operatingCashflow4 = quarterly_statementsDump.loc['operatingCashflow'][15]
    try:
        operatingCashflow4 = int(operatingCashflow4)
    except Exception:
        operatingCashflow4 = 0
    paymentsForOperatingActivities4 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][15]
    try:
        paymentsForOperatingActivities4 = int(paymentsForOperatingActivities4)
    except Exception:
        paymentsForOperatingActivities4 = 0
    proceedsFromOperatingActivities4 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][15]
    try:
        proceedsFromOperatingActivities4 = int(proceedsFromOperatingActivities4)
    except Exception:
        proceedsFromOperatingActivities4 = 0
    changeInOperatingLiabilities4 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][15]
    try:
        changeInOperatingLiabilities4 = int(changeInOperatingLiabilities4)
    except Exception:
        changeInOperatingLiabilities4 = 0
    changeInOperatingAssets4 = quarterly_statementsDump.loc['changeInOperatingAssets'][15]
    try:
        changeInOperatingAssets4 = int(changeInOperatingAssets4)
    except Exception:
        changeInOperatingAssets4 = 0
    depreciationDepletionAndAmortization4 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][15]
    try:
        depreciationDepletionAndAmortization4 = int(depreciationDepletionAndAmortization4)
    except Exception:
        depreciationDepletionAndAmortization4 = 0
    capitalExpenditures4 = quarterly_statementsDump.loc['capitalExpenditures'][15]
    try:
        capitalExpenditures4 = int(capitalExpenditures4)
    except Exception:
        capitalExpenditures4 = 0
    changeInReceivables4 = quarterly_statementsDump.loc['changeInReceivables'][15]
    try:
        changeInReceivables4 = int(changeInReceivables4)
    except Exception:
        changeInReceivables4 = 0
    changeInInventory4 = quarterly_statementsDump.loc['changeInInventory'][15]
    try:
        changeInInventory4 = int(changeInInventory4)
    except Exception:
        changeInInventory4 = 0
    profitLoss4 = quarterly_statementsDump.loc['profitLoss'][15]
    try:
        profitLoss4 = int(profitLoss4)
    except Exception:
        profitLoss4 = 0
    cashflowFromInvestment4 = quarterly_statementsDump.loc['cashflowFromInvestment'][15]
    try:
        cashflowFromInvestment4 = int(cashflowFromInvestment4)
    except Exception:
        cashflowFromInvestment4 = 0
    cashflowFromFinancing4 = quarterly_statementsDump.loc['cashflowFromFinancing'][15]
    try:
        cashflowFromFinancing4 = int(cashflowFromFinancing4)
    except Exception:
        cashflowFromFinancing4 = 0
    proceedsFromRepaymentsOfShortTermDebt4 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][15]
    try:
        proceedsFromRepaymentsOfShortTermDebt4 = int(proceedsFromRepaymentsOfShortTermDebt4)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt4 = 0
    paymentsForRepurchaseOfCommonStock4 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][15]
    try:
        paymentsForRepurchaseOfCommonStock4 = int(paymentsForRepurchaseOfCommonStock4)
    except Exception:
        paymentsForRepurchaseOfCommonStock4 = 0
    paymentsForRepurchaseOfEquity4 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][15]
    try:
        paymentsForRepurchaseOfEquity4 = int(paymentsForRepurchaseOfEquity4)
    except Exception:
        paymentsForRepurchaseOfEquity4 = 0
    paymentsForRepurchaseOfPreferredStock4 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][15]
    try:
        paymentsForRepurchaseOfPreferredStock4 = int(paymentsForRepurchaseOfPreferredStock4)
    except Exception:
        paymentsForRepurchaseOfPreferredStock4 = 0
    dividendPayout4 = quarterly_statementsDump.loc['dividendPayout'][15]
    try:
        dividendPayout4 = int(dividendPayout4)
    except Exception:
        dividendPayout4 = 0
    dividendPayoutCommonStock4 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][15]
    try:
        dividendPayoutCommonStock4 = int(dividendPayoutCommonStock4)
    except Exception:
        dividendPayoutCommonStock4 = 0
    dividendPayoutPreferredStock4 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][15]
    try:
        dividendPayoutPreferredStock4 = int(dividendPayoutPreferredStock4)
    except Exception:
        dividendPayoutPreferredStock4 = 0
    proceedsFromIssuanceOfCommonStock4 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][15]
    try:
        proceedsFromIssuanceOfCommonStock4 = int(proceedsFromIssuanceOfCommonStock4)
    except Exception:
        proceedsFromIssuanceOfCommonStock4 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet4 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][15]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet4 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet4)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet4 = 0
    proceedsFromIssuanceOfPreferredStock4 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][15]
    try:
        proceedsFromIssuanceOfPreferredStock4 = int(proceedsFromIssuanceOfPreferredStock4)
    except Exception:
        proceedsFromIssuanceOfPreferredStock4 = 0
    proceedsFromRepurchaseOfEquity4 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][15]
    try:
        proceedsFromRepurchaseOfEquity4 = int(proceedsFromRepurchaseOfEquity4)
    except Exception:
        proceedsFromRepurchaseOfEquity4 = 0
    proceedsFromSaleOfTreasuryStock4 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][15]
    try:
        proceedsFromSaleOfTreasuryStock4 = int(proceedsFromSaleOfTreasuryStock4)
    except Exception:
        proceedsFromSaleOfTreasuryStock4 = 0
    changeInCashAndCashEquivalents4 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][15]
    try:
        changeInCashAndCashEquivalents4 = int(changeInCashAndCashEquivalents4)
    except Exception:
        changeInCashAndCashEquivalents4 = 0
    changeInExchangeRate4 = quarterly_statementsDump.loc['changeInExchangeRate'][15]
    try:
        changeInExchangeRate4 = int(changeInExchangeRate4)
    except Exception:
        changeInExchangeRate4 = 0
    netIncome4 = quarterly_statementsDump.loc['netIncome'][15]
    try:
        netIncome4 = int(netIncome4)
    except Exception:
        netIncome4 = 0

    tTMnetIncome4 = (float(netIncome4) + float(netIncome5) + float(netIncome6) + float(netIncome7))
    try:
        tTMpreferredDivs4 = (int(dividendPayoutPreferredStock4) + int(dividendPayoutPreferredStock5) + int(
            dividendPayoutPreferredStock6) + int(dividendPayoutPreferredStock7))
    except Exception:
        tTMpreferredDivs4 = 0
    weightedAvgCommShrsOutstanding4 = (
                (float(commonStockSharesOutstanding4) + float(commonStockSharesOutstanding5) + float(
                    commonStockSharesOutstanding6) + float(commonStockSharesOutstanding7)) / 4)
    quoteUnformatted4 = quoteUnformatted
    marketCap4 = calculateMarketCap(quoteUnformatted4, commonStockSharesOutstanding4)
    basicEPS4 = calculateBasicEPS(tTMnetIncome4, tTMpreferredDivs4, weightedAvgCommShrsOutstanding4)
    pE4 = calculatePE(quoteUnformatted4, basicEPS4)
    pCF4 = calculatePriceToCashFlow(quoteUnformatted4,
                                    calculateOperatingCashFlowPerShare(operatingCashflow4,
                                                                       weightedAvgCommShrsOutstanding4))
    pS4 = calculatePS(quoteUnformatted4, calculateSalesPerShare(totalRevenue4, weightedAvgCommShrsOutstanding4))
    pB4 = calculatePB(quoteUnformatted4,
                      calculateMarketToBookValue(marketCap4, totalAssets4, shortLongTermDebtTotal4, preferredStock=0))
    sustainableGrowthRate4 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout4, netIncome4)),
        calculateROE(netIncome4, totalShareholderEquity4))
    pEGRatio4 = calculatePEGRatio(pE4, (sustainableGrowthRate4 * 400))
    earningsYield4 = calculateEarningsYield(basicEPS4, quoteUnformatted4)
    cashFlowPerShare4 = calculateOperatingCashFlowPerShare(operatingCashflow4, weightedAvgCommShrsOutstanding4)
    ebitdaPerShare4 = calculateEBITDAperShare(ebitda4, weightedAvgCommShrsOutstanding4)
    tTMDividendPayout4 = (
        (float(dividendPayout4) + float(dividendPayout5) + float(dividendPayout6) + float(dividendPayout7)))
    dividendsPerShare4 = calculateDividendsPerShare(tTMDividendPayout4, weightedAvgCommShrsOutstanding4)
    currentQuarterGrossProfitMargin4 = calculateGrossProfitMargin(totalRevenue4, costofGoodsAndServicesSold4)
    tTmTotalRevenue4 = ((float(totalRevenue4) + float(totalRevenue5) + float(totalRevenue6) + float(totalRevenue7)))
    tTmCOGS4 = ((float(costofGoodsAndServicesSold4) + float(costofGoodsAndServicesSold5) + float(
        costofGoodsAndServicesSold6) + float(costofGoodsAndServicesSold7)))
    tTMGrossProfitMargin4 = calculateGrossProfitMargin(tTmTotalRevenue4, tTmCOGS4)
    currentQuarterOperatingMargin4 = calculateOperatingMargin(operatingIncome4, totalRevenue4)
    tTMOperatingIncome4 = (
        (float(operatingIncome4) + float(operatingIncome5) + float(operatingIncome6) + float(operatingIncome7)))
    tTMOperatingMargin4 = calculateOperatingMargin(tTMOperatingIncome4, tTmTotalRevenue4)
    currentQuarterPreTaxMargin4 = calculatePreTaxMargin(calculateEBT(ebit4, interestExpense4), totalRevenue4)
    tTMebit4 = ((float(ebit4) + float(ebit5) + float(ebit6) + float(ebit7)))
    tTMInterestExpense4 = (
        (float(interestExpense4) + float(interestExpense5) + float(interestExpense6) + float(interestExpense7)))
    tTMPreTaxMargin4 = calculatePreTaxMargin(calculateEBT(tTMebit4, tTMInterestExpense4), tTmTotalRevenue4)
    currentQuarterNetProfitMargin4 = calculateNetProfitMargin(netIncome4, totalRevenue4)
    tTMNetProfitMargin4 = calculateNetProfitMargin(tTMnetIncome4, tTmTotalRevenue4)
    currentQuarterAvgTotalAssets4 = ((float(totalAssets4) + float(totalAssets5)) / 4)
    currentQuarterOperatingROA4 = (calculateOperatingROA(operatingIncome4, currentQuarterAvgTotalAssets4)) * 4
    tTMAvgTotalAssets4 = ((float(totalAssets4) + float(totalAssets5) + float(totalAssets6) + float(totalAssets7)) / 4)
    tTMOperatingROA4 = calculateOperatingROA(tTMOperatingIncome4, tTMAvgTotalAssets4)
    currentQuarterROA4 = (calculateROA(netIncome4, currentQuarterAvgTotalAssets4)) * 4
    tTMROA4 = calculateROA(tTMnetIncome4, tTMAvgTotalAssets4)
    currentQuarterReturnOnTotalCapital4 = (calculateReturnOnTotalCapital(ebit4, shortLongTermDebtTotal4,
                                                                         totalShareholderEquity4)) * 4
    tTMReturnOnTotalCapital4 = calculateReturnOnTotalCapital(tTMebit4, shortLongTermDebtTotal4, totalShareholderEquity4)
    currentQuarterROE4 = (calculateROE(netIncome4, totalShareholderEquity4)) * 4
    tTMROE4 = calculateROE(tTMnetIncome4, totalShareholderEquity4)
    currentQuarterAvgCommonEquity4 = ((float(totalShareholderEquity4) + float(totalShareholderEquity4)) / 4)
    currentQuarterReturnOnCommonEquity4 = (calculateReturnOnCommonEquity(netIncome4, dividendPayoutPreferredStock4,
                                                                         currentQuarterAvgCommonEquity4)) * 4
    tTMAvgCommonEquity4 = ((float(totalShareholderEquity4) + float(totalShareholderEquity5) + float(
        totalShareholderEquity6) + float(totalShareholderEquity7)) / 4)
    tTMReturnOnCommonEquity4 = calculateReturnOnCommonEquity(tTMnetIncome4, tTMpreferredDivs4, tTMAvgCommonEquity4)
    debtRatio4 = calculateDebtRatio(totalLiabilities4, totalAssets4)
    debtToEquityRatio4 = calculateDebtToEquity(shortLongTermDebtTotal4, totalShareholderEquity4)
    debtToAssetRatio4 = calculateDebtToAssetRatio(shortLongTermDebtTotal4, totalAssets4)
    debtToCapitalRatio4 = calculateDebtToCapitalRatio(shortLongTermDebtTotal4, totalShareholderEquity4)

    financialLeverage4 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets4, currentQuarterAvgCommonEquity4)
    interestCoverage4 = calculateInterestCoverageRatio(operatingCashflow4, interestExpense4, incomeTaxExpense4)
    fixedChargeCoverageRatio4 = calculateFixedChargeCoverage(ebit4, capitalLeaseObligations4, interestExpense4)

    ## tm3  VARIABLES
    # Income Statement Variables for tm3
    gross_profit3 = quarterly_statementsDump.loc['grossProfit'][16]
    try:
        gross_profit3 = int(gross_profit3)
    except Exception:
        gross_profit3 = 0
    totalRevenue3 = quarterly_statementsDump.loc['totalRevenue'][16]
    try:
        totalRevenue3 = int(totalRevenue3)
    except Exception:
        totalRevenue3 = 0
    costOfRevenue3 = quarterly_statementsDump.loc['costOfRevenue'][16]
    try:
        costOfRevenue3 = int(costOfRevenue3)
    except Exception:
        costOfRevenue3 = 0
    costofGoodsAndServicesSold3 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][16]
    try:
        costofGoodsAndServicesSold3 = int(costofGoodsAndServicesSold3)
    except Exception:
        costofGoodsAndServicesSold3 = 0
    operatingIncome3 = quarterly_statementsDump.loc['operatingIncome'][16]
    try:
        operatingIncome3 = int(operatingIncome3)
    except Exception:
        operatingIncome3 = 0
    sellingGeneralAndAdministrative3 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][16]
    try:
        sellingGeneralAndAdministrative3 = int(sellingGeneralAndAdministrative3)
    except Exception:
        sellingGeneralAndAdministrative3 = 0
    researchAndDevelopment3 = quarterly_statementsDump.loc['researchAndDevelopment'][16]
    try:
        researchAndDevelopment3 = int(researchAndDevelopment3)
    except Exception:
        researchAndDevelopment3 = 0
    operatingExpenses3 = quarterly_statementsDump.loc['operatingExpenses'][16]
    try:
        operatingExpenses3 = int(operatingExpenses3)
    except Exception:
        operatingExpenses3 = 0
    investmentIncomeNet3 = quarterly_statementsDump.loc['investmentIncomeNet'][16]
    try:
        investmentIncomeNet3 = int(investmentIncomeNet3)
    except Exception:
        investmentIncomeNet3 = 0

    netInterestIncome3 = quarterly_statementsDump.loc['netInterestIncome'][16]
    try:
        netInterestIncome3 = int(netInterestIncome3)
    except Exception:
        netInterestIncome3 = 0
    interestIncome3 = quarterly_statementsDump.loc['interestIncome'][16]
    try:
        interestIncome3 = int(interestIncome3)
    except Exception:
        interestIncome3 = 0
    interestExpense3 = quarterly_statementsDump.loc['interestExpense'][16]
    try:
        interestExpense3 = int(interestExpense3)
    except Exception:
        interestExpense3 = 0
    nonInterestIncome3 = quarterly_statementsDump.loc['nonInterestIncome'][16]
    try:
        nonInterestIncome3 = int(nonInterestIncome3)
    except Exception:
        nonInterestIncome3 = 0
    otherNonOperatingIncome3 = quarterly_statementsDump.loc['otherNonOperatingIncome'][16]
    try:
        otherNonOperatingIncome3 = int(otherNonOperatingIncome3)
    except Exception:
        otherNonOperatingIncome3 = 0
    depreciation3 = quarterly_statementsDump.loc['depreciation'][16]
    try:
        depreciation3 = int(depreciation3)
    except Exception:
        depreciation3 = 0
    depreciationAndAmortization3 = quarterly_statementsDump.loc['depreciationAndAmortization'][16]
    try:
        depreciationAndAmortization3 = int(depreciationAndAmortization3)
    except Exception:
        depreciationAndAmortization3 = 0

    incomeBeforeTax3 = quarterly_statementsDump.loc['incomeBeforeTax'][16]
    try:
        incomeBeforeTax3 = int(incomeBeforeTax3)
    except Exception:
        incomeBeforeTax3 = 0

    incomeTaxExpense3 = quarterly_statementsDump.loc['incomeTaxExpense'][16]
    try:
        incomeTaxExpense3 = int(incomeTaxExpense3)
    except Exception:
        incomeTaxExpense3 = 0
    interestAndDebtExpense3 = quarterly_statementsDump.loc['interestAndDebtExpense'][16]
    try:
        interestAndDebtExpense3 = int(interestAndDebtExpense3)
    except Exception:
        interestAndDebtExpense3 = 0
    netIncomeFromContinuingOperations3 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][16]
    try:
        netIncomeFromContinuingOperations3 = int(netIncomeFromContinuingOperations3)
    except Exception:
        netIncomeFromContinuingOperations3 = 0
    comprehensiveIncomeNetOfTax3 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][16]
    try:
        comprehensiveIncomeNetOfTax3 = int(comprehensiveIncomeNetOfTax3)
    except Exception:
        comprehensiveIncomeNetOfTax3 = 0
    ebit3 = quarterly_statementsDump.loc['ebit'][16]
    try:
        ebit3 = int(ebit3)
    except Exception:
        ebit3 = 0
    ebitda3 = quarterly_statementsDump.loc['ebitda'][16]
    try:
        ebitda3 = int(ebitda3)
    except Exception:
        ebitda3 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 16]

    # Balance Sheet Values for tm

    totalAssets3 = quarterly_statementsDump.loc['totalAssets'][16]
    try:
        totalAssets3 = int(totalAssets3)
    except Exception:
        totalAssets3 = 0
    totalCurrentAssets3 = quarterly_statementsDump.loc['totalCurrentAssets'][16]
    try:
        totalCurrentAssets3 = int(totalCurrentAssets3)
    except Exception:
        totalCurrentAssets3 = 0
    cashAndCashEquivalentsAtCarryingValue3 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][16]
    try:
        cashAndCashEquivalentsAtCarryingValue3 = int(cashAndCashEquivalentsAtCarryingValue3)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue3 = 0
    cashAndShortTermInvestments3 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][16]
    try:
        cashAndShortTermInvestments3 = int(cashAndShortTermInvestments3)
    except Exception:
        cashAndShortTermInvestments3 = 0
    inventory3 = quarterly_statementsDump.loc['inventory'][16]
    try:
        inventory3 = int(inventory3)
    except Exception:
        inventory3 = 0
    currentNetReceivables3 = quarterly_statementsDump.loc['currentNetReceivables'][16]
    try:
        currentNetReceivables3 = int(currentNetReceivables3)
    except Exception:
        currentNetReceivables3 = 0
    totalNonCurrentAssets3 = quarterly_statementsDump.loc['totalNonCurrentAssets'][16]
    try:
        totalNonCurrentAssets3 = int(totalNonCurrentAssets3)
    except Exception:
        totalNonCurrentAssets3 = 0
    propertyPlantEquipment3 = quarterly_statementsDump.loc['propertyPlantEquipment'][16]
    try:
        propertyPlantEquipment3 = int(propertyPlantEquipment3)
    except Exception:
        propertyPlantEquipment3 = 0
    accumulatedDepreciationAmortizationPPE3 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][16]
    try:
        accumulatedDepreciationAmortizationPPE3 = int(accumulatedDepreciationAmortizationPPE3)
    except Exception:
        accumulatedDepreciationAmortizationPPE3 = 0
    intangibleAssets3 = quarterly_statementsDump.loc['intangibleAssets'][16]
    try:
        intangibleAssets3 = int(intangibleAssets3)
    except Exception:
        intangibleAssets3 = 0
    intangibleAssetsExcludingGoodwill3 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][16]
    try:
        intangibleAssetsExcludingGoodwill3 = int(intangibleAssetsExcludingGoodwill3)
    except Exception:
        intangibleAssetsExcludingGoodwill3 = 0
    goodwill3 = quarterly_statementsDump.loc['goodwill'][16]
    try:
        goodwill3 = int(goodwill3)
    except Exception:
        goodwill3 = 0
    investments3 = quarterly_statementsDump.loc['investments'][16]
    try:
        investments3 = int(investments3)
    except Exception:
        investments3 = 0
    longTermInvestments3 = quarterly_statementsDump.loc['longTermInvestments'][16]
    try:
        longTermInvestments3 = int(longTermInvestments3)
    except Exception:
        longTermInvestments3 = 0
    shortTermInvestments3 = quarterly_statementsDump.loc['shortTermInvestments'][16]
    try:
        shortTermInvestments3 = int(shortTermInvestments3)
    except Exception:
        shortTermInvestments3 = 0
    otherCurrentAssets3 = quarterly_statementsDump.loc['otherCurrentAssets'][16]
    try:
        otherCurrentAssets3 = int(otherCurrentAssets3)
    except Exception:
        otherCurrentAssets3 = 0
    otherNonCurrrentAssets3 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][16]
    try:
        otherNonCurrrentAssets3 = int(otherNonCurrrentAssets3)
    except Exception:
        otherNonCurrrentAssets3 = 0
    totalLiabilities3 = quarterly_statementsDump.loc['totalLiabilities'][16]
    try:
        totalLiabilities3 = int(totalLiabilities3)
    except Exception:
        totalLiabilities3 = 0
    totalCurrentLiabilities3 = quarterly_statementsDump.loc['totalCurrentLiabilities'][16]
    try:
        totalCurrentLiabilities3 = int(totalCurrentLiabilities3)
    except Exception:
        totalCurrentLiabilities3 = 0
    currentAccountsPayable3 = quarterly_statementsDump.loc['currentAccountsPayable'][16]
    try:
        currentAccountsPayable3 = int(currentAccountsPayable3)
    except Exception:
        currentAccountsPayable3 = 0
    deferredRevenue3 = quarterly_statementsDump.loc['deferredRevenue'][16]
    try:
        deferredRevenue3 = int(deferredRevenue3)
    except Exception:
        deferredRevenue3 = 0
    currentDebt3 = quarterly_statementsDump.loc['currentDebt'][16]
    try:
        currentDebt3 = int(currentDebt3)
    except Exception:
        currentDebt3 = 0
    shortTermDebt3 = quarterly_statementsDump.loc['shortTermDebt'][16]
    try:
        shortTermDebt3 = int(shortTermDebt3)
    except Exception:
        shortTermDebt3 = 0
    totalNonCurrentLiabilities3 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][16]
    try:
        totalNonCurrentLiabilities3 = int(totalNonCurrentLiabilities3)
    except Exception:
        totalNonCurrentLiabilities3 = 0
    capitalLeaseObligations3 = quarterly_statementsDump.loc['capitalLeaseObligations'][16]
    try:
        capitalLeaseObligations3 = int(capitalLeaseObligations3)
    except Exception:
        capitalLeaseObligations3 = 0

    longTermDebt3 = quarterly_statementsDump.loc['longTermDebt'][16]
    try:
        longTermDebt3 = int(longTermDebt3)
    except Exception:
        longTermDebt3 = 0
    currentLongTermDebt3 = quarterly_statementsDump.loc['currentLongTermDebt'][16]
    try:
        currentLongTermDebt3 = int(currentLongTermDebt3)
    except Exception:
        currentLongTermDebt3 = 0
    longTermDebtNoncurrent3 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][16]
    try:
        longTermDebtNoncurrent3 = int(longTermDebtNoncurrent3)
    except Exception:
        longTermDebtNoncurrent3 = 0
    shortLongTermDebtTotal3 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][16]
    try:
        shortLongTermDebtTotal3 = int(shortLongTermDebtTotal3)
    except Exception:
        shortLongTermDebtTotal3 = 0
    otherCurrentLiabilities3 = quarterly_statementsDump.loc['otherCurrentLiabilities'][16]
    try:
        otherCurrentLiabilities3 = int(otherCurrentLiabilities3)
    except Exception:
        otherCurrentLiabilities3 = 0
    otherNonCurrentLiabilities3 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][16]
    try:
        otherNonCurrentLiabilities3 = int(otherNonCurrentLiabilities3)
    except Exception:
        otherNonCurrentLiabilities3 = 0
    totalShareholderEquity3 = quarterly_statementsDump.loc['totalShareholderEquity'][16]
    try:
        totalShareholderEquity3 = int(totalShareholderEquity3)
    except Exception:
        totalShareholderEquity3 = 0
    treasuryStock3 = quarterly_statementsDump.loc['treasuryStock'][16]
    try:
        treasuryStock3 = int(treasuryStock3)
    except Exception:
        treasuryStock3 = 0
    retainedEarnings3 = quarterly_statementsDump.loc['retainedEarnings'][16]
    try:
        retainedEarnings3 = int(retainedEarnings3)
    except Exception:
        retainedEarnings3 = 0
    commonStock3 = quarterly_statementsDump.loc['commonStock'][16]
    try:
        commonStock3 = int(commonStock3)
    except Exception:
        commonStock3 = 0
    commonStockSharesOutstanding3 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][16]
    try:
        commonStockSharesOutstanding3 = int(commonStockSharesOutstanding3)
    except Exception:
        commonStockSharesOutstanding3 = 0
    # Cash-Flow Statement values for tm
    operatingCashflow3 = quarterly_statementsDump.loc['operatingCashflow'][16]
    try:
        operatingCashflow3 = int(operatingCashflow3)
    except Exception:
        operatingCashflow3 = 0
    paymentsForOperatingActivities3 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][16]
    try:
        paymentsForOperatingActivities3 = int(paymentsForOperatingActivities3)
    except Exception:
        paymentsForOperatingActivities3 = 0
    proceedsFromOperatingActivities3 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][16]
    try:
        proceedsFromOperatingActivities3 = int(proceedsFromOperatingActivities3)
    except Exception:
        proceedsFromOperatingActivities3 = 0
    changeInOperatingLiabilities3 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][16]
    try:
        changeInOperatingLiabilities3 = int(changeInOperatingLiabilities3)
    except Exception:
        changeInOperatingLiabilities3 = 0
    changeInOperatingAssets3 = quarterly_statementsDump.loc['changeInOperatingAssets'][16]
    try:
        changeInOperatingAssets3 = int(changeInOperatingAssets3)
    except Exception:
        changeInOperatingAssets3 = 0
    depreciationDepletionAndAmortization3 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][16]
    try:
        depreciationDepletionAndAmortization3 = int(depreciationDepletionAndAmortization3)
    except Exception:
        depreciationDepletionAndAmortization3 = 0
    capitalExpenditures3 = quarterly_statementsDump.loc['capitalExpenditures'][16]
    try:
        capitalExpenditures3 = int(capitalExpenditures3)
    except Exception:
        capitalExpenditures3 = 0
    changeInReceivables3 = quarterly_statementsDump.loc['changeInReceivables'][16]
    try:
        changeInReceivables3 = int(changeInReceivables3)
    except Exception:
        changeInReceivables3 = 0
    changeInInventory3 = quarterly_statementsDump.loc['changeInInventory'][16]
    try:
        changeInInventory3 = int(changeInInventory3)
    except Exception:
        changeInInventory3 = 0
    profitLoss3 = quarterly_statementsDump.loc['profitLoss'][16]
    try:
        profitLoss3 = int(profitLoss3)
    except Exception:
        profitLoss3 = 0
    cashflowFromInvestment3 = quarterly_statementsDump.loc['cashflowFromInvestment'][16]
    try:
        cashflowFromInvestment3 = int(cashflowFromInvestment3)
    except Exception:
        cashflowFromInvestment3 = 0
    cashflowFromFinancing3 = quarterly_statementsDump.loc['cashflowFromFinancing'][16]
    try:
        cashflowFromFinancing3 = int(cashflowFromFinancing3)
    except Exception:
        cashflowFromFinancing3 = 0
    proceedsFromRepaymentsOfShortTermDebt3 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][16]
    try:
        proceedsFromRepaymentsOfShortTermDebt3 = int(proceedsFromRepaymentsOfShortTermDebt3)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt3 = 0
    paymentsForRepurchaseOfCommonStock3 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][16]
    try:
        paymentsForRepurchaseOfCommonStock3 = int(paymentsForRepurchaseOfCommonStock3)
    except Exception:
        paymentsForRepurchaseOfCommonStock3 = 0
    paymentsForRepurchaseOfEquity3 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][16]
    try:
        paymentsForRepurchaseOfEquity3 = int(paymentsForRepurchaseOfEquity3)
    except Exception:
        paymentsForRepurchaseOfEquity3 = 0
    paymentsForRepurchaseOfPreferredStock3 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][16]
    try:
        paymentsForRepurchaseOfPreferredStock3 = int(paymentsForRepurchaseOfPreferredStock3)
    except Exception:
        paymentsForRepurchaseOfPreferredStock3 = 0
    dividendPayout3 = quarterly_statementsDump.loc['dividendPayout'][16]
    try:
        dividendPayout3 = int(dividendPayout3)
    except Exception:
        dividendPayout3 = 0
    dividendPayoutCommonStock3 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][16]
    try:
        dividendPayoutCommonStock3 = int(dividendPayoutCommonStock3)
    except Exception:
        dividendPayoutCommonStock3 = 0
    dividendPayoutPreferredStock3 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][16]
    try:
        dividendPayoutPreferredStock3 = int(dividendPayoutPreferredStock3)
    except Exception:
        dividendPayoutPreferredStock3 = 0
    proceedsFromIssuanceOfCommonStock3 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][16]
    try:
        proceedsFromIssuanceOfCommonStock3 = int(proceedsFromIssuanceOfCommonStock3)
    except Exception:
        proceedsFromIssuanceOfCommonStock3 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet3 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][16]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet3 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet3)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet3 = 0
    proceedsFromIssuanceOfPreferredStock3 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][16]
    try:
        proceedsFromIssuanceOfPreferredStock3 = int(proceedsFromIssuanceOfPreferredStock3)
    except Exception:
        proceedsFromIssuanceOfPreferredStock3 = 0
    proceedsFromRepurchaseOfEquity3 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][16]
    try:
        proceedsFromRepurchaseOfEquity3 = int(proceedsFromRepurchaseOfEquity3)
    except Exception:
        proceedsFromRepurchaseOfEquity3 = 0
    proceedsFromSaleOfTreasuryStock3 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][16]
    try:
        proceedsFromSaleOfTreasuryStock3 = int(proceedsFromSaleOfTreasuryStock3)
    except Exception:
        proceedsFromSaleOfTreasuryStock3 = 0
    changeInCashAndCashEquivalents3 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][16]
    try:
        changeInCashAndCashEquivalents3 = int(changeInCashAndCashEquivalents3)
    except Exception:
        changeInCashAndCashEquivalents3 = 0
    changeInExchangeRate3 = quarterly_statementsDump.loc['changeInExchangeRate'][16]
    try:
        changeInExchangeRate3 = int(changeInExchangeRate3)
    except Exception:
        changeInExchangeRate3 = 0
    netIncome3 = quarterly_statementsDump.loc['netIncome'][16]
    try:
        netIncome3 = int(netIncome3)
    except Exception:
        netIncome3 = 0

    tTMnetIncome3 = (float(netIncome3) + float(netIncome4) + float(netIncome5) + float(netIncome6))
    try:
        tTMpreferredDivs3 = (int(dividendPayoutPreferredStock3) + int(dividendPayoutPreferredStock4) + int(
            dividendPayoutPreferredStock5) + int(dividendPayoutPreferredStock6))
    except Exception:
        tTMpreferredDivs3 = 0
    weightedAvgCommShrsOutstanding3 = (
                (float(commonStockSharesOutstanding3) + float(commonStockSharesOutstanding4) + float(
                    commonStockSharesOutstanding5) + float(commonStockSharesOutstanding6)) / 4)
    quoteUnformatted3 = quoteUnformatted
    marketCap3 = calculateMarketCap(quoteUnformatted3, commonStockSharesOutstanding3)
    basicEPS3 = calculateBasicEPS(tTMnetIncome3, tTMpreferredDivs3, weightedAvgCommShrsOutstanding3)
    pE3 = calculatePE(quoteUnformatted3, basicEPS3)
    pCF3 = calculatePriceToCashFlow(quoteUnformatted3,
                                    calculateOperatingCashFlowPerShare(operatingCashflow3,
                                                                       weightedAvgCommShrsOutstanding3))
    pS3 = calculatePS(quoteUnformatted3, calculateSalesPerShare(totalRevenue3, weightedAvgCommShrsOutstanding3))
    pB3 = calculatePB(quoteUnformatted3,
                      calculateMarketToBookValue(marketCap3, totalAssets3, shortLongTermDebtTotal3, preferredStock=0))
    sustainableGrowthRate3 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout3, netIncome3)),
        calculateROE(netIncome3, totalShareholderEquity3))
    pEGRatio3 = calculatePEGRatio(pE3, (sustainableGrowthRate3 * 300))
    earningsYield3 = calculateEarningsYield(basicEPS3, quoteUnformatted3)
    cashFlowPerShare3 = calculateOperatingCashFlowPerShare(operatingCashflow3, weightedAvgCommShrsOutstanding3)
    ebitdaPerShare3 = calculateEBITDAperShare(ebitda3, weightedAvgCommShrsOutstanding3)
    tTMDividendPayout3 = (
        (float(dividendPayout3) + float(dividendPayout4) + float(dividendPayout5) + float(dividendPayout6)))
    dividendsPerShare3 = calculateDividendsPerShare(tTMDividendPayout3, weightedAvgCommShrsOutstanding3)
    currentQuarterGrossProfitMargin3 = calculateGrossProfitMargin(totalRevenue3, costofGoodsAndServicesSold3)
    tTmTotalRevenue3 = ((float(totalRevenue3) + float(totalRevenue4) + float(totalRevenue5) + float(totalRevenue6)))
    tTmCOGS3 = ((float(costofGoodsAndServicesSold3) + float(costofGoodsAndServicesSold4) + float(
        costofGoodsAndServicesSold5) + float(costofGoodsAndServicesSold6)))
    tTMGrossProfitMargin3 = calculateGrossProfitMargin(tTmTotalRevenue3, tTmCOGS3)
    currentQuarterOperatingMargin3 = calculateOperatingMargin(operatingIncome3, totalRevenue3)
    tTMOperatingIncome3 = (
        (float(operatingIncome3) + float(operatingIncome4) + float(operatingIncome5) + float(operatingIncome6)))
    tTMOperatingMargin3 = calculateOperatingMargin(tTMOperatingIncome3, tTmTotalRevenue3)
    currentQuarterPreTaxMargin3 = calculatePreTaxMargin(calculateEBT(ebit3, interestExpense3), totalRevenue3)
    tTMebit3 = ((float(ebit3) + float(ebit4) + float(ebit5) + float(ebit6)))
    tTMInterestExpense3 = (
        (float(interestExpense3) + float(interestExpense4) + float(interestExpense5) + float(interestExpense6)))
    tTMPreTaxMargin3 = calculatePreTaxMargin(calculateEBT(tTMebit3, tTMInterestExpense3), tTmTotalRevenue3)
    currentQuarterNetProfitMargin3 = calculateNetProfitMargin(netIncome3, totalRevenue3)
    tTMNetProfitMargin3 = calculateNetProfitMargin(tTMnetIncome3, tTmTotalRevenue3)
    currentQuarterAvgTotalAssets3 = ((float(totalAssets3) + float(totalAssets4)) / 3)
    currentQuarterOperatingROA3 = (calculateOperatingROA(operatingIncome3, currentQuarterAvgTotalAssets3)) * 4
    tTMAvgTotalAssets3 = ((float(totalAssets3) + float(totalAssets4) + float(totalAssets5) + float(totalAssets6)) / 4)
    tTMOperatingROA3 = calculateOperatingROA(tTMOperatingIncome3, tTMAvgTotalAssets3)
    currentQuarterROA3 = (calculateROA(netIncome3, currentQuarterAvgTotalAssets3)) * 4
    tTMROA3 = calculateROA(tTMnetIncome3, tTMAvgTotalAssets3)
    currentQuarterReturnOnTotalCapital3 = (calculateReturnOnTotalCapital(ebit3, shortLongTermDebtTotal3,
                                                                         totalShareholderEquity3)) * 4
    tTMReturnOnTotalCapital3 = calculateReturnOnTotalCapital(tTMebit3, shortLongTermDebtTotal3, totalShareholderEquity3)
    currentQuarterROE3 = (calculateROE(netIncome3, totalShareholderEquity3)) * 4
    tTMROE3 = calculateROE(tTMnetIncome3, totalShareholderEquity3)
    currentQuarterAvgCommonEquity3 = ((float(totalShareholderEquity3) + float(totalShareholderEquity4)) / 3)
    currentQuarterReturnOnCommonEquity3 = (calculateReturnOnCommonEquity(netIncome3, dividendPayoutPreferredStock3,
                                                                         currentQuarterAvgCommonEquity3)) * 4
    tTMAvgCommonEquity3 = ((float(totalShareholderEquity3) + float(totalShareholderEquity4) + float(
        totalShareholderEquity5) + float(totalShareholderEquity6)) / 4)
    tTMReturnOnCommonEquity3 = calculateReturnOnCommonEquity(tTMnetIncome3, tTMpreferredDivs3, tTMAvgCommonEquity3)
    debtRatio3 = calculateDebtRatio(totalLiabilities3, totalAssets3)
    debtToEquityRatio3 = calculateDebtToEquity(shortLongTermDebtTotal3, totalShareholderEquity3)
    debtToAssetRatio3 = calculateDebtToAssetRatio(shortLongTermDebtTotal3, totalAssets3)
    debtToCapitalRatio3 = calculateDebtToCapitalRatio(shortLongTermDebtTotal3, totalShareholderEquity3)

    financialLeverage3 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets3, currentQuarterAvgCommonEquity3)
    interestCoverage3 = calculateInterestCoverageRatio(operatingCashflow3, interestExpense3, incomeTaxExpense3)
    fixedChargeCoverageRatio3 = calculateFixedChargeCoverage(ebit3, capitalLeaseObligations3, interestExpense3)

    ## tm2  VARIABLES
    # Income Statement Variables for tm2
    gross_profit2 = quarterly_statementsDump.loc['grossProfit'][17]
    try:
        gross_profit2 = int(gross_profit2)
    except Exception:
        gross_profit2 = 0
    totalRevenue2 = quarterly_statementsDump.loc['totalRevenue'][17]
    try:
        totalRevenue2 = int(totalRevenue2)
    except Exception:
        totalRevenue2 = 0
    costOfRevenue2 = quarterly_statementsDump.loc['costOfRevenue'][17]
    try:
        costOfRevenue2 = int(costOfRevenue2)
    except Exception:
        costOfRevenue2 = 0
    costofGoodsAndServicesSold2 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][17]
    try:
        costofGoodsAndServicesSold2 = int(costofGoodsAndServicesSold2)
    except Exception:
        costofGoodsAndServicesSold2 = 0
    operatingIncome2 = quarterly_statementsDump.loc['operatingIncome'][17]
    try:
        operatingIncome2 = int(operatingIncome2)
    except Exception:
        operatingIncome2 = 0
    sellingGeneralAndAdministrative2 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][17]
    try:
        sellingGeneralAndAdministrative2 = int(sellingGeneralAndAdministrative2)
    except Exception:
        sellingGeneralAndAdministrative2 = 0
    researchAndDevelopment2 = quarterly_statementsDump.loc['researchAndDevelopment'][17]
    try:
        researchAndDevelopment2 = int(researchAndDevelopment2)
    except Exception:
        researchAndDevelopment2 = 0
    operatingExpenses2 = quarterly_statementsDump.loc['operatingExpenses'][17]
    try:
        operatingExpenses2 = int(operatingExpenses2)
    except Exception:
        operatingExpenses2 = 0
    investmentIncomeNet2 = quarterly_statementsDump.loc['investmentIncomeNet'][17]
    try:
        investmentIncomeNet2 = int(investmentIncomeNet2)
    except Exception:
        investmentIncomeNet2 = 0

    netInterestIncome2 = quarterly_statementsDump.loc['netInterestIncome'][17]
    try:
        netInterestIncome2 = int(netInterestIncome2)
    except Exception:
        netInterestIncome2 = 0
    interestIncome2 = quarterly_statementsDump.loc['interestIncome'][17]
    try:
        interestIncome2 = int(interestIncome2)
    except Exception:
        interestIncome2 = 0
    interestExpense2 = quarterly_statementsDump.loc['interestExpense'][17]
    try:
        interestExpense2 = int(interestExpense2)
    except Exception:
        interestExpense2 = 0
    nonInterestIncome2 = quarterly_statementsDump.loc['nonInterestIncome'][17]
    try:
        nonInterestIncome2 = int(nonInterestIncome2)
    except Exception:
        nonInterestIncome2 = 0
    otherNonOperatingIncome2 = quarterly_statementsDump.loc['otherNonOperatingIncome'][17]
    try:
        otherNonOperatingIncome2 = int(otherNonOperatingIncome2)
    except Exception:
        otherNonOperatingIncome2 = 0
    depreciation2 = quarterly_statementsDump.loc['depreciation'][17]
    try:
        depreciation2 = int(depreciation2)
    except Exception:
        depreciation2 = 0
    depreciationAndAmortization2 = quarterly_statementsDump.loc['depreciationAndAmortization'][17]
    try:
        depreciationAndAmortization2 = int(depreciationAndAmortization2)
    except Exception:
        depreciationAndAmortization2 = 0

    incomeBeforeTax2 = quarterly_statementsDump.loc['incomeBeforeTax'][17]
    try:
        incomeBeforeTax2 = int(incomeBeforeTax2)
    except Exception:
        incomeBeforeTax2 = 0

    incomeTaxExpense2 = quarterly_statementsDump.loc['incomeTaxExpense'][17]
    try:
        incomeTaxExpense2 = int(incomeTaxExpense2)
    except Exception:
        incomeTaxExpense2 = 0
    interestAndDebtExpense2 = quarterly_statementsDump.loc['interestAndDebtExpense'][17]
    try:
        interestAndDebtExpense2 = int(interestAndDebtExpense2)
    except Exception:
        interestAndDebtExpense2 = 0
    netIncomeFromContinuingOperations2 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][17]
    try:
        netIncomeFromContinuingOperations2 = int(netIncomeFromContinuingOperations2)
    except Exception:
        netIncomeFromContinuingOperations2 = 0
    comprehensiveIncomeNetOfTax2 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][17]
    try:
        comprehensiveIncomeNetOfTax2 = int(comprehensiveIncomeNetOfTax2)
    except Exception:
        comprehensiveIncomeNetOfTax2 = 0
    ebit2 = quarterly_statementsDump.loc['ebit'][17]
    try:
        ebit2 = int(ebit2)
    except Exception:
        ebit2 = 0
    ebitda2 = quarterly_statementsDump.loc['ebitda'][17]
    try:
        ebitda2 = int(ebitda2)
    except Exception:
        ebitda2 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 17]

    # Balance Sheet Values for tm2

    totalAssets2 = quarterly_statementsDump.loc['totalAssets'][17]
    try:
        totalAssets2 = int(totalAssets2)
    except Exception:
        totalAssets2 = 0
    totalCurrentAssets2 = quarterly_statementsDump.loc['totalCurrentAssets'][17]
    try:
        totalCurrentAssets2 = int(totalCurrentAssets2)
    except Exception:
        totalCurrentAssets2 = 0
    cashAndCashEquivalentsAtCarryingValue2 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][17]
    try:
        cashAndCashEquivalentsAtCarryingValue2 = int(cashAndCashEquivalentsAtCarryingValue2)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue2 = 0
    cashAndShortTermInvestments2 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][17]
    try:
        cashAndShortTermInvestments2 = int(cashAndShortTermInvestments2)
    except Exception:
        cashAndShortTermInvestments2 = 0
    inventory2 = quarterly_statementsDump.loc['inventory'][17]
    try:
        inventory2 = int(inventory2)
    except Exception:
        inventory2 = 0
    currentNetReceivables2 = quarterly_statementsDump.loc['currentNetReceivables'][17]
    try:
        currentNetReceivables2 = int(currentNetReceivables2)
    except Exception:
        currentNetReceivables2 = 0
    totalNonCurrentAssets2 = quarterly_statementsDump.loc['totalNonCurrentAssets'][17]
    try:
        totalNonCurrentAssets2 = int(totalNonCurrentAssets2)
    except Exception:
        totalNonCurrentAssets2 = 0
    propertyPlantEquipment2 = quarterly_statementsDump.loc['propertyPlantEquipment'][17]
    try:
        propertyPlantEquipment2 = int(propertyPlantEquipment2)
    except Exception:
        propertyPlantEquipment2 = 0
    accumulatedDepreciationAmortizationPPE2 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][17]
    try:
        accumulatedDepreciationAmortizationPPE2 = int(accumulatedDepreciationAmortizationPPE2)
    except Exception:
        accumulatedDepreciationAmortizationPPE2 = 0
    intangibleAssets2 = quarterly_statementsDump.loc['intangibleAssets'][17]
    try:
        intangibleAssets2 = int(intangibleAssets2)
    except Exception:
        intangibleAssets2 = 0
    intangibleAssetsExcludingGoodwill2 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][17]
    try:
        intangibleAssetsExcludingGoodwill2 = int(intangibleAssetsExcludingGoodwill2)
    except Exception:
        intangibleAssetsExcludingGoodwill2 = 0
    goodwill2 = quarterly_statementsDump.loc['goodwill'][17]
    try:
        goodwill2 = int(goodwill2)
    except Exception:
        goodwill2 = 0
    investments2 = quarterly_statementsDump.loc['investments'][17]
    try:
        investments2 = int(investments2)
    except Exception:
        investments2 = 0
    longTermInvestments2 = quarterly_statementsDump.loc['longTermInvestments'][17]
    try:
        longTermInvestments2 = int(longTermInvestments2)
    except Exception:
        longTermInvestments2 = 0
    shortTermInvestments2 = quarterly_statementsDump.loc['shortTermInvestments'][17]
    try:
        shortTermInvestments2 = int(shortTermInvestments2)
    except Exception:
        shortTermInvestments2 = 0
    otherCurrentAssets2 = quarterly_statementsDump.loc['otherCurrentAssets'][17]
    try:
        otherCurrentAssets2 = int(otherCurrentAssets2)
    except Exception:
        otherCurrentAssets2 = 0
    otherNonCurrrentAssets2 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][17]
    try:
        otherNonCurrrentAssets2 = int(otherNonCurrrentAssets2)
    except Exception:
        otherNonCurrrentAssets2 = 0
    totalLiabilities2 = quarterly_statementsDump.loc['totalLiabilities'][17]
    try:
        totalLiabilities2 = int(totalLiabilities2)
    except Exception:
        totalLiabilities2 = 0
    totalCurrentLiabilities2 = quarterly_statementsDump.loc['totalCurrentLiabilities'][17]
    try:
        totalCurrentLiabilities2 = int(totalCurrentLiabilities2)
    except Exception:
        totalCurrentLiabilities2 = 0
    currentAccountsPayable2 = quarterly_statementsDump.loc['currentAccountsPayable'][17]
    try:
        currentAccountsPayable2 = int(currentAccountsPayable2)
    except Exception:
        currentAccountsPayable2 = 0
    deferredRevenue2 = quarterly_statementsDump.loc['deferredRevenue'][17]
    try:
        deferredRevenue2 = int(deferredRevenue2)
    except Exception:
        deferredRevenue2 = 0
    currentDebt2 = quarterly_statementsDump.loc['currentDebt'][17]
    try:
        currentDebt2 = int(currentDebt2)
    except Exception:
        currentDebt2 = 0
    shortTermDebt2 = quarterly_statementsDump.loc['shortTermDebt'][17]
    try:
        shortTermDebt2 = int(shortTermDebt2)
    except Exception:
        shortTermDebt2 = 0
    totalNonCurrentLiabilities2 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][17]
    try:
        totalNonCurrentLiabilities2 = int(totalNonCurrentLiabilities2)
    except Exception:
        totalNonCurrentLiabilities2 = 0
    capitalLeaseObligations2 = quarterly_statementsDump.loc['capitalLeaseObligations'][17]
    try:
        capitalLeaseObligations2 = int(capitalLeaseObligations2)
    except Exception:
        capitalLeaseObligations2 = 0

    longTermDebt2 = quarterly_statementsDump.loc['longTermDebt'][17]
    try:
        longTermDebt2 = int(longTermDebt2)
    except Exception:
        longTermDebt2 = 0
    currentLongTermDebt2 = quarterly_statementsDump.loc['currentLongTermDebt'][17]
    try:
        currentLongTermDebt2 = int(currentLongTermDebt2)
    except Exception:
        currentLongTermDebt2 = 0
    longTermDebtNoncurrent2 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][17]
    try:
        longTermDebtNoncurrent2 = int(longTermDebtNoncurrent2)
    except Exception:
        longTermDebtNoncurrent2 = 0
    shortLongTermDebtTotal2 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][17]
    try:
        shortLongTermDebtTotal2 = int(shortLongTermDebtTotal2)
    except Exception:
        shortLongTermDebtTotal2 = 0
    otherCurrentLiabilities2 = quarterly_statementsDump.loc['otherCurrentLiabilities'][17]
    try:
        otherCurrentLiabilities2 = int(otherCurrentLiabilities2)
    except Exception:
        otherCurrentLiabilities2 = 0
    otherNonCurrentLiabilities2 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][17]
    try:
        otherNonCurrentLiabilities2 = int(otherNonCurrentLiabilities2)
    except Exception:
        otherNonCurrentLiabilities2 = 0
    totalShareholderEquity2 = quarterly_statementsDump.loc['totalShareholderEquity'][17]
    try:
        totalShareholderEquity2 = int(totalShareholderEquity2)
    except Exception:
        totalShareholderEquity2 = 0
    treasuryStock2 = quarterly_statementsDump.loc['treasuryStock'][17]
    try:
        treasuryStock2 = int(treasuryStock2)
    except Exception:
        treasuryStock2 = 0
    retainedEarnings2 = quarterly_statementsDump.loc['retainedEarnings'][17]
    try:
        retainedEarnings2 = int(retainedEarnings2)
    except Exception:
        retainedEarnings2 = 0
    commonStock2 = quarterly_statementsDump.loc['commonStock'][17]
    try:
        commonStock2 = int(commonStock2)
    except Exception:
        commonStock2 = 0
    commonStockSharesOutstanding2 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][17]
    try:
        commonStockSharesOutstanding2 = int(commonStockSharesOutstanding2)
    except Exception:
        commonStockSharesOutstanding2 = 0


    # Cash-Flow Statement values for tm2
    operatingCashflow2 = quarterly_statementsDump.loc['operatingCashflow'][17]
    try:
        operatingCashflow2 = int(operatingCashflow2)
    except Exception:
        operatingCashflow2 = 0
    paymentsForOperatingActivities2 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][17]
    try:
        paymentsForOperatingActivities2 = int(paymentsForOperatingActivities2)
    except Exception:
        paymentsForOperatingActivities2 = 0
    proceedsFromOperatingActivities2 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][17]
    try:
        proceedsFromOperatingActivities2 = int(proceedsFromOperatingActivities2)
    except Exception:
        proceedsFromOperatingActivities2 = 0
    changeInOperatingLiabilities2 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][17]
    try:
        changeInOperatingLiabilities2 = int(changeInOperatingLiabilities2)
    except Exception:
        changeInOperatingLiabilities2 = 0
    changeInOperatingAssets2 = quarterly_statementsDump.loc['changeInOperatingAssets'][17]
    try:
        changeInOperatingAssets2 = int(changeInOperatingAssets2)
    except Exception:
        changeInOperatingAssets2 = 0
    depreciationDepletionAndAmortization2 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][17]
    try:
        depreciationDepletionAndAmortization2 = int(depreciationDepletionAndAmortization2)
    except Exception:
        depreciationDepletionAndAmortization2 = 0
    capitalExpenditures2 = quarterly_statementsDump.loc['capitalExpenditures'][17]
    try:
        capitalExpenditures2 = int(capitalExpenditures2)
    except Exception:
        capitalExpenditures2 = 0
    changeInReceivables2 = quarterly_statementsDump.loc['changeInReceivables'][17]
    try:
        changeInReceivables2 = int(changeInReceivables2)
    except Exception:
        changeInReceivables2 = 0
    changeInInventory2 = quarterly_statementsDump.loc['changeInInventory'][17]
    try:
        changeInInventory2 = int(changeInInventory2)
    except Exception:
        changeInInventory2 = 0
    profitLoss2 = quarterly_statementsDump.loc['profitLoss'][17]
    try:
        profitLoss2 = int(profitLoss2)
    except Exception:
        profitLoss2 = 0
    cashflowFromInvestment2 = quarterly_statementsDump.loc['cashflowFromInvestment'][17]
    try:
        cashflowFromInvestment2 = int(cashflowFromInvestment2)
    except Exception:
        cashflowFromInvestment2 = 0
    cashflowFromFinancing2 = quarterly_statementsDump.loc['cashflowFromFinancing'][17]
    try:
        cashflowFromFinancing2 = int(cashflowFromFinancing2)
    except Exception:
        cashflowFromFinancing2 = 0
    proceedsFromRepaymentsOfShortTermDebt2 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][17]
    try:
        proceedsFromRepaymentsOfShortTermDebt2 = int(proceedsFromRepaymentsOfShortTermDebt2)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt2 = 0
    paymentsForRepurchaseOfCommonStock2 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][17]
    try:
        paymentsForRepurchaseOfCommonStock2 = int(paymentsForRepurchaseOfCommonStock2)
    except Exception:
        paymentsForRepurchaseOfCommonStock2 = 0
    paymentsForRepurchaseOfEquity2 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][17]
    try:
        paymentsForRepurchaseOfEquity2 = int(paymentsForRepurchaseOfEquity2)
    except Exception:
        paymentsForRepurchaseOfEquity2 = 0
    paymentsForRepurchaseOfPreferredStock2 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][17]
    try:
        paymentsForRepurchaseOfPreferredStock2 = int(paymentsForRepurchaseOfPreferredStock2)
    except Exception:
        paymentsForRepurchaseOfPreferredStock2 = 0
    dividendPayout2 = quarterly_statementsDump.loc['dividendPayout'][17]
    try:
        dividendPayout2 = int(dividendPayout2)
    except Exception:
        dividendPayout2 = 0
    dividendPayoutCommonStock2 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][17]
    try:
        dividendPayoutCommonStock2 = int(dividendPayoutCommonStock2)
    except Exception:
        dividendPayoutCommonStock2 = 0
    dividendPayoutPreferredStock2 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][17]
    try:
        dividendPayoutPreferredStock2 = int(dividendPayoutPreferredStock2)
    except Exception:
        dividendPayoutPreferredStock2 = 0
    proceedsFromIssuanceOfCommonStock2 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][17]
    try:
        proceedsFromIssuanceOfCommonStock2 = int(proceedsFromIssuanceOfCommonStock2)
    except Exception:
        proceedsFromIssuanceOfCommonStock2 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet2 = \
        quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][17]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet2 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet2)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet2 = 0
    proceedsFromIssuanceOfPreferredStock2 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][17]
    try:
        proceedsFromIssuanceOfPreferredStock2 = int(proceedsFromIssuanceOfPreferredStock2)
    except Exception:
        proceedsFromIssuanceOfPreferredStock2 = 0
    proceedsFromRepurchaseOfEquity2 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][17]
    try:
        proceedsFromRepurchaseOfEquity2 = int(proceedsFromRepurchaseOfEquity2)
    except Exception:
        proceedsFromRepurchaseOfEquity2 = 0
    proceedsFromSaleOfTreasuryStock2 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][17]
    try:
        proceedsFromSaleOfTreasuryStock2 = int(proceedsFromSaleOfTreasuryStock2)
    except Exception:
        proceedsFromSaleOfTreasuryStock2 = 0
    changeInCashAndCashEquivalents2 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][17]
    try:
        changeInCashAndCashEquivalents2 = int(changeInCashAndCashEquivalents2)
    except Exception:
        changeInCashAndCashEquivalents2 = 0
    changeInExchangeRate2 = quarterly_statementsDump.loc['changeInExchangeRate'][17]
    try:
        changeInExchangeRate2 = int(changeInExchangeRate2)
    except Exception:
        changeInExchangeRate2 = 0
    netIncome2 = quarterly_statementsDump.loc['netIncome'][17]
    try:
        netIncome2 = int(netIncome2)
    except Exception:
        netIncome2 = 0

    tTMnetIncome2 = (float(netIncome2) + float(netIncome3) + float(netIncome4) + float(netIncome5))
    try:
        tTMpreferredDivs2 = (int(dividendPayoutPreferredStock2) + int(dividendPayoutPreferredStock3) + int(
            dividendPayoutPreferredStock4) + int(dividendPayoutPreferredStock5))
    except Exception:
        tTMpreferredDivs2 = 0
    weightedAvgCommShrsOutstanding2 = (
                (float(commonStockSharesOutstanding2) + float(commonStockSharesOutstanding3) + float(
                    commonStockSharesOutstanding4) + float(commonStockSharesOutstanding5)) / 4)
    quoteUnformatted2 = quoteUnformatted
    marketCap2 = calculateMarketCap(quoteUnformatted2, commonStockSharesOutstanding2)
    basicEPS2 = calculateBasicEPS(tTMnetIncome2, tTMpreferredDivs2, weightedAvgCommShrsOutstanding2)
    pE2 = calculatePE(quoteUnformatted2, basicEPS2)
    pCF2 = calculatePriceToCashFlow(quoteUnformatted2,
                                    calculateOperatingCashFlowPerShare(operatingCashflow2,
                                                                       weightedAvgCommShrsOutstanding2))
    pS2 = calculatePS(quoteUnformatted2, calculateSalesPerShare(totalRevenue2, weightedAvgCommShrsOutstanding2))
    pB2 = calculatePB(quoteUnformatted2,
                      calculateMarketToBookValue(marketCap2, totalAssets2, shortLongTermDebtTotal2, preferredStock=0))
    sustainableGrowthRate2 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout2, netIncome2)),
        calculateROE(netIncome2, totalShareholderEquity2))
    pEGRatio2 = calculatePEGRatio(pE2, (sustainableGrowthRate2 * 200))
    earningsYield2 = calculateEarningsYield(basicEPS2, quoteUnformatted2)
    cashFlowPerShare2 = calculateOperatingCashFlowPerShare(operatingCashflow2, weightedAvgCommShrsOutstanding2)
    ebitdaPerShare2 = calculateEBITDAperShare(ebitda2, weightedAvgCommShrsOutstanding2)
    tTMDividendPayout2 = (
        (float(dividendPayout2) + float(dividendPayout3) + float(dividendPayout4) + float(dividendPayout5)))
    dividendsPerShare2 = calculateDividendsPerShare(tTMDividendPayout2, weightedAvgCommShrsOutstanding2)
    currentQuarterGrossProfitMargin2 = calculateGrossProfitMargin(totalRevenue2, costofGoodsAndServicesSold2)
    tTmTotalRevenue2 = ((float(totalRevenue2) + float(totalRevenue3) + float(totalRevenue4) + float(totalRevenue5)))
    tTmCOGS2 = ((float(costofGoodsAndServicesSold2) + float(costofGoodsAndServicesSold3) + float(
        costofGoodsAndServicesSold4) + float(costofGoodsAndServicesSold5)))
    tTMGrossProfitMargin2 = calculateGrossProfitMargin(tTmTotalRevenue2, tTmCOGS2)
    currentQuarterOperatingMargin2 = calculateOperatingMargin(operatingIncome2, totalRevenue2)
    tTMOperatingIncome2 = (
        (float(operatingIncome2) + float(operatingIncome3) + float(operatingIncome4) + float(operatingIncome5)))
    tTMOperatingMargin2 = calculateOperatingMargin(tTMOperatingIncome2, tTmTotalRevenue2)
    currentQuarterPreTaxMargin2 = calculatePreTaxMargin(calculateEBT(ebit2, interestExpense2), totalRevenue2)
    tTMebit2 = ((float(ebit2) + float(ebit3) + float(ebit4) + float(ebit5)))
    tTMInterestExpense2 = (
        (float(interestExpense2) + float(interestExpense3) + float(interestExpense4) + float(interestExpense5)))
    tTMPreTaxMargin2 = calculatePreTaxMargin(calculateEBT(tTMebit2, tTMInterestExpense2), tTmTotalRevenue2)
    currentQuarterNetProfitMargin2 = calculateNetProfitMargin(netIncome2, totalRevenue2)
    tTMNetProfitMargin2 = calculateNetProfitMargin(tTMnetIncome2, tTmTotalRevenue2)
    currentQuarterAvgTotalAssets2 = ((float(totalAssets2) + float(totalAssets3)) / 2)
    currentQuarterOperatingROA2 = (calculateOperatingROA(operatingIncome2, currentQuarterAvgTotalAssets2)) * 4
    tTMAvgTotalAssets2 = ((float(totalAssets2) + float(totalAssets3) + float(totalAssets4) + float(totalAssets5)) / 4)
    tTMOperatingROA2 = calculateOperatingROA(tTMOperatingIncome2, tTMAvgTotalAssets2)
    currentQuarterROA2 = (calculateROA(netIncome2, currentQuarterAvgTotalAssets2)) * 4
    tTMROA2 = calculateROA(tTMnetIncome2, tTMAvgTotalAssets2)
    currentQuarterReturnOnTotalCapital2 = (calculateReturnOnTotalCapital(ebit2, shortLongTermDebtTotal2,
                                                                         totalShareholderEquity2)) * 4
    tTMReturnOnTotalCapital2 = calculateReturnOnTotalCapital(tTMebit2, shortLongTermDebtTotal2, totalShareholderEquity2)
    currentQuarterROE2 = (calculateROE(netIncome2, totalShareholderEquity2)) * 4
    tTMROE2 = calculateROE(tTMnetIncome2, totalShareholderEquity2)
    currentQuarterAvgCommonEquity2 = ((float(totalShareholderEquity2) + float(totalShareholderEquity3)) / 2)
    currentQuarterReturnOnCommonEquity2 = (calculateReturnOnCommonEquity(netIncome2, dividendPayoutPreferredStock2,
                                                                         currentQuarterAvgCommonEquity2)) * 4
    tTMAvgCommonEquity2 = ((float(totalShareholderEquity2) + float(totalShareholderEquity3) + float(
        totalShareholderEquity4) + float(totalShareholderEquity5)) / 4)
    tTMReturnOnCommonEquity2 = calculateReturnOnCommonEquity(tTMnetIncome2, tTMpreferredDivs2, tTMAvgCommonEquity2)
    debtRatio2 = calculateDebtRatio(totalLiabilities2, totalAssets2)
    debtToEquityRatio2 = calculateDebtToEquity(shortLongTermDebtTotal2, totalShareholderEquity2)
    debtToAssetRatio2 = calculateDebtToAssetRatio(shortLongTermDebtTotal2, totalAssets2)
    debtToCapitalRatio2 = calculateDebtToCapitalRatio(shortLongTermDebtTotal2, totalShareholderEquity2)

    financialLeverage2 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets2, currentQuarterAvgCommonEquity2)
    interestCoverage2 = calculateInterestCoverageRatio(operatingCashflow2, interestExpense2, incomeTaxExpense2)
    fixedChargeCoverageRatio2 = calculateFixedChargeCoverage(ebit2, capitalLeaseObligations2, interestExpense2)

    ## tm1  VARIABLES
    # Income Statement Variables for tm1
    gross_profit1 = quarterly_statementsDump.loc['grossProfit'][18]
    try:
        gross_profit1 = int(gross_profit1)
    except Exception:
        gross_profit1 = 0
    totalRevenue1 = quarterly_statementsDump.loc['totalRevenue'][18]
    try:
        totalRevenue1 = int(totalRevenue1)
    except Exception:
        totalRevenue1 = 0
    costOfRevenue1 = quarterly_statementsDump.loc['costOfRevenue'][18]
    try:
        costOfRevenue1 = int(costOfRevenue1)
    except Exception:
        costOfRevenue1 = 0
    costofGoodsAndServicesSold1 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][18]
    try:
        costofGoodsAndServicesSold1 = int(costofGoodsAndServicesSold1)
    except Exception:
        costofGoodsAndServicesSold1 = 0
    operatingIncome1 = quarterly_statementsDump.loc['operatingIncome'][18]
    try:
        operatingIncome1 = int(operatingIncome1)
    except Exception:
        operatingIncome1 = 0
    sellingGeneralAndAdministrative1 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][18]
    try:
        sellingGeneralAndAdministrative1 = int(sellingGeneralAndAdministrative1)
    except Exception:
        sellingGeneralAndAdministrative1 = 0
    researchAndDevelopment1 = quarterly_statementsDump.loc['researchAndDevelopment'][18]
    try:
        researchAndDevelopment1 = int(researchAndDevelopment1)
    except Exception:
        researchAndDevelopment1 = 0
    operatingExpenses1 = quarterly_statementsDump.loc['operatingExpenses'][18]
    try:
        operatingExpenses1 = int(operatingExpenses1)
    except Exception:
        operatingExpenses1 = 0
    investmentIncomeNet1 = quarterly_statementsDump.loc['investmentIncomeNet'][18]
    try:
        investmentIncomeNet1 = int(investmentIncomeNet1)
    except Exception:
        investmentIncomeNet1 = 0

    netInterestIncome1 = quarterly_statementsDump.loc['netInterestIncome'][18]
    try:
        netInterestIncome1 = int(netInterestIncome1)
    except Exception:
        netInterestIncome1 = 0
    interestIncome1 = quarterly_statementsDump.loc['interestIncome'][18]
    try:
        interestIncome1 = int(interestIncome1)
    except Exception:
        interestIncome1 = 0
    interestExpense1 = quarterly_statementsDump.loc['interestExpense'][18]
    try:
        interestExpense1 = int(interestExpense1)
    except Exception:
        interestExpense1 = 0
    nonInterestIncome1 = quarterly_statementsDump.loc['nonInterestIncome'][18]
    try:
        nonInterestIncome1 = int(nonInterestIncome1)
    except Exception:
        nonInterestIncome1 = 0
    otherNonOperatingIncome1 = quarterly_statementsDump.loc['otherNonOperatingIncome'][18]
    try:
        otherNonOperatingIncome1 = int(otherNonOperatingIncome1)
    except Exception:
        otherNonOperatingIncome1 = 0
    depreciation1 = quarterly_statementsDump.loc['depreciation'][18]
    try:
        depreciation1 = int(depreciation1)
    except Exception:
        depreciation1 = 0
    depreciationAndAmortization1 = quarterly_statementsDump.loc['depreciationAndAmortization'][18]
    try:
        depreciationAndAmortization1 = int(depreciationAndAmortization1)
    except Exception:
        depreciationAndAmortization1 = 0

    incomeBeforeTax1 = quarterly_statementsDump.loc['incomeBeforeTax'][18]
    try:
        incomeBeforeTax1 = int(incomeBeforeTax1)
    except Exception:
        incomeBeforeTax1 = 0

    incomeTaxExpense1 = quarterly_statementsDump.loc['incomeTaxExpense'][18]
    try:
        incomeTaxExpense1 = int(incomeTaxExpense1)
    except Exception:
        incomeTaxExpense1 = 0
    interestAndDebtExpense1 = quarterly_statementsDump.loc['interestAndDebtExpense'][18]
    try:
        interestAndDebtExpense1 = int(interestAndDebtExpense1)
    except Exception:
        interestAndDebtExpense1 = 0
    netIncomeFromContinuingOperations1 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][18]
    try:
        netIncomeFromContinuingOperations1 = int(netIncomeFromContinuingOperations1)
    except Exception:
        netIncomeFromContinuingOperations1 = 0
    comprehensiveIncomeNetOfTax1 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][18]
    try:
        comprehensiveIncomeNetOfTax1 = int(comprehensiveIncomeNetOfTax1)
    except Exception:
        comprehensiveIncomeNetOfTax1 = 0
    ebit1 = quarterly_statementsDump.loc['ebit'][18]
    try:
        ebit1 = int(ebit1)
    except Exception:
        ebit1 = 0
    ebitda1 = quarterly_statementsDump.loc['ebitda'][18]
    try:
        ebitda1 = int(ebitda1)
    except Exception:
        ebitda1 = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 18]

    # Balance Sheet Values for tm1

    totalAssets1 = quarterly_statementsDump.loc['totalAssets'][18]
    try:
        totalAssets1 = int(totalAssets1)
    except Exception:
        totalAssets1 = 0
    totalCurrentAssets1 = quarterly_statementsDump.loc['totalCurrentAssets'][18]
    try:
        totalCurrentAssets1 = int(totalCurrentAssets1)
    except Exception:
        totalCurrentAssets1 = 0
    cashAndCashEquivalentsAtCarryingValue1 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][18]
    try:
        cashAndCashEquivalentsAtCarryingValue1 = int(cashAndCashEquivalentsAtCarryingValue1)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue1 = 0
    cashAndShortTermInvestments1 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][18]
    try:
        cashAndShortTermInvestments1 = int(cashAndShortTermInvestments1)
    except Exception:
        cashAndShortTermInvestments1 = 0
    inventory1 = quarterly_statementsDump.loc['inventory'][18]
    try:
        inventory1 = int(inventory1)
    except Exception:
        inventory1 = 0
    currentNetReceivables1 = quarterly_statementsDump.loc['currentNetReceivables'][18]
    try:
        currentNetReceivables1 = int(currentNetReceivables1)
    except Exception:
        currentNetReceivables1 = 0
    totalNonCurrentAssets1 = quarterly_statementsDump.loc['totalNonCurrentAssets'][18]
    try:
        totalNonCurrentAssets1 = int(totalNonCurrentAssets1)
    except Exception:
        totalNonCurrentAssets1 = 0
    propertyPlantEquipment1 = quarterly_statementsDump.loc['propertyPlantEquipment'][18]
    try:
        propertyPlantEquipment1 = int(propertyPlantEquipment1)
    except Exception:
        propertyPlantEquipment1 = 0
    accumulatedDepreciationAmortizationPPE1 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][18]
    try:
        accumulatedDepreciationAmortizationPPE1 = int(accumulatedDepreciationAmortizationPPE1)
    except Exception:
        accumulatedDepreciationAmortizationPPE1 = 0
    intangibleAssets1 = quarterly_statementsDump.loc['intangibleAssets'][18]
    try:
        intangibleAssets1 = int(intangibleAssets1)
    except Exception:
        intangibleAssets1 = 0
    intangibleAssetsExcludingGoodwill1 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][18]
    try:
        intangibleAssetsExcludingGoodwill1 = int(intangibleAssetsExcludingGoodwill1)
    except Exception:
        intangibleAssetsExcludingGoodwill1 = 0
    goodwill1 = quarterly_statementsDump.loc['goodwill'][18]
    try:
        goodwill1 = int(goodwill1)
    except Exception:
        goodwill1 = 0
    investments1 = quarterly_statementsDump.loc['investments'][18]
    try:
        investments1 = int(investments1)
    except Exception:
        investments1 = 0
    longTermInvestments1 = quarterly_statementsDump.loc['longTermInvestments'][18]
    try:
        longTermInvestments1 = int(longTermInvestments1)
    except Exception:
        longTermInvestments1 = 0
    shortTermInvestments1 = quarterly_statementsDump.loc['shortTermInvestments'][18]
    try:
        shortTermInvestments1 = int(shortTermInvestments1)
    except Exception:
        shortTermInvestments1 = 0
    otherCurrentAssets1 = quarterly_statementsDump.loc['otherCurrentAssets'][18]
    try:
        otherCurrentAssets1 = int(otherCurrentAssets1)
    except Exception:
        otherCurrentAssets1 = 0
    otherNonCurrrentAssets1 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][18]
    try:
        otherNonCurrrentAssets1 = int(otherNonCurrrentAssets1)
    except Exception:
        otherNonCurrrentAssets1 = 0
    totalLiabilities1 = quarterly_statementsDump.loc['totalLiabilities'][18]
    try:
        totalLiabilities1 = int(totalLiabilities1)
    except Exception:
        totalLiabilities1 = 0
    totalCurrentLiabilities1 = quarterly_statementsDump.loc['totalCurrentLiabilities'][18]
    try:
        totalCurrentLiabilities1 = int(totalCurrentLiabilities1)
    except Exception:
        totalCurrentLiabilities1 = 0
    currentAccountsPayable1 = quarterly_statementsDump.loc['currentAccountsPayable'][18]
    try:
        currentAccountsPayable1 = int(currentAccountsPayable1)
    except Exception:
        currentAccountsPayable1 = 0
    deferredRevenue1 = quarterly_statementsDump.loc['deferredRevenue'][18]
    try:
        deferredRevenue1 = int(deferredRevenue1)
    except Exception:
        deferredRevenue1 = 0
    currentDebt1 = quarterly_statementsDump.loc['currentDebt'][18]
    try:
        currentDebt1 = int(currentDebt1)
    except Exception:
        currentDebt1 = 0
    shortTermDebt1 = quarterly_statementsDump.loc['shortTermDebt'][18]
    try:
        shortTermDebt1 = int(shortTermDebt1)
    except Exception:
        shortTermDebt1 = 0
    totalNonCurrentLiabilities1 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][18]
    try:
        totalNonCurrentLiabilities1 = int(totalNonCurrentLiabilities1)
    except Exception:
        totalNonCurrentLiabilities1 = 0
    capitalLeaseObligations1 = quarterly_statementsDump.loc['capitalLeaseObligations'][18]
    try:
        capitalLeaseObligations1 = int(capitalLeaseObligations1)
    except Exception:
        capitalLeaseObligations1 = 0

    longTermDebt1 = quarterly_statementsDump.loc['longTermDebt'][18]
    try:
        longTermDebt1 = int(longTermDebt1)
    except Exception:
        longTermDebt1 = 0
    currentLongTermDebt1 = quarterly_statementsDump.loc['currentLongTermDebt'][18]
    try:
        currentLongTermDebt1 = int(currentLongTermDebt1)
    except Exception:
        currentLongTermDebt1 = 0
    longTermDebtNoncurrent1 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][18]
    try:
        longTermDebtNoncurrent1 = int(longTermDebtNoncurrent1)
    except Exception:
        longTermDebtNoncurrent1 = 0
    shortLongTermDebtTotal1 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][18]
    try:
        shortLongTermDebtTotal1 = int(shortLongTermDebtTotal1)
    except Exception:
        shortLongTermDebtTotal1 = 0
    otherCurrentLiabilities1 = quarterly_statementsDump.loc['otherCurrentLiabilities'][18]
    try:
        otherCurrentLiabilities1 = int(otherCurrentLiabilities1)
    except Exception:
        otherCurrentLiabilities1 = 0
    otherNonCurrentLiabilities1 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][18]
    try:
        otherNonCurrentLiabilities1 = int(otherNonCurrentLiabilities1)
    except Exception:
        otherNonCurrentLiabilities1 = 0
    totalShareholderEquity1 = quarterly_statementsDump.loc['totalShareholderEquity'][18]
    try:
        totalShareholderEquity1 = int(totalShareholderEquity1)
    except Exception:
        totalShareholderEquity1 = 0
    treasuryStock1 = quarterly_statementsDump.loc['treasuryStock'][18]
    try:
        treasuryStock1 = int(treasuryStock1)
    except Exception:
        treasuryStock1 = 0
    retainedEarnings1 = quarterly_statementsDump.loc['retainedEarnings'][18]
    try:
        retainedEarnings1 = int(retainedEarnings1)
    except Exception:
        retainedEarnings1 = 0
    commonStock1 = quarterly_statementsDump.loc['commonStock'][18]
    try:
        commonStock1 = int(commonStock1)
    except Exception:
        commonStock1 = 0
    commonStockSharesOutstanding1 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][18]
    try:
        commonStockSharesOutstanding1 = int(commonStockSharesOutstanding1)
    except Exception:
        commonStockSharesOutstanding1 = 0
    # Cash-Flow Statement values for tm1
    operatingCashflow1 = quarterly_statementsDump.loc['operatingCashflow'][18]
    try:
        operatingCashflow1 = int(operatingCashflow1)
    except Exception:
        operatingCashflow1 = 0
    paymentsForOperatingActivities1 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][18]
    try:
        paymentsForOperatingActivities1 = int(paymentsForOperatingActivities1)
    except Exception:
        paymentsForOperatingActivities1 = 0
    proceedsFromOperatingActivities1 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][18]
    try:
        proceedsFromOperatingActivities1 = int(proceedsFromOperatingActivities1)
    except Exception:
        proceedsFromOperatingActivities1 = 0
    changeInOperatingLiabilities1 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][18]
    try:
        changeInOperatingLiabilities1 = int(changeInOperatingLiabilities1)
    except Exception:
        changeInOperatingLiabilities1 = 0
    changeInOperatingAssets1 = quarterly_statementsDump.loc['changeInOperatingAssets'][18]
    try:
        changeInOperatingAssets1 = int(changeInOperatingAssets1)
    except Exception:
        changeInOperatingAssets1 = 0
    depreciationDepletionAndAmortization1 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][18]
    try:
        depreciationDepletionAndAmortization1 = int(depreciationDepletionAndAmortization1)
    except Exception:
        depreciationDepletionAndAmortization1 = 0
    capitalExpenditures1 = quarterly_statementsDump.loc['capitalExpenditures'][18]
    try:
        capitalExpenditures1 = int(capitalExpenditures1)
    except Exception:
        capitalExpenditures1 = 0
    changeInReceivables1 = quarterly_statementsDump.loc['changeInReceivables'][18]
    try:
        changeInReceivables1 = int(changeInReceivables1)
    except Exception:
        changeInReceivables1 = 0
    changeInInventory1 = quarterly_statementsDump.loc['changeInInventory'][18]
    try:
        changeInInventory1 = int(changeInInventory1)
    except Exception:
        changeInInventory1 = 0
    profitLoss1 = quarterly_statementsDump.loc['profitLoss'][18]
    try:
        profitLoss1 = int(profitLoss1)
    except Exception:
        profitLoss1 = 0
    cashflowFromInvestment1 = quarterly_statementsDump.loc['cashflowFromInvestment'][18]
    try:
        cashflowFromInvestment1 = int(cashflowFromInvestment1)
    except Exception:
        cashflowFromInvestment1 = 0
    cashflowFromFinancing1 = quarterly_statementsDump.loc['cashflowFromFinancing'][18]
    try:
        cashflowFromFinancing1 = int(cashflowFromFinancing1)
    except Exception:
        cashflowFromFinancing1 = 0
    proceedsFromRepaymentsOfShortTermDebt1 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][18]
    try:
        proceedsFromRepaymentsOfShortTermDebt1 = int(proceedsFromRepaymentsOfShortTermDebt1)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt1 = 0
    paymentsForRepurchaseOfCommonStock1 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][18]
    try:
        paymentsForRepurchaseOfCommonStock1 = int(paymentsForRepurchaseOfCommonStock1)
    except Exception:
        paymentsForRepurchaseOfCommonStock1 = 0
    paymentsForRepurchaseOfEquity1 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][18]
    try:
        paymentsForRepurchaseOfEquity1 = int(paymentsForRepurchaseOfEquity1)
    except Exception:
        paymentsForRepurchaseOfEquity1 = 0
    paymentsForRepurchaseOfPreferredStock1 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][18]
    try:
        paymentsForRepurchaseOfPreferredStock1 = int(paymentsForRepurchaseOfPreferredStock1)
    except Exception:
        paymentsForRepurchaseOfPreferredStock1 = 0
    dividendPayout1 = quarterly_statementsDump.loc['dividendPayout'][18]
    try:
        dividendPayout1 = int(dividendPayout1)
    except Exception:
        dividendPayout1 = 0
    dividendPayoutCommonStock1 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][18]
    try:
        dividendPayoutCommonStock1 = int(dividendPayoutCommonStock1)
    except Exception:
        dividendPayoutCommonStock1 = 0
    dividendPayoutPreferredStock1 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][18]
    try:
        dividendPayoutPreferredStock1 = int(dividendPayoutPreferredStock1)
    except Exception:
        dividendPayoutPreferredStock1 = 0
    proceedsFromIssuanceOfCommonStock1 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][18]
    try:
        proceedsFromIssuanceOfCommonStock1 = int(proceedsFromIssuanceOfCommonStock1)
    except Exception:
        proceedsFromIssuanceOfCommonStock1 = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet1 = \
    quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][18]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet1 = int(
            proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet1)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet1 = 0
    proceedsFromIssuanceOfPreferredStock1 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][18]
    try:
        proceedsFromIssuanceOfPreferredStock1 = int(proceedsFromIssuanceOfPreferredStock1)
    except Exception:
        proceedsFromIssuanceOfPreferredStock1 = 0
    proceedsFromRepurchaseOfEquity1 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][18]
    try:
        proceedsFromRepurchaseOfEquity1 = int(proceedsFromRepurchaseOfEquity1)
    except Exception:
        proceedsFromRepurchaseOfEquity1 = 0
    proceedsFromSaleOfTreasuryStock1 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][18]
    try:
        proceedsFromSaleOfTreasuryStock1 = int(proceedsFromSaleOfTreasuryStock1)
    except Exception:
        proceedsFromSaleOfTreasuryStock1 = 0
    changeInCashAndCashEquivalents1 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][18]
    try:
        changeInCashAndCashEquivalents1 = int(changeInCashAndCashEquivalents1)
    except Exception:
        changeInCashAndCashEquivalents1 = 0
    changeInExchangeRate1 = quarterly_statementsDump.loc['changeInExchangeRate'][18]
    try:
        changeInExchangeRate1 = int(changeInExchangeRate1)
    except Exception:
        changeInExchangeRate1 = 0
    netIncome1 = quarterly_statementsDump.loc['netIncome'][18]
    try:
        netIncome1 = int(netIncome1)
    except Exception:
        netIncome1 = 0

    tTMnetIncome1 = (float(netIncome1) + float(netIncome2) + float(netIncome3) + float(netIncome4))
    try:
        tTMpreferredDivs1 = (int(dividendPayoutPreferredStock1) + int(dividendPayoutPreferredStock2) + int(
            dividendPayoutPreferredStock3) + int(dividendPayoutPreferredStock4))
    except Exception:
        tTMpreferredDivs1 = 0
    weightedAvgCommShrsOutstanding1 = ((float(commonStockSharesOutstanding1) + float(
        commonStockSharesOutstanding2) + float(commonStockSharesOutstanding3) + float(
        commonStockSharesOutstanding4)) / 4)
    quoteUnformatted1 = quoteUnformatted
    marketCap1 = calculateMarketCap(quoteUnformatted1, commonStockSharesOutstanding1)
    basicEPS1 = calculateBasicEPS(tTMnetIncome1, tTMpreferredDivs1, weightedAvgCommShrsOutstanding1)
    pE1 = calculatePE(quoteUnformatted1, basicEPS1)
    pCF1 = calculatePriceToCashFlow(quoteUnformatted1, calculateOperatingCashFlowPerShare(operatingCashflow1,
                                                                                          weightedAvgCommShrsOutstanding1))
    pS1 = calculatePS(quoteUnformatted1, calculateSalesPerShare(totalRevenue1, weightedAvgCommShrsOutstanding1))
    pB1 = calculatePB(quoteUnformatted1,
                      calculateMarketToBookValue(marketCap1, totalAssets1, shortLongTermDebtTotal1, preferredStock=0))
    sustainableGrowthRate1 = calculateSustainableGrowthRate(
        calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout1, netIncome1)),
        calculateROE(netIncome1, totalShareholderEquity1))
    pEGRatio1 = calculatePEGRatio(pE1, (sustainableGrowthRate1 * 100))
    earningsYield1 = calculateEarningsYield(basicEPS1, quoteUnformatted1)
    cashFlowPerShare1 = calculateOperatingCashFlowPerShare(operatingCashflow1, weightedAvgCommShrsOutstanding1)
    ebitdaPerShare1 = calculateEBITDAperShare(ebitda1, weightedAvgCommShrsOutstanding1)
    tTMDividendPayout1 = (
    (float(dividendPayout1) + float(dividendPayout2) + float(dividendPayout3) + float(dividendPayout4)))
    dividendsPerShare1 = calculateDividendsPerShare(tTMDividendPayout1, weightedAvgCommShrsOutstanding1)
    currentQuarterGrossProfitMargin1 = calculateGrossProfitMargin(totalRevenue1, costofGoodsAndServicesSold1)
    tTmTotalRevenue1 = ((float(totalRevenue1) + float(totalRevenue2) + float(totalRevenue3) + float(totalRevenue4)))
    tTmCOGS1 = ((float(costofGoodsAndServicesSold1) + float(costofGoodsAndServicesSold2) + float(
        costofGoodsAndServicesSold3) + float(costofGoodsAndServicesSold4)))
    tTMGrossProfitMargin1 = calculateGrossProfitMargin(tTmTotalRevenue1, tTmCOGS1)
    currentQuarterOperatingMargin1 = calculateOperatingMargin(operatingIncome1, totalRevenue1)
    tTMOperatingIncome1 = (
    (float(operatingIncome1) + float(operatingIncome2) + float(operatingIncome3) + float(operatingIncome4)))
    tTMOperatingMargin1 = calculateOperatingMargin(tTMOperatingIncome1, tTmTotalRevenue1)
    currentQuarterPreTaxMargin1 = calculatePreTaxMargin(calculateEBT(ebit1, interestExpense1), totalRevenue1)
    tTMebit1 = ((float(ebit1) + float(ebit2) + float(ebit3) + float(ebit4)))
    tTMInterestExpense1 = (
    (float(interestExpense1) + float(interestExpense2) + float(interestExpense3) + float(interestExpense4)))
    tTMPreTaxMargin1 = calculatePreTaxMargin(calculateEBT(tTMebit1, tTMInterestExpense1), tTmTotalRevenue1)
    currentQuarterNetProfitMargin1 = calculateNetProfitMargin(netIncome1, totalRevenue1)
    tTMNetProfitMargin1 = calculateNetProfitMargin(tTMnetIncome1, tTmTotalRevenue1)
    currentQuarterAvgTotalAssets1 = ((float(totalAssets1) + float(totalAssets2)) / 2)
    currentQuarterOperatingROA1 = (calculateOperatingROA(operatingIncome1, currentQuarterAvgTotalAssets1)) * 4
    tTMAvgTotalAssets1 = ((float(totalAssets1) + float(totalAssets2) + float(totalAssets3) + float(totalAssets4)) / 4)
    tTMOperatingROA1 = calculateOperatingROA(tTMOperatingIncome1, tTMAvgTotalAssets1)
    currentQuarterROA1 = (calculateROA(netIncome1, currentQuarterAvgTotalAssets1)) * 4
    tTMROA1 = calculateROA(tTMnetIncome1, tTMAvgTotalAssets1)
    currentQuarterReturnOnTotalCapital1 = (calculateReturnOnTotalCapital(ebit1, shortLongTermDebtTotal1,
                                                                         totalShareholderEquity1)) * 4
    tTMReturnOnTotalCapital1 = calculateReturnOnTotalCapital(tTMebit1, shortLongTermDebtTotal1, totalShareholderEquity1)
    currentQuarterROE1 = (calculateROE(netIncome1, totalShareholderEquity1)) * 4
    tTMROE1 = calculateROE(tTMnetIncome1, totalShareholderEquity1)
    currentQuarterAvgCommonEquity1 = ((float(totalShareholderEquity1) + float(totalShareholderEquity2)) / 2)
    currentQuarterReturnOnCommonEquity1 = (calculateReturnOnCommonEquity(netIncome1, dividendPayoutPreferredStock1,
                                                                         currentQuarterAvgCommonEquity1)) * 4
    tTMAvgCommonEquity1 = ((float(totalShareholderEquity1) + float(totalShareholderEquity2) + float(
        totalShareholderEquity3) + float(totalShareholderEquity4)) / 4)
    tTMReturnOnCommonEquity1 = calculateReturnOnCommonEquity(tTMnetIncome1, tTMpreferredDivs1, tTMAvgCommonEquity1)
    debtRatio1 = calculateDebtRatio(totalLiabilities1, totalAssets1)
    debtToEquityRatio1 = calculateDebtToEquity(shortLongTermDebtTotal1, totalShareholderEquity1)
    debtToAssetRatio1 = calculateDebtToAssetRatio(shortLongTermDebtTotal1, totalAssets1)
    debtToCapitalRatio1 = calculateDebtToCapitalRatio(shortLongTermDebtTotal1, totalShareholderEquity1)

    financialLeverage1 = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets1, currentQuarterAvgCommonEquity1)
    interestCoverage1 = calculateInterestCoverageRatio(operatingCashflow1, interestExpense1, incomeTaxExpense1)
    fixedChargeCoverageRatio1 = calculateFixedChargeCoverage(ebit1, capitalLeaseObligations1, interestExpense1)


    print('------------------------------------------------------------------------------------------------')
    ## Current Time T  VARIABLES
    # Income Statement Variables for t
    gross_profit = quarterly_statementsDump.loc['grossProfit'][19]
    try:
        gross_profit = int(gross_profit)
    except Exception:
        gross_profit = 0
    totalRevenue = quarterly_statementsDump.loc['totalRevenue'][19]
    try:
        totalRevenue = int(totalRevenue)
    except Exception:
        totalRevenue = 0
    costOfRevenue = quarterly_statementsDump.loc['costOfRevenue'][19]
    try:
        costOfRevenue = int(costOfRevenue)
    except Exception:
        costOfRevenue = 0
    costofGoodsAndServicesSold = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][19]
    try:
        costofGoodsAndServicesSold = int(costofGoodsAndServicesSold)
    except Exception:
        costofGoodsAndServicesSold = 0
    operatingIncome = quarterly_statementsDump.loc['operatingIncome'][19]
    try:
        operatingIncome = int(operatingIncome)
    except Exception:
        operatingIncome = 0
    sellingGeneralAndAdministrative = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][19]
    try:
        sellingGeneralAndAdministrative = int(sellingGeneralAndAdministrative)
    except Exception:
        sellingGeneralAndAdministrative = 0
    researchAndDevelopment = quarterly_statementsDump.loc['researchAndDevelopment'][19]
    try:
        researchAndDevelopment = int(researchAndDevelopment)
    except Exception:
        researchAndDevelopment = 0
    operatingExpenses = quarterly_statementsDump.loc['operatingExpenses'][19]
    try:
        operatingExpenses = int(operatingExpenses)
    except Exception:
        operatingExpenses = 0
    investmentIncomeNet = quarterly_statementsDump.loc['investmentIncomeNet'][19]
    try:
        investmentIncomeNet = int(investmentIncomeNet)
    except Exception:
        investmentIncomeNet = 0

    netInterestIncome = quarterly_statementsDump.loc['netInterestIncome'][19]
    try:
        netInterestIncome = int(netInterestIncome)
    except Exception:
        netInterestIncome = 0
    interestIncome = quarterly_statementsDump.loc['interestIncome'][19]
    try:
        interestIncome = int(interestIncome)
    except Exception:
        interestIncome = 0
    interestExpense = quarterly_statementsDump.loc['interestExpense'][19]
    try:
        interestExpense = int(interestExpense)
    except Exception:
        interestExpense = 0
    nonInterestIncome = quarterly_statementsDump.loc['nonInterestIncome'][19]
    try:
        nonInterestIncome = int(nonInterestIncome)
    except Exception:
        nonInterestIncome = 0
    otherNonOperatingIncome = quarterly_statementsDump.loc['otherNonOperatingIncome'][19]
    try:
        otherNonOperatingIncome = int(otherNonOperatingIncome)
    except Exception:
        otherNonOperatingIncome = 0
    depreciation = quarterly_statementsDump.loc['depreciation'][19]
    try:
        depreciation = int(depreciation)
    except Exception:
        depreciation = 0
    depreciationAndAmortization = quarterly_statementsDump.loc['depreciationAndAmortization'][19]
    try:
        depreciationAndAmortization = int(depreciationAndAmortization)
    except Exception:
        depreciationAndAmortization = 0

    incomeBeforeTax = quarterly_statementsDump.loc['incomeBeforeTax'][19]
    try:
        incomeBeforeTax = int(incomeBeforeTax)
    except Exception:
        incomeBeforeTax = 0

    incomeTaxExpense = quarterly_statementsDump.loc['incomeTaxExpense'][19]
    try:
        incomeTaxExpense = int(incomeTaxExpense)
    except Exception:
        incomeTaxExpense = 0
    interestAndDebtExpense = quarterly_statementsDump.loc['interestAndDebtExpense'][19]
    try:
        interestAndDebtExpense = int(interestAndDebtExpense)
    except Exception:
        interestAndDebtExpense = 0
    netIncomeFromContinuingOperations = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][19]
    try:
        netIncomeFromContinuingOperations = int(netIncomeFromContinuingOperations)
    except Exception:
        netIncomeFromContinuingOperations = 0
    comprehensiveIncomeNetOfTax = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][19]
    try:
        comprehensiveIncomeNetOfTax = int(comprehensiveIncomeNetOfTax)
    except Exception:
        comprehensiveIncomeNetOfTax = 0
    ebit = quarterly_statementsDump.loc['ebit'][19]
    try:
        ebit = int(ebit)
    except Exception:
        ebit = 0
    ebitda = quarterly_statementsDump.loc['ebitda'][19]
    try:
        ebitda = int(ebitda)
    except Exception:
        ebitda = 0
    # netIncome  = quarterly_statementsDump.loc['netIncome'][ 19]

    # Balance Sheet Values for tm

    totalAssets = quarterly_statementsDump.loc['totalAssets'][19]
    try:
        totalAssets = int(totalAssets)
    except Exception:
        totalAssets = 0
    totalCurrentAssets = quarterly_statementsDump.loc['totalCurrentAssets'][19]
    try:
        totalCurrentAssets = int(totalCurrentAssets)
    except Exception:
        totalCurrentAssets = 0
    cashAndCashEquivalentsAtCarryingValue = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][19]
    try:
        cashAndCashEquivalentsAtCarryingValue = int(cashAndCashEquivalentsAtCarryingValue)
    except Exception:
        cashAndCashEquivalentsAtCarryingValue = 0
    cashAndShortTermInvestments = quarterly_statementsDump.loc['cashAndShortTermInvestments'][19]
    try:
        cashAndShortTermInvestments = int(cashAndShortTermInvestments)
    except Exception:
        cashAndShortTermInvestments = 0
    inventory = quarterly_statementsDump.loc['inventory'][19]
    try:
        inventory = int(inventory)
    except Exception:
        inventory = 0
    currentNetReceivables = quarterly_statementsDump.loc['currentNetReceivables'][19]
    try:
        currentNetReceivables = int(currentNetReceivables)
    except Exception:
        currentNetReceivables = 0
    totalNonCurrentAssets = quarterly_statementsDump.loc['totalNonCurrentAssets'][19]
    try:
        totalNonCurrentAssets = int(totalNonCurrentAssets)
    except Exception:
        totalNonCurrentAssets = 0
    propertyPlantEquipment = quarterly_statementsDump.loc['propertyPlantEquipment'][19]
    try:
        propertyPlantEquipment = int(propertyPlantEquipment)
    except Exception:
        propertyPlantEquipment = 0
    accumulatedDepreciationAmortizationPPE = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][19]
    try:
        accumulatedDepreciationAmortizationPPE = int(accumulatedDepreciationAmortizationPPE)
    except Exception:
        accumulatedDepreciationAmortizationPPE = 0
    intangibleAssets = quarterly_statementsDump.loc['intangibleAssets'][19]
    try:
        intangibleAssets = int(intangibleAssets)
    except Exception:
        intangibleAssets = 0
    intangibleAssetsExcludingGoodwill = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][19]
    try:
        intangibleAssetsExcludingGoodwill = int(intangibleAssetsExcludingGoodwill)
    except Exception:
        intangibleAssetsExcludingGoodwill = 0
    goodwill = quarterly_statementsDump.loc['goodwill'][19]
    try:
        goodwill = int(goodwill)
    except Exception:
        goodwill = 0
    investments = quarterly_statementsDump.loc['investments'][19]
    try:
        investments = int(investments)
    except Exception:
        investments = 0
    longTermInvestments = quarterly_statementsDump.loc['longTermInvestments'][19]
    try:
        longTermInvestments = int(longTermInvestments)
    except Exception:
        longTermInvestments = 0
    shortTermInvestments = quarterly_statementsDump.loc['shortTermInvestments'][19]
    try:
        shortTermInvestments = int(shortTermInvestments)
    except Exception:
        shortTermInvestments = 0
    otherCurrentAssets = quarterly_statementsDump.loc['otherCurrentAssets'][19]
    try:
        otherCurrentAssets = int(otherCurrentAssets)
    except Exception:
        otherCurrentAssets = 0
    otherNonCurrrentAssets = quarterly_statementsDump.loc['otherNonCurrrentAssets'][19]
    try:
        otherNonCurrrentAssets = int(otherNonCurrrentAssets)
    except Exception:
        otherNonCurrrentAssets = 0
    totalLiabilities = quarterly_statementsDump.loc['totalLiabilities'][19]
    try:
        totalLiabilities = int(totalLiabilities)
    except Exception:
        totalLiabilities = 0
    totalCurrentLiabilities = quarterly_statementsDump.loc['totalCurrentLiabilities'][19]
    try:
        totalCurrentLiabilities = int(totalCurrentLiabilities)
    except Exception:
        totalCurrentLiabilities = 0
    currentAccountsPayable = quarterly_statementsDump.loc['currentAccountsPayable'][19]
    try:
        currentAccountsPayable = int(currentAccountsPayable)
    except Exception:
        currentAccountsPayable = 0
    deferredRevenue = quarterly_statementsDump.loc['deferredRevenue'][19]
    try:
        deferredRevenue = int(deferredRevenue)
    except Exception:
        deferredRevenue = 0
    currentDebt = quarterly_statementsDump.loc['currentDebt'][19]
    try:
        currentDebt = int(currentDebt)
    except Exception:
        currentDebt = 0
    shortTermDebt = quarterly_statementsDump.loc['shortTermDebt'][19]
    try:
        shortTermDebt = int(shortTermDebt)
    except Exception:
        shortTermDebt = 0
    totalNonCurrentLiabilities = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][19]
    try:
        totalNonCurrentLiabilities = int(totalNonCurrentLiabilities)
    except Exception:
        totalNonCurrentLiabilities = 0
    capitalLeaseObligations = quarterly_statementsDump.loc['capitalLeaseObligations'][19]
    try:
        capitalLeaseObligations = int(capitalLeaseObligations)
    except Exception:
        capitalLeaseObligations = 0

    longTermDebt = quarterly_statementsDump.loc['longTermDebt'][19]
    try:
        longTermDebt = int(longTermDebt)
    except Exception:
        longTermDebt = 0
    currentLongTermDebt = quarterly_statementsDump.loc['currentLongTermDebt'][19]
    try:
        currentLongTermDebt = int(currentLongTermDebt)
    except Exception:
        currentLongTermDebt = 0
    longTermDebtNoncurrent = quarterly_statementsDump.loc['longTermDebtNoncurrent'][19]
    try:
        longTermDebtNoncurrent = int(longTermDebtNoncurrent)
    except Exception:
        longTermDebtNoncurrent = 0
    shortLongTermDebtTotal = quarterly_statementsDump.loc['shortLongTermDebtTotal'][19]
    try:
        shortLongTermDebtTotal = int(shortLongTermDebtTotal)
    except Exception:
        shortLongTermDebtTotal = 0
    otherCurrentLiabilities = quarterly_statementsDump.loc['otherCurrentLiabilities'][19]
    try:
        otherCurrentLiabilities = int(otherCurrentLiabilities)
    except Exception:
        otherCurrentLiabilities = 0
    otherNonCurrentLiabilities = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][19]
    try:
        otherNonCurrentLiabilities = int(otherNonCurrentLiabilities)
    except Exception:
        otherNonCurrentLiabilities = 0
    totalShareholderEquity = quarterly_statementsDump.loc['totalShareholderEquity'][19]
    try:
        totalShareholderEquity = int(totalShareholderEquity)
    except Exception:
        totalShareholderEquity = 0
    treasuryStock = quarterly_statementsDump.loc['treasuryStock'][19]
    try:
        treasuryStock = int(treasuryStock)
    except Exception:
        treasuryStock = 0
    retainedEarnings = quarterly_statementsDump.loc['retainedEarnings'][19]
    try:
        retainedEarnings = int(retainedEarnings)
    except Exception:
        retainedEarnings = 0
    commonStock = quarterly_statementsDump.loc['commonStock'][19]
    try:
        commonStock = int(commonStock)
    except Exception:
        commonStock = 0
    commonStockSharesOutstanding = quarterly_statementsDump.loc['commonStockSharesOutstanding'][19]
    try:
        commonStockSharesOutstanding = int(commonStockSharesOutstanding)
    except Exception:
        commonStockSharesOutstanding = 0
    # Cash-Flow Statement values for tm
    operatingCashflow = quarterly_statementsDump.loc['operatingCashflow'][19]
    try:
        operatingCashflow = int(operatingCashflow)
    except Exception:
        operatingCashflow = 0
    paymentsForOperatingActivities = quarterly_statementsDump.loc['paymentsForOperatingActivities'][19]
    try:
        paymentsForOperatingActivities = int(paymentsForOperatingActivities)
    except Exception:
        paymentsForOperatingActivities = 0
    proceedsFromOperatingActivities = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][19]
    try:
        proceedsFromOperatingActivities = int(proceedsFromOperatingActivities)
    except Exception:
        proceedsFromOperatingActivities = 0
    changeInOperatingLiabilities = quarterly_statementsDump.loc['changeInOperatingLiabilities'][19]
    try:
        changeInOperatingLiabilities = int(changeInOperatingLiabilities)
    except Exception:
        changeInOperatingLiabilities = 0
    changeInOperatingAssets = quarterly_statementsDump.loc['changeInOperatingAssets'][19]
    try:
        changeInOperatingAssets = int(changeInOperatingAssets)
    except Exception:
        changeInOperatingAssets = 0
    depreciationDepletionAndAmortization = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][19]
    try:
        depreciationDepletionAndAmortization = int(depreciationDepletionAndAmortization)
    except Exception:
        depreciationDepletionAndAmortization = 0
    capitalExpenditures = quarterly_statementsDump.loc['capitalExpenditures'][19]
    try:
        capitalExpenditures = int(capitalExpenditures)
    except Exception:
        capitalExpenditures = 0
    changeInReceivables = quarterly_statementsDump.loc['changeInReceivables'][19]
    try:
        changeInReceivables = int(changeInReceivables)
    except Exception:
        changeInReceivables = 0
    changeInInventory = quarterly_statementsDump.loc['changeInInventory'][19]
    try:
        changeInInventory = int(changeInInventory)
    except Exception:
        changeInInventory = 0
    profitLoss = quarterly_statementsDump.loc['profitLoss'][19]
    try:
        profitLoss = int(profitLoss)
    except Exception:
        profitLoss = 0
    cashflowFromInvestment = quarterly_statementsDump.loc['cashflowFromInvestment'][19]
    try:
        cashflowFromInvestment = int(cashflowFromInvestment)
    except Exception:
        cashflowFromInvestment = 0
    cashflowFromFinancing = quarterly_statementsDump.loc['cashflowFromFinancing'][19]
    try:
        cashflowFromFinancing = int(cashflowFromFinancing)
    except Exception:
        cashflowFromFinancing = 0
    proceedsFromRepaymentsOfShortTermDebt = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][19]
    try:
        proceedsFromRepaymentsOfShortTermDebt = int(proceedsFromRepaymentsOfShortTermDebt)
    except Exception:
        proceedsFromRepaymentsOfShortTermDebt = 0
    paymentsForRepurchaseOfCommonStock = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][19]
    try:
        paymentsForRepurchaseOfCommonStock = int(paymentsForRepurchaseOfCommonStock)
    except Exception:
        paymentsForRepurchaseOfCommonStock = 0
    paymentsForRepurchaseOfEquity = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][19]
    try:
        paymentsForRepurchaseOfEquity = int(paymentsForRepurchaseOfEquity)
    except Exception:
        paymentsForRepurchaseOfEquity = 0
    paymentsForRepurchaseOfPreferredStock = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][19]
    try:
        paymentsForRepurchaseOfPreferredStock = int(paymentsForRepurchaseOfPreferredStock)
    except Exception:
        paymentsForRepurchaseOfPreferredStock = 0
    dividendPayout = quarterly_statementsDump.loc['dividendPayout'][19]
    try:
        dividendPayout = int(dividendPayout)
    except Exception:
        dividendPayout = 0
    dividendPayoutCommonStock = quarterly_statementsDump.loc['dividendPayoutCommonStock'][19]
    try:
        dividendPayoutCommonStock = int(dividendPayoutCommonStock)
    except Exception:
        dividendPayoutCommonStock = 0
    dividendPayoutPreferredStock = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][19]
    try:
        dividendPayoutPreferredStock = int(dividendPayoutPreferredStock)
    except Exception:
        dividendPayoutPreferredStock = 0
    proceedsFromIssuanceOfCommonStock = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][19]
    try:
        proceedsFromIssuanceOfCommonStock = int(proceedsFromIssuanceOfCommonStock)
    except Exception:
        proceedsFromIssuanceOfCommonStock = 0
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][19]
    try:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = int(proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet)
    except Exception:
        proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = 0
    proceedsFromIssuanceOfPreferredStock = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][19]
    try:
        proceedsFromIssuanceOfPreferredStock = int(proceedsFromIssuanceOfPreferredStock)
    except Exception:
        proceedsFromIssuanceOfPreferredStock = 0
    proceedsFromRepurchaseOfEquity = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][19]
    try:
        proceedsFromRepurchaseOfEquity = int(proceedsFromRepurchaseOfEquity)
    except Exception:
        proceedsFromRepurchaseOfEquity = 0
    proceedsFromSaleOfTreasuryStock = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][19]
    try:
        proceedsFromSaleOfTreasuryStock = int(proceedsFromSaleOfTreasuryStock)
    except Exception:
        proceedsFromSaleOfTreasuryStock = 0
    changeInCashAndCashEquivalents = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][19]
    try:
        changeInCashAndCashEquivalents = int(changeInCashAndCashEquivalents)
    except Exception:
        changeInCashAndCashEquivalents = 0
    changeInExchangeRate = quarterly_statementsDump.loc['changeInExchangeRate'][19]
    try:
        changeInExchangeRate = int(changeInExchangeRate)
    except Exception:
        changeInExchangeRate = 0
    netIncome = quarterly_statementsDump.loc['netIncome'][19]
    try:
        netIncome = int(netIncome)
    except Exception:
        netIncome = 0
    tTMnetIncome = (float(netIncome) + float(netIncome1) + float(netIncome2) + float(netIncome3))
    try:
        tTMpreferredDivs = (int(dividendPayoutPreferredStock) + int(dividendPayoutPreferredStock1) + int(dividendPayoutPreferredStock2) + int(dividendPayoutPreferredStock3))
    except Exception:
        tTMpreferredDivs = 0
    weightedAvgCommShrsOutstanding = ((float(commonStockSharesOutstanding) + float(commonStockSharesOutstanding1) + float(commonStockSharesOutstanding2) + float(commonStockSharesOutstanding3))/4)
    marketCap = calculateMarketCap(quoteUnformatted, commonStockSharesOutstanding)
    basicEPS = calculateBasicEPS(tTMnetIncome, tTMpreferredDivs, weightedAvgCommShrsOutstanding)
    pE = calculatePE(quoteUnformatted, basicEPS)
    pCF = calculatePriceToCashFlow(quoteUnformatted, calculateOperatingCashFlowPerShare(operatingCashflow, weightedAvgCommShrsOutstanding))
    pS = calculatePS(quoteUnformatted, calculateSalesPerShare(totalRevenue, weightedAvgCommShrsOutstanding))
    pB = calculatePB(quoteUnformatted, calculateMarketToBookValue(marketCap, totalAssets, shortLongTermDebtTotal, preferredStock=0))
    sustainableGrowthRate = calculateSustainableGrowthRate(calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout, netIncome)), calculateROE(netIncome, totalShareholderEquity))
    pEGRatio = calculatePEGRatio(pE, (sustainableGrowthRate*100))
    earningsYield = calculateEarningsYield(basicEPS, quoteUnformatted)
    cashFlowPerShare = calculateOperatingCashFlowPerShare(operatingCashflow, weightedAvgCommShrsOutstanding)
    ebitdaPerShare = calculateEBITDAperShare(ebitda, weightedAvgCommShrsOutstanding)
    tTMDividendPayout = ((float(dividendPayout) + float(dividendPayout1) + float(dividendPayout2) + float(dividendPayout3)))
    dividendsPerShare = calculateDividendsPerShare(tTMDividendPayout, weightedAvgCommShrsOutstanding)
    currentQuarterGrossProfitMargin = calculateGrossProfitMargin(totalRevenue, costofGoodsAndServicesSold)
    tTmTotalRevenue = ((float(totalRevenue) + float(totalRevenue1) + float(totalRevenue2) + float(totalRevenue3)))
    tTmCOGS = ((float(costofGoodsAndServicesSold) + float(costofGoodsAndServicesSold1) + float(costofGoodsAndServicesSold2) + float(costofGoodsAndServicesSold3)))
    tTMGrossProfitMargin = calculateGrossProfitMargin(tTmTotalRevenue, tTmCOGS)
    currentQuarterOperatingMargin = calculateOperatingMargin(operatingIncome, totalRevenue)
    tTMOperatingIncome = ((float(operatingIncome) + float(operatingIncome1) + float(operatingIncome2) + float(operatingIncome3)))
    tTMOperatingMargin = calculateOperatingMargin(tTMOperatingIncome, tTmTotalRevenue)
    currentQuarterPreTaxMargin = calculatePreTaxMargin(calculateEBT(ebit, interestExpense), totalRevenue)
    tTMebit = ((float(ebit) + float(ebit1) + float(ebit2) + float(ebit3)))
    tTMInterestExpense = ((float(interestExpense) + float(interestExpense1) + float(interestExpense2) + float(interestExpense3)))
    tTMPreTaxMargin = calculatePreTaxMargin(calculateEBT(tTMebit, tTMInterestExpense), tTmTotalRevenue)
    currentQuarterNetProfitMargin = calculateNetProfitMargin(netIncome, totalRevenue)
    tTMNetProfitMargin = calculateNetProfitMargin(tTMnetIncome, tTmTotalRevenue)
    currentQuarterAvgTotalAssets = ((float(totalAssets) + float(totalAssets1))/2)
    currentQuarterOperatingROA = (calculateOperatingROA(operatingIncome, currentQuarterAvgTotalAssets)) *4
    tTMAvgTotalAssets = ((float(totalAssets) + float(totalAssets1) + float(totalAssets2) + float(totalAssets3))/4)
    tTMOperatingROA = calculateOperatingROA(tTMOperatingIncome, tTMAvgTotalAssets)
    currentQuarterROA = (calculateROA(netIncome, currentQuarterAvgTotalAssets))*4
    tTMROA = calculateROA(tTMnetIncome, tTMAvgTotalAssets)
    currentQuarterReturnOnTotalCapital = (calculateReturnOnTotalCapital(ebit, shortLongTermDebtTotal, totalShareholderEquity))*4
    tTMReturnOnTotalCapital = calculateReturnOnTotalCapital(tTMebit, shortLongTermDebtTotal, totalShareholderEquity)
    currentQuarterROE = (calculateROE(netIncome, totalShareholderEquity)) * 4
    tTMROE = calculateROE(tTMnetIncome, totalShareholderEquity)
    currentQuarterAvgCommonEquity = ((float(totalShareholderEquity) + float(totalShareholderEquity1))/2)
    currentQuarterReturnOnCommonEquity = (calculateReturnOnCommonEquity(netIncome, dividendPayoutPreferredStock, currentQuarterAvgCommonEquity))*4
    tTMAvgCommonEquity = ((float(totalShareholderEquity) + float(totalShareholderEquity1) + float(totalShareholderEquity2) + float(totalShareholderEquity3))/4)
    tTMReturnOnCommonEquity = calculateReturnOnCommonEquity(tTMnetIncome, tTMpreferredDivs, tTMAvgCommonEquity)
    debtRatio = calculateDebtRatio(totalLiabilities, totalAssets)
    debtToEquityRatio = calculateDebtToEquity(shortLongTermDebtTotal, totalShareholderEquity)
    debtToAssetRatio = calculateDebtToAssetRatio(shortLongTermDebtTotal, totalAssets)
    debtToCapitalRatio = calculateDebtToCapitalRatio(shortLongTermDebtTotal, totalShareholderEquity)

    financialLeverage = calculateFinancialLeverageRatio(currentQuarterAvgTotalAssets, currentQuarterAvgCommonEquity)
    interestCoverage = calculateInterestCoverageRatio(operatingCashflow, interestExpense, incomeTaxExpense)
    fixedChargeCoverageRatio = calculateFixedChargeCoverage(ebit, capitalLeaseObligations, interestExpense)






    print('-----------------------------------')
    print('P/E =' + str(pE))
    print('P/CF =' + str(pCF))
    print('P/S =' + str(pS))
    print('P/B =' + str(pB))
    print('PEG Ratio =' + str(pEGRatio))
    print('growthrate =' + str(sustainableGrowthRate))
    print('Earnings Yield =' + str(earningsYield))
    print('Basic EPS =' + str(basicEPS))
    print('cashFlowPerShare =' + str(cashFlowPerShare))
    print('ebitdaPerShare =' + str(ebitdaPerShare))
    print('dividendsPerShare =' + str(dividendsPerShare))
    print('Current Quarter Gross Profit Margin =' + str(currentQuarterGrossProfitMargin))
    print('TTM Gross Profit Margin =' + str(tTMGrossProfitMargin))
    print('Current Quarter Operating Margin =' + str(currentQuarterOperatingMargin))
    print('TTM Operating Margin  =' + str(tTMOperatingMargin))
    print('Current Quarter Pre-Tax Margin =' + str(currentQuarterPreTaxMargin))
    print('TTM Pre-Tax Margin =' + str(tTMPreTaxMargin))
    print('Current Quarter Net Profit Margin =' + str(currentQuarterNetProfitMargin))
    print('TTM Net Profit Margin  =' + str(tTMNetProfitMargin))
    print('Current Quarter Operating ROA =' + str(currentQuarterOperatingROA))
    print('TTM Operating ROA  =' + str(tTMOperatingROA))
    print('Current Quarter  ROA =' + str(currentQuarterROA))
    print('TTM  ROA  =' + str(tTMROA))
    print('Current Quarter Return On Total Capital  =' + str(currentQuarterReturnOnTotalCapital))
    print('TTM Return On Total Capital  =' + str(tTMReturnOnTotalCapital))
    print('Current Quarter  ROE =' + str(currentQuarterROE))
    print('TTM  ROE  =' + str(tTMROE))
    print('Current Quarter Return on Common Equity =' + str(currentQuarterReturnOnCommonEquity))
    print('TTM  Return on Common Equity  =' + str(tTMReturnOnCommonEquity))
    print('Debt Ratio  =' + str(debtRatio))
    print('Debt to Equity Ratio  =' + str(debtToEquityRatio))
    print('Debt to Asset Ratio  =' + str(debtToAssetRatio))
    print('Debt to Capital Ratio  =' + str(debtToCapitalRatio))
    print('Financial Legerage Ratio  =' + str(financialLeverage))
    print('Fixed-Charge Coverage Ratio  =' + str(fixedChargeCoverageRatio))

    print(quote)

build_master('SQ')

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

    ## TM19 VARIABLES
    # Income Statement Variables for tm19
    gross_profit19 = quarterly_statementsDump.loc['grossProfit'][0]
    totalRevenue19 = quarterly_statementsDump.loc['totalRevenue'][0]
    costOfRevenue19 = quarterly_statementsDump.loc['costOfRevenue'][0]
    costofGoodsAndServicesSold19 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][0]
    operatingIncome19 = quarterly_statementsDump.loc['operatingIncome'][0]
    sellingGeneralAndAdministrative19 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][0]
    researchAndDevelopment19 = quarterly_statementsDump.loc['researchAndDevelopment'][0]
    operatingExpenses19 = quarterly_statementsDump.loc['operatingExpenses'][0]
    investmentIncomeNet19 = quarterly_statementsDump.loc['investmentIncomeNet'][0]
    netInterestIncome19 = quarterly_statementsDump.loc['netInterestIncome'][0]
    interestIncome19 = quarterly_statementsDump.loc['interestIncome'][0]
    interestExpense19 = quarterly_statementsDump.loc['interestExpense'][0]
    nonInterestIncome19 = quarterly_statementsDump.loc['nonInterestIncome'][0]
    otherNonOperatingIncome19 = quarterly_statementsDump.loc['otherNonOperatingIncome'][0]
    depreciation19 = quarterly_statementsDump.loc['depreciation'][0]
    depreciationAndAmortization19 = quarterly_statementsDump.loc['depreciationAndAmortization'][0]
    incomeBeforeTax19 = quarterly_statementsDump.loc['incomeBeforeTax'][0]
    incomeTaxExpense19 = quarterly_statementsDump.loc['incomeTaxExpense'][0]
    interestAndDebtExpense19 = quarterly_statementsDump.loc['interestAndDebtExpense'][0]
    netIncomeFromContinuingOperations19 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][0]
    comprehensiveIncomeNetOfTax19 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][0]
    ebit19 = quarterly_statementsDump.loc['ebit'][0]
    ebitda19 = quarterly_statementsDump.loc['ebitda'][0]
    #netIncome19 = quarterly_statementsDump.loc['netIncome'][0]

    # Balance Sheet Values for tm19
    totalAssets19 = quarterly_statementsDump.loc['totalAssets'][0]
    totalCurrentAssets19 = quarterly_statementsDump.loc['totalCurrentAssets'][0]
    cashAndCashEquivalentsAtCarryingValue19 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][0]
    cashAndShortTermInvestments19 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][0]
    inventory19 = quarterly_statementsDump.loc['inventory'][0]
    currentNetReceivables19 = quarterly_statementsDump.loc['currentNetReceivables'][0]
    totalNonCurrentAssets19 = quarterly_statementsDump.loc['totalNonCurrentAssets'][0]
    propertyPlantEquipment19 = quarterly_statementsDump.loc['propertyPlantEquipment'][0]
    accumulatedDepreciationAmortizationPPE19 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][0]
    intangibleAssets19 = quarterly_statementsDump.loc['intangibleAssets'][0]
    intangibleAssetsExcludingGoodwill19 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][0]
    goodwill19 = quarterly_statementsDump.loc['goodwill'][0]
    investments19 = quarterly_statementsDump.loc['investments'][0]
    longTermInvestments19 = quarterly_statementsDump.loc['longTermInvestments'][0]
    shortTermInvestments19 = quarterly_statementsDump.loc['shortTermInvestments'][0]
    otherCurrentAssets19 = quarterly_statementsDump.loc['otherCurrentAssets'][0]
    otherNonCurrrentAssets19 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][0]
    totalLiabilities19 = quarterly_statementsDump.loc['totalLiabilities'][0]
    totalCurrentLiabilities19 = quarterly_statementsDump.loc['totalCurrentLiabilities'][0]
    currentAccountsPayable19 = quarterly_statementsDump.loc['currentAccountsPayable'][0]
    deferredRevenue19 = quarterly_statementsDump.loc['deferredRevenue'][0]
    currentDebt19 = quarterly_statementsDump.loc['currentDebt'][0]
    shortTermDebt19 = quarterly_statementsDump.loc['shortTermDebt'][0]
    totalNonCurrentLiabilities19 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][0]
    capitalLeaseObligations19 = quarterly_statementsDump.loc['capitalLeaseObligations'][0]
    longTermDebt19 = quarterly_statementsDump.loc['longTermDebt'][0]
    currentLongTermDebt19 = quarterly_statementsDump.loc['currentLongTermDebt'][0]
    longTermDebtNoncurrent19 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][0]
    shortLongTermDebtTotal19 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][0]
    otherCurrentLiabilities19 = quarterly_statementsDump.loc['otherCurrentLiabilities'][0]
    otherNonCurrentLiabilities19 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][0]
    totalShareholderEquity19 = quarterly_statementsDump.loc['totalShareholderEquity'][0]
    treasuryStock19 = quarterly_statementsDump.loc['treasuryStock'][0]
    retainedEarnings19 = quarterly_statementsDump.loc['retainedEarnings'][0]
    commonStock19 = quarterly_statementsDump.loc['commonStock'][0]
    commonStockSharesOutstanding19 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][0]

    # Cash-Flow Statement values for tm19
    operatingCashflow19 = quarterly_statementsDump.loc['operatingCashflow'][0]
    paymentsForOperatingActivities19 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][0]
    proceedsFromOperatingActivities19 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][0]
    changeInOperatingLiabilities19 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][0]
    changeInOperatingAssets19 = quarterly_statementsDump.loc['changeInOperatingAssets'][0]
    depreciationDepletionAndAmortization19 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][0]
    capitalExpenditures19 = quarterly_statementsDump.loc['capitalExpenditures'][0]
    changeInReceivables19 = quarterly_statementsDump.loc['changeInReceivables'][0]
    changeInInventory19 = quarterly_statementsDump.loc['changeInInventory'][0]
    profitLoss19 = quarterly_statementsDump.loc['profitLoss'][0]
    cashflowFromInvestment19 = quarterly_statementsDump.loc['cashflowFromInvestment'][0]
    cashflowFromFinancing19 = quarterly_statementsDump.loc['cashflowFromFinancing'][0]
    proceedsFromRepaymentsOfShortTermDebt19 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][0]
    paymentsForRepurchaseOfCommonStock19 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][0]
    paymentsForRepurchaseOfEquity19 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][0]
    paymentsForRepurchaseOfPreferredStock19 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][0]
    dividendPayout19 = quarterly_statementsDump.loc['dividendPayout'][0]
    dividendPayoutCommonStock19 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][0]
    dividendPayoutPreferredStock19 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][0]
    proceedsFromIssuanceOfCommonStock19 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][0]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet19 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][0]
    proceedsFromIssuanceOfPreferredStock19 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][0]
    proceedsFromRepurchaseOfEquity19 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][0]
    proceedsFromSaleOfTreasuryStock19 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][0]
    changeInCashAndCashEquivalents19 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][0]
    changeInExchangeRate19 = quarterly_statementsDump.loc['changeInExchangeRate'][0]
    netIncome19 = quarterly_statementsDump.loc['netIncome'][0]





    ## TM18 VARIABLES
    # Income Statement Variables for tm18
    gross_profit18 = quarterly_statementsDump.loc['grossProfit'][1]
    totalRevenue18 = quarterly_statementsDump.loc['totalRevenue'][1]
    costOfRevenue18 = quarterly_statementsDump.loc['costOfRevenue'][1]
    costofGoodsAndServicesSold18 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][1]
    operatingIncome18 = quarterly_statementsDump.loc['operatingIncome'][1]
    sellingGeneralAndAdministrative18 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][1]
    researchAndDevelopment18 = quarterly_statementsDump.loc['researchAndDevelopment'][1]
    operatingExpenses18 = quarterly_statementsDump.loc['operatingExpenses'][1]
    investmentIncomeNet18 = quarterly_statementsDump.loc['investmentIncomeNet'][1]
    netInterestIncome18 = quarterly_statementsDump.loc['netInterestIncome'][1]
    interestIncome18 = quarterly_statementsDump.loc['interestIncome'][1]
    interestExpense18 = quarterly_statementsDump.loc['interestExpense'][1]
    nonInterestIncome18 = quarterly_statementsDump.loc['nonInterestIncome'][1]
    otherNonOperatingIncome18 = quarterly_statementsDump.loc['otherNonOperatingIncome'][1]
    depreciation18 = quarterly_statementsDump.loc['depreciation'][1]
    depreciationAndAmortization18 = quarterly_statementsDump.loc['depreciationAndAmortization'][1]
    incomeBeforeTax18 = quarterly_statementsDump.loc['incomeBeforeTax'][1]
    incomeTaxExpense18 = quarterly_statementsDump.loc['incomeTaxExpense'][1]
    interestAndDebtExpense18 = quarterly_statementsDump.loc['interestAndDebtExpense'][1]
    netIncomeFromContinuingOperations18 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][1]
    comprehensiveIncomeNetOfTax18 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][1]
    ebit18 = quarterly_statementsDump.loc['ebit'][1]
    ebitda18 = quarterly_statementsDump.loc['ebitda'][1]
    # netIncome18 = quarterly_statementsDump.loc['netIncome'][1]

    # Balance Sheet Values for tm18
    totalAssets18 = quarterly_statementsDump.loc['totalAssets'][1]
    totalCurrentAssets18 = quarterly_statementsDump.loc['totalCurrentAssets'][1]
    cashAndCashEquivalentsAtCarryingValue18 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][1]
    cashAndShortTermInvestments18 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][1]
    inventory18 = quarterly_statementsDump.loc['inventory'][1]
    currentNetReceivables18 = quarterly_statementsDump.loc['currentNetReceivables'][1]
    totalNonCurrentAssets18 = quarterly_statementsDump.loc['totalNonCurrentAssets'][1]
    propertyPlantEquipment18 = quarterly_statementsDump.loc['propertyPlantEquipment'][1]
    accumulatedDepreciationAmortizationPPE18 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][1]
    intangibleAssets18 = quarterly_statementsDump.loc['intangibleAssets'][1]
    intangibleAssetsExcludingGoodwill18 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][1]
    goodwill18 = quarterly_statementsDump.loc['goodwill'][1]
    investments18 = quarterly_statementsDump.loc['investments'][1]
    longTermInvestments18 = quarterly_statementsDump.loc['longTermInvestments'][1]
    shortTermInvestments18 = quarterly_statementsDump.loc['shortTermInvestments'][1]
    otherCurrentAssets18 = quarterly_statementsDump.loc['otherCurrentAssets'][1]
    otherNonCurrrentAssets18 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][1]
    totalLiabilities18 = quarterly_statementsDump.loc['totalLiabilities'][1]
    totalCurrentLiabilities18 = quarterly_statementsDump.loc['totalCurrentLiabilities'][1]
    currentAccountsPayable18 = quarterly_statementsDump.loc['currentAccountsPayable'][1]
    deferredRevenue18 = quarterly_statementsDump.loc['deferredRevenue'][1]
    currentDebt18 = quarterly_statementsDump.loc['currentDebt'][1]
    shortTermDebt18 = quarterly_statementsDump.loc['shortTermDebt'][1]
    totalNonCurrentLiabilities18 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][1]
    capitalLeaseObligations18 = quarterly_statementsDump.loc['capitalLeaseObligations'][1]
    longTermDebt18 = quarterly_statementsDump.loc['longTermDebt'][1]
    currentLongTermDebt18 = quarterly_statementsDump.loc['currentLongTermDebt'][1]
    longTermDebtNoncurrent18 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][1]
    shortLongTermDebtTotal18 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][1]
    otherCurrentLiabilities18 = quarterly_statementsDump.loc['otherCurrentLiabilities'][1]
    otherNonCurrentLiabilities18 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][1]
    totalShareholderEquity18 = quarterly_statementsDump.loc['totalShareholderEquity'][1]
    treasuryStock18 = quarterly_statementsDump.loc['treasuryStock'][1]
    retainedEarnings18 = quarterly_statementsDump.loc['retainedEarnings'][1]
    commonStock18 = quarterly_statementsDump.loc['commonStock'][1]
    commonStockSharesOutstanding18 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][1]

    # Cash-Flow Statement values for tm18
    operatingCashflow18 = quarterly_statementsDump.loc['operatingCashflow'][1]
    paymentsForOperatingActivities18 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][1]
    proceedsFromOperatingActivities18 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][1]
    changeInOperatingLiabilities18 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][1]
    changeInOperatingAssets18 = quarterly_statementsDump.loc['changeInOperatingAssets'][1]
    depreciationDepletionAndAmortization18 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][1]
    capitalExpenditures18 = quarterly_statementsDump.loc['capitalExpenditures'][1]
    changeInReceivables18 = quarterly_statementsDump.loc['changeInReceivables'][1]
    changeInInventory18 = quarterly_statementsDump.loc['changeInInventory'][1]
    profitLoss18 = quarterly_statementsDump.loc['profitLoss'][1]
    cashflowFromInvestment18 = quarterly_statementsDump.loc['cashflowFromInvestment'][1]
    cashflowFromFinancing18 = quarterly_statementsDump.loc['cashflowFromFinancing'][1]
    proceedsFromRepaymentsOfShortTermDebt18 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][1]
    paymentsForRepurchaseOfCommonStock18 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][1]
    paymentsForRepurchaseOfEquity18 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][1]
    paymentsForRepurchaseOfPreferredStock18 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][1]
    dividendPayout18 = quarterly_statementsDump.loc['dividendPayout'][1]
    dividendPayoutCommonStock18 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][1]
    dividendPayoutPreferredStock18 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][1]
    proceedsFromIssuanceOfCommonStock18 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][1]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet18 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][1]
    proceedsFromIssuanceOfPreferredStock18 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][1]
    proceedsFromRepurchaseOfEquity18 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][1]
    proceedsFromSaleOfTreasuryStock18 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][1]
    changeInCashAndCashEquivalents18 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][1]
    changeInExchangeRate18 = quarterly_statementsDump.loc['changeInExchangeRate'][1]
    netIncome18 = quarterly_statementsDump.loc['netIncome'][1]

    ## TM17 VARIABLES
    # Income Statement Variables for tm17
    gross_profit17 = quarterly_statementsDump.loc['grossProfit'][2]
    totalRevenue17 = quarterly_statementsDump.loc['totalRevenue'][2]
    costOfRevenue17 = quarterly_statementsDump.loc['costOfRevenue'][2]
    costofGoodsAndServicesSold17 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][2]
    operatingIncome17 = quarterly_statementsDump.loc['operatingIncome'][2]
    sellingGeneralAndAdministrative17 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][2]
    researchAndDevelopment17 = quarterly_statementsDump.loc['researchAndDevelopment'][2]
    operatingExpenses17 = quarterly_statementsDump.loc['operatingExpenses'][2]
    investmentIncomeNet17 = quarterly_statementsDump.loc['investmentIncomeNet'][2]
    netInterestIncome17 = quarterly_statementsDump.loc['netInterestIncome'][2]
    interestIncome17 = quarterly_statementsDump.loc['interestIncome'][2]
    interestExpense17 = quarterly_statementsDump.loc['interestExpense'][2]
    nonInterestIncome17 = quarterly_statementsDump.loc['nonInterestIncome'][2]
    otherNonOperatingIncome17 = quarterly_statementsDump.loc['otherNonOperatingIncome'][2]
    depreciation17 = quarterly_statementsDump.loc['depreciation'][2]
    depreciationAndAmortization17 = quarterly_statementsDump.loc['depreciationAndAmortization'][2]
    incomeBeforeTax17 = quarterly_statementsDump.loc['incomeBeforeTax'][2]
    incomeTaxExpense17 = quarterly_statementsDump.loc['incomeTaxExpense'][2]
    interestAndDebtExpense17 = quarterly_statementsDump.loc['interestAndDebtExpense'][2]
    netIncomeFromContinuingOperations17 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][2]
    comprehensiveIncomeNetOfTax17 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][2]
    ebit17 = quarterly_statementsDump.loc['ebit'][2]
    ebitda17 = quarterly_statementsDump.loc['ebitda'][2]
    # netIncome17 = quarterly_statementsDump.loc['netIncome'][2]

    # Balance Sheet Values for tm17
    totalAssets17 = quarterly_statementsDump.loc['totalAssets'][2]
    totalCurrentAssets17 = quarterly_statementsDump.loc['totalCurrentAssets'][2]
    cashAndCashEquivalentsAtCarryingValue17 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][2]
    cashAndShortTermInvestments17 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][2]
    inventory17 = quarterly_statementsDump.loc['inventory'][2]
    currentNetReceivables17 = quarterly_statementsDump.loc['currentNetReceivables'][2]
    totalNonCurrentAssets17 = quarterly_statementsDump.loc['totalNonCurrentAssets'][2]
    propertyPlantEquipment17 = quarterly_statementsDump.loc['propertyPlantEquipment'][2]
    accumulatedDepreciationAmortizationPPE17 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][2]
    intangibleAssets17 = quarterly_statementsDump.loc['intangibleAssets'][2]
    intangibleAssetsExcludingGoodwill17 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][2]
    goodwill17 = quarterly_statementsDump.loc['goodwill'][2]
    investments17 = quarterly_statementsDump.loc['investments'][2]
    longTermInvestments17 = quarterly_statementsDump.loc['longTermInvestments'][2]
    shortTermInvestments17 = quarterly_statementsDump.loc['shortTermInvestments'][2]
    otherCurrentAssets17 = quarterly_statementsDump.loc['otherCurrentAssets'][2]
    otherNonCurrrentAssets17 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][2]
    totalLiabilities17 = quarterly_statementsDump.loc['totalLiabilities'][2]
    totalCurrentLiabilities17 = quarterly_statementsDump.loc['totalCurrentLiabilities'][2]
    currentAccountsPayable17 = quarterly_statementsDump.loc['currentAccountsPayable'][2]
    deferredRevenue17 = quarterly_statementsDump.loc['deferredRevenue'][2]
    currentDebt17 = quarterly_statementsDump.loc['currentDebt'][2]
    shortTermDebt17 = quarterly_statementsDump.loc['shortTermDebt'][2]
    totalNonCurrentLiabilities17 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][2]
    capitalLeaseObligations17 = quarterly_statementsDump.loc['capitalLeaseObligations'][2]
    longTermDebt17 = quarterly_statementsDump.loc['longTermDebt'][2]
    currentLongTermDebt17 = quarterly_statementsDump.loc['currentLongTermDebt'][2]
    longTermDebtNoncurrent17 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][2]
    shortLongTermDebtTotal17 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][2]
    otherCurrentLiabilities17 = quarterly_statementsDump.loc['otherCurrentLiabilities'][2]
    otherNonCurrentLiabilities17 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][2]
    totalShareholderEquity17 = quarterly_statementsDump.loc['totalShareholderEquity'][2]
    treasuryStock17 = quarterly_statementsDump.loc['treasuryStock'][2]
    retainedEarnings17 = quarterly_statementsDump.loc['retainedEarnings'][2]
    commonStock17 = quarterly_statementsDump.loc['commonStock'][2]
    commonStockSharesOutstanding17 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][2]

    # Cash-Flow Statement values for tm17
    operatingCashflow17 = quarterly_statementsDump.loc['operatingCashflow'][2]
    paymentsForOperatingActivities17 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][2]
    proceedsFromOperatingActivities17 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][2]
    changeInOperatingLiabilities17 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][2]
    changeInOperatingAssets17 = quarterly_statementsDump.loc['changeInOperatingAssets'][2]
    depreciationDepletionAndAmortization17 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][2]
    capitalExpenditures17 = quarterly_statementsDump.loc['capitalExpenditures'][2]
    changeInReceivables17 = quarterly_statementsDump.loc['changeInReceivables'][2]
    changeInInventory17 = quarterly_statementsDump.loc['changeInInventory'][2]
    profitLoss17 = quarterly_statementsDump.loc['profitLoss'][2]
    cashflowFromInvestment17 = quarterly_statementsDump.loc['cashflowFromInvestment'][2]
    cashflowFromFinancing17 = quarterly_statementsDump.loc['cashflowFromFinancing'][2]
    proceedsFromRepaymentsOfShortTermDebt17 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][2]
    paymentsForRepurchaseOfCommonStock17 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][2]
    paymentsForRepurchaseOfEquity17 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][2]
    paymentsForRepurchaseOfPreferredStock17 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][2]
    dividendPayout17 = quarterly_statementsDump.loc['dividendPayout'][2]
    dividendPayoutCommonStock17 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][2]
    dividendPayoutPreferredStock17 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][2]
    proceedsFromIssuanceOfCommonStock17 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][2]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet17 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][2]
    proceedsFromIssuanceOfPreferredStock17 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][2]
    proceedsFromRepurchaseOfEquity17 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][2]
    proceedsFromSaleOfTreasuryStock17 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][2]
    changeInCashAndCashEquivalents17 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][2]
    changeInExchangeRate17 = quarterly_statementsDump.loc['changeInExchangeRate'][2]
    netIncome17 = quarterly_statementsDump.loc['netIncome'][2]

    ## TM16 VARIABLES
    # Income Statement Variables for tm16
    gross_profit16 = quarterly_statementsDump.loc['grossProfit'][3]
    totalRevenue16 = quarterly_statementsDump.loc['totalRevenue'][3]
    costOfRevenue16 = quarterly_statementsDump.loc['costOfRevenue'][3]
    costofGoodsAndServicesSold16 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][3]
    operatingIncome16 = quarterly_statementsDump.loc['operatingIncome'][3]
    sellingGeneralAndAdministrative16 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][3]
    researchAndDevelopment16 = quarterly_statementsDump.loc['researchAndDevelopment'][3]
    operatingExpenses16 = quarterly_statementsDump.loc['operatingExpenses'][3]
    investmentIncomeNet16 = quarterly_statementsDump.loc['investmentIncomeNet'][3]
    netInterestIncome16 = quarterly_statementsDump.loc['netInterestIncome'][3]
    interestIncome16 = quarterly_statementsDump.loc['interestIncome'][3]
    interestExpense16 = quarterly_statementsDump.loc['interestExpense'][3]
    nonInterestIncome16 = quarterly_statementsDump.loc['nonInterestIncome'][3]
    otherNonOperatingIncome16 = quarterly_statementsDump.loc['otherNonOperatingIncome'][3]
    depreciation16 = quarterly_statementsDump.loc['depreciation'][3]
    depreciationAndAmortization16 = quarterly_statementsDump.loc['depreciationAndAmortization'][3]
    incomeBeforeTax16 = quarterly_statementsDump.loc['incomeBeforeTax'][3]
    incomeTaxExpense16 = quarterly_statementsDump.loc['incomeTaxExpense'][3]
    interestAndDebtExpense16 = quarterly_statementsDump.loc['interestAndDebtExpense'][3]
    netIncomeFromContinuingOperations16 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][3]
    comprehensiveIncomeNetOfTax16 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][3]
    ebit16 = quarterly_statementsDump.loc['ebit'][3]
    ebitda16 = quarterly_statementsDump.loc['ebitda'][3]
    # netIncome16 = quarterly_statementsDump.loc['netIncome'][3]

    # Balance Sheet Values for tm16
    totalAssets16 = quarterly_statementsDump.loc['totalAssets'][3]
    totalCurrentAssets16 = quarterly_statementsDump.loc['totalCurrentAssets'][3]
    cashAndCashEquivalentsAtCarryingValue16 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][3]
    cashAndShortTermInvestments16 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][3]
    inventory16 = quarterly_statementsDump.loc['inventory'][3]
    currentNetReceivables16 = quarterly_statementsDump.loc['currentNetReceivables'][3]
    totalNonCurrentAssets16 = quarterly_statementsDump.loc['totalNonCurrentAssets'][3]
    propertyPlantEquipment16 = quarterly_statementsDump.loc['propertyPlantEquipment'][3]
    accumulatedDepreciationAmortizationPPE16 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][3]
    intangibleAssets16 = quarterly_statementsDump.loc['intangibleAssets'][3]
    intangibleAssetsExcludingGoodwill16 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][3]
    goodwill16 = quarterly_statementsDump.loc['goodwill'][3]
    investments16 = quarterly_statementsDump.loc['investments'][3]
    longTermInvestments16 = quarterly_statementsDump.loc['longTermInvestments'][3]
    shortTermInvestments16 = quarterly_statementsDump.loc['shortTermInvestments'][3]
    otherCurrentAssets16 = quarterly_statementsDump.loc['otherCurrentAssets'][3]
    otherNonCurrrentAssets16 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][3]
    totalLiabilities16 = quarterly_statementsDump.loc['totalLiabilities'][3]
    totalCurrentLiabilities16 = quarterly_statementsDump.loc['totalCurrentLiabilities'][3]
    currentAccountsPayable16 = quarterly_statementsDump.loc['currentAccountsPayable'][3]
    deferredRevenue16 = quarterly_statementsDump.loc['deferredRevenue'][3]
    currentDebt16 = quarterly_statementsDump.loc['currentDebt'][3]
    shortTermDebt16 = quarterly_statementsDump.loc['shortTermDebt'][3]
    totalNonCurrentLiabilities16 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][3]
    capitalLeaseObligations16 = quarterly_statementsDump.loc['capitalLeaseObligations'][3]
    longTermDebt16 = quarterly_statementsDump.loc['longTermDebt'][3]
    currentLongTermDebt16 = quarterly_statementsDump.loc['currentLongTermDebt'][3]
    longTermDebtNoncurrent16 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][3]
    shortLongTermDebtTotal16 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][3]
    otherCurrentLiabilities16 = quarterly_statementsDump.loc['otherCurrentLiabilities'][3]
    otherNonCurrentLiabilities16 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][3]
    totalShareholderEquity16 = quarterly_statementsDump.loc['totalShareholderEquity'][3]
    treasuryStock16 = quarterly_statementsDump.loc['treasuryStock'][3]
    retainedEarnings16 = quarterly_statementsDump.loc['retainedEarnings'][3]
    commonStock16 = quarterly_statementsDump.loc['commonStock'][3]
    commonStockSharesOutstanding16 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][3]

    # Cash-Flow Statement values for tm16
    operatingCashflow16 = quarterly_statementsDump.loc['operatingCashflow'][3]
    paymentsForOperatingActivities16 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][3]
    proceedsFromOperatingActivities16 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][3]
    changeInOperatingLiabilities16 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][3]
    changeInOperatingAssets16 = quarterly_statementsDump.loc['changeInOperatingAssets'][3]
    depreciationDepletionAndAmortization16 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][3]
    capitalExpenditures16 = quarterly_statementsDump.loc['capitalExpenditures'][3]
    changeInReceivables16 = quarterly_statementsDump.loc['changeInReceivables'][3]
    changeInInventory16 = quarterly_statementsDump.loc['changeInInventory'][3]
    profitLoss16 = quarterly_statementsDump.loc['profitLoss'][3]
    cashflowFromInvestment16 = quarterly_statementsDump.loc['cashflowFromInvestment'][3]
    cashflowFromFinancing16 = quarterly_statementsDump.loc['cashflowFromFinancing'][3]
    proceedsFromRepaymentsOfShortTermDebt16 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][3]
    paymentsForRepurchaseOfCommonStock16 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][3]
    paymentsForRepurchaseOfEquity16 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][3]
    paymentsForRepurchaseOfPreferredStock16 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][3]
    dividendPayout16 = quarterly_statementsDump.loc['dividendPayout'][3]
    dividendPayoutCommonStock16 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][3]
    dividendPayoutPreferredStock16 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][3]
    proceedsFromIssuanceOfCommonStock16 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][3]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet16 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][3]
    proceedsFromIssuanceOfPreferredStock16 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][3]
    proceedsFromRepurchaseOfEquity16 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][3]
    proceedsFromSaleOfTreasuryStock16 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][3]
    changeInCashAndCashEquivalents16 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][3]
    changeInExchangeRate16 = quarterly_statementsDump.loc['changeInExchangeRate'][3]
    netIncome16 = quarterly_statementsDump.loc['netIncome'][3]

    ## TM15 VARIABLES
    # Income Statement Variables for tm15
    gross_profit15 = quarterly_statementsDump.loc['grossProfit'][4]
    totalRevenue15 = quarterly_statementsDump.loc['totalRevenue'][4]
    costOfRevenue15 = quarterly_statementsDump.loc['costOfRevenue'][4]
    costofGoodsAndServicesSold15 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][4]
    operatingIncome15 = quarterly_statementsDump.loc['operatingIncome'][4]
    sellingGeneralAndAdministrative15 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][4]
    researchAndDevelopment15 = quarterly_statementsDump.loc['researchAndDevelopment'][4]
    operatingExpenses15 = quarterly_statementsDump.loc['operatingExpenses'][4]
    investmentIncomeNet15 = quarterly_statementsDump.loc['investmentIncomeNet'][4]
    netInterestIncome15 = quarterly_statementsDump.loc['netInterestIncome'][4]
    interestIncome15 = quarterly_statementsDump.loc['interestIncome'][4]
    interestExpense15 = quarterly_statementsDump.loc['interestExpense'][4]
    nonInterestIncome15 = quarterly_statementsDump.loc['nonInterestIncome'][4]
    otherNonOperatingIncome15 = quarterly_statementsDump.loc['otherNonOperatingIncome'][4]
    depreciation15 = quarterly_statementsDump.loc['depreciation'][4]
    depreciationAndAmortization15 = quarterly_statementsDump.loc['depreciationAndAmortization'][4]
    incomeBeforeTax15 = quarterly_statementsDump.loc['incomeBeforeTax'][4]
    incomeTaxExpense15 = quarterly_statementsDump.loc['incomeTaxExpense'][4]
    interestAndDebtExpense15 = quarterly_statementsDump.loc['interestAndDebtExpense'][4]
    netIncomeFromContinuingOperations15 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][4]
    comprehensiveIncomeNetOfTax15 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][4]
    ebit15 = quarterly_statementsDump.loc['ebit'][4]
    ebitda15 = quarterly_statementsDump.loc['ebitda'][4]
    # netIncome15 = quarterly_statementsDump.loc['netIncome'][4]

    # Balance Sheet Values for tm15
    totalAssets15 = quarterly_statementsDump.loc['totalAssets'][4]
    totalCurrentAssets15 = quarterly_statementsDump.loc['totalCurrentAssets'][4]
    cashAndCashEquivalentsAtCarryingValue15 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][4]
    cashAndShortTermInvestments15 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][4]
    inventory15 = quarterly_statementsDump.loc['inventory'][4]
    currentNetReceivables15 = quarterly_statementsDump.loc['currentNetReceivables'][4]
    totalNonCurrentAssets15 = quarterly_statementsDump.loc['totalNonCurrentAssets'][4]
    propertyPlantEquipment15 = quarterly_statementsDump.loc['propertyPlantEquipment'][4]
    accumulatedDepreciationAmortizationPPE15 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][4]
    intangibleAssets15 = quarterly_statementsDump.loc['intangibleAssets'][4]
    intangibleAssetsExcludingGoodwill15 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][4]
    goodwill15 = quarterly_statementsDump.loc['goodwill'][4]
    investments15 = quarterly_statementsDump.loc['investments'][4]
    longTermInvestments15 = quarterly_statementsDump.loc['longTermInvestments'][4]
    shortTermInvestments15 = quarterly_statementsDump.loc['shortTermInvestments'][4]
    otherCurrentAssets15 = quarterly_statementsDump.loc['otherCurrentAssets'][4]
    otherNonCurrrentAssets15 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][4]
    totalLiabilities15 = quarterly_statementsDump.loc['totalLiabilities'][4]
    totalCurrentLiabilities15 = quarterly_statementsDump.loc['totalCurrentLiabilities'][4]
    currentAccountsPayable15 = quarterly_statementsDump.loc['currentAccountsPayable'][4]
    deferredRevenue15 = quarterly_statementsDump.loc['deferredRevenue'][4]
    currentDebt15 = quarterly_statementsDump.loc['currentDebt'][4]
    shortTermDebt15 = quarterly_statementsDump.loc['shortTermDebt'][4]
    totalNonCurrentLiabilities15 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][4]
    capitalLeaseObligations15 = quarterly_statementsDump.loc['capitalLeaseObligations'][4]
    longTermDebt15 = quarterly_statementsDump.loc['longTermDebt'][4]
    currentLongTermDebt15 = quarterly_statementsDump.loc['currentLongTermDebt'][4]
    longTermDebtNoncurrent15 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][4]
    shortLongTermDebtTotal15 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][4]
    otherCurrentLiabilities15 = quarterly_statementsDump.loc['otherCurrentLiabilities'][4]
    otherNonCurrentLiabilities15 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][4]
    totalShareholderEquity15 = quarterly_statementsDump.loc['totalShareholderEquity'][4]
    treasuryStock15 = quarterly_statementsDump.loc['treasuryStock'][4]
    retainedEarnings15 = quarterly_statementsDump.loc['retainedEarnings'][4]
    commonStock15 = quarterly_statementsDump.loc['commonStock'][4]
    commonStockSharesOutstanding15 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][4]

    # Cash-Flow Statement values for tm15
    operatingCashflow15 = quarterly_statementsDump.loc['operatingCashflow'][4]
    paymentsForOperatingActivities15 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][4]
    proceedsFromOperatingActivities15 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][4]
    changeInOperatingLiabilities15 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][4]
    changeInOperatingAssets15 = quarterly_statementsDump.loc['changeInOperatingAssets'][4]
    depreciationDepletionAndAmortization15 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][4]
    capitalExpenditures15 = quarterly_statementsDump.loc['capitalExpenditures'][4]
    changeInReceivables15 = quarterly_statementsDump.loc['changeInReceivables'][4]
    changeInInventory15 = quarterly_statementsDump.loc['changeInInventory'][4]
    profitLoss15 = quarterly_statementsDump.loc['profitLoss'][4]
    cashflowFromInvestment15 = quarterly_statementsDump.loc['cashflowFromInvestment'][4]
    cashflowFromFinancing15 = quarterly_statementsDump.loc['cashflowFromFinancing'][4]
    proceedsFromRepaymentsOfShortTermDebt15 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][4]
    paymentsForRepurchaseOfCommonStock15 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][4]
    paymentsForRepurchaseOfEquity15 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][4]
    paymentsForRepurchaseOfPreferredStock15 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][4]
    dividendPayout15 = quarterly_statementsDump.loc['dividendPayout'][4]
    dividendPayoutCommonStock15 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][4]
    dividendPayoutPreferredStock15 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][4]
    proceedsFromIssuanceOfCommonStock15 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][4]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet15 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][4]
    proceedsFromIssuanceOfPreferredStock15 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][4]
    proceedsFromRepurchaseOfEquity15 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][4]
    proceedsFromSaleOfTreasuryStock15 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][4]
    changeInCashAndCashEquivalents15 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][4]
    changeInExchangeRate15 = quarterly_statementsDump.loc['changeInExchangeRate'][4]
    netIncome15 = quarterly_statementsDump.loc['netIncome'][4]

    ## TM14 VARIABLES
    # Income Statement Variables for tm14
    gross_profit14 = quarterly_statementsDump.loc['grossProfit'][5]
    totalRevenue14 = quarterly_statementsDump.loc['totalRevenue'][5]
    costOfRevenue14 = quarterly_statementsDump.loc['costOfRevenue'][5]
    costofGoodsAndServicesSold14 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][5]
    operatingIncome14 = quarterly_statementsDump.loc['operatingIncome'][5]
    sellingGeneralAndAdministrative14 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][5]
    researchAndDevelopment14 = quarterly_statementsDump.loc['researchAndDevelopment'][5]
    operatingExpenses14 = quarterly_statementsDump.loc['operatingExpenses'][5]
    investmentIncomeNet14 = quarterly_statementsDump.loc['investmentIncomeNet'][5]
    netInterestIncome14 = quarterly_statementsDump.loc['netInterestIncome'][5]
    interestIncome14 = quarterly_statementsDump.loc['interestIncome'][5]
    interestExpense14 = quarterly_statementsDump.loc['interestExpense'][5]
    nonInterestIncome14 = quarterly_statementsDump.loc['nonInterestIncome'][5]
    otherNonOperatingIncome14 = quarterly_statementsDump.loc['otherNonOperatingIncome'][5]
    depreciation14 = quarterly_statementsDump.loc['depreciation'][5]
    depreciationAndAmortization14 = quarterly_statementsDump.loc['depreciationAndAmortization'][5]
    incomeBeforeTax14 = quarterly_statementsDump.loc['incomeBeforeTax'][5]
    incomeTaxExpense14 = quarterly_statementsDump.loc['incomeTaxExpense'][5]
    interestAndDebtExpense14 = quarterly_statementsDump.loc['interestAndDebtExpense'][5]
    netIncomeFromContinuingOperations14 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][5]
    comprehensiveIncomeNetOfTax14 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][5]
    ebit14 = quarterly_statementsDump.loc['ebit'][5]
    ebitda14 = quarterly_statementsDump.loc['ebitda'][5]
    # netIncome14 = quarterly_statementsDump.loc['netIncome'][5]

    # Balance Sheet Values for tm14
    totalAssets14 = quarterly_statementsDump.loc['totalAssets'][5]
    totalCurrentAssets14 = quarterly_statementsDump.loc['totalCurrentAssets'][5]
    cashAndCashEquivalentsAtCarryingValue14 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][5]
    cashAndShortTermInvestments14 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][5]
    inventory14 = quarterly_statementsDump.loc['inventory'][5]
    currentNetReceivables14 = quarterly_statementsDump.loc['currentNetReceivables'][5]
    totalNonCurrentAssets14 = quarterly_statementsDump.loc['totalNonCurrentAssets'][5]
    propertyPlantEquipment14 = quarterly_statementsDump.loc['propertyPlantEquipment'][5]
    accumulatedDepreciationAmortizationPPE14 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][5]
    intangibleAssets14 = quarterly_statementsDump.loc['intangibleAssets'][5]
    intangibleAssetsExcludingGoodwill14 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][5]
    goodwill14 = quarterly_statementsDump.loc['goodwill'][5]
    investments14 = quarterly_statementsDump.loc['investments'][5]
    longTermInvestments14 = quarterly_statementsDump.loc['longTermInvestments'][5]
    shortTermInvestments14 = quarterly_statementsDump.loc['shortTermInvestments'][5]
    otherCurrentAssets14 = quarterly_statementsDump.loc['otherCurrentAssets'][5]
    otherNonCurrrentAssets14 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][5]
    totalLiabilities14 = quarterly_statementsDump.loc['totalLiabilities'][5]
    totalCurrentLiabilities14 = quarterly_statementsDump.loc['totalCurrentLiabilities'][5]
    currentAccountsPayable14 = quarterly_statementsDump.loc['currentAccountsPayable'][5]
    deferredRevenue14 = quarterly_statementsDump.loc['deferredRevenue'][5]
    currentDebt14 = quarterly_statementsDump.loc['currentDebt'][5]
    shortTermDebt14 = quarterly_statementsDump.loc['shortTermDebt'][5]
    totalNonCurrentLiabilities14 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][5]
    capitalLeaseObligations14 = quarterly_statementsDump.loc['capitalLeaseObligations'][5]
    longTermDebt14 = quarterly_statementsDump.loc['longTermDebt'][5]
    currentLongTermDebt14 = quarterly_statementsDump.loc['currentLongTermDebt'][5]
    longTermDebtNoncurrent14 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][5]
    shortLongTermDebtTotal14 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][5]
    otherCurrentLiabilities14 = quarterly_statementsDump.loc['otherCurrentLiabilities'][5]
    otherNonCurrentLiabilities14 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][5]
    totalShareholderEquity14 = quarterly_statementsDump.loc['totalShareholderEquity'][5]
    treasuryStock14 = quarterly_statementsDump.loc['treasuryStock'][5]
    retainedEarnings14 = quarterly_statementsDump.loc['retainedEarnings'][5]
    commonStock14 = quarterly_statementsDump.loc['commonStock'][5]
    commonStockSharesOutstanding14 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][5]

    # Cash-Flow Statement values for tm14
    operatingCashflow14 = quarterly_statementsDump.loc['operatingCashflow'][5]
    paymentsForOperatingActivities14 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][5]
    proceedsFromOperatingActivities14 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][5]
    changeInOperatingLiabilities14 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][5]
    changeInOperatingAssets14 = quarterly_statementsDump.loc['changeInOperatingAssets'][5]
    depreciationDepletionAndAmortization14 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][5]
    capitalExpenditures14 = quarterly_statementsDump.loc['capitalExpenditures'][5]
    changeInReceivables14 = quarterly_statementsDump.loc['changeInReceivables'][5]
    changeInInventory14 = quarterly_statementsDump.loc['changeInInventory'][5]
    profitLoss14 = quarterly_statementsDump.loc['profitLoss'][5]
    cashflowFromInvestment14 = quarterly_statementsDump.loc['cashflowFromInvestment'][5]
    cashflowFromFinancing14 = quarterly_statementsDump.loc['cashflowFromFinancing'][5]
    proceedsFromRepaymentsOfShortTermDebt14 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][5]
    paymentsForRepurchaseOfCommonStock14 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][5]
    paymentsForRepurchaseOfEquity14 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][5]
    paymentsForRepurchaseOfPreferredStock14 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][5]
    dividendPayout14 = quarterly_statementsDump.loc['dividendPayout'][5]
    dividendPayoutCommonStock14 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][5]
    dividendPayoutPreferredStock14 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][5]
    proceedsFromIssuanceOfCommonStock14 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][5]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet14 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][5]
    proceedsFromIssuanceOfPreferredStock14 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][5]
    proceedsFromRepurchaseOfEquity14 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][5]
    proceedsFromSaleOfTreasuryStock14 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][5]
    changeInCashAndCashEquivalents14 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][5]
    changeInExchangeRate14 = quarterly_statementsDump.loc['changeInExchangeRate'][5]
    netIncome14 = quarterly_statementsDump.loc['netIncome'][5]

    ## TM13 VARIABLES
    # Income Statement Variables for tm13
    gross_profit13 = quarterly_statementsDump.loc['grossProfit'][6]
    totalRevenue13 = quarterly_statementsDump.loc['totalRevenue'][6]
    costOfRevenue13 = quarterly_statementsDump.loc['costOfRevenue'][6]
    costofGoodsAndServicesSold13 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][6]
    operatingIncome13 = quarterly_statementsDump.loc['operatingIncome'][6]
    sellingGeneralAndAdministrative13 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][6]
    researchAndDevelopment13 = quarterly_statementsDump.loc['researchAndDevelopment'][6]
    operatingExpenses13 = quarterly_statementsDump.loc['operatingExpenses'][6]
    investmentIncomeNet13 = quarterly_statementsDump.loc['investmentIncomeNet'][6]
    netInterestIncome13 = quarterly_statementsDump.loc['netInterestIncome'][6]
    interestIncome13 = quarterly_statementsDump.loc['interestIncome'][6]
    interestExpense13 = quarterly_statementsDump.loc['interestExpense'][6]
    nonInterestIncome13 = quarterly_statementsDump.loc['nonInterestIncome'][6]
    otherNonOperatingIncome13 = quarterly_statementsDump.loc['otherNonOperatingIncome'][6]
    depreciation13 = quarterly_statementsDump.loc['depreciation'][6]
    depreciationAndAmortization13 = quarterly_statementsDump.loc['depreciationAndAmortization'][6]
    incomeBeforeTax13 = quarterly_statementsDump.loc['incomeBeforeTax'][6]
    incomeTaxExpense13 = quarterly_statementsDump.loc['incomeTaxExpense'][6]
    interestAndDebtExpense13 = quarterly_statementsDump.loc['interestAndDebtExpense'][6]
    netIncomeFromContinuingOperations13 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][6]
    comprehensiveIncomeNetOfTax13 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][6]
    ebit13 = quarterly_statementsDump.loc['ebit'][6]
    ebitda13 = quarterly_statementsDump.loc['ebitda'][6]
    # netIncome13 = quarterly_statementsDump.loc['netIncome'][6]

    # Balance Sheet Values for tm13
    totalAssets13 = quarterly_statementsDump.loc['totalAssets'][6]
    totalCurrentAssets13 = quarterly_statementsDump.loc['totalCurrentAssets'][6]
    cashAndCashEquivalentsAtCarryingValue13 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][6]
    cashAndShortTermInvestments13 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][6]
    inventory13 = quarterly_statementsDump.loc['inventory'][6]
    currentNetReceivables13 = quarterly_statementsDump.loc['currentNetReceivables'][6]
    totalNonCurrentAssets13 = quarterly_statementsDump.loc['totalNonCurrentAssets'][6]
    propertyPlantEquipment13 = quarterly_statementsDump.loc['propertyPlantEquipment'][6]
    accumulatedDepreciationAmortizationPPE13 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][6]
    intangibleAssets13 = quarterly_statementsDump.loc['intangibleAssets'][6]
    intangibleAssetsExcludingGoodwill13 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][6]
    goodwill13 = quarterly_statementsDump.loc['goodwill'][6]
    investments13 = quarterly_statementsDump.loc['investments'][6]
    longTermInvestments13 = quarterly_statementsDump.loc['longTermInvestments'][6]
    shortTermInvestments13 = quarterly_statementsDump.loc['shortTermInvestments'][6]
    otherCurrentAssets13 = quarterly_statementsDump.loc['otherCurrentAssets'][6]
    otherNonCurrrentAssets13 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][6]
    totalLiabilities13 = quarterly_statementsDump.loc['totalLiabilities'][6]
    totalCurrentLiabilities13 = quarterly_statementsDump.loc['totalCurrentLiabilities'][6]
    currentAccountsPayable13 = quarterly_statementsDump.loc['currentAccountsPayable'][6]
    deferredRevenue13 = quarterly_statementsDump.loc['deferredRevenue'][6]
    currentDebt13 = quarterly_statementsDump.loc['currentDebt'][6]
    shortTermDebt13 = quarterly_statementsDump.loc['shortTermDebt'][6]
    totalNonCurrentLiabilities13 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][6]
    capitalLeaseObligations13 = quarterly_statementsDump.loc['capitalLeaseObligations'][6]
    longTermDebt13 = quarterly_statementsDump.loc['longTermDebt'][6]
    currentLongTermDebt13 = quarterly_statementsDump.loc['currentLongTermDebt'][6]
    longTermDebtNoncurrent13 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][6]
    shortLongTermDebtTotal13 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][6]
    otherCurrentLiabilities13 = quarterly_statementsDump.loc['otherCurrentLiabilities'][6]
    otherNonCurrentLiabilities13 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][6]
    totalShareholderEquity13 = quarterly_statementsDump.loc['totalShareholderEquity'][6]
    treasuryStock13 = quarterly_statementsDump.loc['treasuryStock'][6]
    retainedEarnings13 = quarterly_statementsDump.loc['retainedEarnings'][6]
    commonStock13 = quarterly_statementsDump.loc['commonStock'][6]
    commonStockSharesOutstanding13 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][6]

    # Cash-Flow Statement values for tm13
    operatingCashflow13 = quarterly_statementsDump.loc['operatingCashflow'][6]
    paymentsForOperatingActivities13 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][6]
    proceedsFromOperatingActivities13 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][6]
    changeInOperatingLiabilities13 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][6]
    changeInOperatingAssets13 = quarterly_statementsDump.loc['changeInOperatingAssets'][6]
    depreciationDepletionAndAmortization13 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][6]
    capitalExpenditures13 = quarterly_statementsDump.loc['capitalExpenditures'][6]
    changeInReceivables13 = quarterly_statementsDump.loc['changeInReceivables'][6]
    changeInInventory13 = quarterly_statementsDump.loc['changeInInventory'][6]
    profitLoss13 = quarterly_statementsDump.loc['profitLoss'][6]
    cashflowFromInvestment13 = quarterly_statementsDump.loc['cashflowFromInvestment'][6]
    cashflowFromFinancing13 = quarterly_statementsDump.loc['cashflowFromFinancing'][6]
    proceedsFromRepaymentsOfShortTermDebt13 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][6]
    paymentsForRepurchaseOfCommonStock13 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][6]
    paymentsForRepurchaseOfEquity13 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][6]
    paymentsForRepurchaseOfPreferredStock13 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][6]
    dividendPayout13 = quarterly_statementsDump.loc['dividendPayout'][6]
    dividendPayoutCommonStock13 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][6]
    dividendPayoutPreferredStock13 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][6]
    proceedsFromIssuanceOfCommonStock13 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][6]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet13 = \
    quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][6]
    proceedsFromIssuanceOfPreferredStock13 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][6]
    proceedsFromRepurchaseOfEquity13 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][6]
    proceedsFromSaleOfTreasuryStock13 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][6]
    changeInCashAndCashEquivalents13 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][6]
    changeInExchangeRate13 = quarterly_statementsDump.loc['changeInExchangeRate'][6]
    netIncome13 = quarterly_statementsDump.loc['netIncome'][6]

    ## TM12 VARIABLES
    # Income Statement Variables for tm12
    gross_profit12 = quarterly_statementsDump.loc['grossProfit'][7]
    totalRevenue12 = quarterly_statementsDump.loc['totalRevenue'][7]
    costOfRevenue12 = quarterly_statementsDump.loc['costOfRevenue'][7]
    costofGoodsAndServicesSold12 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][7]
    operatingIncome12 = quarterly_statementsDump.loc['operatingIncome'][7]
    sellingGeneralAndAdministrative12 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][7]
    researchAndDevelopment12 = quarterly_statementsDump.loc['researchAndDevelopment'][7]
    operatingExpenses12 = quarterly_statementsDump.loc['operatingExpenses'][7]
    investmentIncomeNet12 = quarterly_statementsDump.loc['investmentIncomeNet'][7]
    netInterestIncome12 = quarterly_statementsDump.loc['netInterestIncome'][7]
    interestIncome12 = quarterly_statementsDump.loc['interestIncome'][7]
    interestExpense12 = quarterly_statementsDump.loc['interestExpense'][7]
    nonInterestIncome12 = quarterly_statementsDump.loc['nonInterestIncome'][7]
    otherNonOperatingIncome12 = quarterly_statementsDump.loc['otherNonOperatingIncome'][7]
    depreciation12 = quarterly_statementsDump.loc['depreciation'][7]
    depreciationAndAmortization12 = quarterly_statementsDump.loc['depreciationAndAmortization'][7]
    incomeBeforeTax12 = quarterly_statementsDump.loc['incomeBeforeTax'][7]
    incomeTaxExpense12 = quarterly_statementsDump.loc['incomeTaxExpense'][7]
    interestAndDebtExpense12 = quarterly_statementsDump.loc['interestAndDebtExpense'][7]
    netIncomeFromContinuingOperations12 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][7]
    comprehensiveIncomeNetOfTax12 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][7]
    ebit12 = quarterly_statementsDump.loc['ebit'][7]
    ebitda12 = quarterly_statementsDump.loc['ebitda'][7]
    # netIncome12 = quarterly_statementsDump.loc['netIncome'][7]

    # Balance Sheet Values for tm12
    totalAssets12 = quarterly_statementsDump.loc['totalAssets'][7]
    totalCurrentAssets12 = quarterly_statementsDump.loc['totalCurrentAssets'][7]
    cashAndCashEquivalentsAtCarryingValue12 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][7]
    cashAndShortTermInvestments12 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][7]
    inventory12 = quarterly_statementsDump.loc['inventory'][7]
    currentNetReceivables12 = quarterly_statementsDump.loc['currentNetReceivables'][7]
    totalNonCurrentAssets12 = quarterly_statementsDump.loc['totalNonCurrentAssets'][7]
    propertyPlantEquipment12 = quarterly_statementsDump.loc['propertyPlantEquipment'][7]
    accumulatedDepreciationAmortizationPPE12 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][7]
    intangibleAssets12 = quarterly_statementsDump.loc['intangibleAssets'][7]
    intangibleAssetsExcludingGoodwill12 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][7]
    goodwill12 = quarterly_statementsDump.loc['goodwill'][7]
    investments12 = quarterly_statementsDump.loc['investments'][7]
    longTermInvestments12 = quarterly_statementsDump.loc['longTermInvestments'][7]
    shortTermInvestments12 = quarterly_statementsDump.loc['shortTermInvestments'][7]
    otherCurrentAssets12 = quarterly_statementsDump.loc['otherCurrentAssets'][7]
    otherNonCurrrentAssets12 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][7]
    totalLiabilities12 = quarterly_statementsDump.loc['totalLiabilities'][7]
    totalCurrentLiabilities12 = quarterly_statementsDump.loc['totalCurrentLiabilities'][7]
    currentAccountsPayable12 = quarterly_statementsDump.loc['currentAccountsPayable'][7]
    deferredRevenue12 = quarterly_statementsDump.loc['deferredRevenue'][7]
    currentDebt12 = quarterly_statementsDump.loc['currentDebt'][7]
    shortTermDebt12 = quarterly_statementsDump.loc['shortTermDebt'][7]
    totalNonCurrentLiabilities12 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][7]
    capitalLeaseObligations12 = quarterly_statementsDump.loc['capitalLeaseObligations'][7]
    longTermDebt12 = quarterly_statementsDump.loc['longTermDebt'][7]
    currentLongTermDebt12 = quarterly_statementsDump.loc['currentLongTermDebt'][7]
    longTermDebtNoncurrent12 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][7]
    shortLongTermDebtTotal12 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][7]
    otherCurrentLiabilities12 = quarterly_statementsDump.loc['otherCurrentLiabilities'][7]
    otherNonCurrentLiabilities12 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][7]
    totalShareholderEquity12 = quarterly_statementsDump.loc['totalShareholderEquity'][7]
    treasuryStock12 = quarterly_statementsDump.loc['treasuryStock'][7]
    retainedEarnings12 = quarterly_statementsDump.loc['retainedEarnings'][7]
    commonStock12 = quarterly_statementsDump.loc['commonStock'][7]
    commonStockSharesOutstanding12 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][7]

    # Cash-Flow Statement values for tm12
    operatingCashflow12 = quarterly_statementsDump.loc['operatingCashflow'][7]
    paymentsForOperatingActivities12 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][7]
    proceedsFromOperatingActivities12 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][7]
    changeInOperatingLiabilities12 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][7]
    changeInOperatingAssets12 = quarterly_statementsDump.loc['changeInOperatingAssets'][7]
    depreciationDepletionAndAmortization12 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][7]
    capitalExpenditures12 = quarterly_statementsDump.loc['capitalExpenditures'][7]
    changeInReceivables12 = quarterly_statementsDump.loc['changeInReceivables'][7]
    changeInInventory12 = quarterly_statementsDump.loc['changeInInventory'][7]
    profitLoss12 = quarterly_statementsDump.loc['profitLoss'][7]
    cashflowFromInvestment12 = quarterly_statementsDump.loc['cashflowFromInvestment'][7]
    cashflowFromFinancing12 = quarterly_statementsDump.loc['cashflowFromFinancing'][7]
    proceedsFromRepaymentsOfShortTermDebt12 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][7]
    paymentsForRepurchaseOfCommonStock12 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][7]
    paymentsForRepurchaseOfEquity12 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][7]
    paymentsForRepurchaseOfPreferredStock12 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][7]
    dividendPayout12 = quarterly_statementsDump.loc['dividendPayout'][7]
    dividendPayoutCommonStock12 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][7]
    dividendPayoutPreferredStock12 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][7]
    proceedsFromIssuanceOfCommonStock12 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][7]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet12 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][7]
    proceedsFromIssuanceOfPreferredStock12 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][7]
    proceedsFromRepurchaseOfEquity12 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][7]
    proceedsFromSaleOfTreasuryStock12 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][7]
    changeInCashAndCashEquivalents12 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][7]
    changeInExchangeRate12 = quarterly_statementsDump.loc['changeInExchangeRate'][7]
    netIncome12 = quarterly_statementsDump.loc['netIncome'][7]

    ## TM11 VARIABLES
    # Income Statement Variables for tm11
    gross_profit11 = quarterly_statementsDump.loc['grossProfit'][8]
    totalRevenue11 = quarterly_statementsDump.loc['totalRevenue'][8]
    costOfRevenue11 = quarterly_statementsDump.loc['costOfRevenue'][8]
    costofGoodsAndServicesSold11 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][8]
    operatingIncome11 = quarterly_statementsDump.loc['operatingIncome'][8]
    sellingGeneralAndAdministrative11 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][8]
    researchAndDevelopment11 = quarterly_statementsDump.loc['researchAndDevelopment'][8]
    operatingExpenses11 = quarterly_statementsDump.loc['operatingExpenses'][8]
    investmentIncomeNet11 = quarterly_statementsDump.loc['investmentIncomeNet'][8]
    netInterestIncome11 = quarterly_statementsDump.loc['netInterestIncome'][8]
    interestIncome11 = quarterly_statementsDump.loc['interestIncome'][8]
    interestExpense11 = quarterly_statementsDump.loc['interestExpense'][8]
    nonInterestIncome11 = quarterly_statementsDump.loc['nonInterestIncome'][8]
    otherNonOperatingIncome11 = quarterly_statementsDump.loc['otherNonOperatingIncome'][8]
    depreciation11 = quarterly_statementsDump.loc['depreciation'][8]
    depreciationAndAmortization11 = quarterly_statementsDump.loc['depreciationAndAmortization'][8]
    incomeBeforeTax11 = quarterly_statementsDump.loc['incomeBeforeTax'][8]
    incomeTaxExpense11 = quarterly_statementsDump.loc['incomeTaxExpense'][8]
    interestAndDebtExpense11 = quarterly_statementsDump.loc['interestAndDebtExpense'][8]
    netIncomeFromContinuingOperations11 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][8]
    comprehensiveIncomeNetOfTax11 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][8]
    ebit11 = quarterly_statementsDump.loc['ebit'][8]
    ebitda11 = quarterly_statementsDump.loc['ebitda'][8]
    # netIncome11 = quarterly_statementsDump.loc['netIncome'][8]

    # Balance Sheet Values for tm11
    totalAssets11 = quarterly_statementsDump.loc['totalAssets'][8]
    totalCurrentAssets11 = quarterly_statementsDump.loc['totalCurrentAssets'][8]
    cashAndCashEquivalentsAtCarryingValue11 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][8]
    cashAndShortTermInvestments11 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][8]
    inventory11 = quarterly_statementsDump.loc['inventory'][8]
    currentNetReceivables11 = quarterly_statementsDump.loc['currentNetReceivables'][8]
    totalNonCurrentAssets11 = quarterly_statementsDump.loc['totalNonCurrentAssets'][8]
    propertyPlantEquipment11 = quarterly_statementsDump.loc['propertyPlantEquipment'][8]
    accumulatedDepreciationAmortizationPPE11 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][8]
    intangibleAssets11 = quarterly_statementsDump.loc['intangibleAssets'][8]
    intangibleAssetsExcludingGoodwill11 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][8]
    goodwill11 = quarterly_statementsDump.loc['goodwill'][8]
    investments11 = quarterly_statementsDump.loc['investments'][8]
    longTermInvestments11 = quarterly_statementsDump.loc['longTermInvestments'][8]
    shortTermInvestments11 = quarterly_statementsDump.loc['shortTermInvestments'][8]
    otherCurrentAssets11 = quarterly_statementsDump.loc['otherCurrentAssets'][8]
    otherNonCurrrentAssets11 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][8]
    totalLiabilities11 = quarterly_statementsDump.loc['totalLiabilities'][8]
    totalCurrentLiabilities11 = quarterly_statementsDump.loc['totalCurrentLiabilities'][8]
    currentAccountsPayable11 = quarterly_statementsDump.loc['currentAccountsPayable'][8]
    deferredRevenue11 = quarterly_statementsDump.loc['deferredRevenue'][8]
    currentDebt11 = quarterly_statementsDump.loc['currentDebt'][8]
    shortTermDebt11 = quarterly_statementsDump.loc['shortTermDebt'][8]
    totalNonCurrentLiabilities11 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][8]
    capitalLeaseObligations11 = quarterly_statementsDump.loc['capitalLeaseObligations'][8]
    longTermDebt11 = quarterly_statementsDump.loc['longTermDebt'][8]
    currentLongTermDebt11 = quarterly_statementsDump.loc['currentLongTermDebt'][8]
    longTermDebtNoncurrent11 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][8]
    shortLongTermDebtTotal11 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][8]
    otherCurrentLiabilities11 = quarterly_statementsDump.loc['otherCurrentLiabilities'][8]
    otherNonCurrentLiabilities11 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][8]
    totalShareholderEquity11 = quarterly_statementsDump.loc['totalShareholderEquity'][8]
    treasuryStock11 = quarterly_statementsDump.loc['treasuryStock'][8]
    retainedEarnings11 = quarterly_statementsDump.loc['retainedEarnings'][8]
    commonStock11 = quarterly_statementsDump.loc['commonStock'][8]
    commonStockSharesOutstanding11 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][8]

    # Cash-Flow Statement values for tm11
    operatingCashflow11 = quarterly_statementsDump.loc['operatingCashflow'][8]
    paymentsForOperatingActivities11 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][8]
    proceedsFromOperatingActivities11 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][8]
    changeInOperatingLiabilities11 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][8]
    changeInOperatingAssets11 = quarterly_statementsDump.loc['changeInOperatingAssets'][8]
    depreciationDepletionAndAmortization11 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][8]
    capitalExpenditures11 = quarterly_statementsDump.loc['capitalExpenditures'][8]
    changeInReceivables11 = quarterly_statementsDump.loc['changeInReceivables'][8]
    changeInInventory11 = quarterly_statementsDump.loc['changeInInventory'][8]
    profitLoss11 = quarterly_statementsDump.loc['profitLoss'][8]
    cashflowFromInvestment11 = quarterly_statementsDump.loc['cashflowFromInvestment'][8]
    cashflowFromFinancing11 = quarterly_statementsDump.loc['cashflowFromFinancing'][8]
    proceedsFromRepaymentsOfShortTermDebt11 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][8]
    paymentsForRepurchaseOfCommonStock11 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][8]
    paymentsForRepurchaseOfEquity11 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][8]
    paymentsForRepurchaseOfPreferredStock11 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][8]
    dividendPayout11 = quarterly_statementsDump.loc['dividendPayout'][8]
    dividendPayoutCommonStock11 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][8]
    dividendPayoutPreferredStock11 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][8]
    proceedsFromIssuanceOfCommonStock11 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][8]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet11 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][8]
    proceedsFromIssuanceOfPreferredStock11 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][8]
    proceedsFromRepurchaseOfEquity11 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][8]
    proceedsFromSaleOfTreasuryStock11 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][8]
    changeInCashAndCashEquivalents11 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][8]
    changeInExchangeRate11 = quarterly_statementsDump.loc['changeInExchangeRate'][8]
    netIncome11 = quarterly_statementsDump.loc['netIncome'][8]

    ## TM10 VARIABLES
    # Income Statement Variables for tm10
    gross_profit10 = quarterly_statementsDump.loc['grossProfit'][9]
    totalRevenue10 = quarterly_statementsDump.loc['totalRevenue'][9]
    costOfRevenue10 = quarterly_statementsDump.loc['costOfRevenue'][9]
    costofGoodsAndServicesSold10 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][9]
    operatingIncome10 = quarterly_statementsDump.loc['operatingIncome'][9]
    sellingGeneralAndAdministrative10 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][9]
    researchAndDevelopment10 = quarterly_statementsDump.loc['researchAndDevelopment'][9]
    operatingExpenses10 = quarterly_statementsDump.loc['operatingExpenses'][9]
    investmentIncomeNet10 = quarterly_statementsDump.loc['investmentIncomeNet'][9]
    netInterestIncome10 = quarterly_statementsDump.loc['netInterestIncome'][9]
    interestIncome10 = quarterly_statementsDump.loc['interestIncome'][9]
    interestExpense10 = quarterly_statementsDump.loc['interestExpense'][9]
    nonInterestIncome10 = quarterly_statementsDump.loc['nonInterestIncome'][9]
    otherNonOperatingIncome10 = quarterly_statementsDump.loc['otherNonOperatingIncome'][9]
    depreciation10 = quarterly_statementsDump.loc['depreciation'][9]
    depreciationAndAmortization10 = quarterly_statementsDump.loc['depreciationAndAmortization'][9]
    incomeBeforeTax10 = quarterly_statementsDump.loc['incomeBeforeTax'][9]
    incomeTaxExpense10 = quarterly_statementsDump.loc['incomeTaxExpense'][9]
    interestAndDebtExpense10 = quarterly_statementsDump.loc['interestAndDebtExpense'][9]
    netIncomeFromContinuingOperations10 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][9]
    comprehensiveIncomeNetOfTax10 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][9]
    ebit10 = quarterly_statementsDump.loc['ebit'][9]
    ebitda10 = quarterly_statementsDump.loc['ebitda'][9]
    # netIncome10 = quarterly_statementsDump.loc['netIncome'][9]

    # Balance Sheet Values for tm10
    totalAssets10 = quarterly_statementsDump.loc['totalAssets'][9]
    totalCurrentAssets10 = quarterly_statementsDump.loc['totalCurrentAssets'][9]
    cashAndCashEquivalentsAtCarryingValue10 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][9]
    cashAndShortTermInvestments10 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][9]
    inventory10 = quarterly_statementsDump.loc['inventory'][9]
    currentNetReceivables10 = quarterly_statementsDump.loc['currentNetReceivables'][9]
    totalNonCurrentAssets10 = quarterly_statementsDump.loc['totalNonCurrentAssets'][9]
    propertyPlantEquipment10 = quarterly_statementsDump.loc['propertyPlantEquipment'][9]
    accumulatedDepreciationAmortizationPPE10 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][9]
    intangibleAssets10 = quarterly_statementsDump.loc['intangibleAssets'][9]
    intangibleAssetsExcludingGoodwill10 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][9]
    goodwill10 = quarterly_statementsDump.loc['goodwill'][9]
    investments10 = quarterly_statementsDump.loc['investments'][9]
    longTermInvestments10 = quarterly_statementsDump.loc['longTermInvestments'][9]
    shortTermInvestments10 = quarterly_statementsDump.loc['shortTermInvestments'][9]
    otherCurrentAssets10 = quarterly_statementsDump.loc['otherCurrentAssets'][9]
    otherNonCurrrentAssets10 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][9]
    totalLiabilities10 = quarterly_statementsDump.loc['totalLiabilities'][9]
    totalCurrentLiabilities10 = quarterly_statementsDump.loc['totalCurrentLiabilities'][9]
    currentAccountsPayable10 = quarterly_statementsDump.loc['currentAccountsPayable'][9]
    deferredRevenue10 = quarterly_statementsDump.loc['deferredRevenue'][9]
    currentDebt10 = quarterly_statementsDump.loc['currentDebt'][9]
    shortTermDebt10 = quarterly_statementsDump.loc['shortTermDebt'][9]
    totalNonCurrentLiabilities10 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][9]
    capitalLeaseObligations10 = quarterly_statementsDump.loc['capitalLeaseObligations'][9]
    longTermDebt10 = quarterly_statementsDump.loc['longTermDebt'][9]
    currentLongTermDebt10 = quarterly_statementsDump.loc['currentLongTermDebt'][9]
    longTermDebtNoncurrent10 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][9]
    shortLongTermDebtTotal10 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][9]
    otherCurrentLiabilities10 = quarterly_statementsDump.loc['otherCurrentLiabilities'][9]
    otherNonCurrentLiabilities10 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][9]
    totalShareholderEquity10 = quarterly_statementsDump.loc['totalShareholderEquity'][9]
    treasuryStock10 = quarterly_statementsDump.loc['treasuryStock'][9]
    retainedEarnings10 = quarterly_statementsDump.loc['retainedEarnings'][9]
    commonStock10 = quarterly_statementsDump.loc['commonStock'][9]
    commonStockSharesOutstanding10 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][9]

    # Cash-Flow Statement values for tm10
    operatingCashflow10 = quarterly_statementsDump.loc['operatingCashflow'][9]
    paymentsForOperatingActivities10 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][9]
    proceedsFromOperatingActivities10 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][9]
    changeInOperatingLiabilities10 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][9]
    changeInOperatingAssets10 = quarterly_statementsDump.loc['changeInOperatingAssets'][9]
    depreciationDepletionAndAmortization10 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][9]
    capitalExpenditures10 = quarterly_statementsDump.loc['capitalExpenditures'][9]
    changeInReceivables10 = quarterly_statementsDump.loc['changeInReceivables'][9]
    changeInInventory10 = quarterly_statementsDump.loc['changeInInventory'][9]
    profitLoss10 = quarterly_statementsDump.loc['profitLoss'][9]
    cashflowFromInvestment10 = quarterly_statementsDump.loc['cashflowFromInvestment'][9]
    cashflowFromFinancing10 = quarterly_statementsDump.loc['cashflowFromFinancing'][9]
    proceedsFromRepaymentsOfShortTermDebt10 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][9]
    paymentsForRepurchaseOfCommonStock10 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][9]
    paymentsForRepurchaseOfEquity10 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][9]
    paymentsForRepurchaseOfPreferredStock10 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][9]
    dividendPayout10 = quarterly_statementsDump.loc['dividendPayout'][9]
    dividendPayoutCommonStock10 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][9]
    dividendPayoutPreferredStock10 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][9]
    proceedsFromIssuanceOfCommonStock10 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][9]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet10 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][9]
    proceedsFromIssuanceOfPreferredStock10 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][9]
    proceedsFromRepurchaseOfEquity10 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][9]
    proceedsFromSaleOfTreasuryStock10 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][9]
    changeInCashAndCashEquivalents10 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][9]
    changeInExchangeRate10 = quarterly_statementsDump.loc['changeInExchangeRate'][9]
    netIncome10 = quarterly_statementsDump.loc['netIncome'][9]

    ## TM9 VARIABLES
    # Income Statement Variables for tm9
    gross_profit9 = quarterly_statementsDump.loc['grossProfit'][10]
    totalRevenue9 = quarterly_statementsDump.loc['totalRevenue'][10]
    costOfRevenue9 = quarterly_statementsDump.loc['costOfRevenue'][10]
    costofGoodsAndServicesSold9 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][10]
    operatingIncome9 = quarterly_statementsDump.loc['operatingIncome'][10]
    sellingGeneralAndAdministrative9 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][10]
    researchAndDevelopment9 = quarterly_statementsDump.loc['researchAndDevelopment'][10]
    operatingExpenses9 = quarterly_statementsDump.loc['operatingExpenses'][10]
    investmentIncomeNet9 = quarterly_statementsDump.loc['investmentIncomeNet'][10]
    netInterestIncome9 = quarterly_statementsDump.loc['netInterestIncome'][10]
    interestIncome9 = quarterly_statementsDump.loc['interestIncome'][10]
    interestExpense9 = quarterly_statementsDump.loc['interestExpense'][10]
    nonInterestIncome9 = quarterly_statementsDump.loc['nonInterestIncome'][10]
    otherNonOperatingIncome9 = quarterly_statementsDump.loc['otherNonOperatingIncome'][10]
    depreciation9 = quarterly_statementsDump.loc['depreciation'][10]
    depreciationAndAmortization9 = quarterly_statementsDump.loc['depreciationAndAmortization'][10]
    incomeBeforeTax9 = quarterly_statementsDump.loc['incomeBeforeTax'][10]
    incomeTaxExpense9 = quarterly_statementsDump.loc['incomeTaxExpense'][10]
    interestAndDebtExpense9 = quarterly_statementsDump.loc['interestAndDebtExpense'][10]
    netIncomeFromContinuingOperations9 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][10]
    comprehensiveIncomeNetOfTax9 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][10]
    ebit9 = quarterly_statementsDump.loc['ebit'][10]
    ebitda9 = quarterly_statementsDump.loc['ebitda'][10]
    # netIncome9 = quarterly_statementsDump.loc['netIncome'][10]

    # Balance Sheet Values for tm9
    totalAssets9 = quarterly_statementsDump.loc['totalAssets'][10]
    totalCurrentAssets9 = quarterly_statementsDump.loc['totalCurrentAssets'][10]
    cashAndCashEquivalentsAtCarryingValue9 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][10]
    cashAndShortTermInvestments9 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][10]
    inventory9 = quarterly_statementsDump.loc['inventory'][10]
    currentNetReceivables9 = quarterly_statementsDump.loc['currentNetReceivables'][10]
    totalNonCurrentAssets9 = quarterly_statementsDump.loc['totalNonCurrentAssets'][10]
    propertyPlantEquipment9 = quarterly_statementsDump.loc['propertyPlantEquipment'][10]
    accumulatedDepreciationAmortizationPPE9 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][10]
    intangibleAssets9 = quarterly_statementsDump.loc['intangibleAssets'][10]
    intangibleAssetsExcludingGoodwill9 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][10]
    goodwill9 = quarterly_statementsDump.loc['goodwill'][10]
    investments9 = quarterly_statementsDump.loc['investments'][10]
    longTermInvestments9 = quarterly_statementsDump.loc['longTermInvestments'][10]
    shortTermInvestments9 = quarterly_statementsDump.loc['shortTermInvestments'][10]
    otherCurrentAssets9 = quarterly_statementsDump.loc['otherCurrentAssets'][10]
    otherNonCurrrentAssets9 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][10]
    totalLiabilities9 = quarterly_statementsDump.loc['totalLiabilities'][10]
    totalCurrentLiabilities9 = quarterly_statementsDump.loc['totalCurrentLiabilities'][10]
    currentAccountsPayable9 = quarterly_statementsDump.loc['currentAccountsPayable'][10]
    deferredRevenue9 = quarterly_statementsDump.loc['deferredRevenue'][10]
    currentDebt9 = quarterly_statementsDump.loc['currentDebt'][10]
    shortTermDebt9 = quarterly_statementsDump.loc['shortTermDebt'][10]
    totalNonCurrentLiabilities9 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][10]
    capitalLeaseObligations9 = quarterly_statementsDump.loc['capitalLeaseObligations'][10]
    longTermDebt9 = quarterly_statementsDump.loc['longTermDebt'][10]
    currentLongTermDebt9 = quarterly_statementsDump.loc['currentLongTermDebt'][10]
    longTermDebtNoncurrent9 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][10]
    shortLongTermDebtTotal9 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][10]
    otherCurrentLiabilities9 = quarterly_statementsDump.loc['otherCurrentLiabilities'][10]
    otherNonCurrentLiabilities9 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][10]
    totalShareholderEquity9 = quarterly_statementsDump.loc['totalShareholderEquity'][10]
    treasuryStock9 = quarterly_statementsDump.loc['treasuryStock'][10]
    retainedEarnings9 = quarterly_statementsDump.loc['retainedEarnings'][10]
    commonStock9 = quarterly_statementsDump.loc['commonStock'][10]
    commonStockSharesOutstanding9 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][10]

    # Cash-Flow Statement values for tm9
    operatingCashflow9 = quarterly_statementsDump.loc['operatingCashflow'][10]
    paymentsForOperatingActivities9 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][10]
    proceedsFromOperatingActivities9 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][10]
    changeInOperatingLiabilities9 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][10]
    changeInOperatingAssets9 = quarterly_statementsDump.loc['changeInOperatingAssets'][10]
    depreciationDepletionAndAmortization9 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][10]
    capitalExpenditures9 = quarterly_statementsDump.loc['capitalExpenditures'][10]
    changeInReceivables9 = quarterly_statementsDump.loc['changeInReceivables'][10]
    changeInInventory9 = quarterly_statementsDump.loc['changeInInventory'][10]
    profitLoss9 = quarterly_statementsDump.loc['profitLoss'][10]
    cashflowFromInvestment9 = quarterly_statementsDump.loc['cashflowFromInvestment'][10]
    cashflowFromFinancing9 = quarterly_statementsDump.loc['cashflowFromFinancing'][10]
    proceedsFromRepaymentsOfShortTermDebt9 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][10]
    paymentsForRepurchaseOfCommonStock9 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][10]
    paymentsForRepurchaseOfEquity9 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][10]
    paymentsForRepurchaseOfPreferredStock9 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][10]
    dividendPayout9 = quarterly_statementsDump.loc['dividendPayout'][10]
    dividendPayoutCommonStock9 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][10]
    dividendPayoutPreferredStock9 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][10]
    proceedsFromIssuanceOfCommonStock9 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][10]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet9 = \
    quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][10]
    proceedsFromIssuanceOfPreferredStock9 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][10]
    proceedsFromRepurchaseOfEquity9 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][10]
    proceedsFromSaleOfTreasuryStock9 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][10]
    changeInCashAndCashEquivalents9 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][10]
    changeInExchangeRate9 = quarterly_statementsDump.loc['changeInExchangeRate'][10]
    netIncome9 = quarterly_statementsDump.loc['netIncome'][10]

    ## TM8 VARIABLES
    # Income Statement Variables for tm8
    gross_profit8 = quarterly_statementsDump.loc['grossProfit'][11]
    totalRevenue8 = quarterly_statementsDump.loc['totalRevenue'][11]
    costOfRevenue8 = quarterly_statementsDump.loc['costOfRevenue'][11]
    costofGoodsAndServicesSold8 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][11]
    operatingIncome8 = quarterly_statementsDump.loc['operatingIncome'][11]
    sellingGeneralAndAdministrative8 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][11]
    researchAndDevelopment8 = quarterly_statementsDump.loc['researchAndDevelopment'][11]
    operatingExpenses8 = quarterly_statementsDump.loc['operatingExpenses'][11]
    investmentIncomeNet8 = quarterly_statementsDump.loc['investmentIncomeNet'][11]
    netInterestIncome8 = quarterly_statementsDump.loc['netInterestIncome'][11]
    interestIncome8 = quarterly_statementsDump.loc['interestIncome'][11]
    interestExpense8 = quarterly_statementsDump.loc['interestExpense'][11]
    nonInterestIncome8 = quarterly_statementsDump.loc['nonInterestIncome'][11]
    otherNonOperatingIncome8 = quarterly_statementsDump.loc['otherNonOperatingIncome'][11]
    depreciation8 = quarterly_statementsDump.loc['depreciation'][11]
    depreciationAndAmortization8 = quarterly_statementsDump.loc['depreciationAndAmortization'][11]
    incomeBeforeTax8 = quarterly_statementsDump.loc['incomeBeforeTax'][11]
    incomeTaxExpense8 = quarterly_statementsDump.loc['incomeTaxExpense'][11]
    interestAndDebtExpense8 = quarterly_statementsDump.loc['interestAndDebtExpense'][11]
    netIncomeFromContinuingOperations8 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][11]
    comprehensiveIncomeNetOfTax8 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][11]
    ebit8 = quarterly_statementsDump.loc['ebit'][11]
    ebitda8 = quarterly_statementsDump.loc['ebitda'][11]
    # netIncome8 = quarterly_statementsDump.loc['netIncome'][11]

    # Balance Sheet Values for tm8
    totalAssets8 = quarterly_statementsDump.loc['totalAssets'][11]
    totalCurrentAssets8 = quarterly_statementsDump.loc['totalCurrentAssets'][11]
    cashAndCashEquivalentsAtCarryingValue8 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][11]
    cashAndShortTermInvestments8 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][11]
    inventory8 = quarterly_statementsDump.loc['inventory'][11]
    currentNetReceivables8 = quarterly_statementsDump.loc['currentNetReceivables'][11]
    totalNonCurrentAssets8 = quarterly_statementsDump.loc['totalNonCurrentAssets'][11]
    propertyPlantEquipment8 = quarterly_statementsDump.loc['propertyPlantEquipment'][11]
    accumulatedDepreciationAmortizationPPE8 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][11]
    intangibleAssets8 = quarterly_statementsDump.loc['intangibleAssets'][11]
    intangibleAssetsExcludingGoodwill8 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][11]
    goodwill8 = quarterly_statementsDump.loc['goodwill'][11]
    investments8 = quarterly_statementsDump.loc['investments'][11]
    longTermInvestments8 = quarterly_statementsDump.loc['longTermInvestments'][11]
    shortTermInvestments8 = quarterly_statementsDump.loc['shortTermInvestments'][11]
    otherCurrentAssets8 = quarterly_statementsDump.loc['otherCurrentAssets'][11]
    otherNonCurrrentAssets8 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][11]
    totalLiabilities8 = quarterly_statementsDump.loc['totalLiabilities'][11]
    totalCurrentLiabilities8 = quarterly_statementsDump.loc['totalCurrentLiabilities'][11]
    currentAccountsPayable8 = quarterly_statementsDump.loc['currentAccountsPayable'][11]
    deferredRevenue8 = quarterly_statementsDump.loc['deferredRevenue'][11]
    currentDebt8 = quarterly_statementsDump.loc['currentDebt'][11]
    shortTermDebt8 = quarterly_statementsDump.loc['shortTermDebt'][11]
    totalNonCurrentLiabilities8 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][11]
    capitalLeaseObligations8 = quarterly_statementsDump.loc['capitalLeaseObligations'][11]
    longTermDebt8 = quarterly_statementsDump.loc['longTermDebt'][11]
    currentLongTermDebt8 = quarterly_statementsDump.loc['currentLongTermDebt'][11]
    longTermDebtNoncurrent8 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][11]
    shortLongTermDebtTotal8 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][11]
    otherCurrentLiabilities8 = quarterly_statementsDump.loc['otherCurrentLiabilities'][11]
    otherNonCurrentLiabilities8 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][11]
    totalShareholderEquity8 = quarterly_statementsDump.loc['totalShareholderEquity'][11]
    treasuryStock8 = quarterly_statementsDump.loc['treasuryStock'][11]
    retainedEarnings8 = quarterly_statementsDump.loc['retainedEarnings'][11]
    commonStock8 = quarterly_statementsDump.loc['commonStock'][11]
    commonStockSharesOutstanding8 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][11]

    # Cash-Flow Statement values for tm8
    operatingCashflow8 = quarterly_statementsDump.loc['operatingCashflow'][11]
    paymentsForOperatingActivities8 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][11]
    proceedsFromOperatingActivities8 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][11]
    changeInOperatingLiabilities8 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][11]
    changeInOperatingAssets8 = quarterly_statementsDump.loc['changeInOperatingAssets'][11]
    depreciationDepletionAndAmortization8 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][11]
    capitalExpenditures8 = quarterly_statementsDump.loc['capitalExpenditures'][11]
    changeInReceivables8 = quarterly_statementsDump.loc['changeInReceivables'][11]
    changeInInventory8 = quarterly_statementsDump.loc['changeInInventory'][11]
    profitLoss8 = quarterly_statementsDump.loc['profitLoss'][11]
    cashflowFromInvestment8 = quarterly_statementsDump.loc['cashflowFromInvestment'][11]
    cashflowFromFinancing8 = quarterly_statementsDump.loc['cashflowFromFinancing'][11]
    proceedsFromRepaymentsOfShortTermDebt8 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][11]
    paymentsForRepurchaseOfCommonStock8 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][11]
    paymentsForRepurchaseOfEquity8 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][11]
    paymentsForRepurchaseOfPreferredStock8 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][11]
    dividendPayout8 = quarterly_statementsDump.loc['dividendPayout'][11]
    dividendPayoutCommonStock8 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][11]
    dividendPayoutPreferredStock8 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][11]
    proceedsFromIssuanceOfCommonStock8 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][11]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet8 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][11]
    proceedsFromIssuanceOfPreferredStock8 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][11]
    proceedsFromRepurchaseOfEquity8 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][11]
    proceedsFromSaleOfTreasuryStock8 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][11]
    changeInCashAndCashEquivalents8 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][11]
    changeInExchangeRate8 = quarterly_statementsDump.loc['changeInExchangeRate'][11]
    netIncome8 = quarterly_statementsDump.loc['netIncome'][11]

    ## TM7 VARIABLES
    # Income Statement Variables for tm7
    gross_profit7 = quarterly_statementsDump.loc['grossProfit'][12]
    totalRevenue7 = quarterly_statementsDump.loc['totalRevenue'][12]
    costOfRevenue7 = quarterly_statementsDump.loc['costOfRevenue'][12]
    costofGoodsAndServicesSold7 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][12]
    operatingIncome7 = quarterly_statementsDump.loc['operatingIncome'][12]
    sellingGeneralAndAdministrative7 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][12]
    researchAndDevelopment7 = quarterly_statementsDump.loc['researchAndDevelopment'][12]
    operatingExpenses7 = quarterly_statementsDump.loc['operatingExpenses'][12]
    investmentIncomeNet7 = quarterly_statementsDump.loc['investmentIncomeNet'][12]
    netInterestIncome7 = quarterly_statementsDump.loc['netInterestIncome'][12]
    interestIncome7 = quarterly_statementsDump.loc['interestIncome'][12]
    interestExpense7 = quarterly_statementsDump.loc['interestExpense'][12]
    nonInterestIncome7 = quarterly_statementsDump.loc['nonInterestIncome'][12]
    otherNonOperatingIncome7 = quarterly_statementsDump.loc['otherNonOperatingIncome'][12]
    depreciation7 = quarterly_statementsDump.loc['depreciation'][12]
    depreciationAndAmortization7 = quarterly_statementsDump.loc['depreciationAndAmortization'][12]
    incomeBeforeTax7 = quarterly_statementsDump.loc['incomeBeforeTax'][12]
    incomeTaxExpense7 = quarterly_statementsDump.loc['incomeTaxExpense'][12]
    interestAndDebtExpense7 = quarterly_statementsDump.loc['interestAndDebtExpense'][12]
    netIncomeFromContinuingOperations7 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][12]
    comprehensiveIncomeNetOfTax7 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][12]
    ebit7 = quarterly_statementsDump.loc['ebit'][12]
    ebitda7 = quarterly_statementsDump.loc['ebitda'][12]
    # netIncome7 = quarterly_statementsDump.loc['netIncome'][12]

    # Balance Sheet Values for tm7
    totalAssets7 = quarterly_statementsDump.loc['totalAssets'][12]
    totalCurrentAssets7 = quarterly_statementsDump.loc['totalCurrentAssets'][12]
    cashAndCashEquivalentsAtCarryingValue7 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][12]
    cashAndShortTermInvestments7 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][12]
    inventory7 = quarterly_statementsDump.loc['inventory'][12]
    currentNetReceivables7 = quarterly_statementsDump.loc['currentNetReceivables'][12]
    totalNonCurrentAssets7 = quarterly_statementsDump.loc['totalNonCurrentAssets'][12]
    propertyPlantEquipment7 = quarterly_statementsDump.loc['propertyPlantEquipment'][12]
    accumulatedDepreciationAmortizationPPE7 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][12]
    intangibleAssets7 = quarterly_statementsDump.loc['intangibleAssets'][12]
    intangibleAssetsExcludingGoodwill7 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][12]
    goodwill7 = quarterly_statementsDump.loc['goodwill'][12]
    investments7 = quarterly_statementsDump.loc['investments'][12]
    longTermInvestments7 = quarterly_statementsDump.loc['longTermInvestments'][12]
    shortTermInvestments7 = quarterly_statementsDump.loc['shortTermInvestments'][12]
    otherCurrentAssets7 = quarterly_statementsDump.loc['otherCurrentAssets'][12]
    otherNonCurrrentAssets7 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][12]
    totalLiabilities7 = quarterly_statementsDump.loc['totalLiabilities'][12]
    totalCurrentLiabilities7 = quarterly_statementsDump.loc['totalCurrentLiabilities'][12]
    currentAccountsPayable7 = quarterly_statementsDump.loc['currentAccountsPayable'][12]
    deferredRevenue7 = quarterly_statementsDump.loc['deferredRevenue'][12]
    currentDebt7 = quarterly_statementsDump.loc['currentDebt'][12]
    shortTermDebt7 = quarterly_statementsDump.loc['shortTermDebt'][12]
    totalNonCurrentLiabilities7 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][12]
    capitalLeaseObligations7 = quarterly_statementsDump.loc['capitalLeaseObligations'][12]
    longTermDebt7 = quarterly_statementsDump.loc['longTermDebt'][12]
    currentLongTermDebt7 = quarterly_statementsDump.loc['currentLongTermDebt'][12]
    longTermDebtNoncurrent7 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][12]
    shortLongTermDebtTotal7 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][12]
    otherCurrentLiabilities7 = quarterly_statementsDump.loc['otherCurrentLiabilities'][12]
    otherNonCurrentLiabilities7 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][12]
    totalShareholderEquity7 = quarterly_statementsDump.loc['totalShareholderEquity'][12]
    treasuryStock7 = quarterly_statementsDump.loc['treasuryStock'][12]
    retainedEarnings7 = quarterly_statementsDump.loc['retainedEarnings'][12]
    commonStock7 = quarterly_statementsDump.loc['commonStock'][12]
    commonStockSharesOutstanding7 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][12]

    # Cash-Flow Statement values for tm7
    operatingCashflow7 = quarterly_statementsDump.loc['operatingCashflow'][12]
    paymentsForOperatingActivities7 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][12]
    proceedsFromOperatingActivities7 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][12]
    changeInOperatingLiabilities7 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][12]
    changeInOperatingAssets7 = quarterly_statementsDump.loc['changeInOperatingAssets'][12]
    depreciationDepletionAndAmortization7 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][12]
    capitalExpenditures7 = quarterly_statementsDump.loc['capitalExpenditures'][12]
    changeInReceivables7 = quarterly_statementsDump.loc['changeInReceivables'][12]
    changeInInventory7 = quarterly_statementsDump.loc['changeInInventory'][12]
    profitLoss7 = quarterly_statementsDump.loc['profitLoss'][12]
    cashflowFromInvestment7 = quarterly_statementsDump.loc['cashflowFromInvestment'][12]
    cashflowFromFinancing7 = quarterly_statementsDump.loc['cashflowFromFinancing'][12]
    proceedsFromRepaymentsOfShortTermDebt7 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][12]
    paymentsForRepurchaseOfCommonStock7 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][12]
    paymentsForRepurchaseOfEquity7 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][12]
    paymentsForRepurchaseOfPreferredStock7 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][12]
    dividendPayout7 = quarterly_statementsDump.loc['dividendPayout'][12]
    dividendPayoutCommonStock7 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][12]
    dividendPayoutPreferredStock7 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][12]
    proceedsFromIssuanceOfCommonStock7 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][12]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet7 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][12]
    proceedsFromIssuanceOfPreferredStock7 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][12]
    proceedsFromRepurchaseOfEquity7 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][12]
    proceedsFromSaleOfTreasuryStock7 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][12]
    changeInCashAndCashEquivalents7 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][12]
    changeInExchangeRate7 = quarterly_statementsDump.loc['changeInExchangeRate'][12]
    netIncome7 = quarterly_statementsDump.loc['netIncome'][12]

    ## TM6 VARIABLES
    # Income Statement Variables for tm6
    gross_profit6 = quarterly_statementsDump.loc['grossProfit'][13]
    totalRevenue6 = quarterly_statementsDump.loc['totalRevenue'][13]
    costOfRevenue6 = quarterly_statementsDump.loc['costOfRevenue'][13]
    costofGoodsAndServicesSold6 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][13]
    operatingIncome6 = quarterly_statementsDump.loc['operatingIncome'][13]
    sellingGeneralAndAdministrative6 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][13]
    researchAndDevelopment6 = quarterly_statementsDump.loc['researchAndDevelopment'][13]
    operatingExpenses6 = quarterly_statementsDump.loc['operatingExpenses'][13]
    investmentIncomeNet6 = quarterly_statementsDump.loc['investmentIncomeNet'][13]
    netInterestIncome6 = quarterly_statementsDump.loc['netInterestIncome'][13]
    interestIncome6 = quarterly_statementsDump.loc['interestIncome'][13]
    interestExpense6 = quarterly_statementsDump.loc['interestExpense'][13]
    nonInterestIncome6 = quarterly_statementsDump.loc['nonInterestIncome'][13]
    otherNonOperatingIncome6 = quarterly_statementsDump.loc['otherNonOperatingIncome'][13]
    depreciation6 = quarterly_statementsDump.loc['depreciation'][13]
    depreciationAndAmortization6 = quarterly_statementsDump.loc['depreciationAndAmortization'][13]
    incomeBeforeTax6 = quarterly_statementsDump.loc['incomeBeforeTax'][13]
    incomeTaxExpense6 = quarterly_statementsDump.loc['incomeTaxExpense'][13]
    interestAndDebtExpense6 = quarterly_statementsDump.loc['interestAndDebtExpense'][13]
    netIncomeFromContinuingOperations6 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][13]
    comprehensiveIncomeNetOfTax6 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][13]
    ebit6 = quarterly_statementsDump.loc['ebit'][13]
    ebitda6 = quarterly_statementsDump.loc['ebitda'][13]
    # netIncome6 = quarterly_statementsDump.loc['netIncome'][13]

    # Balance Sheet Values for tm6
    totalAssets6 = quarterly_statementsDump.loc['totalAssets'][13]
    totalCurrentAssets6 = quarterly_statementsDump.loc['totalCurrentAssets'][13]
    cashAndCashEquivalentsAtCarryingValue6 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][13]
    cashAndShortTermInvestments6 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][13]
    inventory6 = quarterly_statementsDump.loc['inventory'][13]
    currentNetReceivables6 = quarterly_statementsDump.loc['currentNetReceivables'][13]
    totalNonCurrentAssets6 = quarterly_statementsDump.loc['totalNonCurrentAssets'][13]
    propertyPlantEquipment6 = quarterly_statementsDump.loc['propertyPlantEquipment'][13]
    accumulatedDepreciationAmortizationPPE6 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][13]
    intangibleAssets6 = quarterly_statementsDump.loc['intangibleAssets'][13]
    intangibleAssetsExcludingGoodwill6 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][13]
    goodwill6 = quarterly_statementsDump.loc['goodwill'][13]
    investments6 = quarterly_statementsDump.loc['investments'][13]
    longTermInvestments6 = quarterly_statementsDump.loc['longTermInvestments'][13]
    shortTermInvestments6 = quarterly_statementsDump.loc['shortTermInvestments'][13]
    otherCurrentAssets6 = quarterly_statementsDump.loc['otherCurrentAssets'][13]
    otherNonCurrrentAssets6 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][13]
    totalLiabilities6 = quarterly_statementsDump.loc['totalLiabilities'][13]
    totalCurrentLiabilities6 = quarterly_statementsDump.loc['totalCurrentLiabilities'][13]
    currentAccountsPayable6 = quarterly_statementsDump.loc['currentAccountsPayable'][13]
    deferredRevenue6 = quarterly_statementsDump.loc['deferredRevenue'][13]
    currentDebt6 = quarterly_statementsDump.loc['currentDebt'][13]
    shortTermDebt6 = quarterly_statementsDump.loc['shortTermDebt'][13]
    totalNonCurrentLiabilities6 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][13]
    capitalLeaseObligations6 = quarterly_statementsDump.loc['capitalLeaseObligations'][13]
    longTermDebt6 = quarterly_statementsDump.loc['longTermDebt'][13]
    currentLongTermDebt6 = quarterly_statementsDump.loc['currentLongTermDebt'][13]
    longTermDebtNoncurrent6 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][13]
    shortLongTermDebtTotal6 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][13]
    otherCurrentLiabilities6 = quarterly_statementsDump.loc['otherCurrentLiabilities'][13]
    otherNonCurrentLiabilities6 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][13]
    totalShareholderEquity6 = quarterly_statementsDump.loc['totalShareholderEquity'][13]
    treasuryStock6 = quarterly_statementsDump.loc['treasuryStock'][13]
    retainedEarnings6 = quarterly_statementsDump.loc['retainedEarnings'][13]
    commonStock6 = quarterly_statementsDump.loc['commonStock'][13]
    commonStockSharesOutstanding6 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][13]

    # Cash-Flow Statement values for tm6
    operatingCashflow6 = quarterly_statementsDump.loc['operatingCashflow'][13]
    paymentsForOperatingActivities6 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][13]
    proceedsFromOperatingActivities6 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][13]
    changeInOperatingLiabilities6 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][13]
    changeInOperatingAssets6 = quarterly_statementsDump.loc['changeInOperatingAssets'][13]
    depreciationDepletionAndAmortization6 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][13]
    capitalExpenditures6 = quarterly_statementsDump.loc['capitalExpenditures'][13]
    changeInReceivables6 = quarterly_statementsDump.loc['changeInReceivables'][13]
    changeInInventory6 = quarterly_statementsDump.loc['changeInInventory'][13]
    profitLoss6 = quarterly_statementsDump.loc['profitLoss'][13]
    cashflowFromInvestment6 = quarterly_statementsDump.loc['cashflowFromInvestment'][13]
    cashflowFromFinancing6 = quarterly_statementsDump.loc['cashflowFromFinancing'][13]
    proceedsFromRepaymentsOfShortTermDebt6 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][13]
    paymentsForRepurchaseOfCommonStock6 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][13]
    paymentsForRepurchaseOfEquity6 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][13]
    paymentsForRepurchaseOfPreferredStock6 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][13]
    dividendPayout6 = quarterly_statementsDump.loc['dividendPayout'][13]
    dividendPayoutCommonStock6 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][13]
    dividendPayoutPreferredStock6 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][13]
    proceedsFromIssuanceOfCommonStock6 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][13]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet6 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][13]
    proceedsFromIssuanceOfPreferredStock6 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][13]
    proceedsFromRepurchaseOfEquity6 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][13]
    proceedsFromSaleOfTreasuryStock6 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][13]
    changeInCashAndCashEquivalents6 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][13]
    changeInExchangeRate6 = quarterly_statementsDump.loc['changeInExchangeRate'][13]
    netIncome6 = quarterly_statementsDump.loc['netIncome'][13]

    ## TM5 VARIABLES
    # Income Statement Variables for tm5
    gross_profit5 = quarterly_statementsDump.loc['grossProfit'][14]
    totalRevenue5 = quarterly_statementsDump.loc['totalRevenue'][14]
    costOfRevenue5 = quarterly_statementsDump.loc['costOfRevenue'][14]
    costofGoodsAndServicesSold5 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][14]
    operatingIncome5 = quarterly_statementsDump.loc['operatingIncome'][14]
    sellingGeneralAndAdministrative5 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][14]
    researchAndDevelopment5 = quarterly_statementsDump.loc['researchAndDevelopment'][14]
    operatingExpenses5 = quarterly_statementsDump.loc['operatingExpenses'][14]
    investmentIncomeNet5 = quarterly_statementsDump.loc['investmentIncomeNet'][14]
    netInterestIncome5 = quarterly_statementsDump.loc['netInterestIncome'][14]
    interestIncome5 = quarterly_statementsDump.loc['interestIncome'][14]
    interestExpense5 = quarterly_statementsDump.loc['interestExpense'][14]
    nonInterestIncome5 = quarterly_statementsDump.loc['nonInterestIncome'][14]
    otherNonOperatingIncome5 = quarterly_statementsDump.loc['otherNonOperatingIncome'][14]
    depreciation5 = quarterly_statementsDump.loc['depreciation'][14]
    depreciationAndAmortization5 = quarterly_statementsDump.loc['depreciationAndAmortization'][14]
    incomeBeforeTax5 = quarterly_statementsDump.loc['incomeBeforeTax'][14]
    incomeTaxExpense5 = quarterly_statementsDump.loc['incomeTaxExpense'][14]
    interestAndDebtExpense5 = quarterly_statementsDump.loc['interestAndDebtExpense'][14]
    netIncomeFromContinuingOperations5 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][14]
    comprehensiveIncomeNetOfTax5 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][14]
    ebit5 = quarterly_statementsDump.loc['ebit'][14]
    ebitda5 = quarterly_statementsDump.loc['ebitda'][14]
    # netIncome5 = quarterly_statementsDump.loc['netIncome'][14]

    # Balance Sheet Values for tm5
    totalAssets5 = quarterly_statementsDump.loc['totalAssets'][14]
    totalCurrentAssets5 = quarterly_statementsDump.loc['totalCurrentAssets'][14]
    cashAndCashEquivalentsAtCarryingValue5 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][14]
    cashAndShortTermInvestments5 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][14]
    inventory5 = quarterly_statementsDump.loc['inventory'][14]
    currentNetReceivables5 = quarterly_statementsDump.loc['currentNetReceivables'][14]
    totalNonCurrentAssets5 = quarterly_statementsDump.loc['totalNonCurrentAssets'][14]
    propertyPlantEquipment5 = quarterly_statementsDump.loc['propertyPlantEquipment'][14]
    accumulatedDepreciationAmortizationPPE5 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][14]
    intangibleAssets5 = quarterly_statementsDump.loc['intangibleAssets'][14]
    intangibleAssetsExcludingGoodwill5 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][14]
    goodwill5 = quarterly_statementsDump.loc['goodwill'][14]
    investments5 = quarterly_statementsDump.loc['investments'][14]
    longTermInvestments5 = quarterly_statementsDump.loc['longTermInvestments'][14]
    shortTermInvestments5 = quarterly_statementsDump.loc['shortTermInvestments'][14]
    otherCurrentAssets5 = quarterly_statementsDump.loc['otherCurrentAssets'][14]
    otherNonCurrrentAssets5 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][14]
    totalLiabilities5 = quarterly_statementsDump.loc['totalLiabilities'][14]
    totalCurrentLiabilities5 = quarterly_statementsDump.loc['totalCurrentLiabilities'][14]
    currentAccountsPayable5 = quarterly_statementsDump.loc['currentAccountsPayable'][14]
    deferredRevenue5 = quarterly_statementsDump.loc['deferredRevenue'][14]
    currentDebt5 = quarterly_statementsDump.loc['currentDebt'][14]
    shortTermDebt5 = quarterly_statementsDump.loc['shortTermDebt'][14]
    totalNonCurrentLiabilities5 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][14]
    capitalLeaseObligations5 = quarterly_statementsDump.loc['capitalLeaseObligations'][14]
    longTermDebt5 = quarterly_statementsDump.loc['longTermDebt'][14]
    currentLongTermDebt5 = quarterly_statementsDump.loc['currentLongTermDebt'][14]
    longTermDebtNoncurrent5 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][14]
    shortLongTermDebtTotal5 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][14]
    otherCurrentLiabilities5 = quarterly_statementsDump.loc['otherCurrentLiabilities'][14]
    otherNonCurrentLiabilities5 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][14]
    totalShareholderEquity5 = quarterly_statementsDump.loc['totalShareholderEquity'][14]
    treasuryStock5 = quarterly_statementsDump.loc['treasuryStock'][14]
    retainedEarnings5 = quarterly_statementsDump.loc['retainedEarnings'][14]
    commonStock5 = quarterly_statementsDump.loc['commonStock'][14]
    commonStockSharesOutstanding5 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][14]

    # Cash-Flow Statement values for tm5
    operatingCashflow5 = quarterly_statementsDump.loc['operatingCashflow'][14]
    paymentsForOperatingActivities5 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][14]
    proceedsFromOperatingActivities5 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][14]
    changeInOperatingLiabilities5 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][14]
    changeInOperatingAssets5 = quarterly_statementsDump.loc['changeInOperatingAssets'][14]
    depreciationDepletionAndAmortization5 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][14]
    capitalExpenditures5 = quarterly_statementsDump.loc['capitalExpenditures'][14]
    changeInReceivables5 = quarterly_statementsDump.loc['changeInReceivables'][14]
    changeInInventory5 = quarterly_statementsDump.loc['changeInInventory'][14]
    profitLoss5 = quarterly_statementsDump.loc['profitLoss'][14]
    cashflowFromInvestment5 = quarterly_statementsDump.loc['cashflowFromInvestment'][14]
    cashflowFromFinancing5 = quarterly_statementsDump.loc['cashflowFromFinancing'][14]
    proceedsFromRepaymentsOfShortTermDebt5 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][14]
    paymentsForRepurchaseOfCommonStock5 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][14]
    paymentsForRepurchaseOfEquity5 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][14]
    paymentsForRepurchaseOfPreferredStock5 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][14]
    dividendPayout5 = quarterly_statementsDump.loc['dividendPayout'][14]
    dividendPayoutCommonStock5 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][14]
    dividendPayoutPreferredStock5 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][14]
    proceedsFromIssuanceOfCommonStock5 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][14]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet5 = \
    quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][14]
    proceedsFromIssuanceOfPreferredStock5 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][14]
    proceedsFromRepurchaseOfEquity5 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][14]
    proceedsFromSaleOfTreasuryStock5 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][14]
    changeInCashAndCashEquivalents5 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][14]
    changeInExchangeRate5 = quarterly_statementsDump.loc['changeInExchangeRate'][14]
    netIncome5 = quarterly_statementsDump.loc['netIncome'][14]

    ## TM4 VARIABLES
    # Income Statement Variables for tm4
    gross_profit4 = quarterly_statementsDump.loc['grossProfit'][15]
    totalRevenue4 = quarterly_statementsDump.loc['totalRevenue'][15]
    costOfRevenue4 = quarterly_statementsDump.loc['costOfRevenue'][15]
    costofGoodsAndServicesSold4 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][15]
    operatingIncome4 = quarterly_statementsDump.loc['operatingIncome'][15]
    sellingGeneralAndAdministrative4 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][15]
    researchAndDevelopment4 = quarterly_statementsDump.loc['researchAndDevelopment'][15]
    operatingExpenses4 = quarterly_statementsDump.loc['operatingExpenses'][15]
    investmentIncomeNet4 = quarterly_statementsDump.loc['investmentIncomeNet'][15]
    netInterestIncome4 = quarterly_statementsDump.loc['netInterestIncome'][15]
    interestIncome4 = quarterly_statementsDump.loc['interestIncome'][15]
    interestExpense4 = quarterly_statementsDump.loc['interestExpense'][15]
    nonInterestIncome4 = quarterly_statementsDump.loc['nonInterestIncome'][15]
    otherNonOperatingIncome4 = quarterly_statementsDump.loc['otherNonOperatingIncome'][15]
    depreciation4 = quarterly_statementsDump.loc['depreciation'][15]
    depreciationAndAmortization4 = quarterly_statementsDump.loc['depreciationAndAmortization'][15]
    incomeBeforeTax4 = quarterly_statementsDump.loc['incomeBeforeTax'][15]
    incomeTaxExpense4 = quarterly_statementsDump.loc['incomeTaxExpense'][15]
    interestAndDebtExpense4 = quarterly_statementsDump.loc['interestAndDebtExpense'][15]
    netIncomeFromContinuingOperations4 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][15]
    comprehensiveIncomeNetOfTax4 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][15]
    ebit4 = quarterly_statementsDump.loc['ebit'][15]
    ebitda4 = quarterly_statementsDump.loc['ebitda'][15]
    # netIncome4 = quarterly_statementsDump.loc['netIncome'][15]

    # Balance Sheet Values for tm4
    totalAssets4 = quarterly_statementsDump.loc['totalAssets'][15]
    totalCurrentAssets4 = quarterly_statementsDump.loc['totalCurrentAssets'][15]
    cashAndCashEquivalentsAtCarryingValue4 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][15]
    cashAndShortTermInvestments4 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][15]
    inventory4 = quarterly_statementsDump.loc['inventory'][15]
    currentNetReceivables4 = quarterly_statementsDump.loc['currentNetReceivables'][15]
    totalNonCurrentAssets4 = quarterly_statementsDump.loc['totalNonCurrentAssets'][15]
    propertyPlantEquipment4 = quarterly_statementsDump.loc['propertyPlantEquipment'][15]
    accumulatedDepreciationAmortizationPPE4 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][15]
    intangibleAssets4 = quarterly_statementsDump.loc['intangibleAssets'][15]
    intangibleAssetsExcludingGoodwill4 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][15]
    goodwill4 = quarterly_statementsDump.loc['goodwill'][15]
    investments4 = quarterly_statementsDump.loc['investments'][15]
    longTermInvestments4 = quarterly_statementsDump.loc['longTermInvestments'][15]
    shortTermInvestments4 = quarterly_statementsDump.loc['shortTermInvestments'][15]
    otherCurrentAssets4 = quarterly_statementsDump.loc['otherCurrentAssets'][15]
    otherNonCurrrentAssets4 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][15]
    totalLiabilities4 = quarterly_statementsDump.loc['totalLiabilities'][15]
    totalCurrentLiabilities4 = quarterly_statementsDump.loc['totalCurrentLiabilities'][15]
    currentAccountsPayable4 = quarterly_statementsDump.loc['currentAccountsPayable'][15]
    deferredRevenue4 = quarterly_statementsDump.loc['deferredRevenue'][15]
    currentDebt4 = quarterly_statementsDump.loc['currentDebt'][15]
    shortTermDebt4 = quarterly_statementsDump.loc['shortTermDebt'][15]
    totalNonCurrentLiabilities4 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][15]
    capitalLeaseObligations4 = quarterly_statementsDump.loc['capitalLeaseObligations'][15]
    longTermDebt4 = quarterly_statementsDump.loc['longTermDebt'][15]
    currentLongTermDebt4 = quarterly_statementsDump.loc['currentLongTermDebt'][15]
    longTermDebtNoncurrent4 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][15]
    shortLongTermDebtTotal4 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][15]
    otherCurrentLiabilities4 = quarterly_statementsDump.loc['otherCurrentLiabilities'][15]
    otherNonCurrentLiabilities4 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][15]
    totalShareholderEquity4 = quarterly_statementsDump.loc['totalShareholderEquity'][15]
    treasuryStock4 = quarterly_statementsDump.loc['treasuryStock'][15]
    retainedEarnings4 = quarterly_statementsDump.loc['retainedEarnings'][15]
    commonStock4 = quarterly_statementsDump.loc['commonStock'][15]
    commonStockSharesOutstanding4 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][15]

    # Cash-Flow Statement values for tm4
    operatingCashflow4 = quarterly_statementsDump.loc['operatingCashflow'][15]
    paymentsForOperatingActivities4 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][15]
    proceedsFromOperatingActivities4 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][15]
    changeInOperatingLiabilities4 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][15]
    changeInOperatingAssets4 = quarterly_statementsDump.loc['changeInOperatingAssets'][15]
    depreciationDepletionAndAmortization4 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][15]
    capitalExpenditures4 = quarterly_statementsDump.loc['capitalExpenditures'][15]
    changeInReceivables4 = quarterly_statementsDump.loc['changeInReceivables'][15]
    changeInInventory4 = quarterly_statementsDump.loc['changeInInventory'][15]
    profitLoss4 = quarterly_statementsDump.loc['profitLoss'][15]
    cashflowFromInvestment4 = quarterly_statementsDump.loc['cashflowFromInvestment'][15]
    cashflowFromFinancing4 = quarterly_statementsDump.loc['cashflowFromFinancing'][15]
    proceedsFromRepaymentsOfShortTermDebt4 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][15]
    paymentsForRepurchaseOfCommonStock4 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][15]
    paymentsForRepurchaseOfEquity4 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][15]
    paymentsForRepurchaseOfPreferredStock4 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][15]
    dividendPayout4 = quarterly_statementsDump.loc['dividendPayout'][15]
    dividendPayoutCommonStock4 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][15]
    dividendPayoutPreferredStock4 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][15]
    proceedsFromIssuanceOfCommonStock4 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][15]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet4 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][15]
    proceedsFromIssuanceOfPreferredStock4 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][15]
    proceedsFromRepurchaseOfEquity4 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][15]
    proceedsFromSaleOfTreasuryStock4 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][15]
    changeInCashAndCashEquivalents4 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][15]
    changeInExchangeRate4 = quarterly_statementsDump.loc['changeInExchangeRate'][15]
    netIncome4 = quarterly_statementsDump.loc['netIncome'][15]

    ## TM3 VARIABLES
    # Income Statement Variables for tm3
    gross_profit3 = quarterly_statementsDump.loc['grossProfit'][16]
    totalRevenue3 = quarterly_statementsDump.loc['totalRevenue'][16]
    costOfRevenue3 = quarterly_statementsDump.loc['costOfRevenue'][16]
    costofGoodsAndServicesSold3 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][16]
    operatingIncome3 = quarterly_statementsDump.loc['operatingIncome'][16]
    sellingGeneralAndAdministrative3 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][16]
    researchAndDevelopment3 = quarterly_statementsDump.loc['researchAndDevelopment'][16]
    operatingExpenses3 = quarterly_statementsDump.loc['operatingExpenses'][16]
    investmentIncomeNet3 = quarterly_statementsDump.loc['investmentIncomeNet'][16]
    netInterestIncome3 = quarterly_statementsDump.loc['netInterestIncome'][16]
    interestIncome3 = quarterly_statementsDump.loc['interestIncome'][16]
    interestExpense3 = quarterly_statementsDump.loc['interestExpense'][16]
    nonInterestIncome3 = quarterly_statementsDump.loc['nonInterestIncome'][16]
    otherNonOperatingIncome3 = quarterly_statementsDump.loc['otherNonOperatingIncome'][16]
    depreciation3 = quarterly_statementsDump.loc['depreciation'][16]
    depreciationAndAmortization3 = quarterly_statementsDump.loc['depreciationAndAmortization'][16]
    incomeBeforeTax3 = quarterly_statementsDump.loc['incomeBeforeTax'][16]
    incomeTaxExpense3 = quarterly_statementsDump.loc['incomeTaxExpense'][16]
    interestAndDebtExpense3 = quarterly_statementsDump.loc['interestAndDebtExpense'][16]
    netIncomeFromContinuingOperations3 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][16]
    comprehensiveIncomeNetOfTax3 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][16]
    ebit3 = quarterly_statementsDump.loc['ebit'][16]
    ebitda3 = quarterly_statementsDump.loc['ebitda'][16]
    # netIncome3 = quarterly_statementsDump.loc['netIncome'][16]

    # Balance Sheet Values for tm3
    totalAssets3 = quarterly_statementsDump.loc['totalAssets'][16]
    totalCurrentAssets3 = quarterly_statementsDump.loc['totalCurrentAssets'][16]
    cashAndCashEquivalentsAtCarryingValue3 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][16]
    cashAndShortTermInvestments3 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][16]
    inventory3 = quarterly_statementsDump.loc['inventory'][16]
    currentNetReceivables3 = quarterly_statementsDump.loc['currentNetReceivables'][16]
    totalNonCurrentAssets3 = quarterly_statementsDump.loc['totalNonCurrentAssets'][16]
    propertyPlantEquipment3 = quarterly_statementsDump.loc['propertyPlantEquipment'][16]
    accumulatedDepreciationAmortizationPPE3 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][16]
    intangibleAssets3 = quarterly_statementsDump.loc['intangibleAssets'][16]
    intangibleAssetsExcludingGoodwill3 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][16]
    goodwill3 = quarterly_statementsDump.loc['goodwill'][16]
    investments3 = quarterly_statementsDump.loc['investments'][16]
    longTermInvestments3 = quarterly_statementsDump.loc['longTermInvestments'][16]
    shortTermInvestments3 = quarterly_statementsDump.loc['shortTermInvestments'][16]
    otherCurrentAssets3 = quarterly_statementsDump.loc['otherCurrentAssets'][16]
    otherNonCurrrentAssets3 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][16]
    totalLiabilities3 = quarterly_statementsDump.loc['totalLiabilities'][16]
    totalCurrentLiabilities3 = quarterly_statementsDump.loc['totalCurrentLiabilities'][16]
    currentAccountsPayable3 = quarterly_statementsDump.loc['currentAccountsPayable'][16]
    deferredRevenue3 = quarterly_statementsDump.loc['deferredRevenue'][16]
    currentDebt3 = quarterly_statementsDump.loc['currentDebt'][16]
    shortTermDebt3 = quarterly_statementsDump.loc['shortTermDebt'][16]
    totalNonCurrentLiabilities3 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][16]
    capitalLeaseObligations3 = quarterly_statementsDump.loc['capitalLeaseObligations'][16]
    longTermDebt3 = quarterly_statementsDump.loc['longTermDebt'][16]
    currentLongTermDebt3 = quarterly_statementsDump.loc['currentLongTermDebt'][16]
    longTermDebtNoncurrent3 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][16]
    shortLongTermDebtTotal3 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][16]
    otherCurrentLiabilities3 = quarterly_statementsDump.loc['otherCurrentLiabilities'][16]
    otherNonCurrentLiabilities3 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][16]
    totalShareholderEquity3 = quarterly_statementsDump.loc['totalShareholderEquity'][16]
    treasuryStock3 = quarterly_statementsDump.loc['treasuryStock'][16]
    retainedEarnings3 = quarterly_statementsDump.loc['retainedEarnings'][16]
    commonStock3 = quarterly_statementsDump.loc['commonStock'][16]
    commonStockSharesOutstanding3 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][16]

    # Cash-Flow Statement values for tm3
    operatingCashflow3 = quarterly_statementsDump.loc['operatingCashflow'][16]
    paymentsForOperatingActivities3 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][16]
    proceedsFromOperatingActivities3 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][16]
    changeInOperatingLiabilities3 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][16]
    changeInOperatingAssets3 = quarterly_statementsDump.loc['changeInOperatingAssets'][16]
    depreciationDepletionAndAmortization3 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][16]
    capitalExpenditures3 = quarterly_statementsDump.loc['capitalExpenditures'][16]
    changeInReceivables3 = quarterly_statementsDump.loc['changeInReceivables'][16]
    changeInInventory3 = quarterly_statementsDump.loc['changeInInventory'][16]
    profitLoss3 = quarterly_statementsDump.loc['profitLoss'][16]
    cashflowFromInvestment3 = quarterly_statementsDump.loc['cashflowFromInvestment'][16]
    cashflowFromFinancing3 = quarterly_statementsDump.loc['cashflowFromFinancing'][16]
    proceedsFromRepaymentsOfShortTermDebt3 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][16]
    paymentsForRepurchaseOfCommonStock3 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][16]
    paymentsForRepurchaseOfEquity3 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][16]
    paymentsForRepurchaseOfPreferredStock3 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][16]
    dividendPayout3 = quarterly_statementsDump.loc['dividendPayout'][16]
    try:
        dividendPayout3 = int(dividendPayout3)
    except Exception:
        dividendPayout3 = 0
    dividendPayoutCommonStock3 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][16]
    dividendPayoutPreferredStock3 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][16]
    proceedsFromIssuanceOfCommonStock3 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][16]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet3 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][16]
    proceedsFromIssuanceOfPreferredStock3 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][16]
    proceedsFromRepurchaseOfEquity3 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][16]
    proceedsFromSaleOfTreasuryStock3 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][16]
    changeInCashAndCashEquivalents3 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][16]
    changeInExchangeRate3 = quarterly_statementsDump.loc['changeInExchangeRate'][16]
    netIncome3 = quarterly_statementsDump.loc['netIncome'][16]

    ## TM2 VARIABLES
    # Income Statement Variables for tm2
    gross_profit2 = quarterly_statementsDump.loc['grossProfit'][17]
    totalRevenue2 = quarterly_statementsDump.loc['totalRevenue'][17]
    costOfRevenue2 = quarterly_statementsDump.loc['costOfRevenue'][17]
    costofGoodsAndServicesSold2 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][17]
    operatingIncome2 = quarterly_statementsDump.loc['operatingIncome'][17]
    sellingGeneralAndAdministrative2 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][17]
    researchAndDevelopment2 = quarterly_statementsDump.loc['researchAndDevelopment'][17]
    operatingExpenses2 = quarterly_statementsDump.loc['operatingExpenses'][17]
    investmentIncomeNet2 = quarterly_statementsDump.loc['investmentIncomeNet'][17]
    netInterestIncome2 = quarterly_statementsDump.loc['netInterestIncome'][17]
    interestIncome2 = quarterly_statementsDump.loc['interestIncome'][17]
    interestExpense2 = quarterly_statementsDump.loc['interestExpense'][17]
    nonInterestIncome2 = quarterly_statementsDump.loc['nonInterestIncome'][17]
    otherNonOperatingIncome2 = quarterly_statementsDump.loc['otherNonOperatingIncome'][17]
    depreciation2 = quarterly_statementsDump.loc['depreciation'][17]
    depreciationAndAmortization2 = quarterly_statementsDump.loc['depreciationAndAmortization'][17]
    incomeBeforeTax2 = quarterly_statementsDump.loc['incomeBeforeTax'][17]
    incomeTaxExpense2 = quarterly_statementsDump.loc['incomeTaxExpense'][17]
    interestAndDebtExpense2 = quarterly_statementsDump.loc['interestAndDebtExpense'][17]
    netIncomeFromContinuingOperations2 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][17]
    comprehensiveIncomeNetOfTax2 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][17]
    ebit2 = quarterly_statementsDump.loc['ebit'][17]
    ebitda2 = quarterly_statementsDump.loc['ebitda'][17]
    # netIncome2 = quarterly_statementsDump.loc['netIncome'][17]

    # Balance Sheet Values for tm2
    totalAssets2 = quarterly_statementsDump.loc['totalAssets'][17]
    totalCurrentAssets2 = quarterly_statementsDump.loc['totalCurrentAssets'][17]
    cashAndCashEquivalentsAtCarryingValue2 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][17]
    cashAndShortTermInvestments2 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][17]
    inventory2 = quarterly_statementsDump.loc['inventory'][17]
    currentNetReceivables2 = quarterly_statementsDump.loc['currentNetReceivables'][17]
    totalNonCurrentAssets2 = quarterly_statementsDump.loc['totalNonCurrentAssets'][17]
    propertyPlantEquipment2 = quarterly_statementsDump.loc['propertyPlantEquipment'][17]
    accumulatedDepreciationAmortizationPPE2 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][17]
    intangibleAssets2 = quarterly_statementsDump.loc['intangibleAssets'][17]
    intangibleAssetsExcludingGoodwill2 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][17]
    goodwill2 = quarterly_statementsDump.loc['goodwill'][17]
    investments2 = quarterly_statementsDump.loc['investments'][17]
    longTermInvestments2 = quarterly_statementsDump.loc['longTermInvestments'][17]
    shortTermInvestments2 = quarterly_statementsDump.loc['shortTermInvestments'][17]
    otherCurrentAssets2 = quarterly_statementsDump.loc['otherCurrentAssets'][17]
    otherNonCurrrentAssets2 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][17]
    totalLiabilities2 = quarterly_statementsDump.loc['totalLiabilities'][17]
    totalCurrentLiabilities2 = quarterly_statementsDump.loc['totalCurrentLiabilities'][17]
    currentAccountsPayable2 = quarterly_statementsDump.loc['currentAccountsPayable'][17]
    deferredRevenue2 = quarterly_statementsDump.loc['deferredRevenue'][17]
    currentDebt2 = quarterly_statementsDump.loc['currentDebt'][17]
    shortTermDebt2 = quarterly_statementsDump.loc['shortTermDebt'][17]
    totalNonCurrentLiabilities2 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][17]
    capitalLeaseObligations2 = quarterly_statementsDump.loc['capitalLeaseObligations'][17]
    longTermDebt2 = quarterly_statementsDump.loc['longTermDebt'][17]
    currentLongTermDebt2 = quarterly_statementsDump.loc['currentLongTermDebt'][17]
    longTermDebtNoncurrent2 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][17]
    shortLongTermDebtTotal2 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][17]
    otherCurrentLiabilities2 = quarterly_statementsDump.loc['otherCurrentLiabilities'][17]
    otherNonCurrentLiabilities2 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][17]
    totalShareholderEquity2 = quarterly_statementsDump.loc['totalShareholderEquity'][17]
    treasuryStock2 = quarterly_statementsDump.loc['treasuryStock'][17]
    retainedEarnings2 = quarterly_statementsDump.loc['retainedEarnings'][17]
    commonStock2 = quarterly_statementsDump.loc['commonStock'][17]
    commonStockSharesOutstanding2 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][17]

    # Cash-Flow Statement values for tm2
    operatingCashflow2 = quarterly_statementsDump.loc['operatingCashflow'][17]
    paymentsForOperatingActivities2 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][17]
    proceedsFromOperatingActivities2 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][17]
    changeInOperatingLiabilities2 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][17]
    changeInOperatingAssets2 = quarterly_statementsDump.loc['changeInOperatingAssets'][17]
    depreciationDepletionAndAmortization2 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][17]
    capitalExpenditures2 = quarterly_statementsDump.loc['capitalExpenditures'][17]
    changeInReceivables2 = quarterly_statementsDump.loc['changeInReceivables'][17]
    changeInInventory2 = quarterly_statementsDump.loc['changeInInventory'][17]
    profitLoss2 = quarterly_statementsDump.loc['profitLoss'][17]
    cashflowFromInvestment2 = quarterly_statementsDump.loc['cashflowFromInvestment'][17]
    cashflowFromFinancing2 = quarterly_statementsDump.loc['cashflowFromFinancing'][17]
    proceedsFromRepaymentsOfShortTermDebt2 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][17]
    paymentsForRepurchaseOfCommonStock2 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][17]
    paymentsForRepurchaseOfEquity2 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][17]
    paymentsForRepurchaseOfPreferredStock2 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][17]
    dividendPayout2 = quarterly_statementsDump.loc['dividendPayout'][17]
    try:
        dividendPayout2 = int(dividendPayout2)
    except Exception:
        dividendPayout2 = 0
    dividendPayoutCommonStock2 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][17]
    dividendPayoutPreferredStock2 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][17]
    proceedsFromIssuanceOfCommonStock2 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][17]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet2 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][17]
    proceedsFromIssuanceOfPreferredStock2 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][17]
    proceedsFromRepurchaseOfEquity2 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][17]
    proceedsFromSaleOfTreasuryStock2 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][17]
    changeInCashAndCashEquivalents2 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][17]
    changeInExchangeRate2 = quarterly_statementsDump.loc['changeInExchangeRate'][17]
    netIncome2 = quarterly_statementsDump.loc['netIncome'][17]

    ## TM1 VARIABLES
    # Income Statement Variables for tm1
    gross_profit1 = quarterly_statementsDump.loc['grossProfit'][18]
    totalRevenue1 = quarterly_statementsDump.loc['totalRevenue'][18]
    costOfRevenue1 = quarterly_statementsDump.loc['costOfRevenue'][18]
    costofGoodsAndServicesSold1 = quarterly_statementsDump.loc['costofGoodsAndServicesSold'][18]
    operatingIncome1 = quarterly_statementsDump.loc['operatingIncome'][18]
    sellingGeneralAndAdministrative1 = quarterly_statementsDump.loc['sellingGeneralAndAdministrative'][18]
    researchAndDevelopment1 = quarterly_statementsDump.loc['researchAndDevelopment'][18]
    operatingExpenses1 = quarterly_statementsDump.loc['operatingExpenses'][18]
    investmentIncomeNet1 = quarterly_statementsDump.loc['investmentIncomeNet'][18]
    netInterestIncome1 = quarterly_statementsDump.loc['netInterestIncome'][18]
    interestIncome1 = quarterly_statementsDump.loc['interestIncome'][18]
    interestExpense1 = quarterly_statementsDump.loc['interestExpense'][18]
    nonInterestIncome1 = quarterly_statementsDump.loc['nonInterestIncome'][18]
    otherNonOperatingIncome1 = quarterly_statementsDump.loc['otherNonOperatingIncome'][18]
    depreciation1 = quarterly_statementsDump.loc['depreciation'][18]
    depreciationAndAmortization1 = quarterly_statementsDump.loc['depreciationAndAmortization'][18]
    incomeBeforeTax1 = quarterly_statementsDump.loc['incomeBeforeTax'][18]
    incomeTaxExpense1 = quarterly_statementsDump.loc['incomeTaxExpense'][18]
    interestAndDebtExpense1 = quarterly_statementsDump.loc['interestAndDebtExpense'][18]
    netIncomeFromContinuingOperations1 = quarterly_statementsDump.loc['netIncomeFromContinuingOperations'][18]
    comprehensiveIncomeNetOfTax1 = quarterly_statementsDump.loc['comprehensiveIncomeNetOfTax'][18]
    ebit1 = quarterly_statementsDump.loc['ebit'][18]
    ebitda1 = quarterly_statementsDump.loc['ebitda'][18]
    # netIncome1 = quarterly_statementsDump.loc['netIncome'][18]

    # Balance Sheet Values for tm1
    totalAssets1 = quarterly_statementsDump.loc['totalAssets'][18]
    totalCurrentAssets1 = quarterly_statementsDump.loc['totalCurrentAssets'][18]
    cashAndCashEquivalentsAtCarryingValue1 = quarterly_statementsDump.loc['cashAndCashEquivalentsAtCarryingValue'][18]
    cashAndShortTermInvestments1 = quarterly_statementsDump.loc['cashAndShortTermInvestments'][18]
    inventory1 = quarterly_statementsDump.loc['inventory'][18]
    currentNetReceivables1 = quarterly_statementsDump.loc['currentNetReceivables'][18]
    totalNonCurrentAssets1 = quarterly_statementsDump.loc['totalNonCurrentAssets'][18]
    propertyPlantEquipment1 = quarterly_statementsDump.loc['propertyPlantEquipment'][18]
    accumulatedDepreciationAmortizationPPE1 = quarterly_statementsDump.loc['accumulatedDepreciationAmortizationPPE'][18]
    intangibleAssets1 = quarterly_statementsDump.loc['intangibleAssets'][18]
    intangibleAssetsExcludingGoodwill1 = quarterly_statementsDump.loc['intangibleAssetsExcludingGoodwill'][18]
    goodwill1 = quarterly_statementsDump.loc['goodwill'][18]
    investments1 = quarterly_statementsDump.loc['investments'][18]
    longTermInvestments1 = quarterly_statementsDump.loc['longTermInvestments'][18]
    shortTermInvestments1 = quarterly_statementsDump.loc['shortTermInvestments'][18]
    otherCurrentAssets1 = quarterly_statementsDump.loc['otherCurrentAssets'][18]
    otherNonCurrrentAssets1 = quarterly_statementsDump.loc['otherNonCurrrentAssets'][18]
    totalLiabilities1 = quarterly_statementsDump.loc['totalLiabilities'][18]
    totalCurrentLiabilities1 = quarterly_statementsDump.loc['totalCurrentLiabilities'][18]
    currentAccountsPayable1 = quarterly_statementsDump.loc['currentAccountsPayable'][18]
    deferredRevenue1 = quarterly_statementsDump.loc['deferredRevenue'][18]
    currentDebt1 = quarterly_statementsDump.loc['currentDebt'][18]
    shortTermDebt1 = quarterly_statementsDump.loc['shortTermDebt'][18]
    totalNonCurrentLiabilities1 = quarterly_statementsDump.loc['totalNonCurrentLiabilities'][18]
    capitalLeaseObligations1 = quarterly_statementsDump.loc['capitalLeaseObligations'][18]
    longTermDebt1 = quarterly_statementsDump.loc['longTermDebt'][18]
    currentLongTermDebt1 = quarterly_statementsDump.loc['currentLongTermDebt'][18]
    longTermDebtNoncurrent1 = quarterly_statementsDump.loc['longTermDebtNoncurrent'][18]
    shortLongTermDebtTotal1 = quarterly_statementsDump.loc['shortLongTermDebtTotal'][18]
    otherCurrentLiabilities1 = quarterly_statementsDump.loc['otherCurrentLiabilities'][18]
    otherNonCurrentLiabilities1 = quarterly_statementsDump.loc['otherNonCurrentLiabilities'][18]
    totalShareholderEquity1 = quarterly_statementsDump.loc['totalShareholderEquity'][18]
    treasuryStock1 = quarterly_statementsDump.loc['treasuryStock'][18]
    retainedEarnings1 = quarterly_statementsDump.loc['retainedEarnings'][18]
    commonStock1 = quarterly_statementsDump.loc['commonStock'][18]
    commonStockSharesOutstanding1 = quarterly_statementsDump.loc['commonStockSharesOutstanding'][18]

    # Cash-Flow Statement values for tm1
    operatingCashflow1 = quarterly_statementsDump.loc['operatingCashflow'][18]
    paymentsForOperatingActivities1 = quarterly_statementsDump.loc['paymentsForOperatingActivities'][18]
    proceedsFromOperatingActivities1 = quarterly_statementsDump.loc['proceedsFromOperatingActivities'][18]
    changeInOperatingLiabilities1 = quarterly_statementsDump.loc['changeInOperatingLiabilities'][18]
    changeInOperatingAssets1 = quarterly_statementsDump.loc['changeInOperatingAssets'][18]
    depreciationDepletionAndAmortization1 = quarterly_statementsDump.loc['depreciationDepletionAndAmortization'][18]
    capitalExpenditures1 = quarterly_statementsDump.loc['capitalExpenditures'][18]
    changeInReceivables1 = quarterly_statementsDump.loc['changeInReceivables'][18]
    changeInInventory1 = quarterly_statementsDump.loc['changeInInventory'][18]
    profitLoss1 = quarterly_statementsDump.loc['profitLoss'][18]
    cashflowFromInvestment1 = quarterly_statementsDump.loc['cashflowFromInvestment'][18]
    cashflowFromFinancing1 = quarterly_statementsDump.loc['cashflowFromFinancing'][18]
    proceedsFromRepaymentsOfShortTermDebt1 = quarterly_statementsDump.loc['proceedsFromRepaymentsOfShortTermDebt'][18]
    paymentsForRepurchaseOfCommonStock1 = quarterly_statementsDump.loc['paymentsForRepurchaseOfCommonStock'][18]
    paymentsForRepurchaseOfEquity1 = quarterly_statementsDump.loc['paymentsForRepurchaseOfEquity'][18]
    paymentsForRepurchaseOfPreferredStock1 = quarterly_statementsDump.loc['paymentsForRepurchaseOfPreferredStock'][18]
    dividendPayout1 = quarterly_statementsDump.loc['dividendPayout'][18]
    try:
        dividendPayout1 = int(dividendPayout1)
    except Exception:
        dividendPayout1 = 0
    dividendPayoutCommonStock1 = quarterly_statementsDump.loc['dividendPayoutCommonStock'][18]
    dividendPayoutPreferredStock1 = quarterly_statementsDump.loc['dividendPayoutPreferredStock'][18]
    proceedsFromIssuanceOfCommonStock1 = quarterly_statementsDump.loc['proceedsFromIssuanceOfCommonStock'][18]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet1 = quarterly_statementsDump.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet'][18]
    proceedsFromIssuanceOfPreferredStock1 = quarterly_statementsDump.loc['proceedsFromIssuanceOfPreferredStock'][18]
    proceedsFromRepurchaseOfEquity1 = quarterly_statementsDump.loc['proceedsFromRepurchaseOfEquity'][18]
    proceedsFromSaleOfTreasuryStock1 = quarterly_statementsDump.loc['proceedsFromSaleOfTreasuryStock'][18]
    changeInCashAndCashEquivalents1 = quarterly_statementsDump.loc['changeInCashAndCashEquivalents'][18]
    changeInExchangeRate1 = quarterly_statementsDump.loc['changeInExchangeRate'][18]
    netIncome1 = quarterly_statementsDump.loc['netIncome'][18]

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

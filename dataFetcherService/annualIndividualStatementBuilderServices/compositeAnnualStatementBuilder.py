
import requests
import pandas as pd
from pandas.io.json import json_normalize

from alphavantageapikey import alpha_vantagi_api_key
import json


# gross_profit = []
# totalRevenue = []
# costOfRevenue = []
# costofGoodsAndServicesSold = []
# operatingIncome = []
# sellingGeneralAndAdministrative = []
# researchAndDevelopment = []
# operatingExpenses = []
# investmentIncomeNet = []
# netInterestIncome = []
# interestIncome = []
# interestExpense = []
# nonInterestIncome = []
# otherNonOperatingIncome = []
# depreciation = []
# depreciationAndAmortization = []
# incomeBeforeTax = []
# incomeTaxExpense = []
# interestAndDebtExpense = []
# netIncomeFromContinuingOperations = []
# comprehensiveIncomeNetOfTax = []
# ebit = []
# ebitda = []
# netIncome = []
# #bsy5df
# totalAssets = []
# totalCurrentAssets = []
# cashAndCashEquivalentsAtCarryingValue = []
# cashAndShortTermInvestments = []
# inventory = []
# currentNetReceivables = []
# totalNonCurrentAssets = []
# propertyPlantEquipment = []
# accumulatedDepreciationAmortizationPPE = []
# intangibleAssets = []
# intangibleAssetsExcludingGoodwill = []
# goodwill = []
# investments = []
# longTermInvestments = []
# shortTermInvestments = []
# otherCurrentAssets = []
# otherNonCurrrentAssets = []
# totalLiabilities = []
# totalCurrentLiabilities = []
# currentAccountsPayable = []
# deferredRevenue = []
# currentDebt = []
# shortTermDebt = []
# totalNonCurrentLiabilities = []
# capitalLeaseObligations = []
# longTermDebt = []
# currentLongTermDebt = []
# longTermDebtNoncurrent = []
# shortLongTermDebtTotal = []
# otherCurrentLiabilities = []
# otherNonCurrentLiabilities = []
# totalShareholderEquity = []
# treasuryStock = []
# retainedEarnings = []
# commonStock = []
# commonStockSharesOutstanding = []
# #cfy5df
# operatingCashflow = []
# paymentsForOperatingActivities = []
# proceedsFromOperatingActivities = []
# changeInOperatingLiabilities = []
# changeInOperatingAssets = []
# depreciationDepletionAndAmortization = []
# capitalExpenditures = []
# changeInReceivables = []
# changeInInventory = []
# profitLoss = []
# cashflowFromInvestment = []
# cashflowFromFinancing = []
# proceedsFromRepaymentsOfShortTermDebt = []
# paymentsForRepurchaseOfCommonStock = []
# paymentsForRepurchaseOfEquity = []
# paymentsForRepurchaseOfPreferredStock = []
# dividendPayout = []
# dividendPayoutCommonStock = []
# dividendPayoutPreferredStock = []
# proceedsFromIssuanceOfCommonStock = []
# proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = []
# proceedsFromIssuanceOfPreferredStock = []
# proceedsFromRepurchaseOfEquity = []
# proceedsFromSaleOfTreasuryStock = []
# changeInCashAndCashEquivalents = []
# changeInExchangeRate = []
# netIncome = []


def build_ann_statements(ticker):

    # Defining URLs for the Requests
    isUrl = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    bsUrl = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    cfUrl = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    overviewURL  = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key

    #Requests
    isr = requests.get(isUrl)
    bsr = requests.get(bsUrl)
    cfr = requests.get(cfUrl)
    overviewr = requests.get(overviewURL)

    #JSON dicts
    isData = isr.json()
    bsData = bsr.json()
    cfData = cfr.json()
    overviewData = overviewr.json()

    #Creating dataframes for Income Statements
    isy5df = pd.DataFrame.from_dict(isData['annualReports'][0], orient='index')
    isy4df = pd.DataFrame.from_dict(isData['annualReports'][1], orient='index')
    isy3df = pd.DataFrame.from_dict(isData['annualReports'][2], orient='index')
    isy2df = pd.DataFrame.from_dict(isData['annualReports'][3], orient='index')
    isy1df = pd.DataFrame.from_dict(isData['annualReports'][4], orient='index')

    annual_income_statement = pd.concat([isy1df, isy2df, isy3df, isy4df, isy5df], axis=1)
    #annual_income_statement.to_csv('annual_income_statement')
    #print(annual_income_statement)

    # Creating dataframes for Balance Sheets
    bsy5df = pd.DataFrame.from_dict(bsData['annualReports'][0], orient='index')
    bsy4df = pd.DataFrame.from_dict(bsData['annualReports'][1], orient='index')
    bsy3df = pd.DataFrame.from_dict(bsData['annualReports'][2], orient='index')
    bsy2df = pd.DataFrame.from_dict(bsData['annualReports'][3], orient='index')
    bsy1df = pd.DataFrame.from_dict(bsData['annualReports'][4], orient='index')

    annual_balance_sheet = pd.concat([bsy1df, bsy2df, bsy3df, bsy4df, bsy5df], axis=1)
    #annual_balance_sheet.to_csv('annual_balance_sheet')
    #print(annual_balance_sheet)


    #Creating dataframes for Cash Flow Statements
    cfy5df = pd.DataFrame.from_dict(cfData['annualReports'][0], orient='index')
    cfy4df = pd.DataFrame.from_dict(cfData['annualReports'][1], orient='index')
    cfy3df = pd.DataFrame.from_dict(cfData['annualReports'][2], orient='index')
    cfy2df = pd.DataFrame.from_dict(cfData['annualReports'][3], orient='index')
    cfy1df = pd.DataFrame.from_dict(cfData['annualReports'][4], orient='index')

    #Creating overview
    js = pd.json_normalize(overviewData)
    print(js)
    overviewDf = pd.DataFrame.from_dict(overviewData, orient='index')
    sharesOutstanding = overviewData['SharesOutstanding'],

    annual_cash_flow_statement = pd.concat([cfy1df, cfy2df, cfy3df, cfy4df, cfy5df], axis=1)
    #annual_cash_flow_statement.to_csv('annual_cash_flow_statement')
    #print(annual_cash_flow_statement)

    isAndBsDf = annual_income_statement.append(annual_balance_sheet)
    statementsDump = isAndBsDf.append(annual_cash_flow_statement)
    statementsDumpHtml = statementsDump.to_html()
    statementsDump.to_csv('full_statements_dump.csv')
    print('-------------------------------------------')
    pd.set_option('display.max_rows', None)
    print(statementsDump)
    print(statementsDump[0])
    # print(statementsDumpHtml)
    # print(type(statementsDumpHtml))
    print(sharesOutstanding)
    return statementsDump

    gross_profit = isy5df.loc['grossProfit']
    totalRevenue = isy5df.loc['totalRevenue']
    costOfRevenue = isy5df.loc['costOfRevenue']
    costofGoodsAndServicesSold = isy5df.loc['costofGoodsAndServicesSold']
    operatingIncome = isy5df.loc['operatingIncome']
    sellingGeneralAndAdministrative = isy5df.loc['sellingGeneralAndAdministrative']
    researchAndDevelopment = isy5df.loc['researchAndDevelopment']
    operatingExpenses = isy5df.loc['operatingExpenses']
    investmentIncomeNet = isy5df.loc['investmentIncomeNet']
    netInterestIncome = isy5df.loc['netInterestIncome']
    interestIncome = isy5df.loc['interestIncome']
    interestExpense = isy5df.loc['interestExpense']
    nonInterestIncome = isy5df.loc['nonInterestIncome']
    otherNonOperatingIncome = isy5df.loc['otherNonOperatingIncome']
    depreciation = isy5df.loc['depreciation']
    depreciationAndAmortization = isy5df.loc['depreciationAndAmortization']
    incomeBeforeTax = isy5df.loc['incomeBeforeTax']
    incomeTaxExpense = isy5df.loc['incomeTaxExpense']
    interestAndDebtExpense = isy5df.loc['interestAndDebtExpense']
    netIncomeFromContinuingOperations = isy5df.loc['netIncomeFromContinuingOperations']
    comprehensiveIncomeNetOfTax = isy5df.loc['comprehensiveIncomeNetOfTax']
    ebit = isy5df.loc['ebit']
    ebitda = isy5df.loc['ebitda']
    netIncome = isy5df.loc['netIncome']
    # bsy5df
    totalAssets = bsy5df.loc['totalAssets']
    totalCurrentAssets = bsy5df.loc['totalCurrentAssets']
    cashAndCashEquivalentsAtCarryingValue = bsy5df.loc['cashAndCashEquivalentsAtCarryingValue']
    cashAndShortTermInvestments = bsy5df.loc['cashAndShortTermInvestments']
    inventory = bsy5df.loc['inventory']
    currentNetReceivables = bsy5df.loc['currentNetReceivables']
    totalNonCurrentAssets = bsy5df.loc['totalNonCurrentAssets']
    propertyPlantEquipment = bsy5df.loc['propertyPlantEquipment']
    accumulatedDepreciationAmortizationPPE = bsy5df.loc['accumulatedDepreciationAmortizationPPE']
    intangibleAssets = bsy5df.loc['intangibleAssets']
    intangibleAssetsExcludingGoodwill = bsy5df.loc['intangibleAssetsExcludingGoodwill']
    goodwill = bsy5df.loc['goodwill']
    investments = bsy5df.loc['investments']
    longTermInvestments = bsy5df.loc['longTermInvestments']
    shortTermInvestments = bsy5df.loc['shortTermInvestments']
    otherCurrentAssets = bsy5df.loc['otherCurrentAssets']
    otherNonCurrrentAssets = bsy5df.loc['otherNonCurrrentAssets']
    totalLiabilities = bsy5df.loc['totalLiabilities']
    totalCurrentLiabilities = bsy5df.loc['totalCurrentLiabilities']
    currentAccountsPayable = bsy5df.loc['currentAccountsPayable']
    deferredRevenue = bsy5df.loc['deferredRevenue']
    currentDebt = bsy5df.loc['currentDebt']
    shortTermDebt = bsy5df.loc['shortTermDebt']
    totalNonCurrentLiabilities = bsy5df.loc['totalNonCurrentLiabilities']
    capitalLeaseObligations = bsy5df.loc['capitalLeaseObligations']
    longTermDebt = bsy5df.loc['longTermDebt']
    currentLongTermDebt = bsy5df.loc['currentLongTermDebt']
    longTermDebtNoncurrent = bsy5df.loc['longTermDebtNoncurrent']
    shortLongTermDebtTotal = bsy5df.loc['shortLongTermDebtTotal']
    otherCurrentLiabilities = bsy5df.loc['otherCurrentLiabilities']
    otherNonCurrentLiabilities = bsy5df.loc['otherNonCurrentLiabilities']
    totalShareholderEquity = bsy5df.loc['totalShareholderEquity']
    treasuryStock = bsy5df.loc['treasuryStock']
    retainedEarnings = bsy5df.loc['retainedEarnings']
    commonStock = bsy5df.loc['commonStock']
    commonStockSharesOutstanding = bsy5df.loc['commonStockSharesOutstanding']
    # cfy5df
    operatingCashflow = cfy5df.loc['operatingCashflow']
    paymentsForOperatingActivities = cfy5df.loc['paymentsForOperatingActivities']
    proceedsFromOperatingActivities = cfy5df.loc['proceedsFromOperatingActivities']
    changeInOperatingLiabilities = cfy5df.loc['changeInOperatingLiabilities']
    changeInOperatingAssets = cfy5df.loc['changeInOperatingAssets']
    depreciationDepletionAndAmortization = cfy5df.loc['depreciationDepletionAndAmortization']
    capitalExpenditures = cfy5df.loc['capitalExpenditures']
    changeInReceivables = cfy5df.loc['changeInReceivables']
    changeInInventory = cfy5df.loc['changeInInventory']
    profitLoss = cfy5df.loc['profitLoss']
    cashflowFromInvestment = cfy5df.loc['cashflowFromInvestment']
    cashflowFromFinancing = cfy5df.loc['cashflowFromFinancing']
    proceedsFromRepaymentsOfShortTermDebt = cfy5df.loc['proceedsFromRepaymentsOfShortTermDebt']
    paymentsForRepurchaseOfCommonStock = cfy5df.loc['paymentsForRepurchaseOfCommonStock']
    paymentsForRepurchaseOfEquity = cfy5df.loc['paymentsForRepurchaseOfEquity']
    paymentsForRepurchaseOfPreferredStock = cfy5df.loc['paymentsForRepurchaseOfPreferredStock']
    dividendPayout = cfy5df.loc['dividendPayout']
    dividendPayoutCommonStock = cfy5df.loc['dividendPayoutCommonStock']
    dividendPayoutPreferredStock = cfy5df.loc['dividendPayoutPreferredStock']
    proceedsFromIssuanceOfCommonStock = cfy5df.loc['proceedsFromIssuanceOfCommonStock']
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = cfy5df.loc[
        'proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet']
    proceedsFromIssuanceOfPreferredStock = cfy5df.loc['proceedsFromIssuanceOfPreferredStock']
    proceedsFromRepurchaseOfEquity = cfy5df.loc['proceedsFromRepurchaseOfEquity']
    proceedsFromSaleOfTreasuryStock = cfy5df.loc['proceedsFromSaleOfTreasuryStock']
    changeInCashAndCashEquivalents = cfy5df.loc['changeInCashAndCashEquivalents']
    changeInExchangeRate = cfy5df.loc['changeInExchangeRate']
    netIncome = cfy5df.loc['netIncome']



build_ann_statements('IBM')


statementsDump = build_ann_statements.statementsDump
isy5df = build_ann_statements.isy5df
bsy5df = build_ann_statements.bsy5df
cfy5df = build_ann_statements.cfy5df
isy4df = build_ann_statements.isy4df
bsy4df = build_ann_statements.bsy4df
cfy4df = build_ann_statements.cfy4df
isy3df = build_ann_statements.isy3df
bsy3df = build_ann_statements.bsy3df
cfy3df = build_ann_statements.cfy3df
isy2df = build_ann_statements.isy2df
bsy2df = build_ann_statements.bsy2df
cfy2df = build_ann_statements.cfy2df
isy1df = build_ann_statements.isy1df
bsy1df = build_ann_statements.bsy1df
cfy1df = build_ann_statements.cfy1df




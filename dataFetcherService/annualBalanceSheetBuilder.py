import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


ticker = 'AAPL'

# Convert Balance Sheet json request to pandas data frame
bsUrl = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
bsr = requests.get(bsUrl)
bsData = bsr.json()

y5df = pd.DataFrame.from_dict(bsData['annualReports'][0], orient='index')
y4df = pd.DataFrame.from_dict(bsData['annualReports'][1], orient='index')
y3df = pd.DataFrame.from_dict(bsData['annualReports'][2], orient='index')
y2df = pd.DataFrame.from_dict(bsData['annualReports'][3], orient='index')
y1df = pd.DataFrame.from_dict(bsData['annualReports'][4], orient='index')

annual_balance_sheet = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
annual_balance_sheet.to_csv('annual_balance_sheet')


def calc_ann_bs(ticker):
    y5df = pd.DataFrame.from_dict(bsData['annualReports'][0], orient='index')
    y4df = pd.DataFrame.from_dict(bsData['annualReports'][1], orient='index')
    y3df = pd.DataFrame.from_dict(bsData['annualReports'][2], orient='index')
    y2df = pd.DataFrame.from_dict(bsData['annualReports'][3], orient='index')
    y1df = pd.DataFrame.from_dict(bsData['annualReports'][4], orient='index')

    annual_balance_sheet = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
    print(annual_balance_sheet)
    annual_balance_sheet.to_csv('annual_balance_sheet')
    return annual_balance_sheet


totalAssets = y5df.loc['totalAssets']
totalCurrentAssets = y5df.loc['totalCurrentAssets']
cashAndCashEquivalentsAtCarryingValue = y5df.loc['cashAndCashEquivalentsAtCarryingValue']
cashAndShortTermInvestments = y5df.loc['cashAndShortTermInvestments']
inventory = y5df.loc['inventory']
currentNetReceivables = y5df.loc['currentNetReceivables']
totalNonCurrentAssets = y5df.loc['totalNonCurrentAssets']
propertyPlantEquipment = y5df.loc['propertyPlantEquipment']
accumulatedDepreciationAmortizationPPE = y5df.loc['accumulatedDepreciationAmortizationPPE']
intangibleAssets = y5df.loc['intangibleAssets']
intangibleAssetsExcludingGoodwill = y5df.loc['intangibleAssetsExcludingGoodwill']
goodwill = y5df.loc['goodwill']
investments = y5df.loc['investments']
longTermInvestments = y5df.loc['longTermInvestments']
shortTermInvestments = y5df.loc['shortTermInvestments']
otherCurrentAssets = y5df.loc['otherCurrentAssets']
otherNonCurrrentAssets = y5df.loc['otherNonCurrrentAssets']
totalLiabilities = y5df.loc['totalLiabilities']
totalCurrentLiabilities = y5df.loc['totalCurrentLiabilities']
currentAccountsPayable = y5df.loc['currentAccountsPayable']
deferredRevenue = y5df.loc['deferredRevenue']
currentDebt = y5df.loc['currentDebt']
shortTermDebt = y5df.loc['shortTermDebt']
totalNonCurrentLiabilities = y5df.loc['totalNonCurrentLiabilities']
capitalLeaseObligations = y5df.loc['capitalLeaseObligations']
longTermDebt = y5df.loc['longTermDebt']
currentLongTermDebt = y5df.loc['currentLongTermDebt']
longTermDebtNoncurrent = y5df.loc['longTermDebtNoncurrent']
shortLongTermDebtTotal = y5df.loc['shortLongTermDebtTotal']
otherCurrentLiabilities = y5df.loc['otherCurrentLiabilities']
otherNonCurrentLiabilities = y5df.loc['otherNonCurrentLiabilities']
totalShareholderEquity = y5df.loc['totalShareholderEquity']
treasuryStock = y5df.loc['treasuryStock']
retainedEarnings = y5df.loc['retainedEarnings']
commonStock = y5df.loc['commonStock']
commonStockSharesOutstanding = y5df.loc['commonStockSharesOutstanding']
import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key

ticker = 'AAPL'

# Convert Cash Flow json request to pandas data frame
cfUrl = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
cfr = requests.get(cfUrl)
cfData = cfr.json()

y5df = pd.DataFrame.from_dict(cfData['annualReports'][0], orient='index')
y4df = pd.DataFrame.from_dict(cfData['annualReports'][1], orient='index')
y3df = pd.DataFrame.from_dict(cfData['annualReports'][2], orient='index')
y2df = pd.DataFrame.from_dict(cfData['annualReports'][3], orient='index')
y1df = pd.DataFrame.from_dict(cfData['annualReports'][4], orient='index')

annual_cash_flow_statement = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
print(annual_cash_flow_statement)
annual_cash_flow_statement.to_csv('annual_balance_sheet')


def calc_ann_cf(ticker):

    cfr = requests.get(cfUrl)
    cfData = cfr.json()

    y5df = pd.DataFrame.from_dict(cfData['annualReports'][0], orient='index')
    y4df = pd.DataFrame.from_dict(cfData['annualReports'][1], orient='index')
    y3df = pd.DataFrame.from_dict(cfData['annualReports'][2], orient='index')
    y2df = pd.DataFrame.from_dict(cfData['annualReports'][3], orient='index')
    y1df = pd.DataFrame.from_dict(cfData['annualReports'][4], orient='index')

    annual_cash_flow_statement = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
    print(annual_cash_flow_statement)
    annual_cash_flow_statement.to_csv('annual_cash_flow_statement')


operatingCashflow = y5df.loc['operatingCashflow']
paymentsForOperatingActivities = y5df.loc['paymentsForOperatingActivities']
proceedsFromOperatingActivities = y5df.loc['proceedsFromOperatingActivities']
changeInOperatingLiabilities = y5df.loc['changeInOperatingLiabilities']
changeInOperatingAssets = y5df.loc['changeInOperatingAssets']
depreciationDepletionAndAmortization = y5df.loc['depreciationDepletionAndAmortization']
capitalExpenditures = y5df.loc['capitalExpenditures']
changeInReceivables = y5df.loc['changeInReceivables']
changeInInventory = y5df.loc['changeInInventory']
profitLoss = y5df.loc['profitLoss']
cashflowFromInvestment = y5df.loc['cashflowFromInvestment']
cashflowFromFinancing = y5df.loc['cashflowFromFinancing']
proceedsFromRepaymentsOfShortTermDebt = y5df.loc['proceedsFromRepaymentsOfShortTermDebt']
paymentsForRepurchaseOfCommonStock = y5df.loc['paymentsForRepurchaseOfCommonStock']
paymentsForRepurchaseOfEquity = y5df.loc['paymentsForRepurchaseOfEquity']
paymentsForRepurchaseOfPreferredStock = y5df.loc['paymentsForRepurchaseOfPreferredStock']
dividendPayout = y5df.loc['dividendPayout']
dividendPayoutCommonStock = y5df.loc['dividendPayoutCommonStock']
dividendPayoutPreferredStock = y5df.loc['dividendPayoutPreferredStock']
proceedsFromIssuanceOfCommonStock = y5df.loc['proceedsFromIssuanceOfCommonStock']
proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = y5df.loc['proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet']
proceedsFromIssuanceOfPreferredStock = y5df.loc['proceedsFromIssuanceOfPreferredStock']
proceedsFromRepurchaseOfEquity = y5df.loc['proceedsFromRepurchaseOfEquity']
proceedsFromSaleOfTreasuryStock = y5df.loc['proceedsFromSaleOfTreasuryStock']
changeInCashAndCashEquivalents = y5df.loc['changeInCashAndCashEquivalents']
changeInExchangeRate = y5df.loc['changeInExchangeRate']
netIncome = y5df.loc['netIncome']


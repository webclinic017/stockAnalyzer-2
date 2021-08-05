import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


ticker = 'AAPL'


# Convert Income Statement json request to pandas data frame
isUrl = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
isr = requests.get(isUrl)
isData = isr.json()

y5df = pd.DataFrame.from_dict(isData['annualReports'][0], orient='index')
y4df = pd.DataFrame.from_dict(isData['annualReports'][1], orient='index')
y3df = pd.DataFrame.from_dict(isData['annualReports'][2], orient='index')
y2df = pd.DataFrame.from_dict(isData['annualReports'][3], orient='index')
y1df = pd.DataFrame.from_dict(isData['annualReports'][4], orient='index')

annual_income_statement = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
annual_income_statement.to_csv('annual_income_statement')



def calc_ann_is(ticker):
    y5df = pd.DataFrame.from_dict(isData['annualReports'][0], orient='index')
    y4df = pd.DataFrame.from_dict(isData['annualReports'][1], orient='index')
    y3df = pd.DataFrame.from_dict(isData['annualReports'][2], orient='index')
    y2df = pd.DataFrame.from_dict(isData['annualReports'][3], orient='index')
    y1df = pd.DataFrame.from_dict(isData['annualReports'][4], orient='index')

    annual_income_statement = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
    annual_income_statement.to_csv('annual_income_statement')
    print(annual_income_statement)
    return annual_income_statement




#calc_ann_is(ticker)


gross_profit = y5df.loc['grossProfit']
totalRevenue = y5df.loc['totalRevenue']
costOfRevenue = y5df.loc['costOfRevenue']
costofGoodsAndServicesSold = y5df.loc['costofGoodsAndServicesSold']
operatingIncome = y5df.loc['operatingIncome']
sellingGeneralAndAdministrative = y5df.loc['sellingGeneralAndAdministrative']
researchAndDevelopment = y5df.loc['researchAndDevelopment']
operatingExpenses = y5df.loc['operatingExpenses']
investmentIncomeNet = y5df.loc['investmentIncomeNet']
netInterestIncome = y5df.loc['netInterestIncome']
interestIncome = y5df.loc['interestIncome']
interestExpense = y5df.loc['interestExpense']
nonInterestIncome = y5df.loc['nonInterestIncome']
otherNonOperatingIncome = y5df.loc['otherNonOperatingIncome']
depreciation = y5df.loc['depreciation']
depreciationAndAmortization = y5df.loc['depreciationAndAmortization']
incomeBeforeTax = y5df.loc['incomeBeforeTax']
incomeTaxExpense = y5df.loc['incomeTaxExpense']
interestAndDebtExpense = y5df.loc['interestAndDebtExpense']
netIncomeFromContinuingOperations = y5df.loc['netIncomeFromContinuingOperations']
comprehensiveIncomeNetOfTax = y5df.loc['comprehensiveIncomeNetOfTax']
ebit = y5df.loc['ebit']
ebitda = y5df.loc['ebitda']
netIncome = y5df.loc['netIncome']






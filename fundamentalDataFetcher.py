import requests
import pandas as pd
from pandas import DataFrame as df
import json
from alphavantageapikey import alpha_vantagi_api_key
from pandas import json_normalize


def pretty_print(data: dict):
    print(json.dumps(data, indent=4))


ticker = 'AAPL'

# Convert overview json request to pandas data frame
overviewurl = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
ovr = requests.get(overviewurl)
overviewdata = ovr.json()

overviewdf = pd.DataFrame(list(overviewdata.items()), columns=['column1', 'column2'])
print(overviewdf)

# Convert Income Statement json request to pandas data frame
isUrl = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
isr = requests.get(isUrl)
isData = isr.json()
isTxt = isr.text

isdf = pd.DataFrame(list(isData.items()), columns=['column1', 'column2'])
# quarterlyisdf = pd.DataFrame(list(isData.items()))

print(isdf)

# Convert Balance Sheet json request to pandas data frame
bsUrl = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
bsr = requests.get(bsUrl)
bsData = bsr.json()
bsTxt = bsr.text

bsdf = pd.DataFrame(list(bsData.items()), columns=['column1', 'column2'])
print(bsdf)

# Convert Cash Flow json request to pandas data frame
cfUrl = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
cfr = requests.get(cfUrl)
cfData = cfr.json()
cfTxt = cfr.text

cfdf = pd.DataFrame(list(cfData.items()), columns=['Key', 'Values'])
print(cfdf)

print(isData)
# print(bsData)
# print(cfData)

print('--------------------------------------------------------------------------')

## Building Annual Income Statement Dataframe ##

annual_is_index = []
annual_is_y1 = []

for i in isData:
    print(i)

print('----------------------------')

for i in isData['annualReports']:
    print(i)

print('----------------------------')

for i in isData['annualReports'][0]:
    annual_is_index.append(i)
    print(i)

print('----------------------------')

print(annual_is_index)
print('----------------------------')

y5df = pd.DataFrame.from_dict(isData['annualReports'][0], orient='index')
y4df = pd.DataFrame.from_dict(isData['annualReports'][1], orient='index')
y3df = pd.DataFrame.from_dict(isData['annualReports'][2], orient='index')
y2df = pd.DataFrame.from_dict(isData['annualReports'][3], orient='index')
y1df = pd.DataFrame.from_dict(isData['annualReports'][4], orient='index')



annual_income_statement = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
print(annual_income_statement)
annual_income_statement.to_csv('annual_income_statement')
#annual_income_statement[] =

print(type(cfdf))
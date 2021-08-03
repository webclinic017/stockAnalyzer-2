import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key

ticker = 'AAPL'

# Convert Balance Sheet json request to pandas data frame
bsUrl = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
bsr = requests.get(bsUrl)
bsData = bsr.json()


y20df = pd.DataFrame.from_dict(bsData['quarterlyReports'][0], orient='index')
y19df = pd.DataFrame.from_dict(bsData['quarterlyReports'][1], orient='index')
y18df = pd.DataFrame.from_dict(bsData['quarterlyReports'][2], orient='index')
y17df = pd.DataFrame.from_dict(bsData['quarterlyReports'][3], orient='index')
y16df = pd.DataFrame.from_dict(bsData['quarterlyReports'][4], orient='index')
y15df = pd.DataFrame.from_dict(bsData['quarterlyReports'][5], orient='index')
y14df = pd.DataFrame.from_dict(bsData['quarterlyReports'][6], orient='index')
y13df = pd.DataFrame.from_dict(bsData['quarterlyReports'][7], orient='index')
y12df = pd.DataFrame.from_dict(bsData['quarterlyReports'][8], orient='index')
y11df = pd.DataFrame.from_dict(bsData['quarterlyReports'][9], orient='index')
y10df = pd.DataFrame.from_dict(bsData['quarterlyReports'][10], orient='index')
y9df = pd.DataFrame.from_dict(bsData['quarterlyReports'][11], orient='index')
y8df = pd.DataFrame.from_dict(bsData['quarterlyReports'][12], orient='index')
y7df = pd.DataFrame.from_dict(bsData['quarterlyReports'][13], orient='index')
y6df = pd.DataFrame.from_dict(bsData['quarterlyReports'][14], orient='index')
y5df = pd.DataFrame.from_dict(bsData['quarterlyReports'][15], orient='index')
y4df = pd.DataFrame.from_dict(bsData['quarterlyReports'][16], orient='index')
y3df = pd.DataFrame.from_dict(bsData['quarterlyReports'][17], orient='index')
y2df = pd.DataFrame.from_dict(bsData['quarterlyReports'][18], orient='index')
y1df = pd.DataFrame.from_dict(bsData['quarterlyReports'][19], orient='index')

quarterly_balance_sheet = pd.concat([y1df, y2df, y3df, y4df, y5df, y6df, y7df, y8df, y9df, y10df, y11df, y12df, y13df, y14df, y15df, y16df, y17df, y18df, y19df, y20df], axis=1)
print(quarterly_balance_sheet)
quarterly_balance_sheet.to_csv('quarterly_balance_sheet')
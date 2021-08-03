import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key

ticker = 'AAPL'

# Convert Cash Flow json request to pandas data frame
cfUrl = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
cfr = requests.get(cfUrl)
cfData = cfr.json()


y20df = pd.DataFrame.from_dict(cfData['quarterlyReports'][0], orient='index')
y19df = pd.DataFrame.from_dict(cfData['quarterlyReports'][1], orient='index')
y18df = pd.DataFrame.from_dict(cfData['quarterlyReports'][2], orient='index')
y17df = pd.DataFrame.from_dict(cfData['quarterlyReports'][3], orient='index')
y16df = pd.DataFrame.from_dict(cfData['quarterlyReports'][4], orient='index')
y15df = pd.DataFrame.from_dict(cfData['quarterlyReports'][5], orient='index')
y14df = pd.DataFrame.from_dict(cfData['quarterlyReports'][6], orient='index')
y13df = pd.DataFrame.from_dict(cfData['quarterlyReports'][7], orient='index')
y12df = pd.DataFrame.from_dict(cfData['quarterlyReports'][8], orient='index')
y11df = pd.DataFrame.from_dict(cfData['quarterlyReports'][9], orient='index')
y10df = pd.DataFrame.from_dict(cfData['quarterlyReports'][10], orient='index')
y9df = pd.DataFrame.from_dict(cfData['quarterlyReports'][11], orient='index')
y8df = pd.DataFrame.from_dict(cfData['quarterlyReports'][12], orient='index')
y7df = pd.DataFrame.from_dict(cfData['quarterlyReports'][13], orient='index')
y6df = pd.DataFrame.from_dict(cfData['quarterlyReports'][14], orient='index')
y5df = pd.DataFrame.from_dict(cfData['quarterlyReports'][15], orient='index')
y4df = pd.DataFrame.from_dict(cfData['quarterlyReports'][16], orient='index')
y3df = pd.DataFrame.from_dict(cfData['quarterlyReports'][17], orient='index')
y2df = pd.DataFrame.from_dict(cfData['quarterlyReports'][18], orient='index')
y1df = pd.DataFrame.from_dict(cfData['quarterlyReports'][19], orient='index')

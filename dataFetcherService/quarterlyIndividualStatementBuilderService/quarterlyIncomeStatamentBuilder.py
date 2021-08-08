import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


def calc_ann_is(ticker):
    isUrl = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    isr = requests.get(isUrl)
    isData = isr.json()

    y20df = pd.DataFrame.from_dict(isData['quarterlyReports'][0], orient='index')
    y19df = pd.DataFrame.from_dict(isData['quarterlyReports'][1], orient='index')
    y18df = pd.DataFrame.from_dict(isData['quarterlyReports'][2], orient='index')
    y17df = pd.DataFrame.from_dict(isData['quarterlyReports'][3], orient='index')
    y16df = pd.DataFrame.from_dict(isData['quarterlyReports'][4], orient='index')
    y15df = pd.DataFrame.from_dict(isData['quarterlyReports'][5], orient='index')
    y14df = pd.DataFrame.from_dict(isData['quarterlyReports'][6], orient='index')
    y13df = pd.DataFrame.from_dict(isData['quarterlyReports'][7], orient='index')
    y12df = pd.DataFrame.from_dict(isData['quarterlyReports'][8], orient='index')
    y11df = pd.DataFrame.from_dict(isData['quarterlyReports'][9], orient='index')
    y10df = pd.DataFrame.from_dict(isData['quarterlyReports'][10], orient='index')
    y9df = pd.DataFrame.from_dict(isData['quarterlyReports'][11], orient='index')
    y8df = pd.DataFrame.from_dict(isData['quarterlyReports'][12], orient='index')
    y7df = pd.DataFrame.from_dict(isData['quarterlyReports'][13], orient='index')
    y6df = pd.DataFrame.from_dict(isData['quarterlyReports'][14], orient='index')
    y5df = pd.DataFrame.from_dict(isData['quarterlyReports'][15], orient='index')
    y4df = pd.DataFrame.from_dict(isData['quarterlyReports'][16], orient='index')
    y3df = pd.DataFrame.from_dict(isData['quarterlyReports'][17], orient='index')
    y2df = pd.DataFrame.from_dict(isData['quarterlyReports'][18], orient='index')
    y1df = pd.DataFrame.from_dict(isData['quarterlyReports'][19], orient='index')

    quarterly_income_statement = pd.concat([y1df, y2df, y3df, y4df, y5df, y6df, y7df, y8df, y9df, y10df, y11df, y12df, y13df, y14df, y15df, y16df, y17df, y18df, y19df, y20df], axis=1)
    #quarterly_income_statement.to_csv('quarterly_income_statement')
    print(quarterly_income_statement)
    return quarterly_income_statement


calc_ann_is('AAPL')




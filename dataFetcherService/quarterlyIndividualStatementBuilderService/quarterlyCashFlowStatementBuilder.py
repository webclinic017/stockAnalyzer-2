import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


def calc_ann_bs(ticker):
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

    quarterly_cash_flow_statement = pd.concat([y1df, y2df, y3df, y4df, y5df, y6df, y7df, y8df, y9df, y10df, y11df, y12df, y13df, y14df, y15df, y16df, y17df, y18df, y19df, y20df], axis=1)
    #quarterly_cash_flow_statement.to_csv('quarterly_cash_flow_statements')
    print(quarterly_cash_flow_statement)
    return quarterly_cash_flow_statement


calc_ann_bs('AAPL')




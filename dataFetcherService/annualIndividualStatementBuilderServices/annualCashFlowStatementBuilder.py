import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


def calc_ann_cf(ticker):
    cfUrl = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    cfr = requests.get(cfUrl)
    cfData = cfr.json()

    y5df = pd.DataFrame.from_dict(cfData['annualReports'][0], orient='index')
    y4df = pd.DataFrame.from_dict(cfData['annualReports'][1], orient='index')
    y3df = pd.DataFrame.from_dict(cfData['annualReports'][2], orient='index')
    y2df = pd.DataFrame.from_dict(cfData['annualReports'][3], orient='index')
    y1df = pd.DataFrame.from_dict(cfData['annualReports'][4], orient='index')

    annual_cash_flow_statement = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
    #annual_cash_flow_statement.to_csv('annual_cash_flow_statement')
    print(annual_cash_flow_statement)
    return annual_cash_flow_statement

calc_ann_cf('AAPl')


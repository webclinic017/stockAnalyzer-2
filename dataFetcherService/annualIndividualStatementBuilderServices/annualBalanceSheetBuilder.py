import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


def calc_ann_bs(ticker):
    bsUrl = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    bsr = requests.get(bsUrl)
    bsData = bsr.json()

    y5df = pd.DataFrame.from_dict(bsData['annualReports'][0], orient='index')
    y4df = pd.DataFrame.from_dict(bsData['annualReports'][1], orient='index')
    y3df = pd.DataFrame.from_dict(bsData['annualReports'][2], orient='index')
    y2df = pd.DataFrame.from_dict(bsData['annualReports'][3], orient='index')
    y1df = pd.DataFrame.from_dict(bsData['annualReports'][4], orient='index')

    annual_balance_sheet = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
    print(annual_balance_sheet)
    #annual_balance_sheet.to_csv('annual_balance_sheet')
    return annual_balance_sheet

calc_ann_bs('AAPL')


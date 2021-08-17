import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


def calc_ann_is(ticker):
    isUrl = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    isr = requests.get(isUrl)
    isData = isr.json()

    y5df = pd.DataFrame.from_dict(isData['annualReports'][0], orient='index')
    y4df = pd.DataFrame.from_dict(isData['annualReports'][1], orient='index')
    y3df = pd.DataFrame.from_dict(isData['annualReports'][2], orient='index')
    y2df = pd.DataFrame.from_dict(isData['annualReports'][3], orient='index')
    y1df = pd.DataFrame.from_dict(isData['annualReports'][4], orient='index')

    annual_income_statement = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
    gross_profit = y5df.loc['grossProfit']
    #annual_income_statement.to_csv('annual_income_statement')
    print(annual_income_statement)
    print(gross_profit)
    return annual_income_statement



calc_ann_is('AAPL')
#calc_ann_is(ticker)

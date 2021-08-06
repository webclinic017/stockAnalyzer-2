import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


def build_ann_statements(ticker):

    # Defining URLs for the Requests
    isUrl = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    bsUrl = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    cfUrl = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key

    #Requests
    isr = requests.get(isUrl)
    bsr = requests.get(bsUrl)
    cfr = requests.get(cfUrl)

    #JSON dicts
    isData = isr.json()
    bsData = bsr.json()
    cfData = cfr.json()

    #Creating dataframes for Income Statements
    isy5df = pd.DataFrame.from_dict(isData['annualReports'][0], orient='index')
    isy4df = pd.DataFrame.from_dict(isData['annualReports'][1], orient='index')
    isy3df = pd.DataFrame.from_dict(isData['annualReports'][2], orient='index')
    isy2df = pd.DataFrame.from_dict(isData['annualReports'][3], orient='index')
    isy1df = pd.DataFrame.from_dict(isData['annualReports'][4], orient='index')

    annual_income_statement = pd.concat([isy1df, isy2df, isy3df, isy4df, isy5df], axis=1)
    #annual_income_statement.to_csv('annual_income_statement')
    #print(annual_income_statement)

    # Creating dataframes for Balance Sheets
    y5df = pd.DataFrame.from_dict(bsData['annualReports'][0], orient='index')
    y4df = pd.DataFrame.from_dict(bsData['annualReports'][1], orient='index')
    y3df = pd.DataFrame.from_dict(bsData['annualReports'][2], orient='index')
    y2df = pd.DataFrame.from_dict(bsData['annualReports'][3], orient='index')
    y1df = pd.DataFrame.from_dict(bsData['annualReports'][4], orient='index')

    annual_balance_sheet = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
    #annual_balance_sheet.to_csv('annual_balance_sheet')
    #print(annual_balance_sheet)


    #Creating dataframes for Cash Flow Statements
    y5df = pd.DataFrame.from_dict(cfData['annualReports'][0], orient='index')
    y4df = pd.DataFrame.from_dict(cfData['annualReports'][1], orient='index')
    y3df = pd.DataFrame.from_dict(cfData['annualReports'][2], orient='index')
    y2df = pd.DataFrame.from_dict(cfData['annualReports'][3], orient='index')
    y1df = pd.DataFrame.from_dict(cfData['annualReports'][4], orient='index')

    annual_cash_flow_statement = pd.concat([y1df, y2df, y3df, y4df, y5df], axis=1)
    #annual_cash_flow_statement.to_csv('annual_cash_flow_statement')
    #print(annual_cash_flow_statement)

    isAndBsDf = annual_income_statement.append(annual_balance_sheet)
    statementsDump = isAndBsDf.append(annual_cash_flow_statement)
    statementsDumpHtml = statementsDump.to_html()
    print('-------------------------------------------')
    print(statementsDump)
    print(statementsDumpHtml)
    print(type(statementsDumpHtml))

build_ann_statements('AAPL')






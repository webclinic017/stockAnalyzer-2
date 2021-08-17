import requests
import pandas as pd
import numpy as np
from alphavantageapikey import alpha_vantagi_api_key


def build_ttm_statements(ticker):
    # Defining URLs for the Requests
    isUrl = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    bsUrl = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    cfUrl = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key

    # Requests
    isr = requests.get(isUrl)
    bsr = requests.get(bsUrl)
    cfr = requests.get(cfUrl)

    # JSON dicts
    isData = isr.json()
    bsData = bsr.json()
    cfData = cfr.json()

    # creating DataFrame of IncomeStatements for the last 4 months
    isq4df = pd.DataFrame.from_dict(isData['quarterlyReports'][0], orient='index')
    isq3df = pd.DataFrame.from_dict(isData['quarterlyReports'][1], orient='index')
    isq2df = pd.DataFrame.from_dict(isData['quarterlyReports'][2], orient='index')
    isq1df = pd.DataFrame.from_dict(isData['quarterlyReports'][3], orient='index')

    ttm_income_statement = pd.concat([isq1df, isq2df, isq3df, isq4df], axis=1)

    # creating DataFrame of Quarterly Balance Sheets for the last 4 months
    bsq4df = pd.DataFrame.from_dict(bsData['quarterlyReports'][0], orient='index')
    bsq3df = pd.DataFrame.from_dict(bsData['quarterlyReports'][1], orient='index')
    bsq2df = pd.DataFrame.from_dict(bsData['quarterlyReports'][2], orient='index')
    bsq1df = pd.DataFrame.from_dict(bsData['quarterlyReports'][3], orient='index')

    ttm_balance_sheet = pd.concat([bsq1df, bsq2df, bsq3df, bsq4df], axis=1)

    # creating DataFrame of Quarterly Cash-Flow Statements for the last 4 months
    cfq4df = pd.DataFrame.from_dict(cfData['quarterlyReports'][0], orient='index')
    cfq3df = pd.DataFrame.from_dict(cfData['quarterlyReports'][1], orient='index')
    cfq2df = pd.DataFrame.from_dict(cfData['quarterlyReports'][2], orient='index')
    cfq1df = pd.DataFrame.from_dict(cfData['quarterlyReports'][3], orient='index')

    ttm_cash_flow_statement = pd.concat([cfq1df, cfq2df, cfq3df, cfq4df], axis=1)

    # Creating composite statements
    isAndBsDf = ttm_income_statement.append(ttm_balance_sheet)
    ttm_statementsDump = isAndBsDf.append(ttm_cash_flow_statement)

    pd.set_option('display.max_rows', None)
    print('-------------------------------------------')

    print(ttm_statementsDump)
    #print(ttm_statementsDump_with_header)
    print('-------------------------------------------')
    print(type(ttm_statementsDump))

    df2= ttm_statementsDump.drop(labels='reportedCurrency', axis=0)
    df3 = df2.drop(labels='fiscalDateEnding', axis=0)

    print(df3)

    print('-------------------------------------------')


    df3.columns = ['tm3', 'tm2', 'tm1', 't']
    print(df3)

    dflist = ['tm3', 'tm2', 'tm1', 't']


    print(df3)

    print(type(df3))

    test = df3.at[df3.index[0],'t']
    print(test)
    print(type(test))


    for index, row in df3.iterrows():
        try:
            df3.loc[index, 'sum'] = float(row['tm3']) + float(row['tm2']) + float(row['tm1']) + float(row['t'])
            row['sum'] = float(row['tm3']) + float(row['tm2']) + float(row['tm1']) + float(row['t'])
        except Exception:
             pass



    print('-------------------------------------------')
    print(df3)
    print('-------------------------------------------')
    print(row)




build_ttm_statements('AAPL')
import requests
import pandas as pd
import numpy as np
from alphavantageapikey import alpha_vantagi_api_key


def build_tm2y_ttm_statements(ticker):
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

    # creating DataFrame for IncomeStatements
    isq4df = pd.DataFrame.from_dict(isData['quarterlyReports'][8], orient='index')
    isq3df = pd.DataFrame.from_dict(isData['quarterlyReports'][9], orient='index')
    isq2df = pd.DataFrame.from_dict(isData['quarterlyReports'][10], orient='index')
    isq1df = pd.DataFrame.from_dict(isData['quarterlyReports'][11], orient='index')

    tm2y_ttm_income_statement = pd.concat([isq1df, isq2df, isq3df, isq4df], axis=1)

    # DataFrame for Quarterly Balance Sheet
    bsq4df = pd.DataFrame.from_dict(bsData['quarterlyReports'][8], orient='index')
    bsq3df = pd.DataFrame.from_dict(bsData['quarterlyReports'][9], orient='index')
    bsq2df = pd.DataFrame.from_dict(bsData['quarterlyReports'][10], orient='index')
    bsq1df = pd.DataFrame.from_dict(bsData['quarterlyReports'][11], orient='index')

    tm2y_ttm_balance_sheet = pd.concat([bsq1df, bsq2df, bsq3df, bsq4df], axis=1)

    # DataFrame for Quarterly Cash Flow Statement
    cfq4df = pd.DataFrame.from_dict(cfData['quarterlyReports'][8], orient='index')
    cfq3df = pd.DataFrame.from_dict(cfData['quarterlyReports'][9], orient='index')
    cfq2df = pd.DataFrame.from_dict(cfData['quarterlyReports'][10], orient='index')
    cfq1df = pd.DataFrame.from_dict(cfData['quarterlyReports'][11], orient='index')

    tm2y_ttm_cash_flow_statement = pd.concat([cfq1df, cfq2df, cfq3df, cfq4df], axis=1)

    isAndBsDf = tm2y_ttm_income_statement.append(tm2y_ttm_balance_sheet)
    tm2y_ttm_statementsDump = isAndBsDf.append(tm2y_ttm_cash_flow_statement)

    pd.set_option('display.max_rows', None)
    print('-------------------------------------------')

    print(tm2y_ttm_statementsDump)
    #print(tm2y_ttm_statementsDump_with_header)
    print('-------------------------------------------')
    print(type(tm2y_ttm_statementsDump))

    df2= tm2y_ttm_statementsDump.drop(labels='reportedCurrency', axis=0)
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



build_tm2y_ttm_statements('AAPL')
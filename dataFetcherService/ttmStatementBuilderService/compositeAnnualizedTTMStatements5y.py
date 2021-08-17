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

    # Creating composite statements for the Trailing 12 Months
    isAndBsDf1 = ttm_income_statement.append(ttm_balance_sheet)
    ttm_statementsDump = isAndBsDf1.append(ttm_cash_flow_statement)
    pd.set_option('display.max_rows', None)
    df2_1 = ttm_statementsDump.drop(labels='reportedCurrency', axis=0)
    ttm_statementsDump = df2_1.drop(labels='fiscalDateEnding', axis=0)
    ttm_statementsDump.columns = ['tm3', 'tm2', 'tm1', 't']
    #print(ttm_statementsDump)

    for index, row in ttm_statementsDump.iterrows():
        try:
            ttm_statementsDump.loc[index, 'sumTTM'] = float(row['tm3']) + float(row['tm2']) + float(row['tm1']) + float(row['t'])
            #row['sumTTM'] = float(row['tm3']) + float(row['tm2']) + float(row['tm1']) + float(row['t'])
        except Exception:
             pass

    print('-------------------------------------------')
    print(ttm_statementsDump)
    print('---------------------------------------------------------------------------------------------------------------------------------')

    # creating DataFrame of IncomeStatements for the last 4 months minus 1 year
    isq4m1ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][4], orient='index')
    isq3m1ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][5], orient='index')
    isq2m1ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][6], orient='index')
    isq1m1ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][7], orient='index')

    ttm_m1y_income_statement = pd.concat([isq1m1ydf, isq2m1ydf, isq3m1ydf, isq4m1ydf], axis=1)

    # creating DataFrame of Quarterly Balance Sheets for the last 4 months minus 1 year
    bsq4m1ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][4], orient='index')
    bsq3m1ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][5], orient='index')
    bsq2m1ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][6], orient='index')
    bsq1m1ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][7], orient='index')

    ttm_m1y_balance_sheet = pd.concat([bsq1m1ydf, bsq2m1ydf, bsq3m1ydf, bsq4m1ydf], axis=1)

    # creating DataFrame of Quarterly Cash-Flow Statements for the last 4 months minus 1 year
    cfq4m1ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][4], orient='index')
    cfq3m1ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][5], orient='index')
    cfq2m1ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][6], orient='index')
    cfq1m1ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][7], orient='index')

    ttm_m1y_cash_flow_statement = pd.concat([cfq1m1ydf, cfq2m1ydf, cfq3m1ydf, cfq4m1ydf], axis=1)

    # Creating composite statements for the Trailing 12 Months minus 1 year
    isAndBsDf2 = ttm_m1y_income_statement.append(ttm_m1y_balance_sheet)
    ttm_m1y_statementsDump = isAndBsDf2.append(ttm_m1y_cash_flow_statement)
    pd.set_option('display.max_rows', None)
    df2_2 = ttm_m1y_statementsDump.drop(labels='reportedCurrency', axis=0)
    ttm_m1y_statementsDump = df2_2.drop(labels='fiscalDateEnding', axis=0)
    ttm_m1y_statementsDump.columns = ['tm7', 'tm6', 'tm5', 'tm4']
    #print(ttm_m1y_statementsDump)

    for index, row in ttm_m1y_statementsDump.iterrows():
        try:
            ttm_m1y_statementsDump.loc[index, 'sumTTMm1y'] = float(row['tm7']) + float(row['tm6']) + float(row['tm5']) + float(row['tm4'])
            #row['sumTTMm1y'] = float(row['tm7']) + float(row['tm6']) + float(row['tm5']) + float(row['tm4'])
        except Exception:
            pass

    print('-------------------------------------------')
    print(ttm_m1y_statementsDump)
    print('---------------------------------------------------------------------------------------------------------------------------------')

    # creating DataFrame of IncomeStatements for the last 4 months minus 2 years
    isq4m2ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][8], orient='index')
    isq3m2ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][9], orient='index')
    isq2m2ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][10], orient='index')
    isq1m2ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][11], orient='index')

    ttm_m2y_income_statement = pd.concat([isq1m2ydf, isq2m2ydf, isq3m2ydf, isq4m2ydf], axis=1)

    # creating DataFrame of Quarterly Balance Sheets for the last 4 months minus 2 years
    bsq4m2ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][8], orient='index')
    bsq3m2ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][9], orient='index')
    bsq2m2ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][10], orient='index')
    bsq1m2ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][11], orient='index')

    ttm_m2y_balance_sheet = pd.concat([bsq1m2ydf, bsq2m2ydf, bsq3m2ydf, bsq4m2ydf], axis=1)

    # creating DataFrame of Quarterly Cash-Flow Statements for the last 4 months minus 2 years
    cfq4m2ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][8], orient='index')
    cfq3m2ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][9], orient='index')
    cfq2m2ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][10], orient='index')
    cfq1m2ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][11], orient='index')

    ttm_m2y_cash_flow_statement = pd.concat([cfq1m2ydf, cfq2m2ydf, cfq3m2ydf, cfq4m2ydf], axis=1)

    # Creating composite statements for the Trailing 12 Months minus 1 year
    isAndBsDf3 = ttm_m2y_income_statement.append(ttm_m2y_balance_sheet)
    ttm_m2y_statementsDump = isAndBsDf3.append(ttm_m2y_cash_flow_statement)
    pd.set_option('display.max_rows', None)
    df2_3 = ttm_m2y_statementsDump.drop(labels='reportedCurrency', axis=0)
    ttm_m2y_statementsDump = df2_3.drop(labels='fiscalDateEnding', axis=0)
    ttm_m2y_statementsDump.columns = ['tm11', 'tm10', 'tm9', 'tm8']
    #print(ttm_m2y_statementsDump)

    for index, row in ttm_m2y_statementsDump.iterrows():
        try:
            ttm_m2y_statementsDump.loc[index, 'sumTTMm2y'] = float(row['tm11']) + float(row['tm10']) + float(row['tm9']) + float(row['tm8'])
            #row['sumTTMm2y'] = float(row['tm11']) + float(row['tm10']) + float(row['tm9']) + float(row['tm8'])
        except Exception:
            pass

    print('-------------------------------------------')
    print(ttm_m2y_statementsDump)
    print('---------------------------------------------------------------------------------------------------------------------------------')

    # creating DataFrame of IncomeStatements for the last 4 months minus 3 years
    isq4m3ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][12], orient='index')
    isq3m3ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][13], orient='index')
    isq2m3ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][14], orient='index')
    isq1m3ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][15], orient='index')

    ttm_m3y_income_statement = pd.concat([isq1m3ydf, isq2m3ydf, isq3m3ydf, isq4m3ydf], axis=1)

    # creating DataFrame of Quarterly Balance Sheets for the last 4 months minus 3 years
    bsq4m3ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][12], orient='index')
    bsq3m3ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][13], orient='index')
    bsq2m3ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][14], orient='index')
    bsq1m3ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][15], orient='index')

    ttm_m3y_balance_sheet = pd.concat([bsq1m3ydf, bsq2m3ydf, bsq3m3ydf, bsq4m3ydf], axis=1)

    # creating DataFrame of Quarterly Cash-Flow Statements for the last 4 months minus 3 years
    cfq4m3ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][12], orient='index')
    cfq3m3ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][13], orient='index')
    cfq2m3ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][14], orient='index')
    cfq1m3ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][15], orient='index')

    ttm_m3y_cash_flow_statement = pd.concat([cfq1m3ydf, cfq2m3ydf, cfq3m3ydf, cfq4m3ydf], axis=1)

    # Creating composite statements for the Trailing 12 Months minus 1 year
    isAndBsDf4 = ttm_m3y_income_statement.append(ttm_m3y_balance_sheet)
    ttm_m3y_statementsDump = isAndBsDf4.append(ttm_m3y_cash_flow_statement)
    pd.set_option('display.max_rows', None)
    df2_4 = ttm_m3y_statementsDump.drop(labels='reportedCurrency', axis=0)
    ttm_m3y_statementsDump = df2_4.drop(labels='fiscalDateEnding', axis=0)
    ttm_m3y_statementsDump.columns = ['tm15', 'tm14', 'tm13', 'tm12']
    #print(ttm_m3y_statementsDump)

    for index, row in ttm_m3y_statementsDump.iterrows():
        try:
            ttm_m3y_statementsDump.loc[index, 'sumTTMm3y'] = float(row['tm15']) + float(row['tm14']) + float(row['tm13']) + float(row['tm12'])
            #row['sumTTMm3y'] = float(row['tm15']) + float(row['tm14']) + float(row['tm13']) + float(row['tm12'])
        except Exception:
            pass

    print('-------------------------------------------')
    print(ttm_m3y_statementsDump)
    print('---------------------------------------------------------------------------------------------------------------------------------')

    # creating DataFrame of IncomeStatements for the last 4 months minus 4 years
    isq4m4ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][16], orient='index')
    isq3m4ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][17], orient='index')
    isq2m4ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][18], orient='index')
    isq1m4ydf = pd.DataFrame.from_dict(isData['quarterlyReports'][19], orient='index')

    ttm_m4y_income_statement = pd.concat([isq1m4ydf, isq2m4ydf, isq3m4ydf, isq4m4ydf], axis=1)

    # creating DataFrame of Quarterly Balance Sheets for the last 4 months minus 4 years
    bsq4m4ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][16], orient='index')
    bsq3m4ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][17], orient='index')
    bsq2m4ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][18], orient='index')
    bsq1m4ydf = pd.DataFrame.from_dict(bsData['quarterlyReports'][19], orient='index')

    ttm_m4y_balance_sheet = pd.concat([bsq1m4ydf, bsq2m4ydf, bsq3m4ydf, bsq4m4ydf], axis=1)

    # creating DataFrame of Quarterly Cash-Flow Statements for the last 4 months minus 4 years
    cfq4m4ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][16], orient='index')
    cfq3m4ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][17], orient='index')
    cfq2m4ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][18], orient='index')
    cfq1m4ydf = pd.DataFrame.from_dict(cfData['quarterlyReports'][19], orient='index')

    ttm_m4y_cash_flow_statement = pd.concat([cfq1m4ydf, cfq2m4ydf, cfq3m4ydf, cfq4m4ydf], axis=1)

    # Creating composite statements for the Trailing 12 Months minus 1 year
    isAndBsDf5 = ttm_m4y_income_statement.append(ttm_m4y_balance_sheet)
    ttm_m4y_statementsDump = isAndBsDf5.append(ttm_m4y_cash_flow_statement)
    pd.set_option('display.max_rows', None)
    df2_4 = ttm_m4y_statementsDump.drop(labels='reportedCurrency', axis=0)
    ttm_m4y_statementsDump = df2_4.drop(labels='fiscalDateEnding', axis=0)
    ttm_m4y_statementsDump.columns = ['tm19', 'tm18', 'tm17', 'tm16']
    #print(ttm_m4y_statementsDump)

    for index, row in ttm_m4y_statementsDump.iterrows():
        try:
            ttm_m4y_statementsDump.loc[index, 'sumTTMm4y'] = float(row['tm19']) + float(row['tm18']) + float(row['tm17']) + float(row['tm16'])
            #row['sumTTMm4y'] = float(row['tm19']) + float(row['tm18']) + float(row['tm17']) + float(row['tm16'])
        except Exception:
            pass

    print('-------------------------------------------')
    print(ttm_m4y_statementsDump)
    print('-------------------------------------------')
    # print('-------------------------------------------')
    # print(ttm_statementsDump['sumTTM'])
    # print('-------------------------------------------')
    # print(ttm_m1y_statementsDump['sumTTMm1y'])
    # print('-------------------------------------------')
    # print(ttm_m2y_statementsDump['sumTTMm2y'])
    # print('-------------------------------------------')
    # print(ttm_m3y_statementsDump['sumTTMm3y'])
    # print('-------------------------------------------')
    # print(ttm_m4y_statementsDump['sumTTMm4y'])
    # print('-------------------------------------------')
    ttm_data_for_composite = [ttm_m4y_statementsDump['sumTTMm4y'], ttm_m3y_statementsDump['sumTTMm3y'], ttm_m2y_statementsDump['sumTTMm2y'], ttm_m1y_statementsDump['sumTTMm1y'], ttm_statementsDump['sumTTM'] ]
    heads = ['sumTTMm4y', 'sumTTMm3y', 'sumTTMm2y', 'sumTTMm1y', 'sumTTM']
    ttm_composite = pd.concat(ttm_data_for_composite, axis=1, keys=heads)
    print(ttm_composite)


build_ttm_statements('AAPL')
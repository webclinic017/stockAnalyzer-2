import requests
import pandas as pd
from alphavantageapikey import alpha_vantagi_api_key


def build_quarterly_statements(ticker):
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
    isy20df = pd.DataFrame.from_dict(isData['quarterlyReports'][0], orient='index')
    isy19df = pd.DataFrame.from_dict(isData['quarterlyReports'][1], orient='index')
    isy18df = pd.DataFrame.from_dict(isData['quarterlyReports'][2], orient='index')
    isy17df = pd.DataFrame.from_dict(isData['quarterlyReports'][3], orient='index')
    isy16df = pd.DataFrame.from_dict(isData['quarterlyReports'][4], orient='index')
    isy15df = pd.DataFrame.from_dict(isData['quarterlyReports'][5], orient='index')
    isy14df = pd.DataFrame.from_dict(isData['quarterlyReports'][6], orient='index')
    isy13df = pd.DataFrame.from_dict(isData['quarterlyReports'][7], orient='index')
    isy12df = pd.DataFrame.from_dict(isData['quarterlyReports'][8], orient='index')
    isy11df = pd.DataFrame.from_dict(isData['quarterlyReports'][9], orient='index')
    isy10df = pd.DataFrame.from_dict(isData['quarterlyReports'][10], orient='index')
    isy9df = pd.DataFrame.from_dict(isData['quarterlyReports'][11], orient='index')
    isy8df = pd.DataFrame.from_dict(isData['quarterlyReports'][12], orient='index')
    isy7df = pd.DataFrame.from_dict(isData['quarterlyReports'][13], orient='index')
    isy6df = pd.DataFrame.from_dict(isData['quarterlyReports'][14], orient='index')
    isy5df = pd.DataFrame.from_dict(isData['quarterlyReports'][15], orient='index')
    isy4df = pd.DataFrame.from_dict(isData['quarterlyReports'][16], orient='index')
    isy3df = pd.DataFrame.from_dict(isData['quarterlyReports'][17], orient='index')
    isy2df = pd.DataFrame.from_dict(isData['quarterlyReports'][18], orient='index')
    isy1df = pd.DataFrame.from_dict(isData['quarterlyReports'][19], orient='index')

    quarterly_income_statement = pd.concat(
        [isy1df, isy2df, isy3df, isy4df, isy5df, isy6df, isy7df, isy8df, isy9df, isy10df, isy11df, isy12df, isy13df, isy14df, isy15df, isy16df, isy17df,
         isy18df, isy19df, isy20df], axis=1)
    # quarterly_income_statement.to_csv('quarterly_income_statements')

    # DataFrame for Quarterly Balance Sheet
    bsy20df = pd.DataFrame.from_dict(bsData['quarterlyReports'][0], orient='index')
    bsy19df = pd.DataFrame.from_dict(bsData['quarterlyReports'][1], orient='index')
    bsy18df = pd.DataFrame.from_dict(bsData['quarterlyReports'][2], orient='index')
    bsy17df = pd.DataFrame.from_dict(bsData['quarterlyReports'][3], orient='index')
    bsy16df = pd.DataFrame.from_dict(bsData['quarterlyReports'][4], orient='index')
    bsy15df = pd.DataFrame.from_dict(bsData['quarterlyReports'][5], orient='index')
    bsy14df = pd.DataFrame.from_dict(bsData['quarterlyReports'][6], orient='index')
    bsy13df = pd.DataFrame.from_dict(bsData['quarterlyReports'][7], orient='index')
    bsy12df = pd.DataFrame.from_dict(bsData['quarterlyReports'][8], orient='index')
    bsy11df = pd.DataFrame.from_dict(bsData['quarterlyReports'][9], orient='index')
    bsy10df = pd.DataFrame.from_dict(bsData['quarterlyReports'][10], orient='index')
    bsy9df = pd.DataFrame.from_dict(bsData['quarterlyReports'][11], orient='index')
    bsy8df = pd.DataFrame.from_dict(bsData['quarterlyReports'][12], orient='index')
    bsy7df = pd.DataFrame.from_dict(bsData['quarterlyReports'][13], orient='index')
    bsy6df = pd.DataFrame.from_dict(bsData['quarterlyReports'][14], orient='index')
    bsy5df = pd.DataFrame.from_dict(bsData['quarterlyReports'][15], orient='index')
    bsy4df = pd.DataFrame.from_dict(bsData['quarterlyReports'][16], orient='index')
    bsy3df = pd.DataFrame.from_dict(bsData['quarterlyReports'][17], orient='index')
    bsy2df = pd.DataFrame.from_dict(bsData['quarterlyReports'][18], orient='index')
    bsy1df = pd.DataFrame.from_dict(bsData['quarterlyReports'][19], orient='index')

    quarterly_balance_sheet = pd.concat(
        [bsy1df, bsy2df, bsy3df, bsy4df, bsy5df, bsy6df, bsy7df, bsy8df, bsy9df, bsy10df, bsy11df, bsy12df, bsy13df, bsy14df, bsy15df, bsy16df, bsy17df,
         bsy18df, bsy19df, bsy20df], axis=1)
    # quarterly_balance_sheet.to_csv('quarterly_balance_sheets')

    # DataFrame for Quarterly Cash Flow Statement
    cfy20df = pd.DataFrame.from_dict(cfData['quarterlyReports'][0], orient='index')
    cfy19df = pd.DataFrame.from_dict(cfData['quarterlyReports'][1], orient='index')
    cfy18df = pd.DataFrame.from_dict(cfData['quarterlyReports'][2], orient='index')
    cfy17df = pd.DataFrame.from_dict(cfData['quarterlyReports'][3], orient='index')
    cfy16df = pd.DataFrame.from_dict(cfData['quarterlyReports'][4], orient='index')
    cfy15df = pd.DataFrame.from_dict(cfData['quarterlyReports'][5], orient='index')
    cfy14df = pd.DataFrame.from_dict(cfData['quarterlyReports'][6], orient='index')
    cfy13df = pd.DataFrame.from_dict(cfData['quarterlyReports'][7], orient='index')
    cfy12df = pd.DataFrame.from_dict(cfData['quarterlyReports'][8], orient='index')
    cfy11df = pd.DataFrame.from_dict(cfData['quarterlyReports'][9], orient='index')
    cfy10df = pd.DataFrame.from_dict(cfData['quarterlyReports'][10], orient='index')
    cfy9df = pd.DataFrame.from_dict(cfData['quarterlyReports'][11], orient='index')
    cfy8df = pd.DataFrame.from_dict(cfData['quarterlyReports'][12], orient='index')
    cfy7df = pd.DataFrame.from_dict(cfData['quarterlyReports'][13], orient='index')
    cfy6df = pd.DataFrame.from_dict(cfData['quarterlyReports'][14], orient='index')
    cfy5df = pd.DataFrame.from_dict(cfData['quarterlyReports'][15], orient='index')
    cfy4df = pd.DataFrame.from_dict(cfData['quarterlyReports'][16], orient='index')
    cfy3df = pd.DataFrame.from_dict(cfData['quarterlyReports'][17], orient='index')
    cfy2df = pd.DataFrame.from_dict(cfData['quarterlyReports'][18], orient='index')
    cfy1df = pd.DataFrame.from_dict(cfData['quarterlyReports'][19], orient='index')

    quarterly_cash_flow_statement = pd.concat(
        [cfy1df, cfy2df, cfy3df, cfy4df, cfy5df, cfy6df, cfy7df, cfy8df, cfy9df, cfy10df, cfy11df, cfy12df, cfy13df, cfy14df, cfy15df, cfy16df, cfy17df,
         cfy18df, cfy19df, cfy20df], axis=1)
    # quarterly_cash_flow_statement.to_csv('quarterly_cash_flow_statements')

    isAndBsDf = quarterly_income_statement.append(quarterly_balance_sheet)
    quarterly_statementsDump = isAndBsDf.append(quarterly_cash_flow_statement)
    quarterly_statementsDumpHtml = quarterly_statementsDump.to_html()
    print('-------------------------------------------')
    print(quarterly_statementsDump)
    # print(quarterly_statementsDumpHtml)
    # print(type(quarterly_statementsDumpHtml))


build_quarterly_statements('AAPL')

from dataFetcherService.annualIncomeStatementBuilder import calc_ann_is, annual_income_statement
from dataFetcherService.annualBalanceSheetBuilder import calc_ann_bs, annual_balance_sheet
from dataFetcherService.annualCashFlowStatementBuilder import calc_ann_cf, annual_cash_flow_statement












def build_ann_statements(ticker):
    calc_ann_is(ticker)
    calc_ann_bs(ticker)
    calc_ann_cf(ticker)

    isAndBsDf = annual_income_statement.append(annual_balance_sheet)
    statementsDump = isAndBsDf.append(annual_cash_flow_statement)
    statementsDumpHtml = statementsDump.to_html()
    print('-------------------------------------------')
    print(statementsDump)
    print(statementsDumpHtml)
    print(type(statementsDumpHtml))





build_ann_statements('AAPL')
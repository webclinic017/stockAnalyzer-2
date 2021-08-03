from dataFetcherService.annualIncomeStatementBuilder import calc_ann_is
from dataFetcherService.annualBalanceSheetBuilder import calc_ann_bs
from dataFetcherService.annualCashFlowStatementBuilder import calc_ann_cf

ticker = 'AAPL'


def build_ann_statements(ticker):
    calc_ann_is(ticker)
    calc_ann_bs(ticker)
    calc_ann_cf(ticker)


build_ann_statements(ticker)
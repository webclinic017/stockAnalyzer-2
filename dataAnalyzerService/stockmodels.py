from dataAnalyzerService.stockstatcalculations import *
from masterAnalyzer import *
ticker = 'test'



current_eps = 2.04
current_dividend = 1.90
growth_rate = 0.0583
req_ror = 0.0937
retention_ratio = 0.4318
free_cash_flow = operatingCashflow - capitalExpenditures



#Constant Growth DDM Model -> vs0 =
def cg_ddm_model(ticker):
    d0 = current_dividend
    g = calculateSustainableGrowthRate(calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout, netIncome)), calculate_roe(netIncome, totalEquity))
    ke = req_ror
    cg_ddm_vs0 = ((d0 * (1 + g))/(ke - g))
    print(cg_ddm_vs0)
    return cg_ddm_vs0

#Earnings Model
def earnings_model(ticker):
    eps1 = 3.60
    ke = req_ror
    g = growth_rate
    b = retention_ratio
    earnings_model_vs0 = ((eps1/ke)*(1+((g-(ke*b))/(ke-g))))
    print(earnings_model_vs0)
    return earnings_model_vs0













cg_ddm_model(ticker)
earnings_model(ticker)


from dataAnalyzerService.stockstatcalculations import *
from dataAnalyzerService.masterAnalyzer import *


ticker = 'test'



current_eps = 2.04
current_dividend = 1.90
growth_rate = 0.0583
req_ror = 0.0937
retention_ratio = 0.4318
free_cash_flow = operatingCashflow - capitalExpenditures


def calculateCAPMSML(rf, eRm, beta):
    eRi = (float(rf) + (float(beta) * (float(eRm) - float(rf))))
    return eRi



#Constant Growth DDM Model -> vs0 =
def cg_ddm_model(currentDivPerShare, dividendPayout, netIncome, totalEquity, eRi):
    d0 = currentDivPerShare
    g = calculateSustainableGrowthRate(calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout, netIncome)), calculateROE(netIncome, totalEquity))
    ke = eRi
    cg_ddm_vs0 = ((d0 * (1 + g))/(ke - g))
    return cg_ddm_vs0

#Earnings Model
def earnings_model(estEPS1, eRi, dividendPayout, netIncome, totalEquity):
    eps1 = 3.60
    ke = req_ror
    g = calculateSustainableGrowthRate(calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout, netIncome)), calculateROE(netIncome, totalEquity))
    b = calculateRetentionRate(calculateDividendPayoutRatio(dividendPayout, netIncome))
    earnings_model_vs0 = ((eps1/ke)*(1+((g-(ke*b))/(ke-g))))
    return earnings_model_vs0













cg_ddm_model(ticker)
earnings_model(ticker)


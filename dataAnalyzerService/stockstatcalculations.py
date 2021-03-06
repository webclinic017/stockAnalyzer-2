import pandas as pd
import numpy as np

def calTtmeps(nI, nIm1, nIm2, nIm3, comShrsOutstnd, comShrsOutstndm1, comShrsOutstndm2, comShrsOutstndm3):
    curm3EPS = (float(nIm3) / float(comShrsOutstndm3))
    curm2EPS = (float(nIm2) / float(comShrsOutstndm2))
    curm1EPS = (float(nIm1) / float(comShrsOutstndm1))
    curmEPS = (float(nI) / float(comShrsOutstnd))
    ttmEps = (curmEPS + curm1EPS + curm2EPS + curm3EPS)
    return ttmEps

def calTrailingPEandEY(sharePrice, nI, nIm1, nIm2, nIm3, comShrsOutstnd, comShrsOutstndm1, comShrsOutstndm2, comShrsOutstndm3):
    ttmweightedAvgShrs = ((float(comShrsOutstnd) + float(comShrsOutstndm1) + float(comShrsOutstndm2) + float(comShrsOutstndm3))/4)
    print('WeightedAvgShrs = ' + str(ttmweightedAvgShrs))
    ttmNetIncome = ((float(nI) + float(nIm1) + float(nIm2) + float(nIm3)))
    print( 'ttmNetIncome=' + str(ttmNetIncome))
    ttmEps = (float(ttmNetIncome)/float(ttmweightedAvgShrs))
    basicEPS = (float(nI) / float(comShrsOutstnd))
    print( 'ttmEPS' + str(ttmEps))
    trailingPE = (float(sharePrice) / float(ttmEps))
    earningsYield = (float(ttmEps) / float(sharePrice))
    return trailingPE, earningsYield, ttmEps, basicEPS

def calPCF(currentPrice, opCF, opCFm1, opCFm2, opCFm3,commShrsOutst, commShrsOutstm1, commShrsOutstm2, commShrsOutstm3):
    ttmweightedAvgShrs = ((float(commShrsOutst) + float(commShrsOutstm1) + float(commShrsOutstm2) + float(commShrsOutstm3))/4)
    ttmOpCF = (float(opCF) + float(opCFm1) + float(opCFm2) + float(opCFm3))
    ttmOpCFps = (ttmOpCF / ttmweightedAvgShrs)
    cFpS = (float(opCF)/ float(commShrsOutst))
    pCF = (currentPrice / ttmOpCFps)
    return pCF, ttmOpCFps, cFpS

def calPS(currentPrice, rev, revm1, revm2, revm3,commShrsOutst, commShrsOutstm1, commShrsOutstm2, commShrsOutstm3):
    ttmweightedAvgShrs = ((float(commShrsOutst) + float(commShrsOutstm1) + float(commShrsOutstm2) + float(commShrsOutstm3))/4)
    ttmRev = (float(rev) + float(revm1) + float(revm2) + float(revm3))
    ttmSps = (ttmRev / ttmweightedAvgShrs)
    pS = (currentPrice / ttmSps)
    return pS

def calpB(currentPrice, comEq, comShrsOutst):
    bv = (float(comEq) / float(comShrsOutst))
    pB = (currentPrice / bv)
    return bv, pB


def calCurrentMargins(rev, oI, nI, cogs):
    gpm = ((float(rev) - float(cogs)) / float(rev))
    opM = (float(oI) / float(rev))
    nPM = (float(nI) / float(rev))
    return gpm, opM, nPM

def calTtmMargins(rev, revm1, revm2, revm3, oi, oim1, oim2, oim3, ni, nim1, nim2, nim3, cogs, cogsm1, cogsm2, cogsm3):
    ttmRev = (float(rev) + float(revm1)+ float(revm2) + float(revm3))
    ttmOI = (float(oi) + float(oim1)+ float(oim2) + float(oim3))
    ttmNI = (float(ni) + float(nim1)+ float(nim2) + float(nim3))
    ttmCOGS = (float(cogs) + float(cogsm1)+ float(cogsm2) + float(cogsm3))
    ttmGPM = ((ttmRev - ttmCOGS)/ttmRev)
    ttmOPM = (ttmOI/ttmRev)
    ttmNPM = (ttmNI/ttmRev)
    return ttmGPM, ttmOPM, ttmNPM


def calTtmEBITDApS(ebitda, ebitdam1, ebitdam2, ebitdam3, commShrsOutst, commShrsOutstm1, commShrsOutstm2, commShrsOutstm3):
    ttmweightedAvgShrs = ((float(commShrsOutst) + float(commShrsOutstm1) + float(commShrsOutstm2) + float(commShrsOutstm3))/4)
    ttmEBITDA = (float(ebitda) + float(ebitdam1) + float(ebitdam2) + float(ebitdam3))
    ttmEbitdaPs = (ttmEBITDA/ttmweightedAvgShrs)
    return ttmEbitdaPs

def calDivPerShare(dividendPayout, comShrsOutstanding, netIncome):
    divPs = (float(dividendPayout) / float(comShrsOutstanding))
    divPayoutRatio = (float(dividendPayout)/ float(netIncome))
    retentionRateB = (1-divPayoutRatio)
    return divPs, divPayoutRatio, retentionRateB

def calReturnOns(nI, oI, tA, tAm1, tSE, tSEm1, comShrsOutstanding, dividendPayout ):
    divPs = (float(dividendPayout) / float(comShrsOutstanding))
    divPayoutRatio = (float(dividendPayout) / float(nI))
    retentionRateB = (1 - divPayoutRatio)

    avgAssets = ((float(tA) + float(tAm1))/2)
    avgEquity = ((float(tSE) + float(tSEm1))/2)

    roa = (float(nI) / avgAssets)
    roe = (float(nI) / avgEquity)
    opRoa = (float(oI) / avgAssets)
    opRoe = (float(oI) / avgEquity)

    sustainableGrowthRate = (roe * retentionRateB)
    return roa, roe, opRoa, opRoe, divPs, divPayoutRatio, retentionRateB, sustainableGrowthRate

def calBsRatios(tA, tL,tD, tSE, inv, cA, cL, cash):
    debtToAsset = (float(tD) / float(tA))
    debtToEquity = (float(tD) / float(tSE))
    financialLeverage = (float(tA) / float(tSE))
    debtToCapital = (float(tD) / (float(tD) + float(tSE)))
    currentRatio = (float(cA) / float(cL))
    quickRatio = ((float(cA) - float(inv))/float(cA))
    cashRatio = (float(cash) / float(cL))
    return debtToAsset, debtToEquity, financialLeverage, debtToCapital, currentRatio, quickRatio, cashRatio

def calDefInt(currentAssets, opExp, opExpm1, opExpm2, opExpm3, noncashchgs,noncashchgsm1,noncashchgsm2,noncashchg3):
    tTMoperatingExpenses = (float(opExp) + float(opExpm1) + float(opExpm2) + float(opExpm3))
    tTMnonCashCharges = (float(noncashchgs) + float(noncashchgsm1) + float(noncashchgsm2) + float(noncashchg3))
    defensiveInterval = (float(currentAssets) / ((float(tTMoperatingExpenses)-float(tTMnonCashCharges))/365))
    return defensiveInterval


def calCashConvCycle(inv, invm1, cogs, aR, nCS, aP):
    avgInv = ((float(inv) + float(invm1))/2)
    daysOfInvOutstanding = ((float(avgInv)/float(cogs))*365)
    daysOfSalesOutstanding = ((float(aR)/float(nCS))*365)
    daysOfPayablesOutstanding = ((float(aP))/(float(cogs)/365))
    cashConvCycle = daysOfInvOutstanding + daysOfSalesOutstanding - daysOfPayablesOutstanding

    return cashConvCycle

def calculateInterestCoverageRatio(ebit, leasePayments, interestExpense):
    fixedChargeCoverageRatio = ((float(ebit) + float(leasePayments)) / (float(interestExpense) + float(leasePayments)))
    interestCoverageRatio = (float(ebit) / float(interestExpense))
    return interestCoverageRatio, fixedChargeCoverageRatio

def invRatios(inv, invm1, cogs):
    avgInv = ((float(inv) + float(invm1)) / 2)
    inventoryTurnoverRatio = (float(cogs) / avgInv)
    daysOfInvOnHand = ((avgInv)/(float(cogs)/365))
    return inventoryTurnoverRatio, daysOfInvOnHand











def ttmTotalRevenue(currentRevenue, curRevM1, curRevm2, curRevm3 ):
    ttmTotalRevenue = sum(currentRevenue, curRevM1, curRevm2, curRevm3)
    return ttmTotalRevenue

def ttmCOGS(curCogs, curCOGSm1, curCOGSm2, curCOGSm3 ):
    ttmTotalCOGS = sum(curCogs, curCOGSm1, curCOGSm2, curCOGSm3)
    return ttmTotalCOGS

def ttmCostofRev(curCostofRev, curCostofRev1, curCostofRev2, curCostofRev3 ):
    ttmTotalCostofRev = sum(curCostofRev, curCostofRev1, curCostofRev2, curCostofRev3)
    return ttmTotalCostofRev

def ttmOperatingIncome(currOpIncome, currOpIncome1, currOpIncome2, currOpIncome3 ):
    ttmOperatingIncome = sum(currOpIncome, currOpIncome1, currOpIncome2, currOpIncome3)
    return ttmOperatingIncome

def ttmNetIncome(curNetIncome, curNetIncomem1, curNetIncomem2, curNetIncomem3 ):
    ttmNetIncome = float(curNetIncome) +float(curNetIncomem1)+ float(curNetIncomem2)+ float(curNetIncomem3)
    return ttmNetIncome

def ttmPreferedDivs(curPreferredDivs, curPreferredDivsm1, curPreferredDivsm2, curPreferredDivsm3 ):
    if curPreferredDivs != np.nan:
        ttmPreferedDivs = float(curPreferredDivs) + float(curPreferredDivsm1) + float(curPreferredDivsm2)+ float(curPreferredDivsm3)
        if curPreferredDivs == np.nan:
            ttmPreferedDivs = float(0)
            return ttmPreferedDivs
        print(type(ttmPreferedDivs))
        return ttmPreferedDivs


def avgInventory(curInv, curInvm1 ):
    avgInventory = sum(curInv, curInvm1) /2
    return avgInventory

def calculatedWeightedAverageSharesOutstanding(curComStockSharesOutstanding,curComStockSharesOutstandingm1,curComStockSharesOutstandingm2,curComStockSharesOutstandingm3):
    weightedAvgShares = (float(curComStockSharesOutstanding) + float(curComStockSharesOutstandingm1) + float(curComStockSharesOutstandingm2) + float(curComStockSharesOutstandingm3))/4
    return weightedAvgShares

# Valuation metrics
def calculateTrailingPE(quoteUnformatted, ttmbasicEPS):
    peRatio = (quoteUnformatted / ttmbasicEPS)
    return peRatio

def calculatePriceToCashFlow(quoteUnformatted, operatingCashFlowPerShare):
    priceToCashFlow = (float(quoteUnformatted) / operatingCashFlowPerShare)
    return priceToCashFlow

def calculatePS(quoteUnformatted, salesPerShare):
    psRatio = (float(quoteUnformatted) / float(salesPerShare))
    return psRatio



def calculateMarketCap(quoteUnformatted, sharesOutstanding):
    marketCap = (float(quoteUnformatted) * float(sharesOutstanding))
    return marketCap

def calculateMarketToBookValue(marketCap, totalAssets, totalDebt, preferredStock):
    bookValue = (float(marketCap) / (float(totalAssets) - float(totalDebt) - float(preferredStock)))
    return bookValue

def calculatePB(quoteUnformatted, bookValue):
    try:
        pbRatio = (float(quoteUnformatted) / float(bookValue))
    except Exception:
        pbRatio = np.nan
    return pbRatio

def calculatePEGRatio(pERatio, sustainableGrowthRate):
    pEG = (float(pERatio) / float(sustainableGrowthRate))
    return pEG

def calculateEarningsYield(basicEPS, quoteUnformatted):
    earningsYield = (float(basicEPS) / float(quoteUnformatted))
    return earningsYield

def calculateBasicEPS(ttm_netIncome, weightedAverageSharesOutstanding):
    basicEPS = ((float(ttm_netIncome) / weightedAverageSharesOutstanding))
    return basicEPS


def calculate_cfa_diluted_eps(net_income, preferred_divs, convertible_pref_dividends, convertible_debt_interest,
                              corporate_tax_rate, weighted_avg_shares, shares_from_convers_of_conv_pref_shares,
                              shares_from_conversion_of_debt, shares_issuable_from_stock_options):
    cfa_diluted_eps = (((net_income - preferred_divs) + convertible_pref_dividends + (
                convertible_debt_interest * (1 - corporate_tax_rate))) / (
                                   weighted_avg_shares + shares_from_convers_of_conv_pref_shares + shares_from_conversion_of_debt + shares_issuable_from_stock_options))
    return cfa_diluted_eps

def calculateOperatingCashFlowPerShare(operatingCashflow, weightedAverageSharesOutstanding):
    operatingCashFlowPerShare = (float(operatingCashflow) / weightedAverageSharesOutstanding)
    return operatingCashFlowPerShare

def calculateEBITDAperShare(ebitda, weightedAverageSharesOutstanding):
    ebitdaPerShare = (float(ebitda) / weightedAverageSharesOutstanding)
    return ebitdaPerShare

def calculateDividendsPerShare(dividendPayout, weightedAverageSharesOutstanding):
    dividendsPerShare = (float(dividendPayout) / weightedAverageSharesOutstanding)
    return dividendsPerShare



def calculateOperatingMargin(operatingIncome, totalRevenue):
    operatingMargin = (float(operatingIncome) / float(totalRevenue))
    return operatingMargin


def calculatePreTaxMargin(ebt, totalRevenue):
    preTaxMargin = (float(ebt) / float(totalRevenue))
    return preTaxMargin


def calculateNetProfitMargin(netIncome, totalRevenue):
    netProfitMargin = (float(netIncome) / float(totalRevenue))
    return netProfitMargin



def calculateSalesPerShare(totalRevenue, weightedAverageSharesOutstanding):
    salesPerShare = (float(totalRevenue) / weightedAverageSharesOutstanding)
    return salesPerShare


def calculateOperatingROA(operatingIncome, averageTotalAssets):
    operatingROA = (float(operatingIncome) / float(averageTotalAssets))
    return operatingROA

def calculateROA(netIncome, averageAssets):
    returnOnAssets = (float(netIncome) / float(averageAssets))
    return returnOnAssets

def calculateReturnOnTotalCapital(ebit, shortLongTermDebtTotal, totalShareholderEquity):
    try:
        returnOnTotalCapital = ((float(ebit)) / (float(shortLongTermDebtTotal) + float(totalShareholderEquity)))
    except Exception:
        returnOnTotalCapital = np.nan
    return returnOnTotalCapital

def calculateROE(netIncome, totalShareholderEquity):
    try:
        returnOnEquity = (float(netIncome) / float(totalShareholderEquity))
    except Exception:
        returnOnEquity = np.nan
    return returnOnEquity

def calculateReturnOnCommonEquity(netIncome, dividendPayoutPreferredStock, averageCommonEquity):
    try:
        returnOnCommonEquity = ((float(netIncome) - float(dividendPayoutPreferredStock)) / float(averageCommonEquity))
    except Exception:
        returnOnCommonEquity = np.nan
    return returnOnCommonEquity




def calculateDebtRatio(totalLiabilities, totalAssets):
    debtRatio = (float(totalLiabilities) / float(totalAssets))
    return debtRatio


def calculateDebtToEquity(totalDebt, totalShareholderEquity):
    try:
        debtToEquity = (float(totalDebt) / float(totalShareholderEquity))
    except Exception:
        debtToEquity = np.nan
    return debtToEquity

def calculateDebtToAssetRatio(shortLongTermDebtTotal, totalAssets):
    debtToAssetRatio = (float(shortLongTermDebtTotal) / float(totalAssets))
    return debtToAssetRatio


def calculateDebtToCapitalRatio(shortLongTermDebtTotal, totalShareholderEquity):
    try:
        debtToCapitalRatio = (
                    (float(shortLongTermDebtTotal)) / (float(totalShareholderEquity) + float(shortLongTermDebtTotal)))
    except Exception:
        debtToCapitalRatio = np.nan
    return debtToCapitalRatio

def calculateFinancialLeverageRatio(avgTotalAssets, avgTotalEquity):
    try:
        financialLeverage = (float(avgTotalAssets) / float(avgTotalEquity))
    except Exception:
        financialLeverage = np.nan
    return financialLeverage




# Solvency Ratios
def calculateCurrentRatio(totalCurrentAssets, totalCurrentLiabilities):
    currentRatio = (float(totalCurrentAssets) / float(totalCurrentLiabilities))
    return currentRatio


def calculateQuickRatio(totalCurrentAssets, totalCurrentLiabilities, inventory):
    quickRatio = ((float(totalCurrentAssets) - float(inventory)) / float(totalCurrentLiabilities))
    return quickRatio


def calculate_cfa_quick_ratio(cash, marketable_securities, recievables, current_liabilities):
    cfa_quick_ratio = ((float(cash) + float(marketable_securities) + float(recievables)) / float(current_liabilities))
    return cfa_quick_ratio


def calculateCashRatio(cashAndCashEquivalentsAtCarryingValue, currentLiabilities):
    cashRatio = (float(cashAndCashEquivalentsAtCarryingValue) / float(currentLiabilities))
    return cashRatio



# lIQUIDITY Ratios




def calculateInterestCoverageRatio(ebit, interestExpense):
    interestCoverageRatio = (float(ebit) / float(interestExpense))
    return interestCoverageRatio






# Dividend-Related


def calculateDividendPayoutRatio(dividendPayout, netIncome):
    payoutRatio = (float(dividendPayout) / float(netIncome))
    return payoutRatio


def calculateRetentionRate(payoutRatio):
    retentionRateB = (1 - payoutRatio)
    return retentionRateB


def calculateSustainableGrowthRate(retentionRateB, roe):
    SustainableGrowthRate = retentionRateB * roe
    return SustainableGrowthRate




# Activity Ratios
def calculateInventoryTurnover(cogs, averageInventory):
    try:
        inventoryTurnover = (float(cogs) / float(averageInventory))
    except Exception:
        inventoryTurnover = np.nan
    return inventoryTurnover


def calculateDaysOfInventoryOnHand(averageInventory, cogs):
    try:
        daysOfInventoryOnHand = ((float(averageInventory) / float(cogs)) * 365)
    except Exception:
        daysOfInventoryOnHand = np.nan
    return daysOfInventoryOnHand


def calculateRecievablesTurnover(totalRevenue, averageRecievables):
    try:
        recievablesTurnover = (float(totalRevenue) / float(averageRecievables))
    except Exception:
        recievablesTurnover = np.nan
    return recievablesTurnover

def calculateDaysOfSalesOutstanding(avgRecievables, totalRevenue):
    daysOfSalesOutstanding = ((float(avgRecievables) / float(totalRevenue)) * 365)
    return daysOfSalesOutstanding

def calculatePayablesTurnover(cogs, averageAccountsPayable):
    try:
        payablesTurnoverRatio = (float(cogs) / float(averageAccountsPayable))
    except Exception:
        payablesTurnoverRatio = np.nan

    if averageAccountsPayable == 0:
        payablesTurnoverRatio = np.nan
    return payablesTurnoverRatio


def calculateNumberOfDaysOfPayables(payablesTurnoverRatio):
    try:
        numberOfDaysOfPayables = (365 / float(payablesTurnoverRatio))
    except Exception:
        numberOfDaysOfPayables = np.nan
    return numberOfDaysOfPayables


def calculateWorkingCapitalTurnover(totalRevenue, averageWorkingCapital):
    try:
        workingCapitalTurnover = (float(totalRevenue) / float(averageWorkingCapital))
    except Exception:
        workingCapitalTurnover = np.nan
    return workingCapitalTurnover


def calculateFixedAssetTurnoverRatio(totalRevenue, averageNetFixedAssets):
    fixedAssetTurnoverRatio = (float(totalRevenue) / float(averageNetFixedAssets))
    return fixedAssetTurnoverRatio


def calculateTotalAssetTurnover(totalRevenue, averageTotalAssets):
    totalAssetTurnover = (float(totalRevenue) / float(averageTotalAssets))
    return totalAssetTurnover


# Coverage Ratios

def calculateDebtCoverageRatio(operatingCashFlow, shortLongTermDebtTotal):
    debtCoverageRatio = (float(operatingCashFlow) / float(shortLongTermDebtTotal))
    return debtCoverageRatio


def calculateInterestCoverageRatio(operatingCashFlow, interestExpense, incomeTaxExpense):
    try:
        interestCoverageRatio = ((float(operatingCashFlow) + float(interestExpense) + float(incomeTaxExpense)) / float(
            interestExpense))
    except Exception:
        interestCoverageRatio = np.nan
    return interestCoverageRatio





# Asset-based Valuation







def calculateEBIT(grossProfit, operatingExpenses):
    ebit = (float(grossProfit) - float(operatingExpenses))
    return ebit


def calculateEBT(ebit, interestExpense):
    try:
        ebt = (float(ebit) - float(interestExpense))
    except Exception:
        ebt = np.nan
    return ebt


def calculateWorkingCapital(totalCurrentAssets, totalCurrentLiabilities):
    try:
        workingCapital = ((float(totalCurrentAssets) - float(totalCurrentLiabilities)))
    except Exception:
        workingCapital = np.nan
    return workingCapital


def calculateNetFixedAssets(totalFixedAssets, accumulatedDepreciation):
    try:
        netFixedAssets = (float(totalFixedAssets) - float(accumulatedDepreciation))
    except Exception:
        netFixedAssets = np.nan
    return netFixedAssets


def calculateavgDailyExpenditures(tTMoperatingExpenses, tTMnonCashCharges):
    avgDailyExpenditures = ((float(tTMoperatingExpenses - float(tTMnonCashCharges)) / 365))
    return avgDailyExpenditures





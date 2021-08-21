import pandas as pd
import numpy as np

# Valuation metrics
def calculatePE(quoteUnformatted, basicEPS):
    peRatio = (quoteUnformatted / basicEPS)
    return peRatio

def calculateEarningsYield(basicEPS, quoteUnformatted):
    earningsYield = (basicEPS / quoteUnformatted)
    return earningsYield

def calculateMarketCap(quoteUnformatted, sharesOutstanding):
    marketCap = (float(quoteUnformatted) * float(sharesOutstanding))
    return marketCap

def calculateMarketToBookValue(marketCap, totalAssets, totalDebt, preferredStock):
    bookValue = (float(marketCap) / (float(totalAssets)-float(totalDebt)-float(preferredStock)))
    return bookValue

def calculatePB(quoteUnformatted, bookValue):
    pbRatio = (float(quoteUnformatted) / float(bookValue))
    return pbRatio

def calculateSalesPerShare(totalRevenue, weightedAverageSharesOutstanding):
    salesPerShare = (float(totalRevenue) / weightedAverageSharesOutstanding)
    return salesPerShare


def calculatePS(quoteUnformatted, salesPerShare):
    psRatio = (float(quoteUnformatted) / float(salesPerShare))
    return psRatio

def calculateOperatingCashFlowPerShare(operatingCashflow, weightedAverageSharesOutstanding):
    operatingCashFlowPerShare = (float(operatingCashflow) / weightedAverageSharesOutstanding)
    return operatingCashFlowPerShare

def calculatePriceToCashFlow(quoteUnformatted, operatingCashFlowPerShare):
    priceToCashFlow = (float(quoteUnformatted) / operatingCashFlowPerShare)
    return priceToCashFlow

# Liquidity Ratios
def calculateCurrentRatio(totalCurrentAssets, totalCurrentLiabilities):
    currentRatio = (float(totalCurrentAssets) / float(totalCurrentLiabilities))
    return currentRatio


def calculateQuickRatio(totalCurrentAssets, totalCurrentLiabilities, inventory):
    quickRatio = ((float(totalCurrentAssets) - float(inventory)) / float(totalCurrentLiabilities))
    return quickRatio


def calculate_cfa_quick_ratio(cash, marketable_securities, recievables, current_liabilities):
    cfa_quick_ratio = ((float(cash) + float(marketable_securities) + float(recievables)) / float(current_liabilities))
    return cfa_quick_ratio


# Leverage Ratios
def calculateDebtRatio(totalLiabilities, totalAssets):
    debtRatio = (float(totalLiabilities) / float(totalAssets))
    return debtRatio


def calculateDebtToEquity(totalDebt, totalShareholderEquity):
    debtToEquity = (float(totalDebt) / float(totalShareholderEquity))
    return debtToEquity

def calculateCashRatio( cashAndCashEquivalentsAtCarryingValue, currentLiabilities):
    cashRatio = ( float(cashAndCashEquivalentsAtCarryingValue) / float(currentLiabilities))
    return cashRatio

def calculateDebtToAssetRatio(shortLongTermDebtTotal, totalAssets):
    debtToAssetRatio = (float(shortLongTermDebtTotal) / float(totalAssets))
    return debtToAssetRatio

def calculateDebtToCapitalRatio(shortLongTermDebtTotal, totalShareholderEquity):
    debtToCapitalRatio = ((float(shortLongTermDebtTotal))/ (float(totalShareholderEquity)+float(shortLongTermDebtTotal)))
    return debtToCapitalRatio

def calculateInterestCoverageRatio(ebit, interestExpense):
    interestCoverageRatio = (float(ebit) / float(interestExpense))
    return interestCoverageRatio

def calculateFixedChargeCoverage(ebit, leasePayments, interestExpense):
    fixedChargeCoverageRatio = ((float(ebit) + float(leasePayments))/(float(interestExpense) + float(leasePayments)))
    return fixedChargeCoverageRatio

def calculateFinancialLeverageRatio(avgTotalAssets, avgTotalEquity):
    financialLeverage = (float(avgTotalAssets) / float(avgTotalEquity))
    return financialLeverage


# def calculate_fixed_charge_coverage_ratio =


# Profitability ratios

def calculateROE(netIncome, totalShareholderEquity):
    returnOnEquity = (float(netIncome) / float(totalShareholderEquity))
    return returnOnEquity


def calculateROA(netIncome, averageAssets):
    returnOnAssets = (float(netIncome) / float(averageAssets))
    return returnOnAssets

def calculateOperatingROA(operatingIncome, averageTotalAssets):
    operatingROA = (float(operatingIncome) / float(averageTotalAssets))
    return operatingROA

def calculateReturnOnTotalCapital(ebit, shortLongTermDebtTotal, totalShareholderEquity):
    returnOnTotalCapital = ((float(ebit))/(float(shortLongTermDebtTotal) + float(totalShareholderEquity)))
    return returnOnTotalCapital

def calculateReturnOnCommonEquity(netIncome, dividendPayoutPreferredStock, averageCommonEquity):
    returnOnCommonEquity = ((float(netIncome) - float(dividendPayoutPreferredStock))/ float(averageCommonEquity))
    return returnOnCommonEquity



# EPS Calculations

def calculateBasicEPS(ttm_netIncome, ttm_preferredDivs, weightedAverageSharesOutstanding):
    basicEPS = ((float(ttm_netIncome) - float(ttm_preferredDivs)) / weightedAverageSharesOutstanding)
    return basicEPS


def calculate_cfa_diluted_eps(net_income, preferred_divs, convertible_pref_dividends, convertible_debt_interest,
                              corporate_tax_rate, weighted_avg_shares, shares_from_convers_of_conv_pref_shares,
                              shares_from_conversion_of_debt, shares_issuable_from_stock_options):
    cfa_diluted_eps = (((net_income - preferred_divs) + convertible_pref_dividends + (convertible_debt_interest * (1 - corporate_tax_rate))) / (weighted_avg_shares + shares_from_convers_of_conv_pref_shares + shares_from_conversion_of_debt + shares_issuable_from_stock_options))
    return cfa_diluted_eps

def calculatePEGRatio(pERatio, sustainableGrowthRate):
    pEG = (float(pERatio) / float(sustainableGrowthRate))
    return pEG

# Activity Ratios
def calculateInventoryTurnover(cogs, averageInventory):
    inventoryTurnover = (float(cogs)/float(averageInventory))
    return inventoryTurnover


def calculateDaysOfInventoryOnHand(averageInventory, cogs):
    daysOfInventoryOnHand = ((float(averageInventory) / float(cogs))*365)
    return daysOfInventoryOnHand


def calculateRecievablesTurnover(totalRevenue, averageRecievables):
    try:
        recievablesTurnover = (float(totalRevenue) / float(averageRecievables))
    except Exception:
        recievablesTurnover = np.nan
    return recievablesTurnover

def calculatePayablesTurnover(cogs, averageAccountsPayable):
    try:
        payablesTurnoverRatio = (float(cogs) / float(averageAccountsPayable))
    except Exception:
        payablesTurnoverRatio = np.nan
    return averageAccountsPayable

def calculateNumberOfDaysOfPayables(payablesTurnoverRatio):
    try:
        numberOfDaysOfPayables = (365 / float(payablesTurnoverRatio))
    except Exception:
        numberOfDaysOfPayables = np.nan
    return numberOfDaysOfPayables

def calculateDaysOfSalesOutstanding(avgRecievables, totalRevenue):
    daysOfSalesOutstanding = ((float(avgRecievables) / float(totalRevenue)) *365)
    return daysOfSalesOutstanding


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

#Coverage Ratios

def calculateDebtCoverageRatio(operatingCashFlow, shortLongTermDebtTotal ):
    debtCoverageRatio = (float(operatingCashFlow) / float(shortLongTermDebtTotal))
    return debtCoverageRatio


def calculateInterestCoverageRatio(operatingCashFlow, interestExpense, incomeTaxExpense):
    try:
        interestCoverageRatio = ((float(operatingCashFlow) + float(interestExpense) + float(incomeTaxExpense)) / float(interestExpense))
    except Exception:
        interestCoverageRatio = np.nan
    return interestCoverageRatio

#Dividend-Related

def calculateDividendsPerShare(dividendPayout, weightedAverageSharesOutstanding ):
    dividendsPerShare = (float(dividendPayout) / weightedAverageSharesOutstanding)
    return dividendsPerShare

def calculateDividendPayoutRatio(dividendPayout, netIncome):
    payoutRatio = (float(dividendPayout) / float(netIncome))
    return payoutRatio

def calculateRetentionRate(payoutRatio):
    retentionRateB = (1-payoutRatio)
    return retentionRateB

def calculateSustainableGrowthRate(retentionRateB, roe):
    SustainableGrowthRate = retentionRateB * roe
    return SustainableGrowthRate

# Asset-based Valuation

def calculateGrossProfitMargin(totalRevenue, cogs):
    grossProfitMargin = ((float(totalRevenue) - float(cogs))/ float(totalRevenue))
    return grossProfitMargin

def calculateOperatingMargin(operatingIncome, totalRevenue):
    operatingMargin = (float(operatingIncome) / float(totalRevenue))
    return operatingMargin

def calculatePreTaxMargin(ebt, totalRevenue):
    preTaxMargin = (float(ebt) / float(totalRevenue))
    return preTaxMargin

def calculateNetProfitMargin(netIncome, totalRevenue):
    netProfitMargin = (float(netIncome) / float(totalRevenue))
    return netProfitMargin

def calculateEBITDAperShare(ebitda, weightedAverageSharesOutstanding):
    ebitdaPerShare = (float(ebitda) / weightedAverageSharesOutstanding)
    return ebitdaPerShare

def calculateEBIT(grossProfit, operatingExpenses):
    ebit = (float(grossProfit) - float(operatingExpenses))
    return ebit

def calculateEBT(ebit, interestExpense):
    ebt = (float(ebit) - float(interestExpense))
    return ebt

def calculateWorkingCapital(totalCurrentAssets, totalCurrentLiabilities):
    workingCapital = ((float(totalCurrentAssets) - float(totalCurrentLiabilities)))
    return workingCapital

def calculateNetFixedAssets(totalFixedAssets, accumulatedDepreciation):
    netFixedAssets = (float(totalFixedAssets) - float(accumulatedDepreciation))
    return netFixedAssets
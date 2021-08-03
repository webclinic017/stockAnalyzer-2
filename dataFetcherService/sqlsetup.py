import mysql
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0595",
    database="stockanalyzerproject",

)

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE stockanalyzerproject")

# mycursor.execute("CREATE TABLE isStockRequest ("
#                  "stockTicker VARCHAR(10),"
#                  "fiscalDateEnding DATE,"
#                  "reportedCurrency VARCHAR(10),"
#                  "grossProfit DECIMAL(15,6), "
#                  "totalRevenue DECIMAL(15,6),"
#                  "costOfRevenue DECIMAL(15,6),"
#                  "costofGoodsAndServicesSold DECIMAL(15,6),"
#                  "operatingIncome DECIMAL(15,6),"
#                  "sellingGeneralAndAdministrative DECIMAL(15,6),"
#                  "researchAndDevelopment DECIMAL(15,6),"
#                  "operatingExpenses DECIMAL(15,6),"
#                  "investmentIncomeNet DECIMAL(15,6),"
#                  "netInterestIncome DECIMAL(15,6),"
#                  "interestIncome DECIMAL(15,6),"
#                  "interestExpense DECIMAL(15,6),"
#                  "nonInterestIncome DECIMAL(15,6),"
#                  "otherNonOperatingIncome DECIMAL(15,6),"
#                  "depreciation DECIMAL(15,6),"
#                  "depreciationAndAmortization DECIMAL(15,6),"
#                  "incomeBeforeTax DECIMAL(15,6),"
#                  "incomeTaxExpense DECIMAL(15,6),"
#                  "interestAndDebtExpense DECIMAL(15,6),"
#                  "netIncomeFromContinuingOperations DECIMAL(15,6),"
#                  "comprehensiveIncomeNetOfTax DECIMAL(15,6),"
#                  "ebit DECIMAL(15,6),"
#                  "ebitda DECIMAL(15,6),"
#                  "netIncome DECIMAL(15,6),"
#                  "stockRequestID int PRIMARY KEY AUTO_INCREMENT   )")


# Created a mySQL Table for the annual Balanace Sheet


# mycursor.execute("CREATE TABLE bsStockRequest ("
#                  "stockTicker VARCHAR(10),"
#                  "fiscalDateEnding DATE,"
#                  "reportedCurrency VARCHAR(10),"
#                  "totalAssets DECIMAL(15,6),"
#                  "totalCurrentAssets DECIMAL(15,6),"
#                  "cashAndCashEquivalentsAtCarryingValue DECIMAL(15,6),"
#                  "cashAndShortTermInvestments DECIMAL(15,6),"
#                  "inventory DECIMAL(15,6),"
#                  "currentNetReceivables DECIMAL(15,6),"
#                  "totalNonCurrentAssets DECIMAL(15,6),"
#                  "propertyPlantEquipment DECIMAL(15,6),"
#                  "accumulatedDepreciationAmortizationPPE DECIMAL(15,6),"
#                  "intangibleAssets DECIMAL(15,6),"
#                  "intangibleAssetsExcludingGoodwill DECIMAL(15,6),"
#                  "goodwill DECIMAL(15,6),"
#                  "investments DECIMAL(15,6),"
#                  "longTermInvestments DECIMAL(15,6),"
#                  "shortTermInvestments DECIMAL(15,6),"
#                  "otherCurrentAssets DECIMAL(15,6),"
#                  "otherNonCurrrentAssets DECIMAL(15,6),"
#                  "totalLiabilities DECIMAL(15,6),"
#                  "totalCurrentLiabilities DECIMAL(15,6),"
#                  "currentAccountsPayable DECIMAL(15,6),"
#                  "deferredRevenue DECIMAL(15,6),"
#                  "currentDebt DECIMAL(15,6),"
#                  "shortTermDebt DECIMAL(15,6),"
#                  "totalNonCurrentLiabilities DECIMAL(15,6),"
#                  "capitalLeaseObligations DECIMAL(15,6),"
#                  "longTermDebt DECIMAL(15,6),"
#                  "currentLongTermDebt DECIMAL(15,6),"
#                  "longTermDebtNoncurrent DECIMAL(15,6),"
#                  "shortLongTermDebtTotal DECIMAL(15,6),"
#                  "otherCurrentLiabilities DECIMAL(15,6),"
#                  "otherNonCurrentLiabilities DECIMAL(15,6),"
#                  "totalShareholderEquity DECIMAL(15,6),"
#                  "treasuryStock DECIMAL(15,6),"
#                  "retainedEarnings DECIMAL(15,6),"
#                  "commonStock DECIMAL(15,6),"
#                  "commonStockSharesOutstanding DECIMAL(15,6),"
#                  "stockRequestID int PRIMARY KEY AUTO_INCREMENT   )")


mycursor.execute("CREATE TABLE cfStockRequest ("
                 "stockTicker VARCHAR(10),"
                 "fiscalDateEnding DATE,"
                 "reportedCurrency VARCHAR(10),"
                 "operatingCashflow DECIMAL(15,6),"
                 "paymentsForOperatingActivities DECIMAL(15,6),"
                 "proceedsFromOperatingActivities DECIMAL(15,6),"
                 "changeInOperatingLiabilities DECIMAL(15,6),"
                 "changeInOperatingAssets DECIMAL(15,6),"
                 "depreciationDepletionAndAmortization DECIMAL(15,6),"
                 "capitalExpenditures DECIMAL(15,6),"
                 "changeInReceivables DECIMAL(15,6),"
                 "changeInInventory DECIMAL(15,6),"
                 "profitLoss DECIMAL(15,6),"
                 "cashflowFromInvestment DECIMAL(15,6),"
                 "cashflowFromFinancing DECIMAL(15,6),"
                 "proceedsFromRepaymentsOfShortTermDebt DECIMAL(15,6),"
                 "paymentsForRepurchaseOfCommonStock DECIMAL(15,6),"
                 "paymentsForRepurchaseOfEquity DECIMAL(15,6),"
                 "paymentsForRepurchaseOfPreferredStock DECIMAL(15,6),"
                 "dividendPayout DECIMAL(15,6),"
                 "dividendPayoutCommonStock DECIMAL(15,6),"
                 "dividendPayoutPreferredStock DECIMAL(15,6),"
                 "proceedsFromIssuanceOfCommonStock DECIMAL(15,6),"
                 "proceedsFromIssuanceOfLongTermDebtAndCapitalSec DECIMAL(15,6),"
                 "proceedsFromIssuanceOfPreferredStock DECIMAL(15,6),"
                 "proceedsFromRepurchaseOfEquity DECIMAL(15,6),"
                 "proceedsFromSaleOfTreasuryStock DECIMAL(15,6),"
                 "changeInCashAndCashEquivalents DECIMAL(15,6),"
                 "changeInExchangeRate DECIMAL(15,6),"
                 "netIncome DECIMAL(15,6),"
                 "stockRequestID int PRIMARY KEY AUTO_INCREMENT   )")

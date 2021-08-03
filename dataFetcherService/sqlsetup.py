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

mycursor.execute("CREATE TABLE isStockRequest ("
                 "stockTicker VARCHAR(10),"
                 "fiscalDateEnding DATE,"
                 "reportedCurrency VARCHAR(10),"
                 "grossProfit DECIMAL(15,6), "
                 "totalRevenue DECIMAL(15,6),"
                 "costOfRevenue DECIMAL(15,6),"
                 "costofGoodsAndServicesSold DECIMAL(15,6),"
                 "operatingIncome DECIMAL(15,6),"
                 "sellingGeneralAndAdministrative DECIMAL(15,6),"
                 "researchAndDevelopment DECIMAL(15,6),"
                 "operatingExpenses DECIMAL(15,6),"
                 "investmentIncomeNet DECIMAL(15,6),"
                 "netInterestIncome DECIMAL(15,6),"
                 "interestIncome DECIMAL(15,6),"
                 "interestExpense DECIMAL(15,6),"
                 "nonInterestIncome DECIMAL(15,6),"
                 "otherNonOperatingIncome DECIMAL(15,6),"
                 "depreciation DECIMAL(15,6),"
                 "depreciationAndAmortization DECIMAL(15,6),"
                 "incomeBeforeTax DECIMAL(15,6),"
                 "incomeTaxExpense DECIMAL(15,6),"
                 "interestAndDebtExpense DECIMAL(15,6),"
                 "netIncomeFromContinuingOperations DECIMAL(15,6),"
                 "comprehensiveIncomeNetOfTax DECIMAL(15,6),"
                 "ebit DECIMAL(15,6),"
                 "ebitda DECIMAL(15,6),"
                 "netIncome DECIMAL(15,6),"
                 "stockRequestID int PRIMARY KEY AUTO_INCREMENT   )")

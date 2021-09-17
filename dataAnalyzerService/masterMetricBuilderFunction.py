import pandas as pd
import numpy as np
from stockstatcalculations import *


statsColumns = ['tm19', 'tm18', 'tm17', 'tm16', 'tm15', 'tm14', 'tm13', 'tm12', 'tm11', 'tm10', 'tm9', 'tm8', 'tm7', 'tm6', 'tm5','tm4', 'tm3','tm2', 'tm1', 't']
statsRows = ['priceToEarnings', 'priceToCashFlow', 'priceToSales', 'priceToBook', 'pEG', 'earningsYield', 'grossProfitMargin', 'operatingProfitMargin', 'netProfitMargin', 'ttmgrossProfitMargin', 'ttmoperatingProfitMargin', 'ttmnetProfitMargin', 'basicEPS', 'dilutedEPS', 'cashFlowPerShare', 'eBITDAperShare', 'divPerShare', 'operatinROA', 'rOA', 'returnOnTotalCapital', 'rOE', 'returnOnCommonEquity', 'debtRatio', 'debtToEquity', 'debtToAsset', 'debtToCapital', 'financialLeverage', 'currentRatio', 'quickRatio','cashRatio', 'deffensiveInterval', 'cashConversionCycle', 'interestCoverage', 'fixedChargeCoverage', 'divPayoutRatio', 'retentionRateB', 'sustainableGrowthRate', 'inventoryTurnoverRatio', ' daysOfInvOnHand', 'recievablesTurnover', 'daysOfSalesOutstanding', 'payableTurnover', 'numDaysofPayables', 'workingCapitalTurnover', 'fixedAssetTurnover', 'totalAssetTurnover']

metricsDf = pd.DataFrame(data=np.nan ,columns=statsColumns, index=statsRows)
print(metricsDf)
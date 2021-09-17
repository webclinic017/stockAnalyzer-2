import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pypfopt
from pypfopt import risk_models
from pypfopt import plotting
from pypfopt import expected_returns
from pypfopt import EfficientFrontier
from portfolioAnalysis.portfolioOptimization import *


twgGrowth = ['AMZN', 'AZO', 'HD', 'PEP', 'ALLY', 'BLK', 'BX', 'JPM', 'SCHW', 'AMGN', 'ANTM', 'BMY', 'ISRG', 'SYK', 'TMO', 'UNH', 'CAT', 'DE', 'FTV', 'LUV', 'AAPL', 'ADBE', 'ADP', 'AKAM', 'GLW', 'MSFT', 'NVDA', 'PYPL', 'V', 'SHW', 'ATVI', 'CMCSA', 'DIS', 'FB', 'GOOGL', 'NEE', 'RSP']
growthCons = ['GOOG', 'AAPL', 'MSFT', 'NEE', 'AMZN', 'UNH', 'FTV', 'SHW', 'ADBE']
twgQuantitativeMomentum = ['AZO', 'DG', 'ETSY', 'TPX', 'TSCO', 'MNST', 'USFD', 'AJG', 'MMC', 'DHR', 'WST', 'KSU', 'ODFL', 'MSI', 'ORCL', 'TTD', 'TYL', 'WORK', 'FCX', 'ATVI', 'LBRDK', 'PINS', 'ROKU', 'TMUS', 'AWK']
quantMoMoCons = ['ODFL', 'DHR', 'WST', 'AWK', 'PINS',  'TMUS', 'ETSY', 'TPX', 'TTD']
twgDividendPortfolio = ['MCD', 'TGT', 'KO', 'PG', 'PM', 'WMT', 'CVX', 'AXP', 'BAC', 'BLK', 'C', 'CB', 'JPM', 'KRE', 'MET', 'ABBV', 'BMY', 'CVS', 'JNJ', 'MDT', 'UNH', 'EMR', 'LMT', 'NOC', 'PH', 'AAPl', 'CSCO', 'MSFT', 'HUM', 'CMCSA', 'VZ', 'NEE', 'SRE', 'CCI', 'SPG']
divCon = ['BAC', 'KO', 'AAPL', 'CMCSA', 'TGT', 'PG', 'BYM', 'AXP', 'CVX', 'KRE', 'BTC-USD']
twgDynamic = ['APTV', 'DG', 'DHI', 'KMX', 'LULU', 'MAR', 'PDD', 'TSLA', 'CFG', 'SYF', 'INCY', 'MRNA', 'TDOC', 'LUV', 'UBER', 'URI', 'ASML', 'DOCU', 'QCOM', 'SEDG', 'ZBRA', 'FCX', 'FB', 'MTCH', 'NFLX', 'TTWO', 'VICI', 'CWI', 'IWM']
dynamicCons = [ 'QCOM', 'FB', 'NFLX', 'TDOC', 'DG','LUV','CFG', 'KMX',  'BTC-USD']
twgMidCapPortfolio = ['AAP', 'FIVE', 'PVH', 'ROST', 'CAG', 'VLO', 'ALLY', 'EWBC', 'FRC', 'HLNE', 'SIVB', 'HAE', 'HOLX', 'IQV', 'LH', 'DCI', 'FTV', 'INFO', 'KNX', 'LUV', 'OSK', 'PH', 'ST', 'SQK', 'TRU', 'ANET', 'APH', 'CDK', 'CIEN', 'IIVI', 'IT', 'PANW', 'RAMP', 'SAIC', 'WEX', 'FCX', 'FMC', 'PPG', 'SIRI', 'TTWO', 'AES', 'CONE', 'GLPI', 'WELL']
midCapCons = ['AAP', 'CAG', 'FIVE', 'ALLY', 'HAE', 'DCF', 'HOLX', 'LH', 'DCI', 'OSK',]

#Growth Opt
# calculateOptWeightsForLongOnlyGMVP(twgGrowth)
# calculateOptWeightsForLongShortGMVP(twgGrowth)
# calculateOptWeightsForLongOnlyTangencyPortfolio(twgGrowth)
# calculateOptWeightsForLongShortTangencyPortffolio(twgGrowth)
# monteCarloEfficientFrontier(twgGrowth)


# #QuantMoMo Opt
calculateOptWeightsForLongOnlyGMVP(divCon)
calculateOptWeightsForLongShortGMVP(divCon)
calculateOptWeightsForLongOnlyTangencyPortfolio(divCon)
calculateOptWeightsForLongShortTangencyPortffolio(divCon)
monteCarloEfficientFrontier(divCon)

optimize(divCon)
#
# #DivPort Opt
# calculateOptWeightsForLongOnlyGMVP(twgGrowth, "twgDividend")
# calculateOptWeightsForLongShortGMVP(twgGrowth, "twgDividend")
# calculateOptWeightsForLongOnlyTangencyPortfolio(twgGrowth, "twgDividend")
# calculateOptWeightsForLongShortTangencyPortffolio(twgGrowth, "twgDividend")
#
# #Dynamic Opt
# calculateOptWeightsForLongOnlyGMVP(twgGrowth, "twgDynamic")
# calculateOptWeightsForLongShortGMVP(twgGrowth, "twgDynamic")
# calculateOptWeightsForLongOnlyTangencyPortfolio(twgGrowth, "twgDynamic")
# calculateOptWeightsForLongShortTangencyPortffolio(twgGrowth, "twgDynamic")
#
# #MidCap Opt
# calculateOptWeightsForLongOnlyGMVP(twgGrowth, "twgMidCap")
# calculateOptWeightsForLongShortGMVP(twgGrowth, "twgMidCap")
# calculateOptWeightsForLongOnlyTangencyPortfolio(twgGrowth, "twgMidCap")
# calculateOptWeightsForLongShortTangencyPortffolio(twgGrowth, "twgMidCap")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

#Creating Dataframe for Historical Prices
dfForPiCycle = pd.read_csv('btcPriceHistory.csv', index_col='Date')
print(dfForPiCycle)

pd.set_option('display.max_rows', None)
dfForPiCycleReversed = dfForPiCycle.iloc[::-1]
dfForPiCycle['111MA'] = dfForPiCycleReversed.rolling(111).mean()
dfForPiCycle['350MA'] = dfForPiCycleReversed.rolling(350).mean()
dfForPiCycle['2x350'] = 2 * dfForPiCycle['350MA']

print(dfForPiCycle.head(500))

mpf.plot(dfForPiCycle, type='line')
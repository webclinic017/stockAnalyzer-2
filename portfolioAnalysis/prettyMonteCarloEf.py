import pathlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import datetime

# importing FinQuant's function to automatically build the portfolio
from finquant.portfolio import build_portfolio


twgGrowth = ['AMZN', 'AZO', 'HD', 'PEP', 'ALLY', 'BLK', 'BX', 'JPM', 'SCHW', 'AMGN', 'ANTM', 'BMY', 'ISRG', 'SYK', 'TMO', 'UNH', 'CAT', 'DE', 'FTV', 'LUV', 'AAPL', 'ADBE', 'ADP', 'AKAM', 'GLW', 'MSFT', 'NVDA', 'PYPL', 'V', 'SHW', 'ATVI', 'CMCSA', 'DIS', 'FB', 'GOOGL', 'NEE', 'RSP']
growthCons = ['GOOG', 'AAPL', 'MSFT', 'NEE', 'AMZN', 'UNH', 'FTV', 'SHW', 'ADBE']

twgQuantitativeMomentum = ['AZO', 'DG', 'ETSY', 'TPX', 'TSCO', 'MNST', 'USFD', 'AJG', 'MMC', 'DHR', 'WST', 'KSU', 'ODFL', 'MSI', 'ORCL', 'TTD', 'TYL', 'WORK', 'FCX', 'ATVI', 'LBRDK', 'PINS', 'ROKU', 'TMUS', 'AWK']

quantMoMoCons = ['ODFL', 'DHR', 'WST', 'AWK', 'PINS', 'TMUS', 'ETSY', 'TPX', 'TTD']

twgDividendPortfolio = ['MCD', 'TGT', 'KO', 'PG', 'PM', 'WMT', 'CVX', 'AXP', 'BAC', 'BLK', 'C', 'CB', 'JPM', 'KRE', 'MET', 'ABBV', 'BMY', 'CVS', 'JNJ', 'MDT', 'UNH', 'EMR', 'LMT', 'NOC', 'PH', 'AAPl', 'CSCO', 'MSFT', 'HUM', 'CMCSA', 'VZ', 'NEE', 'SRE', 'CCI', 'SPG']
divCon = ['BAC', 'KO', 'AAPL', 'MSFT', 'TGT', 'PG', 'BYM', 'AXP', 'CVX', 'KRE']
twgDynamic = ['APTV', 'DG', 'DHI', 'KMX', 'LULU', 'MAR', 'PDD', 'TSLA', 'CFG', 'SYF', 'INCY', 'MRNA', 'TDOC', 'LUV', 'UBER', 'URI', 'ASML', 'DOCU', 'QCOM', 'SEDG', 'ZBRA', 'FCX', 'FB', 'MTCH', 'NFLX', 'TTWO', 'VICI', 'CWI', 'IWM']

dynamicCons = [ 'QCOM', 'FB', 'NFLX', 'TDOC', 'DG','LUV','CFG', 'KMX', 'TSLA']

twgMidCapPortfolio = ['AAP', 'FIVE', 'PVH', 'ROST', 'CAG', 'VLO', 'ALLY', 'EWBC', 'FRC', 'HLNE', 'SIVB', 'HAE', 'HOLX', 'IQV', 'LH', 'DCI', 'FTV', 'INFO', 'KNX', 'LUV', 'OSK', 'PH', 'ST', 'SQK', 'TRU', 'ANET', 'APH', 'CDK', 'CIEN', 'IIVI', 'IT', 'PANW', 'RAMP', 'SAIC', 'WEX', 'FCX', 'FMC', 'PPG', 'SIRI', 'TTWO', 'AES', 'CONE', 'GLPI', 'WELL']
midCapCons = ['AAP', 'CAG', 'FIVE', 'ALLY', 'HAE', 'DCF', 'HOLX', 'LH', 'DCI', 'OSK',]




plt.style.use("seaborn-darkgrid")
# set line width
plt.rcParams["lines.linewidth"] = 2
# set font size for titles
plt.rcParams["axes.titlesize"] = 14
# set font size for labels on axes
plt.rcParams["axes.labelsize"] = 12
# set size of numbers on x-axis
plt.rcParams["xtick.labelsize"] = 10
# set size of numbers on y-axis
plt.rcParams["ytick.labelsize"] = 10
# set figure size
plt.rcParams["figure.figsize"] = (10, 6)

prices = yf.download(dynamicCons, period="max")
df_data = prices["Adj Close"].dropna(how="all")



print('-----------------------------')
print(df_data)
print('-----------------------------')
# building a portfolio by providing stock data
pf = build_portfolio(data=df_data)
print(pf)
pf.properties()

# <markdowncell>

# # Portfolio optimisation
# ## Efficient Frontier
# Based on the **Efficient Frontier**, the portfolio can be optimised for
#  - minimum volatility
#  - maximum Sharpe ratio
#  - minimum volatility for a given target return
#  - maximum Sharpe ratio for a given target volatility
# See below for an example for each optimisation.

# <codecell>

# if needed, change risk free rate and frequency/time window of the portfolio
print("pf.risk_free_rate = {}".format(pf.risk_free_rate))
print("pf.freq = {}".format(pf.freq))

# <codecell>

pf.ef_minimum_volatility(verbose=True)

# <codecell>

# optimisation for maximum Sharpe ratio
pf.ef_maximum_sharpe_ratio(verbose=True)

# <codecell>

# minimum volatility for a given target return of 0.26
pf.ef_efficient_return(0.26, verbose=True)

# <codecell>

# maximum Sharpe ratio for a given target volatility of 0.22
pf.ef_efficient_volatility(0.22, verbose=True)

# <markdowncell>

# ### Manually creating an instance of EfficientFrontier
# If required, or preferred, the below code shows how the same is achieved by manually creating an instance of EfficientFrontier, passing it the mean returns and covariance matrix of the previously assembled portfolio.

# <codecell>

from finquant.efficient_frontier import EfficientFrontier

# creating an instance of EfficientFrontier
ef = EfficientFrontier(pf.comp_mean_returns(freq=1), pf.comp_cov())
# optimisation for minimum volatility
print(ef.minimum_volatility())

# <codecell>

# printing out relevant quantities of the optimised portfolio
(expected_return, volatility, sharpe) = ef.properties(verbose=True)

# <markdowncell>

# ### Computing and visualising the Efficient Frontier
# `FinQuant` offers several ways to compute the *Efficient Frontier*.
#  1. Through the opject `pf`
#   - with automatically setting limits of the *Efficient Frontier*
#  2. By manually creating an instance of `EfficientFrontier` and providing the data from the portfolio
#   - with automatically setting limits of the *Efficient Frontier*
#   - by providing a range of target expected return values
# As before, let `pf` and be an instance of `Portfolio`. The following code snippets compute and plot an *Efficient Frontier* of a portfolio, its optimised portfolios and individual stocks within the portfolio.
#  - `pf.ef_plot_efrontier()`
#  - `pf.ef_plot_optimal_portfolios()`
#  - `pf.plot_stocks()`

# <markdowncell>

# #### Efficient Frontier of `pf`

# <codecell>

# computing and plotting efficient frontier of pf
pf.ef_plot_efrontier()
# adding markers to optimal solutions
pf.ef_plot_optimal_portfolios()
# and adding the individual stocks to the plot
pf.plot_stocks()
plt.show()

# <markdowncell>

# #### Manually creating an Efficient Frontier with target return values

# <codecell>

targets = np.linspace(0.12, 0.45, 50)
# computing efficient frontier
efficient_frontier = ef.efficient_frontier(targets)
# plotting efficient frontier
ef.plot_efrontier()
# adding markers to optimal solutions
pf.ef.plot_optimal_portfolios()
# and adding the individual stocks to the plot
pf.plot_stocks()
plt.show()

# <markdowncell>

# ## Monte Carlo
# Perform a Monte Carlo run to find the portfolio with the minimum volatility and maximum Sharpe Ratio.

# <codecell>

opt_w, opt_res = pf.mc_optimisation(num_trials=5000)
pf.mc_properties()
pf.mc_plot_results()
# again, the individual stocks can be added to the plot
pf.plot_stocks()
plt.show()

# <codecell>

print(opt_res)
print()
print(opt_w)

# <markdowncell>

# # Optimisation overlay
# ## Overlay of Monte Carlo portfolios and Efficient Frontier solutions

# <codecell>

opt_w, opt_res = pf.mc_optimisation(num_trials=5000)
pf.mc_plot_results()
pf.ef_plot_efrontier()
pf.ef.plot_optimal_portfolios()
pf.plot_stocks()
plt.show()

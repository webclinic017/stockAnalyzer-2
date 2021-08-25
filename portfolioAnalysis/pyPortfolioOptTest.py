import pandas as pd
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json

import pypfopt
from pypfopt import risk_models
from pypfopt import plotting
from pypfopt import expected_returns
from pypfopt import EfficientFrontier
from pypfopt import EfficientCVaR
from pypfopt import CLA

INVESTMENT = 2000

# PTR = PetroChina Company Limited ADR
# BUD = Anheuser Busch Inbev SA (AB InBev)
# XOM = Exxon Mobil Corporation
# BA = Boeing Co
# CHTR = Charter Communications Inc
# SHOP = Shopify Inc
# NVDA = NVIDIA Corporation
# NKE = Nike Inc

TICKERS =['PTR','BUD', 'XOM', 'BA','CHTR', 'SHOP', 'NVDA', 'NKE']

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

stocks_prices = pd.DataFrame({'A': []})
stocks_info = pd.DataFrame({'A': []})


for i, ticker in enumerate(TICKERS):
    print(i, ticker)
    yticker = yf.Ticker(ticker)

    # Get max history of prices
    historyPrices = yticker.history(period='max')
    # generate features for historical prices, and what we want to predict
    historyPrices['Ticker'] = ticker
    historyPrices['Year'] = historyPrices.index.year
    historyPrices['Month'] = historyPrices.index.month
    historyPrices['Weekday'] = historyPrices.index.weekday
    historyPrices['Date'] = historyPrices.index.date

    # historical returns
    for i in [1, 3, 7, 30, 90, 365]:
        historyPrices['growth_' + str(i) + 'd'] = historyPrices['Close'] / historyPrices['Close'].shift(i)

    # future growth 3 days
    historyPrices['future_growth_3d'] = historyPrices['Close'].shift(-3) / historyPrices['Close']

    # 30d rolling volatility : https://ycharts.com/glossary/terms/rolling_vol_30
    historyPrices['volatility'] = historyPrices['Close'].rolling(30).std() * np.sqrt(252)

    if stocks_prices.empty:
        stocks_prices = historyPrices
    else:
        stocks_prices = pd.concat([stocks_prices, historyPrices], ignore_index=True)




# Check one day
filter_last_date = stocks_prices.Date==stocks_prices.Date.max()
print(stocks_prices.Date.max())

# https://medium.com/analytics-vidhya/how-to-create-a-stock-correlation-matrix-in-python-4f32f8cb5b50
df_pivot = stocks_prices.pivot('Date','Ticker','Close').reset_index()
df_pivot.tail(5)


# https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/
df_pivot.corr()

# https://seaborn.pydata.org/generated/seaborn.heatmap.html

#def covMatrix(df_pivot):
corr = df_pivot.corr(method='pearson')
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(corr, mask=mask, vmax=.3, square=True, annot=True, cmap='RdYlGn')
plt.savefig("covMatrix.png")


#def covm1(df.pivot):


# User guide: https://pyportfolioopt.readthedocs.io/en/latest/UserGuide.html
# https://github.com/robertmartin8/PyPortfolioOpt

print(f'\n Library version: {pypfopt.__version__}')



# json: for pretty print of a dictionary: https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python/44689627

mu = expected_returns.capm_return(df_pivot.set_index('Date'))
# Other options for the returns values: expected_returns.ema_historical_return(df_pivot.set_index('Date'))
# Other options for the returns values: expected_returns.mean_historical_return(df_pivot.set_index('Date'))
print(f'Expected returns for each stock: {mu} \n')

S = risk_models.CovarianceShrinkage(df_pivot.set_index('Date')).ledoit_wolf()



# Weights between 0 and 1 - we don't allow shorting
ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))
ef.min_volatility()
weights_min_volatility = ef.clean_weights()

print(f'Portfolio weights for min volatility optimisation (lowest level of risk): {json.dumps(weights_min_volatility, indent=4, sort_keys=True)} \n')
print(f'Portfolio performance: {ef.portfolio_performance(verbose=True, risk_free_rate=0.01305)} \n')
# Risk-free rate : 10Y TBonds rate on 21-Jul-2021 https://www.cnbc.com/quotes/US10Y


# MIN VOL PORTFOLIO OPTIMAL WEIGHTS
#pd.Series(weights_min_volatility).plot.barh(title = 'Optimal Portfolio Weights (min volatility) by PyPortfolioOpt');

ef.max_sharpe()
weights_max_sharpe = ef.clean_weights()
plt.savefig("optimalPortfolioWeightsForMinVar.png")

print(f'Portfolio weights for max Sharpe optimisation (highest return-per-risk): {json.dumps(weights_max_sharpe, indent=4, sort_keys=True)} \n')
print(f'Portfolio performance: {ef.portfolio_performance(verbose=True, risk_free_rate=0.01305)} \n')


ef = EfficientFrontier(mu, S)
ef.max_sharpe()
weight_arr = ef.weights
ef.portfolio_performance(verbose=True);
returns = expected_returns.returns_from_prices(df_pivot.set_index('Date')).dropna()
returns.head()


# Compute CVaR
portfolio_rets = (returns * weight_arr).sum(axis=1)
portfolio_rets.hist(bins=50);


# VaR
var = portfolio_rets.quantile(0.05)
cvar = portfolio_rets[portfolio_rets <= var].mean()
print("VaR: {:.2f}%".format(100*var))
print("CVaR: {:.2f}%".format(100*cvar))


ec = EfficientCVaR(mu, returns)
ec.min_cvar()
ec.portfolio_performance(verbose=True);


cla = CLA(mu, S)
cla.max_sharpe()
cla.portfolio_performance(verbose=True, risk_free_rate=0.01305);

#basic Eff Frontier

plotting.plot_efficient_frontier(cla, showfig=False)
plt.savefig('basicEF.png')



#Monte Carlo Efficient Frontier
n_samples = 10000
w = np.random.dirichlet(np.ones(len(mu)), n_samples)
rets = w.dot(mu)
stds = np.sqrt((w.T * (S @ w.T)).sum(axis=0))
sharpes = rets / stds

print("Sample portfolio returns:", rets)
print("Sample portfolio volatilities:", stds)



# Plot efficient frontier with Monte Carlo sim
ef = EfficientFrontier(mu, S)

fig, ax = plt.subplots()
plotting.plot_efficient_frontier(ef, ax=ax, show_assets=False)

# Find and plot the tangency portfolio
ef.max_sharpe()
ret_tangent, std_tangent, _ = ef.portfolio_performance()
ax.scatter(std_tangent, ret_tangent, marker="*", s=100, c="r", label="Max Sharpe")

# Plot random portfolios
ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis_r")

# Format
ax.set_title("PyPortfolioOpt: Efficient Frontier with random portfolios")
ax.legend()
plt.tight_layout()
plt.savefig("monteCarloEfficientFrontier.png")
plt.show()



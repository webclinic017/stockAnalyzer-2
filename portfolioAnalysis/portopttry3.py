import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pypfopt
from pypfopt import risk_models
from pypfopt import plotting
from pypfopt import expected_returns
from pypfopt import EfficientFrontier

tickers = ["MSFT", "AMZN", "KO", "MA", "COST",
           "LUV", "XOM", "PFE", "JPM", "UNH",
           "ACN", "DIS", "GILD", "F", "TSLA", "AAP", "MARA"]

def optimize(tickers):
    #Retreive historical price data
    ohlc = yf.download(tickers, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices.tail())


    #Plot Historical Prices
    # prices[prices.index >= "2008-01-01"].plot(figsize=(15,10));
    # plt.show()

    #Calculating Covariance Matrix, using Ledoit-Wolf shrinkage, which reduces the extreme values in the covariance matrix
    sample_cov = risk_models.sample_cov(prices, frequency=252)
    print(sample_cov)

    # Heat Map of Cov Matrix
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()
    plotting.plot_covariance(S, plot_correlation=True);
    plt.show()
    plt.savefig("covMatrix.png")



    # Calculating mu (eRi) for the tickers using capm returns, not historical mean returns
    mu = expected_returns.capm_return(prices)
    print(mu)

    mu.plot.barh(figsize=(10,6));
    plt.show()
    plt.savefig("expReturns.png")



    #Calculating Long only Minimum Variance Portfolio (GMVP)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # Weights between 0 nad 1 Since we don't allow shorting
    ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))
    ef.min_volatility()
    weights_min_volatility_long_only = ef.clean_weights()
    print(weights_min_volatility_long_only)

    pd.Series(weights_min_volatility_long_only).plot.barh();
    plt.show()
    plt.savefig("longOnlyGMVP.png")



    #Calculating Long/Short Minimum Variance (GMVP)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # You don't have to provide expected returns in this case
    ef = EfficientFrontier(None, S, weight_bounds=(None, None))
    ef.min_volatility()
    weights_min_volatility_long_short = ef.clean_weights()
    print(weights_min_volatility_long_short)

    pd.Series(weights_min_volatility_long_short).plot.barh();
    plt.show()
    plt.savefig("longShortGMVP.png")




    # Calculating Long only Tangency Portfolio (Max Sharpe)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # Weights between 0 nad 1 Since we don't allow shorting
    ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))
    ef.max_sharpe()
    weights_max_sharpe_long_only = ef.clean_weights()
    print(weights_max_sharpe_long_only)

    pd.Series(weights_max_sharpe_long_only).plot.barh();
    plt.show()
    plt.savefig("longOnlyMaxSharpe.png")




    # Calculating Long/Short Tangency Portfolio (Max Sharpe)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # You don't have to provide expected returns in this case
    ef = EfficientFrontier(mu, S, weight_bounds=(-1, 1))
    ef.max_sharpe()
    weights_max_sharpe_long_short = ef.clean_weights()
    print(weights_max_sharpe_long_short)

    pd.Series(weights_max_sharpe_long_short).plot.barh();
    plt.show()
    plt.savefig("longShortMaxSharpe.png")


optimize(tickers)
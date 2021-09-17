from numpy.core.shape_base import block
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pypfopt
from pypfopt import risk_models
from pypfopt import plotting
from pypfopt import expected_returns
from pypfopt import EfficientFrontier

# tickers = ["MSFT", "AMZN", "KO", "MA", "COST",
#            "LUV", "XOM", "PFE", "JPM", "UNH",
#            "ACN", "DIS", "GILD", "F", "TSLA", "AAP", "MARA", "ETH-USD"]


def calculateCovMatrix(tickers):
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
    try:
        S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()
    except ZeroDivisionError:
        pass
    plotting.plot_covariance(S, plot_correlation=True);
    plt.show(block=False)
    plt.savefig("static/app1/assets/img/covMatrix.png")
    #plt.close()


def calculateExpReturnsForTickers(tickers):
    #Retreive historical price data
    ohlc = yf.download(tickers, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices.tail())

    # Calculating mu (eRi) for the tickers using capm returns, not historical mean returns
    mu = expected_returns.capm_return(prices)
    print(mu)

    mu.plot.barh(figsize=(10,6));
    plt.xlabel('Expected Return for Selected Symbols')
    plt.show(block=False)
    plt.savefig("static/app1/assets/img/expReturns.png")
    #plt.close()


def calculateOptWeightsForLongOnlyGMVP(tickers, saveAs):
    #Retreive historical price data
    ohlc = yf.download(tickers, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices.tail())

    mu = expected_returns.capm_return(prices)

     #Calculating Long only Minimum Variance Portfolio (GMVP)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # Weights between 0 nad 1 Since we don't allow shorting
    ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))
    ef.min_volatility()
    weights_min_volatility_long_only = ef.clean_weights()
    print(weights_min_volatility_long_only)

    pd.Series(weights_min_volatility_long_only).plot.barh();
    plt.xlabel('Optimal Weights for Long-Only GMVP')
    plt.show(block=False)
    plt.savefig("twgPortPlots/longOnlyGMVP" + saveAs + ".png")
    #plt.close()


def calculateOptWeightsForLongShortGMVP(tickers, saveAs):
    #Retreive historical price data
    ohlc = yf.download(tickers, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices.tail())

    #Calculating Long/Short Minimum Variance (GMVP)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # You don't have to provide expected returns in this case
    ef = EfficientFrontier(None, S, weight_bounds=(None, None))
    ef.min_volatility()
    weights_min_volatility_long_short = ef.clean_weights()
    print(weights_min_volatility_long_short)

    pd.Series(weights_min_volatility_long_short).plot.barh();
    plt.xlabel('Optimal Weights for Long/Short GMVP')
    #plt.show()
    plt.savefig("twgPortPlots/longShortGMVP" + saveAs + ".png")
    #plt.close()


def calculateOptWeightsForLongOnlyTangencyPortfolio(tickers, saveAs):
    #Retreive historical price data
    ohlc = yf.download(tickers, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices.tail())

    mu = expected_returns.capm_return(prices)
    # Calculating Long only Tangency Portfolio (Max Sharpe)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # Weights between 0 nad 1 Since we don't allow shorting
    ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))
    ef.max_sharpe()
    weights_max_sharpe_long_only = ef.clean_weights()
    print(weights_max_sharpe_long_only)

    pd.Series(weights_max_sharpe_long_only).plot.barh();
    plt.xlabel('Optimal Weights for Long-Only Tangency Portfolio')
    #plt.show()
    plt.savefig("twgPortPlots/longOnlyMaxSharpe" + saveAs + ".png")
    #plt.close()


def calculateOptWeightsForLongShortTangencyPortffolio(tickers, saveAs):
    #Retreive historical price data
    ohlc = yf.download(tickers, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices.tail())

    mu = expected_returns.capm_return(prices)
    # Calculating Long/Short Tangency Portfolio (Max Sharpe)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # You don't have to provide expected returns in this case
    ef = EfficientFrontier(mu, S, weight_bounds=(-1, 1))
    ef.max_sharpe()
    weights_max_sharpe_long_short = ef.clean_weights()
    print(weights_max_sharpe_long_short)

    pd.Series(weights_max_sharpe_long_short).plot.barh();
    plt.xlabel('Optimal Weights for Long/Short Tangency Portfolio')
    plt.savefig("twgPortPlots/longShortMaxSharpe" + saveAs + ".png")
    #plt.show(block=False)
    #plt.close()


def monteCarloEfficientFrontier(tickers, saveAs):
    #Retreive historical price data
    ohlc = yf.download(tickers, period="max")
    prices = ohlc["Adj Close"].dropna(how="all")
    print(prices.tail())

    mu = expected_returns.capm_return(prices)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()
    # Monte Carlo Efficient Frontier
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
    ax.axvline(x=std_tangent, ymin=0,ymax=ret_tangent)
    ax.axhline(y=ret_tangent, xmin=0,xmax=std_tangent)

    # Plot random portfolios
    ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis_r")

    # Format
    ax.set_title("Efficient Frontier with MonteCarlo Simulation")
    ax.legend()
    plt.tight_layout()
    plt.savefig("twgPortPlots/monteCarloEfficientFrontier" + saveAs + ".png")
    #plt.show(block=False)
    #plt.close()

    std_tangent = "{:,.2f}".format(std_tangent)
    ret_tangent = "{:,.2f}".format(ret_tangent)

    return std_tangent, ret_tangent

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
    try:
        S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()
    except ZeroDivisionError:
        pass
    plotting.plot_covariance(S, plot_correlation=True);
    plt.show(block=False)
    plt.savefig("static/app1/assets/img/covMatrix.png")



    # Calculating mu (eRi) for the tickers using capm returns, not historical mean returns
    mu = expected_returns.capm_return(prices)
    print(mu)

    mu.plot.barh(figsize=(10,6));
    plt.xlabel('Expected Return for Selected Symbols')
    plt.show(block=False)
    plt.savefig("static/app1/assets/img/expReturns.png")



    #Calculating Long only Minimum Variance Portfolio (GMVP)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # Weights between 0 nad 1 Since we don't allow shorting
    ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))
    ef.min_volatility()
    weights_min_volatility_long_only = ef.clean_weights()
    print(weights_min_volatility_long_only)

    pd.Series(weights_min_volatility_long_only).plot.barh();
    plt.xlabel('Optimal Weights for Long-Only GMVP')
    plt.show(block=False)
    plt.savefig("static/app1/assets/img/longOnlyGMVP.png")



    #Calculating Long/Short Minimum Variance (GMVP)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # You don't have to provide expected returns in this case
    ef = EfficientFrontier(None, S, weight_bounds=(None, None))
    ef.min_volatility()
    weights_min_volatility_long_short = ef.clean_weights()
    print(weights_min_volatility_long_short)

    pd.Series(weights_min_volatility_long_short).plot.barh();
    plt.xlabel('Optimal Weights for Long/Short GMVP')
    #plt.show()
    plt.savefig("static/app1/assets/img/longShortGMVP.png")




    # Calculating Long only Tangency Portfolio (Max Sharpe)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # Weights between 0 nad 1 Since we don't allow shorting
    ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))
    ef.max_sharpe()
    weights_max_sharpe_long_only = ef.clean_weights()
    print(weights_max_sharpe_long_only)

    pd.Series(weights_max_sharpe_long_only).plot.barh();
    plt.xlabel('Optimal Weights for Long-Only Tangency Portfolio')
    #plt.show()
    plt.savefig("static/app1/assets/img/longOnlyMaxSharpe.png")




    # Calculating Long/Short Tangency Portfolio (Max Sharpe)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    # You don't have to provide expected returns in this case
    ef = EfficientFrontier(mu, S, weight_bounds=(-1, 1))
    ef.max_sharpe()
    weights_max_sharpe_long_short = ef.clean_weights()
    print(weights_max_sharpe_long_short)

    pd.Series(weights_max_sharpe_long_short).plot.barh();
    plt.xlabel('Optimal Weights for Long/Short Tangency Portfolio')
    plt.show(block=False)
    plt.savefig("static/app1/assets/img/longShortMaxSharpe.png")



    # Monte Carlo Efficient Frontier
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
    ax.set_title("Efficient Frontier with MonteCarlo Simulation")
    ax.legend()
    plt.tight_layout()
    plt.savefig("static/app1/assets/img/monteCarloEfficientFrontier.png")
    plt.show(block=False)


#optimize(tickers)
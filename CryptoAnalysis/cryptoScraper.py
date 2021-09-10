from selenium import webdriver
import numpy as np





def scrape_coinbase(ticker):
    coinbaseURL = 'https://www.coinbase.com/price/' + ticker + ''
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(coinbaseURL)
    return 1

def scrape_coinstats(ticker):
    coinstatsURL = 'https://coinstats.app/coins/' + ticker + '/'
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(coinstatsURL)
    return 1

def scrape_coinmarketcap(ticker):
    coinmarketcapURL = 'https://coinmarketcap.com/currencies/' + ticker + '/'
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(coinmarketcapURL)
    return 1

def scrape_coingecko(ticker):
    coingeckoURL = 'https://www.coingecko.com/en/coins/' + ticker + ''
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(coingeckoURL)
    return 1



def scrape_crypto_metrics(cryptoName):
    coinbaseURL = 'https://www.coinbase.com/price/' + cryptoName + ''
    coinstatsURL = 'https://coinstats.app/coins/' + cryptoName + '/'
    coinmarketcapURL = 'https://coinmarketcap.com/currencies/' + cryptoName + '/'
    coingeckoURL = 'https://www.coingecko.com/en/coins/' + cryptoName + ''
    messariURL = 'https://messari.io/asset/' + cryptoName + '/metrics/all'

    driver = webdriver.Chrome('chromedriver.exe')

    # driver.get(coinbaseURL)
    # driver.get(coinstatsURL)
    # driver.get(coingeckoURL)
    driver.get(coinmarketcapURL)

    marketCap = driver.find_element_by_css_selector('div.statsBlock:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
    circulatingSupply = driver.find_element_by_css_selector('.hWTiuI > div:nth-child(2)')
    maxSupply = driver.find_element_by_css_selector('.dwCYJB > div:nth-child(2)')
    fullyDilutedValuation = driver.find_element_by_css_selector('div.statsBlock:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
    volumePast24hr = driver.find_element_by_css_selector('div.statsBlock:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
    marketCapRank = driver.find_element_by_css_selector('.nds9rn-0 > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(2)')
    marketCapDominace = driver.find_element_by_css_selector('.nds9rn-0 > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2) > span:nth-child(1)')

    try:
        tvl = driver.find_element_by_css_selector('div.statsBlock:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
        tvl = tvl.text

        tvlNoFormat = volumePast24hr.replace('$', '')
        tvlNoFormat = tvlNoFormat.replace(',', '')
        print('TVL =' + tvl)
    except Exception:
        tvl = np.nan
        tvlNoFormat = np.nan

    try:
        MktCapToTVL = driver.find_element_by_css_selector('div.statsBlock:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
        MktCapToTVL = MktCapToTVL.text
        print('MktCap To TVL =' + MktCapToTVL)
    except Exception:
        pass

    # ath = driver.find_element_by_css_selector('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.jKrmxw.container > div > div.sc-16r8icm-0.sc-19zk94m-1.gRSJaB > div.sc-16r8icm-0.iutcov > div.sc-16r8icm-0.hgKnTV > div > div.sc-16r8icm-0.kjciSH.show > div:nth-child(2) > table > tbody > tr:nth-child(5) > td > span')
    # ttmHigh = driver.find_element_by_css_selector('.show > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2) > div:nth-child(2)')
    # ttmLow = driver.find_element_by_css_selector('.show > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1)')
    # hrReturn = driver.find_element_by_css_selector('')
    # dayReturn = driver.find_element_by_css_selector('')
    # sevenDayReturn = driver.find_element_by_css_selector('')
    # thirtyDayReturn = driver.find_element_by_css_selector('')
    # ttmReturn = driver.find_element_by_css_selector('')

    #ema10 = driver.find_element_by_css_selector('div.container-2-juHm8n:nth-child(2) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)')


    #ema10 = ema10.text
    marketCap = marketCap.text
    maxSupply = maxSupply.text
    fullyDilutedValuation = fullyDilutedValuation.text
    circulatingSupply = circulatingSupply.text
    volumePast24hr = volumePast24hr.text
    marketCapRank = marketCapRank.text
    marketCapDominace = marketCapDominace.text

    volNoFormat = volumePast24hr.replace('$', '')
    volNoFormat = volNoFormat.replace(',', '')

    mcNoFormat = marketCap.replace('$', '')
    mcNoFormat = mcNoFormat.replace(',', '')

    fdvNoFormat = fullyDilutedValuation.replace('$', '')
    fdvNoFormat = fdvNoFormat.replace(',', '')

    volumePast24hrToMC = (int(volNoFormat) / int(mcNoFormat))
    print('mcNoform' + (mcNoFormat))
    print('vol Nofomat' + volNoFormat)


    try:
        fdvTOtvl = (int(fdvNoFormat) / int(tvlNoFormat))
        print('fdvTOtvl=' + fdvTOtvl)
    except Exception:
        fdvTOtvl = np.nan

    try:
        mcToTvl = (int(mcNoFormat) / int(tvlNoFormat))
        print('fdvTOtvl=' + fdvTOtvl)
    except Exception:
        mcToTvl = np.nan
    # ath = ath.text
    # ttmHigh = ttmHigh.text
    # ttmLow = ttmLow.text

    print('Market-Cap = ' + marketCap)
    print('Max Supply =' + maxSupply)
    print('Fully Dilluted Value =' + fullyDilutedValuation)
    print('Circulating Supply =' + circulatingSupply)
    print('Past 24Hr Volume =' + volumePast24hr)
    print('Market Cap Rank =' + marketCapRank)
    print('MarketCap Dominance' + marketCapDominace)
    print('24Hr Volume / Mkt Cap=' + str(volumePast24hrToMC))

    print('mcNoform' + (mcNoFormat))
    print('vol Nofomat' + volNoFormat)

    # print('All Time High =' + ath)
    # print('52 week high' + ttmHigh)
    # print('52 week low'+ ttmLow)


    driver.close()
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(messariURL)

    #inflationRate = driver.find_element_by_css_selector('#root > div > div.MuiContainer-root.jss167.MuiContainer-maxWidthXl > div > div.MuiBox-root.jss330 > div.MuiBox-root.jss404 > div.MuiGrid-root.MuiGrid-container > div:nth-child(2) > div.jss337 > div.jss343.jss437.undefined > div > div.MuiBox-root.jss438.jss346 > p:nth-child(2)')
    #inflationRate = inflationRate.text
    #print(inflationRate)

    # try:
    #     inflationRate = driver.find_element_by_css_selector('#root > div > div.MuiContainer-root.jss167.MuiContainer-maxWidthXl > div > div.MuiBox-root.jss330 > div.MuiBox-root.jss404 > div.MuiGrid-root.MuiGrid-container > div:nth-child(2) > div.jss337 > div.jss343.jss437.undefined > div > div.MuiBox-root.jss438.jss346 > p:nth-child(2)')
    #     inflationRate = inflationRate.text
    #     print(inflationRate)
    # except Exception:
    #     pass




    driver.close()
scrape_crypto_metrics('bitcoin')
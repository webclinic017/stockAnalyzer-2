from selenium import webdriver






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
        print('TVL =' + tvl)
    except Exception:
        pass

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
    # print('All Time High =' + ath)
    # print('52 week high' + ttmHigh)
    # print('52 week low'+ ttmLow)


    driver.close()
    driver.get(messariURL)

scrape_crypto_metrics('aave')
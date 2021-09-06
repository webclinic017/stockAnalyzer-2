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



def scrape_crypto_metrics(ticker):
    coinbaseURL = 'https://www.coinbase.com/price/' + ticker + ''
    coinstatsURL = 'https://coinstats.app/coins/' + ticker + '/'
    coinmarketcapURL = 'https://coinmarketcap.com/currencies/' + ticker + '/'
    coingeckoURL = 'https://www.coingecko.com/en/coins/' + ticker + ''

    driver = webdriver.Chrome('chromedriver.exe')

    driver.get(coinbaseURL)
    driver.get(coinstatsURL)
    driver.get(coinmarketcapURL)
    driver.get(coingeckoURL)

    ema10 = driver.find_element_by_css_selector('div.container-2-juHm8n:nth-child(2) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)')

    ema10 = ema10.text

scrape_crypto_metrics('BTCUSDT')
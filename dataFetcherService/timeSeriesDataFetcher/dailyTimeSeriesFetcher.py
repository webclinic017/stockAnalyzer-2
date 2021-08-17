from alphavantageapikey import alpha_vantagi_api_key
import requests



def get_daily_candles(ticker):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&apikey=' + alpha_vantagi_api_key
    r = requests.get(url)
    data = r.json()

    print(data)

get_daily_candles('AAPL')
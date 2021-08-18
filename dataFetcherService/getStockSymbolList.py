import finnhub
from finnhubAPIkey import FINNHUB_API_KEY
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)


finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
get_list_of_tickers = finnhub_client.stock_symbols('US')
tickers = get_list_of_tickers
list_tickers_dicts = list(tickers)
list_tickers = list_tickers_dicts[5]
print(tickers)

ticker_list = []
for i in list_tickers_dicts:
    ticker_list.append(str(i['symbol']))
    print(i)

print('------------------------------')
print(ticker_list)
print(len(ticker_list))

# for ele in ticker_list:
#     if len(ele) >= 5:
#         ticker_list.remove(ele)
#     elif len(ele) >=4 and ele[:-1] == 'F':
#         ticker_list.remove(ele)
#     else:
#         pass

print('------------------------------')
print(ticker_list)
print(len(ticker_list))



import requests
import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

#Coins Section

#List All Supported Coins
def listAllCoins():
    data = cg.get_coins_list()
    print(data)
    return data

#List All Supported Coins Mkt Cap, volume, and market data
def listCoinsWithDetails():
    data = cg.get_coins_markets()
    print(data)
    return data

#/coins/{id} (Get current data (name, price, market, ... including exchange tickers) for a coin)
def getDataForCoin(id):
    data = cg.get_coin_by_id(id)
    print(data)
    return data

#/coins/{id}/tickers (Get coin tickers (paginated to 100 items))
def getCryptoTickers(id):
    data = cg.get_coin_ticker_by_id(id)
    print(data)
    return data


#/coins/{id}/history (Get historical data (name, price, market, stats) at a given date for a coin)
def getCoinHistoryByID(id):
    data = cg.get_coin_history_by_id(id)
    print(data)
    return data


#/coins/{id}/market_chart (Get historical market data include price, market cap, and 24h volume (granularity auto))
def getMktChart(id):
    data = cg.get_coin_market_chart_by_id(id)
    print(data)
    return data

#/coins/{id}/market_chart/range (Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto))
def getRangedMktChart(id, fromTS, toTS):
    data = cg.get_coin_market_chart_range_by_id(id, fromTS, toTS)
    print(data)
    return data

#/coins/{id}/status_updates (Get status updates for a given coin (beta))
def getStatusUpdateForOneCoin(id):
    data = cg.get_coin_status_updates_by_id(id)
    print(data)
    return data

#/coins/{id}/ohlc (Get coin's OHLC (beta))
def getCoinOHLC(id):
    data = cg.get_coin_ohlc_by_id(id)
    print(data)
    return data



#CONTRACTS DATA

#/coins/{id}/contract/{contract_address} (Get coin info from contract address)
def getCoinInfoFromContactAddresses(id):
    data = cg.get_coin_info_from_contract_address_by_id(id)
    print(data)
    return data

#/coins/{id}/contract/{contract_address}/market_chart/ (Get historical market data include price, market cap, and 24h volume (granularity auto) from a contract address)
def getHistDataFromContractAddress(id):
    data = cg.get_coin_market_chart_from_contract_address_by_id(id)
    print(data)
    return data

#/coins/{id}/contract/{contract_address}/market_chart/range (Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto) from a contract address)
def getHistDataFromContractAddressInRange(id, contractAddress, fromTS, toTS):
    data = cg.get_coin_market_chart_range_from_contract_address_by_id(id, contractAddress, fromTS, toTS)
    print(data)
    return data



#ASSET PLATFORMS
#/asset_platforms (List all asset platforms (Blockchain networks))
def getCryptoAssetPlatforms():
    data = cg.get_asset_platforms()
    print(data)
    return data


#GET CRYPTO CATEGORIES
#/coins/categories/list (List all categories)
def getCryptoCategories():
    data = cg.get_coins_categories_list()
    print(data)
    return data

#/coins/categories/list (List all categories)
def getCryptoCategoriesWithMarketData():
    data = cg.get_coins_categories()
    print(data)
    return data


#EXCHANGES
#/exchanges (List all exchanges)
def getExchangeList():
    data = cg.get_exchanges_list()
    print(data)
    return data

#/exchanges/list (List all supported markets id and name (no pagination required))
def getExchangesIDNameList():
    data = cg.get_exchanges_id_name_list()
    print(data)
    return data

#/exchanges/{id} (Get exchange volume in BTC and top 100 tickers only)
def getExchangeVolumeByID(id):
    data = cg.get_exchanges_by_id(id)
    print(data)
    return data

#/exchanges/{id}/tickers (Get exchange tickers (paginated, 100 tickers per page))
def getExchangeTickersByID(id):
    data = cg.get_exchanges_tickers_by_id(id)
    print(data)
    return data

#/exchanges/{id}/status_updates (Get status updates for a given exchange (beta))
def getExchangeStatusUpdatesByID(id):
    data = cg.get_exchanges_status_updates_by_id(id)
    print(data)
    return data

#/exchanges/{id}/volume_chart (Get volume_chart data for a given exchange (beta))
def getExchangeVolumeChartByID(id):
    data = cg.get_exchanges_volume_chart_by_id(id)
    print(data)
    return data


#FINANCE PLATFORMS
#/finance_platforms (List all finance platforms)
def listAllFinancePlatforms():
    data = cg.get_finance_platforms()
    print(data)
    return data

#/finance_products (List all finance products)
def listAllFinancialProducts():
    data = cg.get_finance_products()
    print(data)
    return data


#INDEXES
#/indexes (List all market indexes)
def listAllCryptoMarketIndexes():
    data = cg.get_indexes()
    print(data)
    return data

#/indexes/{market_id}/{id} (Get market index by market id and index id)
def getIndexByMarketIDAndIndexID(marketID, id):
    data = cg.get_indexes_by_market_id_and_index_id(marketID, id)
    print(data)
    return data

#/indexes/list (List market indexes id and name)
def ListMarketIndexesIDandNames():
    data = cg.get_indexes_list()
    print(data)
    return data


#DERIVATIVES

#/derivatives (List all derivative tickers)
def getCryptoDerivatives():
    data = cg.get_derivatives()
    print(data)
    return data

#/derivatives/exchanges (List all derivative exchanges)
def listAllCryptoDerivativeExchanges():
    data = cg.get_derivatives_exchanges()
    print(data)
    return data

#/derivatives/exchanges/{id} (Show derivative exchange data)
def getCryptoDerivativeExchangeDataByID(id):
    data = cg.get_derivatives_exchanges_by_id(id)
    print(data)
    return data

#/derivatives/exchanges/list (List all derivative exchanges name and identifier)
def listAllCryptoDerivativeExchangesNameAndID(id):
    data = cg.get_derivatives_exchanges_list()
    print(data)
    return data


#Status Updates
#/status_updates (List all status_updates with data (description, category, created_at, user, user_title and pin))
def getStatusUpdates():
    data = cg.get_status_updates()
    print(data)
    return data



#EVENTS
#/events (Get events, paginated by 100)
def getCryptoEvents():
    data = cg.get_events()
    print(data)
    return data

#/events/countries (Get list of event countries)
def listEventCountries():
    data = cg.get_events_countries()
    print(data)
    return data

#/events/types (Get list of events types)
def getCryptoEventTypes():
    data = cg.get_events_types()
    print(data)
    return data


#EXCHANGE RATES
#/exchange_rates (Get BTC-to-Currency exchange rates)
def getExchangeRates():
    data = cg.get_exchange_rates()
    print(data)
    return data


#TRENDING
#/exchange_rates (Get BTC-to-Currency exchange rates)
def listCryptoTrending():
    data = cg.get_search_trending()
    print(data)
    return data



#GLOBAL
#/global (Get cryptocurrency global data)
def getCryptoGlobalData():
    data = cg.get_global()
    print(data)
    return data

#/global/decentralized_finance_defi (Get cryptocurrency global decentralized finance(defi) data)
def getDefiGlobalData():
    data = cg.get_global_decentralized_finance_defi()
    print(data)
    return data


#Companies
#/companies/public_treasury/{coin_id} (Get public companies data)
def getCryptoCompanyData(coinID):
    data = cg.get_global(coinID)
    print(data)
    return data


print('----------------------')
getCryptoCategories()
print('----------------------')
listAllFinancePlatforms()
print('----------------------')
listAllCryptoMarketIndexes()
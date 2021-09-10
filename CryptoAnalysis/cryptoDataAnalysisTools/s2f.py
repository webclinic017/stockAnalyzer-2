import blockcypher
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
from datetime import date


#Define Total Circulating Bitcoin
import requests

df = pd.read_csv('total-bitcoins', index_col='Timestamp', thousands=',', parse_dates=True)
# dfForPiDate = pd.read_csv('btcPriceHistory1.csv', thousands=',', parse_dates=True)

print(df)

#Define Flow/Production Schedule



begin_date = '2009-01-03'
genesis = date(2009,1,3)
now = date.today()
units = (now - genesis)
print(units.days)
blocksPerDay = (24*6)
dfNew = pd.DataFrame({'Dates': pd.date_range(begin_date, units.days)})
dfNew['Days_Since_Genisis'] = range(units.days)
dfNew['Dates'] = pd.date_range(genesis, periods=units.days)


print(df)
print(dfNew)


dfNew['Block'] = (dfNew['Days_Since_Genisis'] * (6*24))
dfNew['Block_Per_Day'] = 144
print(dfNew)

dfNew['Reward_Per_Block'] = (dfNew['Days_Since_Genisis'] * (1.00) )


for i in range(len(dfNew)):
    if dfNew['Block'][i] < 210000:
        dfNew['Reward_Per_Block'][i] = 50.0
    elif dfNew['Block'][i] > 210000 and dfNew['Block'][i] < 420000:
        dfNew['Reward_Per_Block'][i] = 25.0
    elif dfNew['Block'][i] > 420000 and dfNew['Block'][i] < 630000:
        dfNew['Reward_Per_Block'][i] = 12.5
    elif dfNew['Block'][i] > 630000 and dfNew['Block'][i] < 840000:
        dfNew['Reward_Per_Block'][i] = 6.25
    else:
        pass
dfNew['BTC_Produced_Per_Day'] = (dfNew['Block_Per_Day'] * dfNew['Reward_Per_Block'])
dfNew['CirculatingBTC'] = (dfNew['BTC_Produced_Per_Day'].cumsum())

pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", 10)

blockHeight = blockcypher.get_latest_block_height()
print(blockHeight)


print(dfNew)

url = 'https://api.blockset.com/blocks/btc'
r = requests.get(url)
print(r)

figure = go.Figure(
    data=[
        go.Scatter(
            x=df.index,
            y=df['total-bitcoins'],
            stackgroup='one'
        )
    ]
)
figure.show()

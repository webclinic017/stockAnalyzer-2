import pandas as pd
import datetime




data = pd.read_csv('btcmarket-cap.csv')
print(data)


data['mktSum'] = data['market-cap']

beginning = datetime.datetime(2009, 1, 3)
index = pd.date_range(beginning, periods=4638, freq='D')
day = range(len(index))
print(index)
columns = ['day', 'mktCap', 'cumSum', 'mktAvg']


df = pd.DataFrame(index = index, columns=columns)
df['day'] = day

for i in data:
    data['then'] = datetime.datetime.strptime(data.iloc[data.index[i]][0], '%Y-%m-%d').date()


print(df)
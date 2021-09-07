import plotly.graph_objects as go
import pandas as pd

# Create df of Data
df = pd.read_csv('btcPriceHistory1.csv')
df = df.set_index(pd.DatetimeIndex(df['Date'].values))

print(df)

# Create chart

figure = go.Figure(
    data=[
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Price'],

        )
    ]
)

figure.show()

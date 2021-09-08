import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('total-bitcoins', index_col='Timestamp', thousands=',', parse_dates=True)
# dfForPiDate = pd.read_csv('btcPriceHistory1.csv', thousands=',', parse_dates=True)

print(df)

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

import pandas as pd
import yfinance as yf
import datetime 
from datetime import date, timedelta 
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=720)
d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('AAPL',
                    start=start_date,
                    end=end_date,
                    progress=False)
print(data.head())

import plotly.express as px
figure = px.line(data, x = data.index,
                 y = "Close",
                 title = "Time Series Analysis (Line Plot)")
figure.show()

#candlestick graph 

import plotly.graph_objects as go
figure = go.Figure(data=[go.Candlestick(x = data.index,
                                        open = data["Open"],
                                        high = data["High"],
                                        low = data["Low"],
                                        close = data["Close"])])
figure.update_layout(title = "Time Series Analysis (Candlestick Chart)",
                     xaxis_rangeslider_visible = False)
figure.show()

#a bar chart

figure = px.bar(data, x = data.index,
                y = "Close",
                title = "Time Series Analysis (Bar Chart)")
figure.show()

#line graph between two periods 

figure = px.line(data, x = data.index, 
                 y = 'Close',
                 range_x = ['2021-07-01', '2021-12-31'],
                 title = "Time Series  Analysis (Custom Date Range)")
figure.show()
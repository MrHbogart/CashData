import pandas as pd
import datetime

#importing data downloaded from ducascopy.com
data = pd.read_csv("EURUSD_Candlestick_15_M_BID_05.07.2021-10.07.2021.csv")

#converting date format to python timedate format
date = []
for i in data['Gmt time']:
    date.append(datetime.datetime.strptime(i, '%d.%m.%Y %H:%M:%S.%f'))

data['date'] = date

data.drop(['Gmt time'], axis=1, inplace = True)

# print(data.head())

#importing main and creating an instance from CashData class
from main import CashData

cd = CashData({'date':data['date'], 'open':data['Open'], 'high':data['High'],
               'low':data['Low'], 'close':data['Close'], 'volume':data['Volume']}, 5).CashData()

# print(cd)

#here we want to plot data to check if it works correctly

import plotly.graph_objects as go

#plotting OHLC data
fig = go.Figure(data=go.Ohlc(x=data['date'],
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close']))

#adding neowave cash data to OHLC chart to compare
fig.add_trace(go.Scatter(
    mode="markers+lines", x=cd["date"], y=cd["price"]
))
fig.show()
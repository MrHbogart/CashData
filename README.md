# CashData
a python package that converts OHLC price data to neowave cash data

it's my first git project, and I want to write a python code that, can be used for technical analysis.

to use this, you have to creat an instance from CashData class in main.py file and for initializing
the instance, arguments are a dictionary, and an integer number 'n'

dictionary's keys are 'date','open','high','low','close','volume' and values are a Pandas' series
of that data.

example is in check.py

n is an integer number that represents how many candles are being checked for deriving top and
the least price, for example if n=4, then 4 candles becomes to price: one top price and one least price


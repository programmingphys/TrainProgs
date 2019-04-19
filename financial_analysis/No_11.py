# coding=utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import os

def fetch_data(path):
	#data = web.DataReader(name, website, start, end)
	data = pd.read_csv(path)
	return data

def cut_data(df, item):
	data = df.copy()
	data = data[['Date', item]]
	return data

class exchange():
	def get_data(self, data):
		#get data from csv files
		self.data = data.copy()
	
	def send_data(self, date, stock):
		#return data of 'stock' before 'date'
		accessible_data = self.data[stock][self.data[stock]['Date'] < date]
		return accessible_data

	def settlement(self, date, stock, behavior, number):
		#calculate profit of one day according to 'behavior' and 'number'
		if (date == self.data[stock]['Date'][0]):
			return 0
		price_before = self.data[stock][self.data[stock]['Date'] < date].iloc[-1][1]
		price_after = self.data[stock][self.data[stock]['Date'] == date].iloc[0][1]
		profit = (price_after - price_before) * behavior * number
		return profit


class client():
	def __init__(self, stock):
		self.profit = []
		self.stock = stock

	def get_data(self, data):
		#get data from exchange
		self.data = data.copy()

	def decision(self):
		#return 'behavior' and 'number'
		#make decision according to the price of last four days
		if (self.data.shape[0] < 4):
			return 0, 0
		else:
			d1 = self.data.iloc[-3][1] - self.data.iloc[-4][1]
			d2 = self.data.iloc[-2][1] - self.data.iloc[-3][1]
			d3 = self.data.iloc[-1][1] - self.data.iloc[-2][1]
			tmp = [d1>0, d2>0, d3>0]
			if (tmp.count(True) == 3):
				return 1, 2
			elif(tmp.count(True) == 2):
				return 1, 1
			else:
				return 0, 0

	def settlement(self, profit):
		self.profit.append(profit)

#read local data files
filepath = './data/'
filelist = os.listdir(filepath)
data = {}
for files in filelist:
	data[files.strip('.csv')] = cut_data(fetch_data(filepath + files), 'Open')

#start simulation
client1 = client(filelist[0].strip('.csv'))
client2 = client(filelist[3].strip('.csv'))
ex1 = exchange()
ex1.get_data(data)
for date in data[client1.stock]['Date']:
	client1.get_data(ex1.send_data(date, client1.stock))
	decision, number = client1.decision()
	profit = ex1.settlement(date, client1.stock, decision, number)
	client1.settlement(profit)
for date in data[client2.stock]['Date']:
	client2.get_data(ex1.send_data(date, client2.stock))
	decision, number = client2.decision()
	profit = ex1.settlement(date, client2.stock, decision, number)
	client2.settlement(profit)
print('profit of', client1.stock, 'is', sum(client1.profit))
print('profit of', client2.stock, 'is', sum(client2.profit))

#plot profit curve
'''
date = data[client1.stock]['Date']
plt.plot(date, client1.profit)
plt.show()
'''

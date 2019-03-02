import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys
from copy import deepcopy


#全局变量，city为城市坐标,distmat为距离矩阵,count为城市数量
city = None
distmat = None
count = None
allseq = []

#----------------------------------------------------------------------------


#直接法求最小值
def find_minumum(map_filename):
		#load map
		load_map(map_filename)
		get_count()
		dist_mat()
		#get all sequence
		l = list(range(count))
		pos = 0
		end = count
		all_seq(l,pos,end)
		#get all length
		alllen = []
		for i in range(len(allseq)):
				alllen.append(road_len(allseq[i]))
		#get minimum sequence & length
		minlen = min(alllen)
		minseq = allseq[alllen.index(min(alllen))]
		#print
		print(minlen,minseq)
		plot_road(minseq)
		return [minlen, minseq]
#生成所有路径
def all_seq(l,pos,end):
		if pos == end:
				b = deepcopy(l)
				allseq.append(b)
		else:
				for i in range(pos,end):
						l[i],l[pos] = l[pos],l[i]
						all_seq(l,pos+1,end)
						l[i],l[pos] = l[pos],l[i]

#计算给定路径的长度
def road_len(l):
		length = 0
		for i in range(len(l)-1):
				length = length + distmat[l[i]][l[i+1]]
		length = length + distmat[l[0]][l[len(l)-1]] 
		return length

						
#----------------------------------------------------------------------------


#爬山法，求极值
def find_loc_min(map_filename):
		#读取地图
		load_map(map_filename)
		get_count()
		dist_mat()
		#产生随机路线
		seq = rand_seq(count)
		n =5000
		a = change_cal(seq,n)
		print(a)
		plot_road(a[0])
		return a

#产生随机路线的函数
def rand_seq(number):
		a = list(range(number))
		np.random.shuffle(a)
		return a 

#随机改变一条路径中的两点位置
def change_pos(seq):
		x = len(seq)
		a = np.random.randint(0,x,(1,2))
		seq[a[0][0]], seq[a[0][1]] = seq[a[0][1]], seq[a[0][0]]
		return seq

#对输入的路径做调整,求极小值
def change_cal(seq,n):
		best_seq = seq
		#print(best_seq)
		best_len = road_len(seq)
		#print(best_len)
		for i in range(n):
				#print(best_seq,id(best_seq))
				change_seq = change_pos(best_seq)
				#print(id(change_seq))
				#print('change_seq:',change_seq)
				change_len = road_len(change_seq)
				#print('change_len:',change_len)
				if change_len < best_len:
						#print(id(best_seq))
						best_seq = change_seq
						best_len = change_len
						#print('best_seq:',best_seq)
						#print('best_len:',best_len)
				else:
						continue
		#print(best_seq)
		return [best_seq,best_len]


#----------------------------------------------------------------------------------


#地图生成，包括位置查询
def gen_map(map_filename,n):
		df = pd.DataFrame(np.random.randint(0,100,(n,2)),columns=list('xy'))
		df.to_csv(map_filename,index_label=False)

#载入地图坐标信息
def load_map(map_filename):
		global city
		city = pd.read_csv(map_filename)[['x','y']]

#获取给定标号城市坐标
def get_pos(n):
		return city.iloc[n]

#获取给定两城市间的距离
def get_dis(i,j):
		pt1 = get_pos(i)
		pt2 = get_pos(j)
		return np.sqrt((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)

#查询城市数量
def get_count(): 
		global count
		count = len(city)

#城市距离矩阵
def dist_mat():
		global distmat
		distmat = np.zeros((len(city),len(city)))
		for i in range(len(city)):
				for j in range(len(city)):
						distmat[i][j] = get_dis(i,j)


#------------------------------------------------------------------------


#绘图
def plot_road(seq):
		x = []
		y = []
		for i in range(len(seq)):
				x.append(city['x'][seq[i]])
				y.append(city['y'][seq[i]])
		x.append(city['x'][seq[0]])
		y.append(city['y'][seq[0]])
		plt.plot(x,y,color='b')
		plt.scatter(x,y,color='r')
		plt.show()
		

#----------------------------------------------------------------------
if sys.argv[1] == 'minimum':
		find_minumum(sys.argv[2])
elif sys.argv[1] == 'local':
		find_loc_min(sys.argv[2])
elif sys.argv[1] == 'map':
		gen_map(sys.argv[2],int(sys.argv[3]))
else:
		print('wrong agrv')

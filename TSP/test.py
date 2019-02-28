import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys

#全局变量，city为城市坐标
city = None
distmat = None



#直接法求最小值
def find_minumum(map_filename):
		global city	
		city = load_map(map_filename)	
		print('min')




#爬山法，求极值
def find_loc_min(map_filename):
		global city	
		city = load_map(map_filename)
		print(city)




#地图生成，包括位置查询
def gen_map(map_filename,n):
		df = pd.DataFrame(np.random.randint(0,100,(n,2)),columns=list('xy'))
		df.to_csv(map_filename,)

#载入地图坐标信息
def load_map(map_filename):
		#return pd.read_csv(map_filename)
		return pd.read_csv(map_filename)[['x','y']]

#获取给定标号城市坐标
def get_pos(n):
		return city.iloc[n]

#获取给定两城市间的距离
def get_dis(i,j):
		pt1 = get_pos(i)
		pt2 = get_pos(j)
		return np.sqrt((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)

#查询城市数量
def get_count(city_name):  #忘记了len（）中应该是city_name还是city
		return len(city)

#城市距离矩阵
def dist_mat(city_name):
		global distmat
		distmat = np.zeros((len(city),len(city)))
		for i in range(len(city)):
				for j in range(len(city)):
						distmat[i][j] = get_dis(i,j)
		

if sys.argv[1] == 'minimum':
		find_minumum(sys.argv[2])
elif sys.argv[1] == 'local':
		find_loc_min(sys.argv[2])
elif sys.argv[1] == 'map':
		gen_map(sys.argv[2],int(sys.argv[3]))
else:
		print('wrong agrv')
print(city)

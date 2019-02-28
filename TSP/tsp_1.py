import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from itertools import permutations
def get_city(city_num):
    '''
    随机产生城市city
    '''
   # city = np.random.randint(-10,10,size=(5,2))
  #  print(city)
    city = [[ -9 , -7] ,[ -2 ,  8],[-10 , -5],[  5 ,  9],[ -2 , -7]]
    df = pd.DataFrame(city,columns = ['x','y'])
    return df 

def calculate_distance(df):
    '''
    计算距离
    '''
    dist = 0
    df =df.copy() 
    df.loc[len(df)] = [df.iloc[0,0],df.iloc[0,1]]
    for i in range(len(df)-1):
        two_dist = np.sum((df.loc[i+1]-df.loc[i])**2)
        dist += np.sqrt(two_dist)
    return dist

def give_pass(df):
    '''
    爬山法计算路径
    '''
    df_path0= df.sample(frac=1).reset_index(drop=True)
    path0_length = calculate_distance(df_path0)
    #import pdb
   # pdb.set_trace()
    for i in range(1000):
        df_r = random_swap(df_path0)
        path1_length = calculate_distance(df_r)
        if path1_length < path0_length:
            df = df_r
        else:
            df = df
    return df 

city_xy = get_city(5)
give_pass(city_xy)

        
 #   l = permutations(df.values)
 #   distance = []
 #   for i in l: 
 #       df = pd.DataFrame(list(i),columns=['x','y'])
 #       dist = calculate_distance(df)
 #       distance.append(dist)
 #   return np.min(distance)
    
def random_swap(df):
    '''
    随机交换两个城市，添加扰动
    '''
    x = np.random.randint(df.index.min(),df.index.max())
    y = np.random.randint(df.index.min(),df.index.max())
    city_list = list(df.values)
    a = city_list[x]
    city_list[x] = city_list[y]
    city_list[y] = a 
    df = pd.DataFrame(city_list,columns=['x','y'])
    return df 

    

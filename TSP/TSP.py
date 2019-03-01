# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:34:45 2019

@author: 皇子皇孙
"""
import numpy as np
import matplotlib.pyplot as plt
import itertools
import random
import csv
   
def path_dis(data): #得到旅行路径的长度
    x=data[:,0]
    y=data[:,1]
    distance=0
    for i in range(len(x)):
        if i<len(x)-1:
            x_dis=abs(x[i+1]-x[i])
            y_dis=abs(y[i+1]-y[i])
            distance+=np.sqrt(x_dis**2+y_dis**2)
        else:
            x_dis=abs(x[0]-x[i])
            y_dis=abs(y[0]-y[i])
            distance+=np.sqrt(x_dis**2+y_dis**2)
    return distance

def select_path(data):  #遍历所有的路径求解
    path_min=np.zeros_like(data)
    distance=0
    data1=np.delete(data,0,0)
    path=np.array(list(itertools.permutations(data1,len(data1))))
    path_m=np.zeros((len(path),len(data),2))
    for i in range(len(path)):
        path_m[i]=np.vstack((data[0],path[i]))
        if i==0:
            distance=path_dis(path_m[0])
            path_min=path_m[0]
        else:
            if distance>=path_dis(path_m[i]):
                distance=path_dis(path_m[i])
                path_min=path_m[i]
    return path_min,distance

def climb_path(data):  #爬山法
    path_min=data=np.array(random.sample(list(data),len(data)))
    sw=np.zeros((1,2))
    for j in range(100):
        sw=np.zeros((1,2))
        for i in range(500):
            a,b=sw1=np.random.randint(len(data),size=2)
            if sw1 not in sw:
                data[[a,b],:]=data[[b,a],:]
                if path_dis(path_min)>path_dis(data):
                    path_min=data
                    break
                else:
                    data[[a,b],:]=data[[b,a],:]
            sw=np.vstack((sw,sw1))
    distance=path_dis(path_min)
    return path_min,distance

def drawing(m):  # 数据转化为适合作图的形式
    data=m
    x=data[:,0]
    y=data[:,1]
    for i in range(len(x)):
        if i==0:
            xx=np.array([x[i],x[i+1]])
            yy=np.array([y[i],y[i+1]])
        elif i<len(x)-1:
            x1=np.array([x[i],x[i+1]])
            xx=np.vstack((xx,x1))
            y1=np.array([y[i],y[i+1]])
            yy=np.vstack((yy,y1))
        else:
            x1=np.array([x[i],x[0]])
            xx=np.vstack((xx,x1))
            y1=np.array([y[i],y[0]])
            yy=np.vstack((yy,y1))
    return x,y,xx,yy



data=[]
with open("TSP.csv", "r") as csvfile:
    readcsv = csv.reader(csvfile) 
    for item in readcsv:
        data.append([int(item[0]),int(item[1])])
path,dis=select_path(data)
print('遍历法','最短路径的城市顺序为:', path,'路径长度为：',dis,sep='\n')
x,y,xd,yd=drawing(path)
n=np.arange(len(xd))
fig,ax=plt.subplots()
for i in range(len(xd)):
    ax.plot(xd[i],yd[i],color='r')
    ax.scatter(xd[i],yd[i],color='b')
for i,txt in enumerate(n):
    ax.annotate(txt,(x[i],y[i]))
path,dis=climb_path(data)
print('爬山法','最短路径的城市顺序为:', path,'路径长度为：',dis,sep='\n')
x,y,xd,yd=drawing(path)
n=np.arange(len(xd))
fig,ax=plt.subplots()
for i in range(len(xd)):
    ax.plot(xd[i],yd[i],color='r')
    ax.scatter(xd[i],yd[i],color='b')
for i,txt in enumerate(n):
    ax.annotate(txt,(x[i],y[i]))
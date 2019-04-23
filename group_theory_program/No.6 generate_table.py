# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:51:00 2019

@author: 皇子皇孙
"""
import pandas as pd
def generate_table(group=['r','f','rf']): #导入已知群
    all=[] #用来保存所有组合
    for i in group:
        list=[] #用来保存每一个单位元与所有单位圆的组合
        for j in group:
            x=j+i
            x=simplify(x) #化简函数，可由下面备注部分代替
            list=list+[x]
        all.append(list)
    df=pd.DataFrame({group[0]:all[0]}) #将所有组合排成表
    for i in range(len(group)-1):
        df[group[i+1]]=all[i+1]
    df[' ']=group
    df.set_index(' ',inplace=True)
    return df
def simplify(s): #示意化简函数，效果为在组合尾部加一个a，拼接时删除
    return s+'a'
table=generate_table()
print(table)
'''
for i in range(len(table)):
    for j in range(len(table)):
        table.iloc[i,j]=simplify(table.iloc[i,j])
'''

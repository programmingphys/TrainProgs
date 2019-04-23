# -*- coding: utf-8 -*-
#from Input import get_data
import re

def get_str():
    #得到要化简的字符串
    s = 'fffrrrrrfrffrrf'
    return s

def remove_unit(s,unit_group):
    #从字符串中去掉单位元
    #input:任意字符串，单位元 output：去除单位元的字符串
    s1 = s
    s2 = ''
    while s2 != s1:
        s2 = s1
        for i in range(len(unit_group)):
            s1 = re.sub(unit_group[i],"",s)
            s = s1        
    return s1

def get_formula(unit,group1,group2,formula1,formula2):
    #得到由单位元计算出的替换公式
    #input：当前单位元，字符串及其对应替换元，初始替换公式  output：用于替换的公式
    for m in range(len(group1)):
        if group1[m] in unit_group:
            unit = unit_group.copy()
            unit.remove(unit_group[m])
        for n in range(len(unit)):
            #print(m,n,group1[m],unit)
            if group1[m][0] == unit[n][-1]:
                m_new = remove_unit(unit[n][:-1]+group1[m],unit)
                n_new = remove_unit(unit[n][:-1]+group2[m],unit)
                if m_new not in formula2 and m_new not in formula1: 
                    formula1.append(m_new)
                    formula2.append(n_new)
                if len(m_new) > 1:
                    formula1,formula2 = get_formula(unit,[m_new],[n_new],formula1,formula2)
                    #print('#2#',formula1,formula2)
            if group1[m][-1] == unit[n][0]:
                m_new = remove_unit(group1[m]+unit[n][1:],unit)
                n_new = remove_unit(group2[m]+unit[n][1:],unit)
                if m_new not in formula2 and m_new not in formula1:   
                    formula1.append(m_new)
                    formula2.append(n_new) 
                if len(m_new) > 1:
                    formula1,formula2 = get_formula(unit,[m_new],[n_new],formula1,formula2)            
    return formula1,formula2

def simplification(s1,unit_group,formula1,formula2):
    #化简字符串
    #input：原字符串，单位元列表，用于替换的公式  output：化简完全的字符串
    s2 = ''
    s1 = remove_unit(s1,unit_group)
    while s2 != s1:
        s2 = s1 
        for i in range(len(formula2)):
            if formula2[i] in s1:
                s1 = s1.replace(formula2[i],formula1[i])
                s1 = remove_unit(s1,unit_group)
                #print(a[i],b[i],s1)
                
    return s1

if __name__ == "__main__":
    formula1 = []
    formula2 = []
    unit_group = ['rrr','ff','frfr']
    group_key = ['','','']
    unit = unit_group.copy()
    a,b = get_formula(unit,unit_group,group_key,formula1,formula2)
    s = get_str()
    s1 = simplification(s,unit_group,a,b)
    print('原始字符串：',s,'化简得到的字符串：',s1)

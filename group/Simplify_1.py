# -*- coding: utf-8 -*-
import re

def get_str(s):
    #得到要化简的字符串
    string = s 
    return string

def get_unit_group(unitSet):
    unit_group = unitSet 
    return unit_group

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

def get_formula(unit_group,unit,group1,group2,formula1,formula2):
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
                    formula1,formula2 = get_formula(unit_group,unit,[m_new],[n_new],formula1,formula2)
                    #print('#2#',formula1,formula2)
            if group1[m][-1] == unit[n][0]:
                m_new = remove_unit(group1[m]+unit[n][1:],unit)
                n_new = remove_unit(group2[m]+unit[n][1:],unit)
                if m_new not in formula2 and m_new not in formula1:   
                    formula1.append(m_new)
                    formula2.append(n_new) 
                if len(m_new) > 1:
                    formula1,formula2 = get_formula(unit_group,unit,[m_new],[n_new],formula1,formula2)            
    return formula1,formula2

def simplification(s,unitSet):
    #化简字符串
    #input：原字符串，单位元列表，用于替换的公式  output：化简完全的字符串
    formula1 = []
    formula2 = []
    unit_group = get_unit_group(unitSet)
    group_key = ['']*len(unit_group)
    unit = unit_group.copy()
    a,b = get_formula(unit_group,unit,unit_group,group_key,formula1,formula2)
    s1 = get_str(s)
    s2 = ''
    s1 = remove_unit(s1,unit_group)
    while s2 != s1:
        s2 = s1 
        for i in range(len(formula2)):
            if formula2[i] in s1:
                s1 = s1.replace(formula2[i],formula1[i])
                s1 = remove_unit(s1,unit_group)
                #print(a[i],b[i],s1)
    #print(s1)         
    return s1


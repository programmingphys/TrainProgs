from tkinter import *
import numpy as np
import random
import math
from Table  import Table_Cayley
from GeneGroup import GeneGroup
'''
# D3群
# D3群
generator = ['','r','f']
group = ['rrr','ff','frfr']
element =  GeneGroup(1,func_xx = 1,generator = ['r','f'],unitset = group,initset = ['r','f'])
print(element)
table = Table_Cayley(1,1,element,group)
print(table)
'''
'''
# 给出生成元，默认第一个是单位元
group1 = ['rrr','ff','frfr']
# 给出等于生成元的循环公式
element1 = ['e','r','rr','f','fr','frr']
# 给出全部群元素
table1 = [['e','r','rr','f','fr','frr'],['r','rr','e','frr','f','fr'],['rr','e','r','fr','frr','f'],\
         ['f','fr','frr','e','r','rr'],['fr','frr','f','rr','e','r'],['frr','f','fr','r','rr','e']]
# 给出乘法表，顺序须与群元素一一对应

# D2d群
generator2 =['e','r','f']
group2 = ['rrrr','ff','rfrf']
element2=['e','r','rr','rrr','f','rf','rrf','rrrf']
table2=[['e','r','rr','rrr','f','rf','rrf','rrrf'],['r','rr','rrr','e','rf','rrf','rrrf','f'],\
        ['rr','rrr','e','r','rrf','rrrf','f','rf'],['rrr','e','r','rr','rrrf','f','rf','rrf'],\
        ['f','rrrf','rrf','rf','e','rrr','rr','r'],['rf','f','rrrf','rrf','r','e','rrr','rr'],\
        ['rrf','rf','f','rrrf','rr','r','e','rrr'],['rrrf','rrf','rf','f','rrr','rr','r','e']]

'''
def order(generator, element, table):
    # 通过乘法表得到生成元与每个元素作用的结果矩阵
    n = len(generator)
    gn = []
    c = np.ones((len(element),n),dtype=int)

    for j in range(len(element)):  # 找出生成元在群元素的位置
        c[j][0] = int(j)
        for i in range(n - 1):
            if generator[i+1] == element[j]:
                gn.append(j)

    for i in range(n-1):
        for j in range(len(element)):
            c[j][i+1] = int(element.index(table[gn[i]][j]))

    return c


def gen_coord(generator,group,element,w,h):
    # 给出群元素的初始坐标，选择阶数最大的生成元画成正多边形
    N = 0
    l = 0
    r = 150
    cord = [(random.randint(50,w),random.randint(50,h)) for _ in range(len(element))]
    for i in range(len(generator)-1):
        for j in group:
            num = 0
            for k in range(len(j)):
                if generator[i+1] != j[k]:
                    break
                num += 1
            if num == len(j):
                if N < num:
                    N = num
                    l = i+1
    cord[element.index('')] = (w/2.3+r*math.sin(math.pi/N),h/1.8+r*math.cos(math.pi/N))
    s = generator[l]
    for i in range(N-1):
        cord[element.index(s)]=(w/2.3+r*math.sin(2*math.pi/N*(i+1)+math.pi/N),h/1.8+r*math.cos(2*math.pi/N*(i+1)+math.pi/N))
        s = s+generator[l]
    return cord


def graph(generator,group,element, c1, c2,canvas):
    # 输入生成元、循环公式、群元素、初始坐标、作用矩阵、画布，画出相应的凯莱图。
    K = []
    color = ['black','blueviolet','gray','green','coral']

    for i in range(len(generator)-1):  # 找出阶为2的生成元
        for j in group:
            num = 0
            for k in range(len(j)):
                if generator[i+1] != j[k]:
                    break
                num +=1
            if num == len(j) and num == 2:
                K.append(i+1)

    for i in range(len(c1)):
        for j in range(len(generator)-1):
            if j+1 in K:
                canvas.create_line((c1[c2[i][0]], c1[c2[i][j + 1]]), fill=color[j],width=5)
            else:
                canvas.create_line((c1[c2[i][0]], c1[c2[i][j+1]]), arrow='last', arrowshape='25 20 5',fill=color[j],width=2.5)
            canvas.create_text(c1[c2[i][0]][0]+20,c1[c2[i][0]][1]-20, text=element[i],font=('Couried',35),fill='red')

    for i in range(len(generator)-1):
        if i + 1 in K:
            canvas.create_line(800,150+i*150,950,150+i*150, fill=color[i], width=5)
        else:
            canvas.create_line(800,150+i*150,950,150+i*150,arrow='last', arrowshape='25 20 5', fill=color[i],width=2.5)

    for i in range(len(generator)-1):
        if i + 1 in K:
            canvas.create_text(875,122+i*150, text=generator[i+1], font=('Couried', 35))
        else:
            canvas.create_text(875, 122 + i * 150, text=generator[i + 1], font=('Couried', 35))

    canvas.create_text(450, 40, text='Cayley Graph', font=('Couried', 50))


def Caylay(generator,group,element,table):
    # 生成元、循环公式、群元素，乘法表，利用tkinter画出可响应鼠标左键的凯莱图。
    root = Tk()
    width = 1000
    height = 800
    w = Canvas(root,width=width,height=height,background='white')
    w.pack()
    global c1
    c1 = gen_coord(generator,group,element,width,height)
    c2 = order(generator,element,table)

    def paint(event):
        # 循环画图
        if k:
            global c1
            c1[n] = [event.x,event.y]
            w.delete(ALL)
            graph(generator,group,element, c1, c2,w)

    def coordinate(event):
        # 根据鼠标坐标选择元素点
        global k
        global n
        for i in range(len(c1)):
            if abs(c1[i][0] - event.x) < 20 and abs(c1[i][1] - event.y) < 20:
                k = 1
                n = i
                break
            else:
                k = 0

    graph(generator,group,element, c1, c2,w)
    w.bind("<Button-1>",coordinate)
    w.bind("<B1-Motion>",paint)

    mainloop()

#Caylay(generator,group,element,table)

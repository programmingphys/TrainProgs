import numpy as np
import matplotlib.pyplot as plt
import math
import itertools_recipes as it

data=np.array([[1,1],[5,2],[3,3],[0,2],[9,4],[4,8]])
x=data[:,0]
y=data[:,1]

def choose():
    q=[]
    u=list(it.permutations([0,1,2,3,4,5],6))
    m=np.zeros((6,2))
    n=np.zeros((6,2))
    for i in range(len(u)):
       m[0]=data[u[i][0]]
       m[1]=data[u[i][1]]
       m[2]=data[u[i][2]]
       m[3]=data[u[i][3]]
       m[4]=data[u[i][4]]
       m[5]=data[u[i][5]]
       distance(m)
       q.append(distance(m))
    k=min(q)
    print('最短路程为',k)
    g=q.index(k)
    n[0] = data[u[g][0]]
    n[1] = data[u[g][1]]
    n[2] = data[u[g][2]]
    n[3] = data[u[g][3]]
    n[4] = data[u[g][4]]
    n[5] = data[u[g][5]]
    print(n)
    draw_a_line(n)

def draw_a_line(w):
    i=0
    for i in range(5):
       a=np.linspace(w[i,0],w[i+1,0],100)
       b=np.linspace(w[i,1],w[i+1,1],100)
       plt.plot(a,b,'.')
    c=np.linspace(w[0,0],w[5,0],100)
    d=np.linspace(w[0,1],w[5,1],100)
    plt.plot(c,d,'.')

def distance(w):
    i=0
    sum=0
    e=[]
    for i in range(5):
        e.append(math.sqrt((w[i+1,0]-w[i,0])**2+(w[i+1,1]-w[i,1])**2))
        sum=sum+e[i]
    sum=sum+math.sqrt((w[5,0]-w[1,0])**2+(w[5,1]-w[1,1])**2)
    return(sum)

choose()
plt.show()
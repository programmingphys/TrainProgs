import numpy as np
import matplotlib.pyplot as plt
import itertools

n = 50  # 所求点的个数
k = 15  # 爬山法运行次数

X0 = np.random.rand(n)
Y0 = np.random.rand(n)

points = list(zip(X0,Y0))
print(points, '\n')


def dist(m, k):  # 计算两点距离
    return np.sqrt((m[0]-k[0])**2+(m[1]-k[1])**2)


def climbhill(a):   # 爬山法求局部最短路径
    rt = a+[a[0]]
    test = []
    tmp = list(itertools.combinations(list(range(len(rt[1:-1]))), 2))   # 交换两点的全部情况
    np.random.shuffle(tmp)
    while rt != test:
        test = rt.copy()
        for i in range(len(tmp)):
            a = (dist(rt[tmp[i][0]],rt[tmp[i][0]+1])+dist(rt[tmp[i][0]+2],rt[tmp[i][0]+1])\
                 + dist(rt[tmp[i][1]],rt[tmp[i][1]+1])+dist(rt[tmp[i][1]+2],rt[tmp[i][1]+1]))  # 交换前距离
            wap = rt.copy()
            wap[tmp[i][1] + 1], wap[tmp[i][0] + 1] = wap[tmp[i][0] + 1], wap[tmp[i][1] + 1]
            b = (dist(wap[tmp[i][0]],wap[tmp[i][0]+1])+dist(wap[tmp[i][0]+2],wap[tmp[i][0]+1])\
                 + dist(wap[tmp[i][1]],wap[tmp[i][1]+1])+dist(wap[tmp[i][1]+2],wap[tmp[i][1]+1]))  # 交换后距离

            if a > b:
                rt = wap
                break
    return rt[0:-1]


def graph(x):
    final = x
    X = [final[j][0] for j in range(len(final))]
    Y = [final[j][1] for j in range(len(final))]
    plt.scatter(X, Y, color='r')
    X.append(X[0])
    Y.append(Y[0])
    plt.plot(X,Y)
    plt.axis([0,1,0,1],'equal')
    plt.show()


ntimes = []
distance = []
for i in range(k):    # 求k次爬山法运算最优解
    points2 = points[1:]
    np.random.shuffle(points2)    # 打乱除起点外初始点排序
    points = [points[0]]+points2
    ch = climbhill(points)
    ntimes.append(ch)
    dist_sum = sum([dist(ch[j], ch[j + 1]) for j in range(len(ch) - 1)] + [dist(ch[-1], ch[0])] )
    distance.append(dist_sum)

print('最短路径为：', distance[np.argmin(distance)])

graph(ntimes[np.argmin(distance)])
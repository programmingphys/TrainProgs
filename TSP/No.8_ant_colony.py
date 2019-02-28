import numpy as np
import matplotlib.pyplot as plt

def getdistmat(city,num):
    distmat = np.zeros((num,num))
    for i in range(num):
        for j in range(i,num):
            distmat[i][j] = distmat[j][i]=np.linalg.norm(city[i]-city[j])
    return distmat
    
def ant_colony(city,numant,alpha,beta,rho,Q,itermax):
    
    numcity = city.shape[0]    
    distmat = getdistmat(city,numcity)
    etatable = 1.0/(distmat+np.diag([1e10]*numcity))
    pheromonetable  = np.ones((numcity,numcity))
    pathtable = np.zeros((numant,numcity)).astype(int)

    lengthaver = np.zeros(itermax)
    lengthbest = np.zeros(itermax)
    pathbest = np.zeros((itermax,numcity))

    iterm = 0
    while iterm < itermax:
        if numant <= numcity:
            pathtable[:,0] = np.random.permutation(range(0,numcity))[:numant]
        else:
            pathtable[:numcity,0] = np.random.permutation(range(0,numcity))[:]
            pathtable[numcity:,0] = np.random.randint(0,numcity,[numant-numcity])
        length = np.zeros(numant)

        for i in range(numant):           
            visiting = pathtable[i,0]
        
            unvisited = set(range(numcity))
            unvisited.remove(visiting)

            for j in range(1,numcity):
                #每次用轮盘法选择下一个要访问的城市
                listunvisited = list(unvisited)
                probtrans = np.zeros(len(listunvisited))

                for k in range(len(listunvisited)):
                    probtrans[k] = np.power(pheromonetable[visiting][listunvisited[k]],alpha)\
                            *np.power(etatable[visiting][listunvisited[k]],alpha)
                cumsumprobtrans = (probtrans/sum(probtrans)).cumsum()
                cumsumprobtrans -= np.random.rand()

                for k in range(len(cumsumprobtrans)):
                    if cumsumprobtrans[k]>0:
                        k=listunvisited[k]
                        break

                pathtable[i,j] = k
                unvisited.remove(k)
                length[i] += distmat[visiting][k]
                visiting = k
            length[i] += distmat[visiting][pathtable[i,0]]

        #print length
        lengthaver[iterm] = length.mean()

        if iterm == 0:
            lengthbest[iterm] = length.min()
            pathbest[iterm] = pathtable[length.argmin()].copy()      
        else:
            if length.min() > lengthbest[iterm-1]:
                lengthbest[iterm] = lengthbest[iterm-1]
                pathbest[iterm] = pathbest[iterm-1].copy()

            else:
                lengthbest[iterm] = length.min()
                pathbest[iterm] = pathtable[length.argmin()].copy()    

        # 更新信息素
        changepheromonetable = np.zeros((numcity,numcity))
        for i in range(numant):
            for j in range(numcity-1):
                changepheromonetable[pathtable[i,j]][pathtable[i,j+1]] += Q/distmat[pathtable[i,j]][pathtable[i,j+1]]

            changepheromonetable[pathtable[i,j+1]][pathtable[i,0]] += Q/distmat[pathtable[i,j+1]][pathtable[i,0]]

        pheromonetable = (1-rho)*pheromonetable + changepheromonetable
        iterm += 1
    bestpath = pathbest[-1]
    return lengthaver,lengthbest,bestpath

numant = 40
alpha = 1
beta = 5
rho = 0.1
Q = 1
itermax = 250

#输入城市数据
city=np.array([[0,0],[1,0],[1,1],[0,1],[0.7,0.7],[2,0],[0,2],[0.25,0.5]])

lengthaver,lengthbest,bestpath=ant_colony(city,numant,alpha,beta,rho,Q,itermax)


iterms=range(1,itermax+1)
plt.plot(iterms,lengthaver)
plt.title("lengthaver")
plt.show()
plt.plot(iterms,lengthbest)
plt.title("lengthbest")
plt.show()

#作图
for i in range(len(city)-1):#
    m,n = int(bestpath[i]),int(bestpath[i+1])
    #print(m,n)
    plt.plot([city[m][0],city[n][0]],[city[m][1],city[n][1]],'b')
plt.plot([city[int(bestpath[0])][0],city[n][0]],[city[int(bestpath[0])][1],city[n][1]],'b')
plt.plot(city[:,0],city[:,1],'r*')
plt.title("path")
plt.show()

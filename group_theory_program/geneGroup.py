#author: caozhi
#coding=utf-8

import Simplify
#导入化简模块

def geneNewElement(generator,unitSet,initSet):
    #geneNewElement:通过生成元左右乘获得新的群元
    #input:生成元，单位元关系，初始群元集合
    newSet = []
    for gene in generator:
        for element in initSet:
            leftNewElement = gene + element
            #生成元左乘初始集合中的元素
            rightNewElement = element + gene
            #生成元右乘初始集合中的元素
            newSet.append(leftNewElement)
            newSet.append(rightNewElement)

    newSet = newSet + initSet
    #防止漏掉情况，把初始群元集合与新集合合并，如果初始集合已经是完整的群元集合，则合并后集合元素不变
    newSet = list(set(newSet))
    #先用集合转换去掉newSet中的重复元素
    #再将newSet还原为列表，然后化简
    for i in range(len(newSet)):
        #对新生成群元集合中的元素进行化简
        newSet[i] = Simplify.simplification(newSet[i],unitSet)
    newSet = list(set(newSet))
    #将化简后的newSet转为集合，去掉重复元素
    #再将去掉重复元素的newSet转换为列表
    return newSet


def geneGroup(generator,unitSet,initSet):
    #geneGroup:通过生成元和单位元产生完整的群
    #input:生成元，单位元关系，初始群元集合
    sets = []
    sets.append(initSet)
    #sets中第n个元素为第n次运行geneNewElement产生的群元集合
    #sets中第[-1]个元素和第[-2]个元素分别对应初始集合和新集合
    stop = False
    while not stop:
        newSet = geneNewElement(generator,unitSet,sets[-1])
        #sets的最后一个元素作为每次计算的初始集合输入
        sets.append(newSet)
        #新得到的群元集合置为sets的最后一个元素
        initSet = set(sets[-2])
        newSet  = set(sets[-1])
        #将initSet和newSet转换为集合格式，进行对比
        stop = (newSet == initSet)
        #print(len(sets)+1000)
    for i in range(len(sets[-1])):
        if sets[-1][i] == '':
            sets[-1][i] = 'e'

    return sets[-1]

if __name__ == "__main__":
    #new = geneNewElement(['r','f'],['rrr','ff'],['r','','f'])
    new = geneGroup(['r','f'],['rrr','ff','frfr'],['r','f'])
    print('new set is ',new)

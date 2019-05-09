
class GroupStrings:
    
    def __init__(self,xset,main):
        self.xset=xset
        self.main=main
        self.lenxset=len(xset)
        self.xlens=self.xlenset()
        self.result=[]
        
    
    def inside(self,main):
        poss=[]
        for i in range(self.lenxset):
            pos=[]
            for j in range(len(main)):
                if main[j]==self.xset[i][0]:
                    test=main[j:j+self.xlens[i]]
                    if test==self.xset[i]:
                        pos.append(j)
            poss.append(pos)
        return poss
    

    def cut(self,pos,i,main):
        new=main[:pos]+main[pos+self.xlens[i]:]
        return new


    def xlenset(self):
        xlens=[]
        for x in self.xset:
            xlens.append(len(x))
        return xlens
    

    def exhaustion(self,xset,main):
        pos=self.inside(main)

        #判断二维数组是否为空
        not_empty=False
        for xpos in pos:
            if xpos:
                not_empty=True
                break
        if not_empty:
            for i in range(len(pos)):
                for j in range(len(pos[i])):
                    main=self.cut(pos[i][j],i,main)
                    #递归
                    self.exhaustion(xset,main)
        elif main not in self.result:
            #递归结束，所有结果保存在result中
            self.result.append(main)
            
    def simplify(self,output_result=False):
        self.exhaustion(self.xset,self.main)
        min_result=min(self.result,key=len)
        #找一个最短的字符串，实际上可能存在几个长度相同的最短字符串
        if output_result:
            #可选择是否输出所有化简结果
            return min_result,self.result
        self.exhaustion(self.xset,self.main)
        return min_result

#使用示例
xset=['isi','ha','asd']#所有单位圆组合
main='isishakisishajisisi'#目标化简字符串

gs=GroupStrings(xset,main)#建立字符串类
result=gs.simplify()#调用化简函数
print(result)#使输出最短字符串之一
result2=gs.simplify(True)#更改默认参数
print(result2)#使输出最短字符串之一+所有化简结果

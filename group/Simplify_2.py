
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

        #�ж϶�ά�����Ƿ�Ϊ��
        not_empty=False
        for xpos in pos:
            if xpos:
                not_empty=True
                break
        if not_empty:
            for i in range(len(pos)):
                for j in range(len(pos[i])):
                    main=self.cut(pos[i][j],i,main)
                    #�ݹ�
                    self.exhaustion(xset,main)
        elif main not in self.result:
            #�ݹ���������н��������result��
            self.result.append(main)
            
    def simplify(self,output_result=False):
        self.exhaustion(self.xset,self.main)
        min_result=min(self.result,key=len)
        #��һ����̵��ַ�����ʵ���Ͽ��ܴ��ڼ���������ͬ������ַ���
        if output_result:
            #��ѡ���Ƿ�������л�����
            return min_result,self.result
        self.exhaustion(self.xset,self.main)
        return min_result

#ʹ��ʾ��
xset=['isi','ha','asd']#���е�λԲ���
main='isishakisishajisisi'#Ŀ�껯���ַ���

gs=GroupStrings(xset,main)#�����ַ�����
result=gs.simplify()#���û�����
print(result)#ʹ�������ַ���֮һ
result2=gs.simplify(True)#����Ĭ�ϲ���
print(result2)#ʹ�������ַ���֮һ+���л�����

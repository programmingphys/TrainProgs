from Table import Table_Cayley
from GeneGroup import GeneGroup
from Graph import CayleyGraph
import pandas as pd
df= pd.read_excel('config.xlsx')
print(list(df.iloc[4]))


func_x = df.iloc[0,1]
func_xx =df.iloc[2,1]

func_y = df.iloc[1,1]
func_z =df.iloc[3,1]
generator = ['','r','f']
group = list(df.iloc[4])
#unitset = ['r','f']
initset = ['r','f']
geneElement = GeneGroup(func_x,func_xx,generator=['r','f'],unitset=group,initset = ['r','f'])
cayleyTable  = Table_Cayley(func_y,func_xx,geneElement,group)
cayleyGraph = CayleyGraph(func_z,generator,group,geneElement,cayleyTable)

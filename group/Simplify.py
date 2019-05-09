from  Simplify_1 import simplification
from  Simplify_2 import GroupStrings
def Simplify(func_x,geneator,unset):
    if func_x == 1:
        
        result = simplification(geneator,unset)
        return result
    if func_x == 2:
        gs = GroupStrings(geneator,unset)
        result = gs.simplify(True)
        return result





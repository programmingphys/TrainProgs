from  Table_Cayley import generate_table



def Table_Cayley(func_x,func_xx,group,unit): 
    if func_x == 1:
        result = generate_table(func_xx,group,unit)
        return result


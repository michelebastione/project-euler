import numpy as np
from my_funcs import ab_gen
from itertools import count

AB=np.array([],dtype=int)
NOT_ABS=0

for i in ab_gen():
    if i>28123:
        break
    AB=np.append(AB,i)

def is_sum_ab(n,L=AB):
    if n<24:
        return False 
    for i in L:
        if i>n//2:
            break
        BA=L[np.where(L==i)[0][0]:]
        print(i,BA)
        for j in BA:
            if i+j>n:
                break
            if i+j==n:
                return True
    return False

##for i in count(1):
##    if i>20161:
##        break
##    if i%2500==0:
##        print(i,NOT_ABS)
##    if not is_sum_ab(i):
##        NOT_ABS+=i
##        
##print(NOT_ABS)

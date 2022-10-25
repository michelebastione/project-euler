from my_funcs import Inf_Fract, squares, Pell
from itertools import count

S=squares()
s=[]
for i in range(31):
    s.append(next(S))

M=0
c=0
for i in filter(lambda x : x not in s,count(1)):
    if i==1001:
        break
    P=Pell(i).numerator
    if P>M:
        M=P
        c=i
print(c)
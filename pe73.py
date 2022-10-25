from fractions import Fraction
from math import gcd

c=0
for i in range(2,12001):
    for j in filter(lambda x:gcd(x,i)==1,range(1,i)):
        if j*3>i and j*2<i:
            c+=1
print(c)

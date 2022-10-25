import numpy as np
from sympy import sieve

sieve.extend(10**6)
l=len(sieve._list)//3
L=sieve._list[:l]

M=0
i=1

#approssimazione del cazzo

while i<1000:
    j=i+1
    while sum(L[i:j])<800000:
        j+=2
    while j<l:
        s=sum(L[i:j])
        q=len(L[i:j])
        if s in sieve._list:
            if q>M:
                M=q
                p=s
                x=L[i:j]
                print(M,p)
        j+=2
    i+=1
    

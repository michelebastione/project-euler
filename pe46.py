from itertools import count,filterfalse
from my_funcs import is_prime,squares,primes_gen

for i in filterfalse(is_prime,count(39,2)):
    check=0
    if is_prime(i):
        continue
    s=squares()
    for j in s:
        p=primes_gen()
        if 2*j>=i:
            break
        for k in p:
            if k+2*j>i:
                break
            if k+2*j==i:
                check+=1
                break
        if check!=0:
            break
    if check==0:
        print(i)
        break

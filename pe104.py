from my_funcs import Fib_gen,is_perm
from math import log

k=2750
f=Fib_gen(k)

for i in f:
    if is_perm(str(i%(10**9)),'123456789'):
        if is_perm(str(i//(10**(int(log(i,10)-8)))),'123456789'): 
            break
    k+=1
print(k)

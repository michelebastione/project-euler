from my_funcs import circular_primes
from itertools import count

c=0
for i in count():
    if i==10**6:
        break
    if i%50000==0:
        print(i)
    if circular_primes(i):
        c+=1
print(c)

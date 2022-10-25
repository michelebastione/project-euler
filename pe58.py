from my_funcs import spiral_primes
from itertools import count
from fractions import Fraction

c=3
for i in spiral_primes():
    if i<Fraction(1,10):
        break
    c+=1
        
print(c)

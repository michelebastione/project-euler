import numpy as np
from fractions import Fraction
from my_funcs import coprimes_gen

F=Fraction(42857,100000)
for a in range(2,10**6+1):
    if a%10**3==0:
        print(a)
    for b in coprimes_gen(a):
        if Fraction(b,a)>=Fraction(3,7):
            break
        if Fraction(b,a)>=F:
            F=Fraction(b,a)

print(len(sorted(F[-1].numerator)))

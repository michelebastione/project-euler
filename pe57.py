from my_funcs import Inf_Fract
from itertools import count

g=(2 for i in count())
r2=Inf_Fract(1,g)

s=0
for n in range(1,1000):
    r2.generate(n)
    if len(str(r2.f.numerator))>len(str(r2.f.denominator)):
        s+=1
print(s)

from my_funcs import Inf_Fract
from itertools import count

def g():
   two=count(2,2)
   for i in count(1):
       if (i-2)%3==0:
           yield next(two)
       else:
           yield 1

e=Inf_Fract(2,g())

print(sum(int(i) for i in str(e.generate(99).numerator)))

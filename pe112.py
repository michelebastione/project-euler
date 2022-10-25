from my_funcs import bouncy
from itertools import count


c=0
for i in count(1):
    if bouncy(i):
       c+=1
    if c/i==0.99:
        print(i)
        break

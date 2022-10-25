import numpy as np
from my_funcs import rad

d={n:rad(n) for n in range(1,100001)}
l=sorted(d,key=lambda x: x in d.values())

from itertools import permutations
from my_funcs import is_prime
import numpy as np
from string import digits

L=np.array([])
for i in range(4,9):
    for j in range(1,i+1):
        std=''.join([d for d in digits[1:i] if d!=str(j)])
        for p in permutations(std):
            p1=(str(j),)+p
            p2=''.join(p1)
            if is_prime(int(p2)):
                L=np.append(L,p2)
print(max(L))

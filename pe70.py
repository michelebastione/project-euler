from my_funcs import phi
from itertools import count,permutations

min_phi=1000
for i in count(2):
    if i%(5*10**4)==0:
        print(i)
    if i==10**7:
        break
    if tuple([j for j in str(phi(i))]) in permutations(str(i)):
        if i/phi(i)<min_phi:
            min_phi=i/phi(i)
            value=i

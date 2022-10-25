from itertools import permutations

L=set()

for p in permutations('123456789'):
    s1=int(p[0]),int(''.join(p)[1:5]),int(''.join(p)[5:])
    s2=int(''.join(p)[:2]),int(''.join(p)[2:5]),int(''.join(p)[5:])
    if s1[0]*s1[1]==s1[2]:
        L.add(s1[2])
    if s2[0]*s2[1]==s2[2]:
        L.add(s2[2])
        
print(sum(L))

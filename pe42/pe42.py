import string
from my_funcs import is_tri

F=open('words.txt')
W=F.read().split(',')
F.close()
W.sort()
c=0

for i in range(len(W)):
    W[i]=W[i].strip('"')
    S=0
    for e in W[i]:
        S+=string.ascii_uppercase.index(e)+1
    if is_tri(S):
        c+=1
print(c)

import string

O=open('names1.txt')
N=O.read().split(',')
O.close()
N.sort()
T=0

for i in range(len(N)):
    N[i]=N[i].strip('"')
    M=0
    for e in N[i]:
        M+=string.ascii_uppercase.index(e)+1
    T+=M*(i+1)

print(T)

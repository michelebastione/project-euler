from math import log

file=open('base_exp.txt')
l=file.read().split()
file.close()
L=[(int(i.split(',')[0]),int(i.split(',')[1])) for i in l]

M=0
for j in L:
    if j[1]*log(j[0])>M:
        M=j[1]*log(j[0])
        print(L.index(j)+1)

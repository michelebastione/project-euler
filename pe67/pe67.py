import numpy as np

F=open('triangle.txt')
T=F.read().split()
F.close

c=0
M=np.zeros(shape=(100,100),dtype=int)
for i in range(100):
    for j in range(i+1):
        M[i][j]=T[c]
        c+=1
M=M[::-1]

for i in range(1,100):
    for j in range(100-i):
        M[i][j]+=max(M[i-1][j],M[i-1][j+1])

print(M[99][0])

import numpy as np

F=open('matrix.txt')
matrix=np.matrix([i.split(',') for i in F.read().split()],dtype=np.int64).reshape(80,80)
F.close

nodes = {}

for m in range(80):
    for n in range(80):
        if m==n==0:
            nodes[(0, 0)] = matrix[0, 0]
        elif n==0:
            nodes[(m, 0)] = nodes[(m-1, 0)]+matrix[m, 0]
        elif m==0:
            nodes[(0, n)] = nodes[(0, n-1)]+matrix[0, n]
        else:
            nodes[(m, n)] = min(nodes[(m, n-1)], nodes[(m-1, n)])+matrix[m,n]

print(nodes[79,79])


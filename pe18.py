import my_funcs as mf
import numpy as np
from itertools import product

R="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split()

c=0
M=np.zeros(shape=(15,15),dtype=int)
for i in range(15):
    for j in range(i+1):
        M[i][j]=R[c]
        c+=1

def sum_ric(n,cord):
    s=0
    seq=()
    for k in product('01',repeat=n):
        temp=M[cord[0]][cord[1]]
        cord1=cord
        for c in range(1,n+1):
            cord1=(cord1[0]+1,cord1[1]) if k[c-1]=='0' else (cord1[0]+1,cord1[1]+1)
            temp+=M[cord1[0]][cord1[1]]
        if temp>s:
            s=temp
            seq=k
    print(s)
    return seq


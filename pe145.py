from numpy import array
from time import time

t=time()
s=0

for i in range(10**7):
    if i%10==0:
        continue
    st=str(i)
    if int(st[0])%2==int(st[-1])%2:
        continue
    if all(int(i)%2==1 for i in str(i+int(st[::-1]))):
        s+=1
        
print(s, time()-t)

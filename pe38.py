from itertools import count
from my_funcs import is_perm

M='0'
for i in count():
    if i==10000:
        break
    s=''
    j=1
    while len(s)<9:
       s+=str(i*j)
       j+=1
    if is_perm(s,'123456789') and s>M:
        M=s
print(M)

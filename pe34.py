from math import factorial

s=0
for i in range(10,3000000):
    if sum(factorial(int(j)) for j in str(i))==i:
        s+=i

print(s)
    

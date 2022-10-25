import decimal
from my_funcs import squares
decimal.getcontext().prec=200
s=[]
c=0
for i in squares():
    if i>100:
        break
    s.append(i)
for j in range(1,100):
    if j in s:
        continue
    n=str(decimal.Decimal(j)**decimal.Decimal(0.5))[:101]
    c+=sum(int(k) for k in n if k!='.')
print(c)

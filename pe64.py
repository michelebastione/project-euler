from my_funcs import squares,cont_frac

s=[]
for i in squares():
    if i>10000:
        break
    s.append(i)

c=0
for i in filter(lambda x:x not in s,range(1,10000)):
    if len(cont_frac(i)[1])%2==1:
        c+=1
print(c)

def divs(n):
    D=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            D+=[i,n/i]
    return D

A=[]
     
for i in range(10000):
    if i==sum(divs(sum(divs(i))+1))+1 and i!=sum(divs(i))+1 and (sum(divs(i))+1,i) not in A:
        A.append((i,sum(divs(i))+1))

print(sum([a[0]+a[1] for a in A]))

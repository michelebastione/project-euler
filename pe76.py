d={}

def partitions(n, diz=d):
    if n<0:
        return 0
    if n==0:
        return 1
    s=0
    for k in range(1, n+1):
        a=n-k*(3*k-1)//2
        b=n-k*(3*k+1)//2
        if a in diz:
            temp1=diz[a]
        else:
            temp1=partitions(a)
            if a>0:
                diz[a]=temp1
        if b in diz:
            temp2=diz[b]
        else:
            temp2=partitions(b)
            if b>0:
                diz[b]=temp2        
        if k%2==1:
            s+=temp1+temp2
        else:
            s-=temp1+temp2
    return s


c=1

while partitions(c)%10**6!=0:
    if c%1000==0:
        print(c)
    c+=1
print()

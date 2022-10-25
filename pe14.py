def collatz(n):
    if n%2==0:
        n=int(n/2)
    else:
        n=3*n+1
    return n
   
def chain(n, coll):
    C=[n]
    while n!=1:
        n=collatz(n)
        if n in coll:
            D[C[0]]=len(C)+coll[n]
            return None
        else:
            C.append(n)
    D[C[0]]=len(C)

D={} 
for i in range(1,10**6):
    chain(i, D)
D2={D[x]:x for x in D}   
print(D2[max(D.values())])

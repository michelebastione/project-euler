def is_prime(n):
    for i in range(2,int(n**0.5)+1):   
        if n%i==0:               
            return False        
    return True

def raggr(L):
    diz={}
    for e in L:
        if e not in diz:
            diz[e]=1
        else:
            diz[e]+=1
    return diz

def factors_raw(n):
    F=[]
    if is_prime(n):
        F.append(n)
        return F
    for i in range(2,int(n**.5)+1):   
        if n%i==0:
            if is_prime(i):
                F.append(i)
                F+=factors_raw(int(n/i))
            else:
                continue
            break
    return F
                
def factors(n):
    return raggr(factors_raw(n))

def min_prod_fact(n):
    divs={}
    for i in range(2,n+1):
        for j in factors(i):
            if j not in divs:
                divs[j]=factors(i)[j]
            elif divs[j]<factors(i)[j]:
                divs[j]+=(factors(i)[j]-divs[j])
    potenze=[e**divs[e] for e in divs]
    prod=1
    for k in potenze:
        prod*=k
    return prod

print(min_prod_fact(20))

from itertools import combinations

L=[n*(3*n-1)//2 for n in range(1,3000)]

D=10**6
c=0

for i in combinations(L,2):
    if sum(i) in L:
        a=abs(i[0]-i[1])
        if a in L:
            print(i)
            if a<D:
                D=a
    c+=1
    
print(D)

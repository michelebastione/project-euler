import my_funcs as mf

L=[]
i=23
while len(L)<11:
    if mf.trunc_prime(i):
        L.append(i)
    i+=1
print(sum(L))


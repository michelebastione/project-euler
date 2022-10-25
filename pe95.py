from my_funcs import amicable_chain

M=(0,0)
for i in range(10**4,10**6):
    a=amicable_chain(i)
    if not a:
        continue
    if a[0]>M[0]:
        M=a

print(min(M[1]))

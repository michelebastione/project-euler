from my_funcs import dig_fac_chain

c=0

for i in range(10**6):
    if dig_fac_chain(i)==60:
        c+=1

print(c)


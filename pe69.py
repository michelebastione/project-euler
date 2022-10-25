import my_funcs as mf

max_phi=0
for n in range(2,1000001):
    if n%10000==0:
        print(max_phi)
    if n/mf.phi(n)>max_phi:
        max_n=n
        max_phi=n/mf.phi(n)

print(max_n)

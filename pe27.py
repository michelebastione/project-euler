import my_funcs as mf
import numpy as np

def quad_primes():
    M=0
    for a in range(-999,1000):
        print(a)
        for b in range(-1000,1001):
            S=np.array([])
            for n in range(1000):
                if n>=abs(b):
                    break
                c=n**2+a*n+b
                if c>1 and mf.is_prime(c):
                    S=np.append(S,[c])
            if np.size(S)>M:
                M=np.size(S)
                prod=a*b
    return prod

print(quad_primes())

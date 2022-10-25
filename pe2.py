def somma_fib_pari(n):
    F=[1,2]
    for i in range(n):
        ith=F[-1]+F[-2]
        if ith>n:
            break
        F.append(ith)
    return sum([e for e in F if e%2==0])

print(somma_fib_pari(4*10**6))

Fib=[1,1]
while len(str(Fib[-1]))<1000:
    Fib.append(Fib[-1]+Fib[-2])
print(Fib.index(Fib[-1])+1)

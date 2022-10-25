from sympy import abc
from sympy.solvers.diophantine import diop_quadratic

x,y=abc.x,abc.y

n=3
s=[]

while len(s)<=1000:
    n+=1
    s=diop_quadratic(n*x+n*y-x*y)
    s=[i for i in s if all(j>0 for j in i)]
    s=set(tuple(sorted(k))for k in s)
    
print(n)

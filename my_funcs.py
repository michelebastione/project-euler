#!/usr/bin/python
# -*- coding: utf-8 -*-

from timeit import timeit
import numpy as np
import itertools as itt
import string as st
import math as m
from fractions import Fraction
from copy import copy,deepcopy
import decimal as d

def is_prime(n):
    """Check if the integer n is a prime number"""
    if n==0 or n==1: return False
    if n==2: return True
    if n%2==0: return False
    for i in itt.count(3,2):
        if i>n**0.5: return True
        if n%i==0: return False


def primes_gen():
    """Generates an infinite list of prime numbers"""
    yield 2
    for i in itt.count(3,2):
        if is_prime(i): yield i

def coprimes_gen(n):
    """Generates an infinite list of numbers coprime with n"""
    for i in itt.count(1):
        if m.gcd(n,i)==1: yield i

def pi(n):
    """Returns the number of prime numbers less than n"""
    if n<2: return 0
    if n==2: return 1
    c=0
    for i in primes_generator():
        if i>n: break
        if is_prime(i): c+=1
    return c

def spiral_primes():
    """Arranging all numbers in a increasing spiral this generator returns the ratio of the number
of prime numbers on the diagonals and the total number of numbers on the diagonals at every step."""

    c=1
    for i in itt.count(3):
        if is_prime(i**2-i+1):
            c+=1
        if is_prime((i-1)**2+1):
            c+=1
        yield Fraction(c,(2*i-1))

def circular_primes(n):
    """Returns True if every ordered arrangement of the number is a prime number"""
    if is_prime(n):
        n=str(n)
        pl=[int(n[i:]+n[:i]) for i in range(1,len(n))]
        return all([is_prime(p) for p in pl])
    return False


def trunc_prime(n):
    """Checks if all adjacent subsequences of a digits of a number are prime numbers"""
    if is_prime(n): return all(is_prime(int(str(n)[:i])) for i in range(1,len(str(n)))) and all(is_prime(int(str(n)[i:])) for i in range(1,len(str(n))))
    return False

def squares(n=1):
    """Generates square numbers"""
    for i in itt.count(n): yield i**2

def is_sq(n):
    c=squares()
    t=next(c)
    while t<n: t=next(c)
    return n==t


def tri_num():
    """Generates triangular numbers"""
    for n in itt.count(1):
        yield int(n*(n+1)/2)
        
def is_tri(n):
    """Checks if a number is triangular"""
    c=itt.count(1)
    t=next(c)
    while t<n: t+=next(c)
    return n==t


def is_pal(x):
    """Checks if a sequence is palindrome"""
    if type(x)==int: x=str(x)
    return x==x[::-1]

def raggr(L):
    """Auxiliary factorization function"""
    diz={}
    for e in L:
        if e not in diz: diz[e]=1
        else: diz[e]+=1
    return diz

def factors_raw(n):
    """Auxiliary factorization function"""
    F=[]
    if is_prime(n):
        F.append(n)
        return F
    for i in range(2,int(n**.5)+1):   
        if n%i==0:
            if is_prime(i):
                F.append(i)
                F+=factors_raw(int(n/i))
            else: continue
            break
    return F

def factorization(n,pr=True):
    """Returns the factorization of the integer n"""
    f=raggr(factors_raw(n))
    if pr:
        g=(str(e)+'^'+str(f[e]) for e in f)
        print(n,'= ',end='')
        s=''
        for e in g: s+=e+' × '
        s=s[:-2]
        print(s)
    else:
        return f

def divisors(n):
    """Returns all divisors of integer n"""
    D=np.array([1],dtype=np.uint)
    if is_prime(n): return D
    for d in range(2,int(n**0.5)+1):
        if n%d==0 and n/d!=d: D=np.append(D,[[d,n//d]])
        elif n%d==0: D=np.append(D,[[d]])
    return np.sort(D)

def amicable_chain(n,limit=10**6):
    m=n
    c=0
    L=np.array([])
    while True:
        k=n
        n=sum(divisors(n))
        if n>limit:
##            print("Overflow error!")
            return None
        if k==n or n in L: return None
        c+=1
        L=np.append(L,[n])
        if n==m: return c, L

def is_ab(n):
    """Checks if a number is abundant"""
    if n<5*10**9 and (n%2!=0 and n%3!=0):
        return False
    return sum(divisors(n))>n

def ab_gen(n=12):
    """Generates abundant numbers"""
    for i in itt.count(n):
        if is_ab(i):
            yield i

def nPr(n,k):
    """Returns the number of injective functions from a set with k elements to a set with n elements"""
    if n<k: return 0
    return m.factorial(n)//m.factorial(n-k)

def nCr(n,k):
    """Returns the number of possible subsets with k elements from a set of n elements"""
    return nPr(n,k)//m.factorial(k)
  
def surj(m,n):
    """Returns the number of surjective functions from a set with k elements to a set with n elements"""
    return sum((-1)**j*nCr(n,j)*(n-j)**m for j in range(n))

def prod(S):
    """Returns the product of all elements in S"""
    p=1
    for i in S: p*=i
    return p

def rad(n):
    """Returns the product of all prime factors of a number"""
    return prod(factorization(n,False))

##def bcp(n):
##    return prod(nCr(n,k) for k in range(n+1))
##
##def dbcp(n):
##    b=bcp(n)
##    return sum(divisors(b))+b
##
##def sdbcp(n):
##    return sum(dbcp(k) for k in range(1,n+1))

def phi(n):
    """Euler's Totient Function"""
    return (n*prod([(1-Fraction(1,p)) for p in factorization(n,False)])).numerator

##def resilience(n):
##    return Fraction(phi(n),n-1)

##def Farey(n):
##    print(1+sum(phi(m) for m in range(1,n+1)))


def dig_fac_chain(n):
    """Returns the length of the chain formed by the sum of the factorial of the digits of n"""

    c=0
    L=(169,363601,1454,871,45361,872,45362)
    while n not in L:
        c+=1
        k=sum(m.factorial(int(i)) for i in str(n))
        if k==n: return c
        n=k
    if n in L[:3]: return c+3
    return c+2

def is_anagram(word1, word2):
    """Fancy anagram checker through fundamental theorem of arithmetics,
    does the same job of is_perm but 10 times slower"""
    
    word1, word2=word1.lower(), word2.lower()
    p=primes_gen()
    diz={i:next(p) for i in st.ascii_lowercase}
    return prod(diz[j] for j in word1)==prod(diz[k] for k in word2)

def is_perm(n,m):
    """Checks if sequence n is a permutation of sequence m"""
    if n==m: return True
    if len(n)!=len(m): return False
    n=list(n)
    m=list(m)
    for i in range(len(n)):
        if n[0] in m:
            m.remove(n[0])
            n.remove(n[0])
        else: return False
    return True


def Fib_gen(n=1):
    """Generates Fibonacci numbers"""
    t0=0
    t1=1
    if n==0: yield t0
    if n==1: yield t1
    c=1
    while c<n: 
        t2=t1+t0
        t0=t1
        t1=t2
        c+=1
    yield t2
    while True:
        t2=t1+t0
        t0=t1
        t1=t2
        yield t2


def Fibonacci(n):
    """Returns the n-th Fibonacci number"""
    f=Fib_gen(n)
    return next(f)
    
Tribs=[0,0,1]
def Tribonacci(n):
    """Returns the n-th Tribonacci number"""
    t0=0
    t1=0
    t2=1
    if n<=2:
        return eval('t'+str(n))
    for i in range(2,n):
        if i%(5*10**4)==0:
            print(i)
        t3=t2+t1+t0
        t0=t1
        t1=t2
        t2=t3
    return t3
        


def from_numeral(n):
    """Converts Roman numerals to arabic digits"""
    numerals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    adjust={'IV':2,'IX':2,'XL':20,'XC':20,'CD':200,'CM':200}
    s=0
    for i in n: s+=numerals[i]
    for j in adjust:
        if j in n: s-=adjust[j]
    return s

def to_numeral(n):
 """Converts arabic digits to Roman numerals"""

 s=''
 if n//1000>0:s+='M'*(n//1000);n%=1000
 if n>=900:s+='CM';n-=900
 if n>=500:s+='D';n-=500
 if n>=400:s+='CD';n-=400
 if n//100>0:s+='C'*(n//100);n%=100
 if n>=90:s+='XC';n-=90
 if n>=50:s+='L';n-=50
 if n>=40:s+='XL';n-=40
 if n//10>0:s+='X'*(n//10);n%=10
 if n==9:s+='IX';n-=9
 if n>=5:s+='V';n-=5
 if n==4:s+='IV';n-=4
 return s+'I'*n

def terne_pit(n):
    """Too lazy to explain what this does, has something to do with unique Pythagorean Triplets"""
    L=[]
    for a in range(3,n//3):
        if a%2==1:
            b=int((a**2-1)/2)
            c=int((a**2+1)/2)
        else:
            b=int((a/2)**2-1)
            c=b+2
        if a+b+c==n:
            if not any(is_perm((a1,b1,c1),x) for x in L):
                L.append((a,b,c))
        k=2
        while (a+b+c)*k<=n:
            a1,b1,c1=k*a,k*b,k*c
            if a1+b1+c1==n:
                if not any(is_perm((a1,b1,c1),x) for x in L): 
                    L.append((a1,b1,c1))
            k+=1
    return L

def gen_from_list(L):
    """Continued Fraction auxiliary function"""
    while True:
        for i in L: yield i

def cont_frac(n):
    """Returns integer approximation root and period of the continued fraction of an irrational square root"""
    if is_sq(n): return int(m.sqrt(n))
    rq=int(n**.5)
    pl=rq
    den=1
    L=[]
    while True:
        fr=Fraction((rq+pl),(n-pl**2)//den,_normalize=False)
        num=fr.numerator
        den=fr.denominator
        temp=num//den
        L.append(temp)
        pl=den*temp-pl
        if den==1: break
    return(rq,L)

class Inf_Fract():
    """Class of continued fractions with (virtual) infinite precision"""

    def __init__(self,unit,gen=None):

        if type(cont_frac(unit))==int:
            print('Perfect square')
            self.unit=int(unit**.5)
            self.period=[]
            self.gen=[]
            return None
        self.unit=cont_frac(unit)[0]
        self.period=cont_frac(unit)[1]
        if not gen: self.gen=gen_from_list(cont_frac(unit)[1])
        else: self.gen=gen

    def generate(self,n,dec=False,un=True,):
        """Returns fraction approximation of the square root to the n-th denominator"""

        if not self.gen: return self.unit
        L=[next(self.gen) for m in range(n)][::-1]
        self.f=Fraction(1,L[0])
        for k in L[1:]: self.f=Fraction(1,k+self.f)
        if un: self.f+=self.unit
        if dec: self.f=d.Decimal(self.f.numerator)/d.Decimal(self.f.denominator)
        self.gen=gen_from_list(self.period)
        return self.f

def Pell(n):
    """Returns the smaller solution to the Pell Equation of coefficient n"""
    c=Inf_Fract(n)
    l=len(c.period)
    if l==1: return c.generate(1)
    if l%2==0: return c.generate(l-1)
    return c.generate(2*l-1)

def incr(n):
    """Returns True if n is an increasing number"""
    n=str(n)
    m=sorted([i for i in n])
    return str(n)==''.join(m)

def dicr(n):
    """Returns True if n is a dicreasing number"""
    n=str(n)
    m=sorted([i for i in n],reverse=True)
    return str(n)==''.join(m)

def bouncy(n):
    """Returns True if n is a bouncy number"""
    return not incr(n) and not dicr(n)

def k_partitions(n, k):
    if k==1:
        return 1
    if k>n or k<=0:
        return 0
    return k_partitions(n-1, k-1) + k_partitions (n-k, k)

def partitions(n, diz={}):
    if n<0:
        return 0
    if n==0:
        return 1
    s=0
    for k in range(1, n+1):
        a=n-k*(3*k-1)//2
        b=n-k*(3*k+1)//2
        if a in diz:
            temp1=diz[a]
        else:
            temp1=partitions(a)
            if a>0:
                diz[a]=temp1
        if b in diz:
            temp2=diz[b]
        else:
            temp2=partitions(b)
            if b>0:
                diz[b]=temp2        
        if k%2==1:
            s+=temp1+temp2
        else:
            s-=temp1+temp2
    return s


def B(n):
##    adj = 1 if n%2 else m.factorial(n//2)
##    return prod((pow(n-i,n-(2*i+1))) for i in range(n//2))*adj//prod((m.factorial(j) for j in range(n//2+1)))**2
    "Apparentemente questa sopra è 10 volte meno efficiente di questa sotto, che è già bella inefficiente si suo"
    return prod(nCr(n,k) for k in range(n+1))

def harshad(n):
    return n%sum(int(i) for i in str(n))==0

def right_truncatable_harshad(n):
    n=str(n)
    return all(harshad(int(n[:i])) for i in range(1,len(n)+1))

def strong_harshad(n):
    return harshad(n) and is_prime(n//sum(int(i) for i in str(n)))

def strong_right_truncatable_harshad_prime(n):
    m=str(n)[:-1]
    return is_prime(n) and all(harshad(int(m[:i])) for i in range(1,len(m)+1)) and is_prime(int(m)//sum(int(j) for j in m))




##class irr():
##
##    def __init__(self,ir,symbol,rat=0,coeff=1,exp=1):
##        self.rat=rat
##        self.ir=ir
##        self.coeff=coeff
##        if exp==1:
##            self.symbol=symbol
##        else:
##            self.symbol=symbol[0]+'^'+str(exp)
##        self.value=coeff*ir**exp+rat
##        self.exp=exp
##        
##    def __str__(self):
##        if self.coeff!=0:
##            if self.rat!=0:        
##                return (str(self.rat)+'+'+str(self.coeff)+self.symbol) if self.coeff!=1 else (str(self.rat)+'+'+self.symbol)
##            else:
##                return (str(self.coeff)+self.symbol) if self.coeff!=1 else (self.symbol)
##        else:
##            if self.rat!=0:        
##                return (str(self.rat))
##            else:
##                return ('0')
##            
##    def _add(self,other):
##        if isinstance(other,irr):
##            if self.ir==other.ir:
##                return irr(self.ir,self.symbol,self.rat+other.rat,self.coeff+other.coeff)
##            return irr(self.ir+other.ir,self.symbol+'+'+other.symbol,self.rat+other.rat)
##        else:
##            return irr(self.ir,self.symbol,self.rat+other,self.coeff)
##
##    def _sub(self,other):
##        if isinstance(other,irr):
##            if self.ir==other.ir:
##                return irr(self.ir,self.symbol,self.rat-other.rat,self.coeff-other.coeff)
##            return irr(self.ir,self.symbol+'-'+other.symbol,self.rat-other.rat)
##        else:
##            return irr(self.ir,self.symbol,self.rat-other,self.coeff)
##
##    def _mul(self,other):
##        if isinstance(other,irr):
##            if self.ir==other.ir:
##                return irr(self.ir,self.symbol,self.rat*other.rat,self.coeff*other.coeff+self.rat*other.coeff+other.rat*self.coeff,self.exp+1)
##            return irr(self.ir*other.ir,self.symbol+other.symbol,self.rat*other.rat,self.coeff*other.coeff)    #aggiungere caso 'polare'
##        else:
##            return irr(self.ir,self.symbol,self.rat*other,self.coeff*other)
##
##    def _truediv(self,other):
##        if isinstance(other,irr):
##            if self.ir==other.ir:
##                return irr(self.ir,self.symbol,None,Fraction(self.coeff,other.coeff),self.exp-1)
##            return irr(self.ir/other.ir,self.symbol+'/'+other.symbol,None,self.coeff/other.coeff)            #non so cosa cazzo fare per le frazioni
##        else:
##            return irr(self.ir,self.symbol,Fraction(self.rat,other),Fraction(self.coeff,other))


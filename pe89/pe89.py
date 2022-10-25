file=open('numerals.txt','r')
numbers=file.read().split()
file.close()

numerals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
adjust={'IV':2,'IX':2,'XL':20,'XC':20,'CD':200,'CM':200}

def from_numeral(n):
    s=0
    for i in n:
        s+=numerals[i]
    for j in adjust:
        if j in n:
            s-=adjust[j]
    return s

def to_numeral(n):
    s=''
    if n//1000>0:
        s+='M'*(n//1000)
        n%=1000
    if n>=900:
        s+='CM'
        n-=900
    elif n>=500:
        s+='D'
        n-=500
    elif n>=400:
        s+='CD'
        n-=400
    if n//100>0:
        s+='C'*(n//100)
        n%=100
    if n>=90:
        s+='CX'
        n-=90
    elif n>=50:
        s+='L'
        n-=50
    elif n>=40:
        s+='XL'
        n-=40
    if n//10>0:
        s+='X'*(n//10)
        n%=10
    if n==9:
        s+='IX'
        return s
    elif n>=5:
        s+='V'
        n-=5
    elif n==4:
        s+='IV'
        return s
    s+='I'*n
    return s

S=0
for n in numbers:
    S+=len(n)-len(to_numeral(from_numeral(n)))
print(S)

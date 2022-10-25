from itertools import count

def ssd(n):
    return sum(int(i)**2 for i in str(n))

s=0
for i in count(2):
    if i==10**7:
        break
    n=i
    while n not in (1,89):
        n=ssd(n)
    if n==89:
        s+=1

from itertools import product

class Dadi():
    def __init__(self, tipo, numero):
        self.somme = {i:0 for i in range(numero, tipo*numero+1)}
        self.combinazioni = tipo**numero
        for i in product(range(1, tipo+1), repeat=numero):
            self.somme[sum(i)] += 1

d4=Dadi(4,9)
d6=Dadi(6,6)

c=0
for i in d4.somme:
    for j in d6.somme:
        if i>j:
            c+=d4.somme[i]*d6.somme[j]

print(c/(d4.combinazioni*d6.combinazioni),time())

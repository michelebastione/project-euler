from string import ascii_lowercase as alphabet
from itertools import product

file=open('cipher.txt')
text=[int(i) for i in file.read().split(',')]
file.close()

def xor_encr(letter, key):
    if type(letter)==str:
        letter=ord(letter)
    if type(key)==str:
        key=ord(key)
    return chr(letter^key)

g=product(alphabet, repeat=3)

for i in g:
    new=''
    c=0
    for j in text:
       new+=xor_encr(j, i[c])
       c+=1
       c%=3
    if 'and' in new:
        if 'that' in new:
            if 'have' in new:
                break

print(sum(ord(i) for i in new))  

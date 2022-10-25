from itertools import count,permutations

s=0
for i in permutations('0123456789'):
    if i[0]=='0':
        continue
    if int(''.join(i[1:4]))%2!=0:
        continue
    if int(''.join(i[2:5]))%3!=0:
        continue
    if int(''.join(i[3:6]))%5!=0:
        continue
    if int(''.join(i[4:7]))%7!=0:
        continue
    if int(''.join(i[5:8]))%11!=0:
        continue
    if int(''.join(i[6:9]))%13!=0:
        continue
    if int(''.join(i[7:10]))%17!=0:
        continue
    s+=int(''.join(i))
    print(i)
print(s)

c=3
i=4
while i<10:
    j=1
    while True:
        if j>len(str(i**j)):
            break
        if len(str(i**j))==j:
            c+=1
        j+=1
    i+=1
print(c)

for a in range(10,100):
    a1=[x for x in str(a)]
    if any(x=='0' for x in a1):
        continue
    for b in range(a+1,100):
        b1=[y for y in str(b)]
        if any(y=='0' for y in b1):
            continue
        for i in a1:
            if len(a1)==2:                    
                for j in b1:
                    if len(b1)==2 and i==j:
                        a1.remove(i)
                        a2=int(a1[0])
                        b1.remove(j)
                        b2=int(a1[0])
                        print(a1,b1)
                        if int(a2)/int(b2)==a/b:
                            print(a,b)
                    

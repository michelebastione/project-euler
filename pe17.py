un={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
teen={10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
dec={0:'',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

c=0
for n in range(1,1000):
    m=str(n)
    s=''
    if n>=100:
        s+=un[int(m[0])]+'hundred'
        if int(m[-2]+m[-1])!=0:
            s+='and'
    if n>=10 and m[-2]=='1':
        s+=teen[int(m[-2]+m[-1])]
        c+=len(s)
        continue
    elif n>19:
        s+=dec[int(m[-2])]
    s+=un[int(m[-1])]
    c+=len(s)

    
print(c+len('onethousand'))

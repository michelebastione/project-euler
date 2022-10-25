def is_pal(s):
    s=str(s)
    if s==s[::-1]:
        return True
    return False

max_pal=0

for n in range(100,1000):
    for m in range(100,1000):
        if is_pal(n*m) and n*m>max_pal:
            max_pal=n*m

print(max_pal)
            

def is_prime(n):
    for i in range(2,int(n**0.5)+1):             
        if n%i==0:              
            return False        
    return True                 

num=600851475143
max_fac=1
for i in range(7,int(num**0.5)):
    if num%i==0:
        if is_prime(i):
            max_fac=i

print(max_fac)

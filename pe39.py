from my_funcs import terna_pit_num

M=0
p=12

for i in range(12,1001):
    if len(terna_pit_num(i))>M:
        M=len(terna_pit_num(i))
        p=i

print(p)

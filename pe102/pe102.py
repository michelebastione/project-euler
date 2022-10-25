from sympy import Point,Polygon

file=open('triangles.txt','r')
L=file.read().split()
M=[]
for i in L:
    j=i.split(',')
    M.append(((j[0],j[1]),(j[2],j[3]),(j[4],j[5])))
file.close()
del(L)

c=0
O=Point(0,0)
for k in M:
    if Polygon(k[0],k[1],k[2]).encloses_point(O):
        c+=1
print(c)


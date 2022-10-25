file=open('keylog.txt')
L=[int(i) for i in set(file.read().split())]
file.close()


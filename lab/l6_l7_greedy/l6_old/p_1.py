# infoarena - cifre 2
import os
path = os.path.dirname(__file__)
file_in = path + "/cifre5.in"
f = open(file_in, 'r')
n, k = (int (x) for x in f.readline().split())
cifre = [int (x) for x in f.readline().split()]
cifre.sort()
zerouri = []
for x in cifre:
    if(not x):
        zerouri.append(x)
        cifre = cifre[1:]
    if(x):
        break
cifre[k:k] = zerouri
print(cifre)
suma_minima = 0
# luam cele mai mici cifre si le transformam in primele cifre ale numerelor 

fout = open(path + "/cifre5.out", "w")
fout.write(str(suma_minima))
    
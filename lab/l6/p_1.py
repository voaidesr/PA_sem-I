# infoarena - cifre 2
f = open("C:\\Laboratoare\\LabPA\\l6\\cifre5.in", 'r')
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
suma_minima = 0
# luam cele mai mici cifre si le transformam in primele cifre ale numerelor 

fout = open("cifre5.out", "w")
fout.write(str(suma_minima))
    
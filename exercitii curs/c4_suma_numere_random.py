# biblioteca random
import random

nume_fisier = input("Nume fisier: ").strip()
n = int(input("Numar: "))

#deschidem fisierul citit mai sus
with open(nume_fisier, "w") as f:
    # initializam generatorul de numere aleatorii
    random.seed()
    # generam numere intre 1 si 1000 
    for k in range(n-1):
        num = random.randint(1, 1000)
        f.write(str(num) + " + ")
    num = random.randint(1, 1000)
    f.write(str(num))

########################################

# Acum vrem sa calculam suma numerelor din fisier
f = open(nume_fisier, 'r')
numere = [int(x) for x in f.readline().split(" + ")]
suma = sum(numere)

f.close()

f = open(nume_fisier, 'a')
f.write(" = " + str(suma))
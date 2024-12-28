import random
numf = input("Numele fisierului: ")
n = int(input("Numar valori: "))
with open(numf, "w") as f:
    # se initalizeaza generatorul
    random.seed()
    for k in range(n-1):
        x = random.randint(1, 1000)
        f.write(str(x) + " + ")
    x = random.randint(1, 1000)
    f.write(str(x))
f = open(numf)
numere = [int(x.strip()) for x in f.readline().split("+")]
suma = sum(numere)
f = open(numf, "a")
f.write(" = " + str(suma))
f.close()
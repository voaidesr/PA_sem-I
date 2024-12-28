# Fișierul text numere.txt conține, pe mai multe linii, numere întregi separateîntre ele prin spații. Scrieți un program care afișează pe ecran suma numerelor din fișier.
f = open("input.txt")
g = open("exemplu.txt", 'w')
line = f.readline()
suma = 0
while line != "":
    numere = [int(x) for x in line.split()]
    g.writelines("\n".join(map(str, numere)))
    suma += sum(numere)
    line = f.readline()
print(suma)
# exista si metoda extend la liste
# numere.extent([int(x) for x in line.split()])

# scris cu f.write(sir) sau f.writelines(colectie de siruri)
g.write(str(suma))
# Fișierul text numere.txt conține, pe mai multe linii, numere întregi separateîntre ele prin spații. Scrieți un program care afișează pe ecran suma numerelor din fișier.
f = open("input.txt")
numere = [int(x) for x in f.read().split()]
print(sum(numere))
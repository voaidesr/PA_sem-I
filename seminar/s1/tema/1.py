"""
Se citește un șir format din numere naturale cu proprietatea că fiecare valoare distinctă
din șir apare de un număr par de ori, mai puțin una care apare de un număr impar de ori.
Să se afișeze valoarea care apare de un număr impar de ori în șirul dat.

"""
numere = [int(x) for x in input("Numere: ").split()]
x = 0
for i in numere:
    x ^= i
print(f"Numarul este {x}")
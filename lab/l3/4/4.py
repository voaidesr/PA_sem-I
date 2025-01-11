numere = [int(x) for x in input().strip().split()]
max1 = max(numere)
while max1 in numere:
    numere.remove(max1)
if not numere:
    print(f"Lista nu contine elemente distincte, singurul element fiind {max1}")
else:
    print(f"Cele mai mari numere distincte sunt {max1} si {max(numere)}")
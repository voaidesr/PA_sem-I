#Se citește un șir format din n numere întregi. Să se verifice dacă toate numerele citite au fost pozitive sau nu.
n = int(input())
for i in range(n):
    x = int(input())
    if(x < 0):
        print(f"{x} este negativ!")
        break
else:
    print(f"Toate cele {n} numere sunt pozitive")
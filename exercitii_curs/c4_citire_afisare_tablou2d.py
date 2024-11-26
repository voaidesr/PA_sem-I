m = int(input("Numarul de linii: "))
n = int(input("Numarul de coloane: "))
T = []

for i in range(m):
    linie = []
    for j in range(n):
        x = int(input(f"Elementul T[{i}][{j}]= "))
        linie.append(x)
    T.append(linie)

for linie in T:
    for x in linie:
        print(x, end=" ")
    print()
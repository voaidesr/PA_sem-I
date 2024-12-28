m = int(input("Numarul de linii = "))
n = int(input("Numarul de cloane = "))
matrice = []
for i in range(m):
    linie = []
    for j in range(n):
        x = int(input(f"a[{i}][{j}] = "))
        linie.append(x)
    matrice.append(linie)

for i in range(m):
    for j in range(n):
        print(matrice[i][j], end = " ")
    print()
def gen_matrice(n):
    return [[a*n + b for b in range(1, n+1)] for a in range(n)]

def parcurgere_spirala(matrice):
    pasi = []
    top, bottom, left, right = 0, len(matrice) - 1, 0, len(matrice) - 1
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            pasi.append((top, i))
        top += 1

        for i in range(top, bottom + 1):
            pasi.append((i, right))
        right -= 1

        for i in range(right, left-1, -1):
            pasi.append((bottom, i))
        bottom -= 1

        for i in range(bottom, top-1, -1):
            pasi.append((i, left))
        left += 1
    return pasi

def main():
    n = int(input())
    matrice = gen_matrice(n)
    pasi = parcurgere_spirala(matrice)
    for pas in pasi:
        print(matrice[pas[0]][pas[1]], end=" ")

if __name__ == "__main__":
    main()
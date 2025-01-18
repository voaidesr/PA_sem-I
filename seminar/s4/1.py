def matrice(n):
    matrice = [[i] + [0]* (i-1) for i in range(1,n)]
    matrice.append([i for i in range(n,0,-1)])
    for i in range(n-2, 0, -1):
        for j in range(1, i+1):
            matrice[i][j] = matrice[i][j-1] + matrice[i+1][j] + matrice[i+1][j-1]
    return matrice

def print_m(matrice):
    # find maximum spaced ocuppied by a char
    nrcr = int(max([len(str(max(linie))) for linie in matrice]))
    for linie in matrice:
        for elem in linie:
            print(str(elem).rjust(nrcr), end = " ")
        # rjust - metoda asupra string care aliniaza la dreapta, pe un nr de characters
        print()

def main():
    n = int(input())
    print_m(matrice(n))

if __name__ == "__main__":
    main()
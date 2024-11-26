def genereaza_matrice(n):
    # generam o matrice triunghiulara cu toate elementele zero
    matrice = [[0]*i for i in range(1, n+1)]
    # generam coloana 0 si linia n-1
    for i in range(n):
        matrice[i][0] = i + 1
        matrice[n-1][i] = n-i
    # generam celelalte elemente
    for i in range(n-2, 0, -1):
        for j in range (1, i+1):
            matrice[i][j] = matrice [i+1][j] + matrice [i+1][j-1] + matrice [i][j-1]  
    return matrice

def afiseaza_matrice(matrice):
    # calculam latimea maxima a unei coloane
    latime_maxima = [max(len(str(matrice[i][j])) for i in range(j, n)) for j in range(n)]
    for i in range(n):
        linie = []
        for j in range(len(matrice[i])):
            # aliniem fiecare element la dreapta, pe coloana
            linie.append(f"{matrice[i][j]:>{latime_maxima[j]}}")
        print(" ".join(linie))
        
n = int(input().strip())
matrice = genereaza_matrice(n)
afiseaza_matrice(matrice)
import os 
path =  os.path.dirname(__file__)
in_file = path + "/matrice.in"
out_file = path + "/matrice.out"

def genMatrice(m, n):
    import random
    matrice = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j] = max(matrice[i][j-1], matrice[i-1][j]) + random.randint(1, 10)
    return matrice

def findX(x, matrice, m, n):
    row, col = 0, n-1 # incepem sa cautam din colt dreapta sus 
    while row < m and col >= 0:
        if matrice[row][col] == x:
            return (row, col)
        elif matrice[row][col] > x:
            col -= 1
        else:
            row += 1
    return None

def main():
    import pprint
    a = genMatrice(4, 5)
    pprint.pp(a)
    print(findX(12, a, 4, 5))

if __name__ == "__main__":
    main()
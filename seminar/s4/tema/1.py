def matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[-1][i] = 1
        matrix[i][-1] = 1
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            matrix[i][j] = matrix[i][j+1] + matrix[i+1][j]
    return matrix

def print_m(matrice):
    nrchr = max([len(str(max(line))) for line in matrice])
    for line in matrice:
        for element in line:
            print(str(element).rjust(nrchr), end=" ")
        print()


def main():
    n = int(input())
    print_m(matrix(n))

if __name__ == "__main__":
    main()
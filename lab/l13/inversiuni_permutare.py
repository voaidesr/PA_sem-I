# se da o permutare, sa se afle cate inversiuni sunt
# cu divide et impera
# impartim permutarea in doua: st si dr
# vedem cate inversiuni sunt pe stanga, cate sunt pe dreapta (PARTEA DE DIVIDE)
# vedem cate inversiuni sunt intre stanga si dreapta (partea de IMPERA) --> interclasare

def interclasare(a, b):
    n, m = len(a), len(b)
    i, j = 0, 0
    inv = 0
    c = []
    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
            inv += j
        else:
            c.append(b[j])
            j += 1
            inv += n - i
    c += a[i:]
    c += b[j:]
    return c, inv

def numar_inversiuni(arr):
    if len(arr) < 2:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = numar_inversiuni(arr[:mid])
    right, inv_right = numar_inversiuni(arr[mid:])
    merged, inv_merge = interclasare(left, right)
    return merged, inv_left + inv_right + inv_merge

def inversiuni_permutare(permutare):
    _, num_inversiuni = numar_inversiuni(permutare)
    return num_inversiuni

# Exemplu de utilizare
permutare = [2, 3, 8, 6, 1]
print(f"Numarul de inversiuni: {inversiuni_permutare(permutare)}")
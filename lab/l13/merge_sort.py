# se sorteaza jumatate, dupa care jumatatile jumatatilor, etc
# se interclaseaza la fiecare pas
# fiecare pas (interclasarea) are complexitate O(n)
# sunt log2n pasi
# deci complexitate O(nlogn)
def interclasare(a, b):
    c = []
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n and j < m:
        if(a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
    c += a[i:]
    c += b[j:]
    return c
    # interclasarea are O(len(a)+len(b))
def merge_sort(v, st, dr):
    if st == dr:
        return
    mij = (st + dr)//2
    merge_sort(v, st, mij)
    merge_sort(v, mij+1, dr)
    # aici impartim in jumatati si le sortam 
    # vrem sa interclasam v[st:mij+1], v[mij+1:dr]
    v[st:dr+1] = interclasare(v[st:mij+1], v[mij+1: dr])
    # in python se poate v[5:7] = [1, 2, 3, 4, 5]

v = [0, 1, 3, 8, 2, 7, 9, 8]
merge_sort(v, 0, len(v)-1)
print(v)
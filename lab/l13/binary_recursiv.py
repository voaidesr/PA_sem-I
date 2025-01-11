# se da un vector de numere sortat crescator !!! important la binary_search - se da un vector 
# vrem sa gasim valoarea primului element  >= x
def binary(v, x, st, dr):
    if st == dr:
        return st
    mij = (st+dr)//2
    if v[mij] < x:
        return binary(v, x, mij+1, dr)
    else:
        return binary(v, x, st, mij)
    
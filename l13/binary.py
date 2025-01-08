# se da un vector de numere sortat crescator !!! important la binary_search - se da un vector 
# vrem sa gasim valoarea primului element  >= x
def binary_search(v, x):
    st = 0
    dr = len(v) - 1
    while st < dr:
        mij  = (st + dr)//2
        if v[mij] < x: # cautam mai la dreapta 
            st = mij + 1
        else:
            dr = mij # nu punem +1 pt ca v[mij] poate fi un potential raspuns !!!! foarte mare grija
    return st
v = [1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
print(binary_search(v, 4))
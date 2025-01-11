# primul element <= x 
# la cautare binara, una dintre principalele probleme e u=bucla infinita, in cazul [st, st+1] 
def binary(v, x, st, dr):
    if(st == dr):
        return st
    mij = (st + dr + 1)//2 # in intervale de lungime 2, mijlocul tinde la stanga - trb sa luam practic ceil, sa "tragem mijlocul la dreapta"
    if(v[mij] > x):
        return binary(v, x, st, mij-1)
    else:
        return binary(v, x, mij, dr)
v = [1, 1, 1, 3, 4, 5, 5, 6, 9, 10]
st = binary(v, 8, 0, len(v)-1)
print(st, v[st])
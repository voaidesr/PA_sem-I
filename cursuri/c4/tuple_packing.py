a = 1, 2, 3, 4 # tuple packing
print(a)
c, d, e, f = a # tuple unpacking
print(c, d, e, f)
# daca nu stim numar de valori, se poate folosi *
x, *y, z = a
print(x, y, z)
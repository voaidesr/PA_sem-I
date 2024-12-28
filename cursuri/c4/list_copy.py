import copy
a = [1, 2, 3, 4]
b = a.copy() # shallow copy
a[1] = "abc"
print(a)
print(b)

a = [1, 2, 3, [4, 5]]
b = a.copy() # shallow copy
c = copy.deepcopy(a) # deep copy
a[3][0] = 'abc'
print(a)
print(b)
print(c)
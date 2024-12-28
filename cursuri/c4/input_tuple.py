a = tuple(int(x.strip()) for x in input("Values: ").split())
print(a)
a = tuple(x**3 for x in a if x % 2 == 0)
print(a)
L = [30, 27, 111, 71, 101, 107, 12, 81, 202, 18]
b = sorted(L, key = lambda n: (sum([int(x) for x in str(n)]), n))
print(b)
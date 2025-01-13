def generator_patrate(n):
    x = 0
    while x < n:
        yield x**2
        x += 1
patrate = generator_patrate(10)

x = next(patrate, -1)
while x != -1:
    print(x)
    x = next(patrate, -1)

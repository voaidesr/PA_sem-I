def delta(a, b, c):
    return b*b - 4*a*c
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if delta(a, b, c) < 0:
    print("No real values")
elif delta(a, b, c) == 0:
    x = (-b)/(2*a)
    print(x)
else:
    x1 = (-b + delta(a, b, c))/(2*a)
    x2 = (-b - delta(a, b, c))/(2*a)
    print(x2, x1)
# Să se afișeze cel mai mic număr prim cuprins între două numere naturale a și
# b sau un mesaj corespunzător în cazul în care nu există niciun număr prim
# cuprins între a și b
import math
a = int(input("a = "))
b = int(input("b = "))

def prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    n_div = math.floor(math.sqrt(n))
    for i in range(3, n_div + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(a, b+1):
    if prime(i):
        print(f"{i} este numar prim")
        break
else:
    print(f"Intre {a} si {b} nu exista nici un numar prim")
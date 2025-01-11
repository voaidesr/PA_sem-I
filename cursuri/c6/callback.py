# transmitem o functie ca argument al altei functii
import math
def suma(n, fk):
    sum = 0
    for i in range(1,n+1):
        sum += fk(i)
    return sum

def f1(n):
    return 1/n

def f2(n):
    return n**2

n = 10
print(suma(n, f1))
print(suma(n, f2))
print(suma(n, math.exp))
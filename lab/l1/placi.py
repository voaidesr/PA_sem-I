from math import gcd
l1 = int(input("l1 = "))
l2 = int(input("l2 = "))
l = gcd(l1, l2)
number = l1*l2 // (l*l)
print(f"E nevoie de {number} placi de latime {l}")
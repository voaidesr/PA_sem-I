import math
a = int(input("a = "))
b = int(input("b = "))

# definim functie verificare prim
def prim(n):
    if(n == 2):
        return True
    if (n % 2 == 0 or n == 1):
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if(n % i == 0):
            return False
    else:
        return True

# aflam numerele prime intre a si b 
for i in range (a+1, b):
    if(prim(i)):
        print(f"{i} este cel mai mic numar prim")
        break
else:
    print("nu exista numere prime")
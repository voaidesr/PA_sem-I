def radn(n):
    def baza(numar):
        nonlocal n
        n = 1/n
        return numar**n
    return baza

def suman(n):
    def exp(b):
        nonlocal n
        sum = 0
        for i in range(1,b+1):
            sum += i**n
        return sum
    return exp

f = suman(2)
print(f(3))
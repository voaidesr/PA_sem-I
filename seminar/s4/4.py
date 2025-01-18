def generic(iterabil, property):
    sum = 0
    for i in iterabil:
        if property(i):
            sum += 1
    return sum

def par(x):
    return (x + 1)%2

def vocale(x):
    return x in "aeiou"

def pereche(x):
    return x[0] == x[1]

def verificate(y, t):
    def cmmdc(a, b):
        if b == 0:
            return a
        else:
            return cmmdc(b, a%b)
    
    def aux(x):
        return cmmdc(y, x) == t
    
    return aux


# functia trebuie sa aiba un singur parametru
# folosim functii imbricate 
def len_k(k):
    def sir(str):
        return len(str) == k
    return sir

def main():
    v = [1, 2, 3, 4, 5, 6, 7, 8]
    print(generic(v, par))
    str = "Numele meu"
    print(generic(str, vocale))
    p = [(0, 0), (1, 3), (4, 4), (5, 4), (7, 9)]
    print(generic(p, pereche))
    a = "Eu sunt robert si am lala".split()
    print(generic(a, len_k(8))) 
    L = [10, 142, 24, 17, 18, 100, 13, 15]
    print(generic(L, verificate(4, 2)))


if __name__ == "__main__":
    main()
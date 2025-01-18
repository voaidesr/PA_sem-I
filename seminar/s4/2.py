"""
Scrieți o funcție și un generator care primesc ca parametrii un număr variabil de liste
și o valoare 𝑥 și furnizează toate listele care conțin valoarea 𝑥.

"""
def cauta(*liste, x):
    rez = []
    for lista in liste:
        if x in lista:
            rez.append(lista)
    return rez

def generator(*liste, x):
    for lista in liste:
        if x in lista:
            yield lista
    return()


def main():
    x1 = [1, 2, 5, 7]
    x2 = [3, 7, 8, 9]
    x3 = [1, 9, 10, 20, 25]
    print(cauta(x1, x2, x3, x=1))
    print("Generator".center(30, "_"))
    print("Metoda 1:")
    for l in generator(x1, x2, x3, x=1):
        print(l)
    print("_".center(30, "_"))
    f = generator(x1, x2, x3, x=1)
    pas = next(f, None)
    if pas is None:
        print(f"Nicio lista nu contine valoare 1")
    else:
        while pas is not None:
            print(pas)
            pas = next(f, None)

if __name__ == "__main__":
    main()
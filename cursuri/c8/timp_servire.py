# ts este o lista de tipul (persoana, timp individual de servire)
# se afiseaza tabelar
def AfisareTimpi(ts):
    print("Persoana\tTimp de servire\tTimp de asteptare")
    # timp curent de asteptare
    tcrt = 0
    ttotal = 0

    for pers in ts:
        tcrt += pers[1]
        ttotal += tcrt
        print(str(pers[0]).center(len("Persoana")),
            str(pers[1]).center(len("Timp de servire")),
            str(tcrt).center(len("Timp de astepatre")), sep = "\t")
    print(f"Timpul mediu de asteptare: {round(ttotal/len(ts), 2)}") # rotunjim la doua zecimale

def main():
    aux = [int(x) for x in input("Timpii de asteptare: ").split()]
    # adaugam numar de ordine
    ts = [(i + 1, aux[i]) for i in range(len(aux))]

    # initial
    AfisareTimpi(ts)

    ts = sorted(ts, key = lambda x: x[1])
    AfisareTimpi(ts)

if __name__ == "__main__":
    main()
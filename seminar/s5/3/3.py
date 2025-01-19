def multime_acoperire(lst): # primim lista de intervale - echivalenta cu problema cuielor
    lst.sort(key = lambda x: x[1])  # x = (inceput, final) - sortam dupa final
    acoperire = []
    acoperire.append(lst[0][1])
    for x in lst[1:]:
        if x[0] <= acoperire[-1] <= x[1]:
            continue
        else:
            acoperire.append(x[1])
    return acoperire

def main():
     # lista in care tinem intervalele
    try:
        l = []
        with open("input.txt") as f:
            for line in f:
                beg, end = line.split()
                l.append((int(beg), int(end)))
        g = open("output.txt", 'w')
        g.write(" ".join(str(x) for x in multime_acoperire(l)))
    except FileNotFoundError:
        print("Fisierul nu exista!")

if __name__ == "__main__":
    main()
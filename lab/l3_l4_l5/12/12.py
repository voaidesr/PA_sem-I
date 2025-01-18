
def main():
    l = input()
    punctaje = []
    clas = {}
    k = 1
    while l != "-1":
        l = l.split()
        punctaje.append((int(l[0]), " ".join(l[1:]), k))
        k += 1
        l = input()
    print(punctaje)
    for entry in punctaje:
        if entry[0] not in clas:
            clas[entry[0]] = [(entry[1], entry[2])]
        else:
            clas[entry[0]] += [(entry[1], entry[2])]
    print(*set(clas.keys()))

if __name__ == "__main__":
    main()
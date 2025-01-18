magazine = {}

def get_coduri(file):
    try:
        with open(file) as f:
            global magazine
            semne = ",.;:'?!"
            l = [x.strip(semne) for x in f.readline().split()]
            while l != []:
                if l[0] not in magazine:
                    magazine[l[0]] = set(int(x)  for x in l[1:])
                else:
                    magazine[l[0]].extend(int(x)  for x in l[1:])
                l = [x.strip(semne) for x in f.readline().split()]
    except FileNotFoundError:
        print(f"Fisierul {f} nu exista")

def products_in_all():
    print(*set.intersection(*magazine.values()))

def all_products():
    print(*set.union(*magazine.values()))

def store_exclusive(key):
    global magazine
    import copy
    magazin = copy.deepcopy(magazine)
    for k in magazin:
        if k != key:
            magazin[key].difference_update(magazin[k])
    print(*magazin[key])

def main():
    file = "magazine.txt"
    global magazine
    get_coduri(file)
    products_in_all()
    all_products()
    store_exclusive('StoreA')
    print(magazine)

if __name__ == "__main__":
    main()
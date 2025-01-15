try:
    with open("numar_lipsa.txt") as f:
        line = f.readline().split()
        numbers = {int(x) for x in line}
        numbers2 = {x for x in range(1, len(line)+2)}
        print(*(numbers2 - numbers)) # scadera A-B are complexitate O(len(A))
        # complexitate computationala de O(n)
        # iar spatiu utilizat O(n)
except FileNotFoundError:
    print("Fisierul nu exista!")
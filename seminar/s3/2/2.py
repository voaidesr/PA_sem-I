"""
Fișierul text numere.txt conține numere naturale despărțite prin spații și scrise pe mai
multe linii. Să se scrie în fișierul text numere_comune.txt numerele care apar pe toate
liniile din fișier.

"""
fisier = "numere.txt"
try:
    with open(fisier) as f:
        actual_line = f.readline()
        precedent_set = set(actual_line.split())
        actual_set = set()
        while actual_line != "":
            actual_line = f.readline()
            actual_set = set(actual_line.split())
            if actual_set:
                precedent_set.intersection_update(actual_set)
            if not precedent_set:
                break
        # complexitate O(numar linii*len(linie))
        g = open("numere_comune.txt", 'w')
        g.write(" ".join(precedent_set))
        g.close()
except FileNotFoundError:
    print("Fisierul nu exista")
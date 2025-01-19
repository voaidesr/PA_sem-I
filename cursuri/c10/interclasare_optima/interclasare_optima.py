import queue
# functia pentru interclasarea a doua siruri sortate crescator 
def interclasare(a, b):
    rez = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i]  < b[j]:
            rez.append(a[i])
            i += 1
        else:
            rez.append(b[j])
            j += 1
    rez.extend(a[i:])
    rez.extend(b[j:])
    return rez

def main():
    siruri = queue.PriorityQueue()
    try:
        with open("liste.txt") as f:
            for line in f:
                lista = [int(x) for x in line.split()]
                siruri.put((len(lista), lista))
        # avem sirurile intr-un priority queue 
        # acum interclasam cele mai scurte 2 liste si le adaugam in pqueue
        while siruri.qsize() != 1:
            a = siruri.get()
            b = siruri.get()
            c = interclasare(a[1], b[1])
            siruri.put((len(c), c))
        interclasat = siruri.get()
        g = open('liste_out.txt', 'w')
        g.write(f"Sirul interclasat este:\n{' '.join(str(x) for x in interclasat[1])}")
        g.close()
    except FileNotFoundError:
        print("Fisierul nu exista")

if __name__ == "__main__":
    main()
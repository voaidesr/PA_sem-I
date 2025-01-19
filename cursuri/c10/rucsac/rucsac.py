if __name__ == "__main__":
    try:
        with open("in_rucsac.txt") as f:
            G = float(f.readline().strip())
            obiecte = []
            crt = 1
            for line in f: # iteram prin liniile fisierului
                aux = list(map(float, line.split()))
                obiecte.append((crt, aux[0], aux[1])) # triplete de forma (nr, greutate, castig)
                crt += 1
        obiecte.sort(key=lambda ob: ob[2]/ob[1], reverse=True) # sortam dupa costul unitar, descrescator 
        n = len(obiecte)
        x= [0] * n # solutia, mentine fractii
        spatiu_ramas = G
        for i in range(n):
            if obiecte[i][1] <= spatiu_ramas:
                x[i] = 1
                spatiu_ramas -= obiecte[i][1]
            else:
                x[i] = spatiu_ramas/obiecte[i][1]
                break
        castig = sum([x[i]*obiecte[i][2] for i in range(n)])
        g = open("out_rucsac.txt", "w")
        g.write(f"Castig maxim: {castig}\n")
        g.write("\nObiecte incarcate:\n")
        for i in range(n):
            if x[i] != 0:
                procent = format(x[i]*100, '.2f')
                g.write("Obiect" + str(obiecte[i][0]) + ": " + procent + "%\n")
        g.close()
    except FileNotFoundError:
        print("Fisierul nu exista")
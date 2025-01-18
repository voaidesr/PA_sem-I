def rime(fisier):
    try:
        with open(fisier) as f:
            semne = ",.?!;:-"
            cuvinte = [(x.strip(semne)).lower() for x in f.read().split()]
            rime = {}
            for w in cuvinte:
                if w[-1] not in rime:
                    rime[w[-1]] = [w]
                elif w not in rime[w[-1]]:
                    rime[w[-1]] += [w]
            g = open("rime.txt", 'w')
            for key in rime:
                if len(rime[key]) > 1:
                    g.write(f"{' '.join(rime[key])}\n")
            g.close()
    except FileNotFoundError:
        print(f"Fisierul {fisier} nu exista!")



def main():
    fisier = "text.txt"
    rime(fisier)

if __name__ == "__main__":
    main()
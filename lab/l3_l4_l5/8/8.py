def find_words(file, word):
    try:
        with open(file) as f:
            semne = ",.;:?!"
            fraza = [x.strip(semne) for x in f.readline().split()]
            litere = {}
            for w in fraza:
                l = frozenset(w)
                if l in litere:
                    if word not in litere[l]:
                        litere[l].append(w)
                else:
                    litere[l] = [w]
            l = frozenset(word)
            if l not in litere:
                return None
            else:
                return litere[l]
    except FileNotFoundError:
        print(f"Fisierul {file} nu exista")

def main():
    file = "fraza.txt"
    word = input("Cuvantul: ")
    cuvinte = find_words(file, word)
    if cuvinte is None:
        print(f"Nu exista cuvinte formate din aceleasi litere ca {word}")
    else: 
        print(f"Cuvintele formate din aceleasi litere ca {word} sunt: {', '.join(cuvinte)}")

if __name__ == "__main__":
    main()
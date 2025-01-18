def find_word(file):
    try:
        with open(file) as f:
            exp = {}
            phrases = f.read().split("\n")
            for ph in phrases:
                semne = ",./?;:"
                words = [x.strip(semne).lower() for x in ph.split()]
                exp[words[0]] = -1
                for w in words:
                    if w == words[0] or w == "~":
                        exp[words[0]] += 1
        return list(exp.items())

    except FileNotFoundError:
        print(f"Fisierul {file}  nu exista!")

def main():
    file = "dictionare.txt"
    print(find_word(file))

if __name__ == "__main__":
    main()
def deschide_fisier(nume_fisier):
    try:
        with open(nume_fisier) as f:
            line = f.readline()
            rezultat = []
            while line != "":
                parsed = [x.strip() for x in line.split(",")]
                aux = tuple([parsed[0], int(parsed[1]), tuple(int(x) for x in parsed[2:])])
                rezultat.append(aux)
                line = f.readline()
            return rezultat
    except FileNotFoundError:
        print(f"Fisierul {nume_fisier} nu exista!")
        return None
    
def situatie(studenti):
    updated_studenti = []
    for stud in studenti:
        if 0 in stud[2] or sum(stud[2]) // len(stud[2]) < 5:
            updated_studenti.append(stud + ("False",))
        else:
            updated_studenti.append(stud + ("True",))
    return updated_studenti

def key1(x):
    return x[1], x[0]

def key2(x):
    if x[-1] == "False":
        return 1, x[0]
    elif x[-1] == "True":
        return 0, x[0]

def key3(x):
    return (-sum(x[2]), x[1], x[0])

def key4(x):
    if x[-1] == "False":
        return x[1], 1, -sum(x[2]), x[0]
    elif x[-1] == "True":
        return x[1], 0, -sum(x[2]), x[0]
    
def main():
    nume_fisier = "nume.csv"
    studenti = deschide_fisier(nume_fisier)
    new_stud = situatie(studenti)
    print(sorted(new_stud, key=key4))

if __name__ == "__main__":
    main()
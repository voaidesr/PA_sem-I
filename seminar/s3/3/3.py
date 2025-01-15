# Fișierul text exemplu.txt conține un text pe mai multe linii, cuvintele fiind despărțite
# între ele prin spații și semnele de punctuație uzuale. Implementați un program care să
# scrie în fișierul text grupe_cuvinte.txt cuvintele distincte (fără duplicate) din fișierul dat,
# grupate după mulțimile de litere din care sunt formate (nu se va face distincție între
# literele mari și cele mici). Grupele se vor scrie în fișier în ordinea descrescătoare a
# numărului de elemente din mulțimile literelor, în fiecare grupă literele se vor scrie in ordine crescatoare
try: 
    with open("exemplu.txt") as f:
        semne_de_punctuatie = ",.:;?!"
        text = [x.strip(semne_de_punctuatie) for x in f.read().split()]
        grupe = {}
        for word in text:
            litere = "".join(sorted({x.lower() for x in word}))
            # cheile unui dictionar trebuie sa fie imutabile 
            # fie folosesti string (cum am folosit)
            # daca vrei sa folosesti multime --> frozenset
            if litere in grupe:
                if(word.lower() not in grupe[litere]):
                    grupe[litere].append(word.lower())
            else:
                grupe[litere] = [word.lower()]
        grupe_sortate = sorted(grupe, key=lambda x: (-len(x), x))
        g = open('grupe_cuvinte.txt', 'w')
        for grupa in grupe_sortate:
            g.write(f"Literele {grupa}: {', '.join(sorted(grupe[grupa]))}\n")
        g.close()
except FileNotFoundError:
    print("Fisierul nu exista!")
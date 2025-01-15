# Fișierul text exemplu.txt conține un text pe mai multe linii, cuvintele fiind despărțite
# între ele prin spații și semnele de punctuație uzuale. Implementați un program care să
# scrie în fișierul text grupe_cuvinte.txt cuvintele distincte (fără duplicate) din fișierul dat,
# grupate după lungimile lor. Grupele se vor scrie în fișier în ordinea descrescătoare a lungimilor cuvintelor, iar în fiecare grupă cuvintele vor fi scrise în ordine alfabetică.

try:
    with open("exemplu.txt") as f:
        punctuatie = ".,:;?!"
        text = [x.strip(punctuatie) for x in f.read().split()]
        grupe = {}
        for word in text:
            if len(word) in grupe:
                if word.lower() not in grupe[len(word)]:
                    grupe[len(word)].append(word.lower())
            else:
                grupe[len(word)] = [word.lower()]
        g = open("grupe_cuvinte.txt", 'w')
        for i in sorted(grupe, reverse= True):
            line = f"Lungime {i}: {', '.join(sorted(grupe[i]))}\n"
            g.write(line)
        g.close()
except FileNotFoundError:
    print("Fisierul nu exista")
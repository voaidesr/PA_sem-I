f = open("text.txt")
cont = f.read()
for l in ".,?!":
    cont = cont.replace(l, " ")
cuvinte = cont.split()
for cuvant in set(cuvinte):
    n_cuv = cuvinte.count(cuvant)
    print(f"Cuvantul {cuvant} apare de {n_cuv} ori")
f.close()
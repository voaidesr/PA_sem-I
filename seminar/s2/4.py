"""
Considerăm un șir de caractere reprezentând un titlu în limba engleză. Să se formateze
titlul respectiv conform următoarelor reguli:
1. Prima literă a fiecărui cuvânt trebuie să fie majusculă.
2. Restul literelor din fiecare cuvânt trebuie să fie minuscule.
3. Cuvintele de legătură (de exemplu, 'and', 'or', 'but', 'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with') trebuie să fie minuscule, cu excepția cazului în care sunt primul sau ultimul cuvânt din titlu.

"""
titlu = input("Titlu: ").split()
cuvinte_legatura = ['and', 'or', 'but', 'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', "a", "an", "by", "on", "in", "at", "to", "for", "ago", "the", "past", "over", "into", "onto"]
for i in range(len(titlu)):
    if titlu[i] not in cuvinte_legatura:
        titlu[i] = titlu[i].capitalize()
titlu[-1] = titlu[-1].capitalize()
titlu[1] = titlu[1].capitalize()
print(" ".join(titlu))
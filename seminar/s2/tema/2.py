"""
Se citește o propoziție sau o frază în care cuvintele sunt despărțite între ele prin spații
și semnele de punctuație uzuale. Să se afișeze numărul cuvintelor distincte din propoziția
sau fraza dată. De exemplu, în propoziția "Ana are prune și gutui verzi, dar mai
multe prune decât gutui!" sunt 10 cuvinte distincte (cuvintele "prune" și "gutui"
se iau în considerare o singură data, deși apar de câte două ori în propoziție).

"""
punctuation = ",.?!;:"
propozitie = [word.strip(punctuation) for word in input().split()]
propozitie = set(propozitie)
print(len(propozitie))
"""
Să se afișeze numărul de litere mici, litere mari și semne de punctuație dintr-o
propoziție citită de la tastatură.

"""
from string import ascii_lowercase as al
from string import ascii_uppercase as au
semne = ",.;:?!"
prop = input()
lowercase = 0
uppercase = 0
punctuation = 0
for l in prop:
    if l in al:
        lowercase += 1
    elif l in au:
        uppercase += 1
    elif l in semne:
        punctuation += 1
print(f"Propozitia are {lowercase} litere mici, {uppercase} litere mari si {punctuation} semne de punctuatie")
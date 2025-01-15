"""
Reads a sentence or phrase where words are separated by spaces and usual punctuation marks.
Displays all distinct words of maximum length from the given sentence or phrase.
For example, in the sentence "Ana are prune și gutui verzi, dar mai multe prune decât gutui!",
the distinct words of maximum length, equal to 5, are: "prune", "gutui", "verzi", "multe", and "decât".

"""
semne_punctuatie = ".,:;?!"
propozitie = [word.strip(semne_punctuatie) for word in input().split()]
propozitie = sorted(propozitie, key=lambda w: len(w), reverse=True)
max_len= [word for word in propozitie if len(word) == len(propozitie[0])]
max_len = ", ".join(max_len)
print(f"Lungimea maxima a unui cuvant este {len(propozitie[0])}, iar aceste cuvinte sunt: '{max_len}'.")
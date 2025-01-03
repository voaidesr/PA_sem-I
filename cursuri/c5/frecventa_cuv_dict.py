f = open("text.txt")
cont = f.read()
for l in ".,?!":
    cont = cont.replace(l, " ")
cuvinte = cont.split()
word_counter = {}
for word in cuvinte:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
for word in word_counter:
    print(f"Cuvantul {word} apare de {word_counter[word]}")
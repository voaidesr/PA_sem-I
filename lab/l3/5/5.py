text = input().split()
words = {}
for word in text:
    if word.lower() in words:
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1
frecv = {}
for word in words:
    if words[word] in frecv:
        frecv[words[word]].append(word)
    else:
        frecv[words[word]] = [word]
max_app = max(frecv)
max_word = min(frecv[max_app])
min_app = min(frecv)
min_word = min(frecv[min_app])
print(f"Cuvantul care apare de cele mai multe ori e: {max_word} iar cel care apare de cele mai putine e: {min_word}")
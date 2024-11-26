text = input("text: ").strip()
s = input("cuvantul s: ").strip()
t = input("cuvantul t: ").strip()
words = text.split(" ")
for i in range(len(words)):
    if words[i] == s:
        words[i] = t
text = " ".join(words)
print(text)
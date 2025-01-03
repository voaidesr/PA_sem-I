fraza = input().strip()
s = input("cuvant de inlocuit: ").strip()
t = input('cuvantul cu care inlocuim: ').strip()    

cuvinte = fraza.split()
replace = []
for word in cuvinte:
    if word.lower() == s:
        replace.append(t)
    else:
        replace.append(word)

fraza = " ".join(replace)
print(fraza)
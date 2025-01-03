w1 = input("primul cuvant: ").strip()
w2 = input("al doilea cuvant: ").strip()

for letter in w1:
    if letter in w2:
        index = w2.index(letter)
        w2 = w2[:index]+w2[index+1:]
    else:
        print("Nu sunt anagrame")
        break
else:
    print("Sunt anagrame")
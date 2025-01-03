dialog = input().strip()
replici = dialog.split("$")

valori = []
for i in range(1, len(replici)):
    valoare = ""
    for chr in replici[i]:
        if chr.isnumeric():
            valoare += chr
    valori.append(valoare)

print(f"Valoarea 1 este {valori[0]} iar valoarea 2 este {valori[1]}")

for i in range(len(valori) - 1):
    if valori[i] == valori[i+1]:
        print("S-au inteles!")
        break
else:
    print("Nu s-au inteles")
T = []

while True:
    linie = input()
    if len(linie) != 0:
        T.append([int(x) for x in linie.split()])
    else:
        break

for linie in T:
    for x in linie:
        print(x, end=" ")
    print()
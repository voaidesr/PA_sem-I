frecv = {}
with open("text.txt") as f:
    content = f.read()
    spaces = "  \n"
    for c in content:
        if c in spaces:
            continue
        elif c in frecv:
            frecv[c] += 1
        else:
            frecv[c] = 1
for c in frecv:
    print(f"Caracterul {c} apare de {frecv[c]} ori")
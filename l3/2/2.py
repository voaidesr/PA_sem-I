test = 1
with open("test.in") as f:
    g = open("test.out", 'w')
    s = f.readline()
    while s != "":
        a, b = s.split('*')
        a = int(a)
        b, c = b.split("=")
        b = int(b)
        c = int(c)
        if a*b == c:
            g.write(f"{a}*{b}={c} Corect\n")
            test += 1
        else:
            g.write(f"{a}*{b}={c} Gresit {a*b}\n")
        s = f.readline()
    g.write(f"Nota {test}")



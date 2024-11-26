out_file = open("l3/date2.out", "w")
in_file = open("l3/date2.in", "r")
nota = 1
for line in in_file:
    x = line.strip()
    a = int(x.split('*')[0])
    b = int(x.split('*')[1].split('=')[0])
    c = int(x.split('=')[1])
    rez = a * b
    if rez == c:
        out_file.write(f"{x} Corect\n")
        nota += 1
    else:
        out_file.write(f"{x} Gresit {rez}\n")
out_file.write(f"Nota {nota}")
out_file.close()
in_file.close()
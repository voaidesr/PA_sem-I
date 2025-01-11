def student_sort(a):
    return int(a[1]), -a[2], a[0]
L = [( "Popescu Ion", 131, 9.25),
( "Ionescu Ana", 133, 8.75),
( "Popa Marian", 131, 9.85),
( "David Maria", 132, 8.95),
("Gheorghe Ana", 131, 9.85),
("Popescu Anca", 132, 9.15),
("Corbu Florin", 133, 8.05),
("Gheorghe Dan", 132, 9.15)]

print(sorted(L, key=student_sort))
import time 

numar = 10000
list = []

# initializam lista
start = time.time()
list = [x for x in range(numar)]
stop = time.time()
print(" Initializare: ", stop - start, "s")
list = []

# metoda append
start = time.time()
for x in range(numar):
    list.append(x)
stop = time.time()
print(" Append: ", stop - start, "s")
list = []

# metoda +=
start = time.time()
for x in range(numar):
    list += [x]
stop = time.time()
print(" +=: ", stop - start, "s")

# metoda +
start = time.time()
for x in range(numar):
    list = list + [x]
stop = time.time()
print(" +: ", stop - start, "s")
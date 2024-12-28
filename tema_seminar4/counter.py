with open("input.txt", "r") as f:
    s = f.readline()
    counter = 0
    while s != "":
        s = s.strip().split()
        for x in s:
            counter += 1
        s = f.readline()
print(counter)
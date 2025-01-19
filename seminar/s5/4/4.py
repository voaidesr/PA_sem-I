def main():
    l = []
    with open("intervale.txt") as f:
        for line in f:
            beg, end = line.split()
            l.append((int(beg), int(end)))
    
    # sortam dupa begin si descrescator dupa end, pentru intervalele care au acelasi inceput
    l.sort(key = lambda x: (x[0], -x[1]))
    
    rez = [] # list intersectiilor
    rez.append(list(l[0]))

    for interval in l[1:]:
        if interval[1] <= rez[-1][1]:
            continue
        if interval[0] <= rez[-1][1]:
            rez[-1][1] = interval[1]
        else:
            rez.append(list(interval))

    with open("output.txt", 'w') as g:
        g.write("Intervalele sunt:\n")
        g.write("\n".join([str(x) for x in rez]))
        g.write(f"\nLungimea reuniunii este {sum([x[1]-x[0] for x in rez])}")
if __name__ == "__main__":
    main()
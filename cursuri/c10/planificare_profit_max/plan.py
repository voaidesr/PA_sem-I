import queue

def main():
    p = []
    n = 0
    try:
        with open("input.in") as f:
            for file in f:
                n += 1
                name, dead_line, profit = file.split()
                p.append((-int(profit), int(dead_line), name))
        p.sort(key = lambda x: (-x[1], x[0]))
        print(p)
        n = max([x[1] for x in p])

        res = {k:None for k in range(1, n+1)}

        prog = queue.PriorityQueue()
        k = 0 # ca sa iteram
        profit = 0
        for zcrt in range(n, 0, -1):
            while k < n-1 and p[k][1] == zcrt:
                prog.put(p[k])
                k += 1

            if prog.qsize() > 0:
                res[zcrt] = prog.get()
                profit += abs(res[zcrt][0])
        with open("proiecte.out", 'w') as g:
            g.write(f"Profitul maxim este: {profit}\nIar proiectele sunt programate astfel:\n")
            for key, val in res.items():
                if val is not None:
                    g.write(f"Ziua {key}: proiectul {val[2]}\n")
    except FileNotFoundError:
        print("Fisierul nu exista!")

# aici greedy-ul e optim (proof by exchange argument) dar implementarea nu e O(n**2)
# pentru implementare optima O(nlog2n) vezi in cursuri, curs 10 
if __name__ == "__main__":
    main()
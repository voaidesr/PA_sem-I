def main():
    p = []
    try:
        with open("proiecte.in") as f:
            for file in f:
                name, dead_line, profit = file.split()
                p.append((name, int(dead_line), int(profit)))
        p.sort(key = lambda x: -x[2])

        zi_max = max([x[1] for x in p])
        res = {key:None for key in range(1, zi_max+1)}

        p_maxim = 0
        
        for x in p:
            for k in range(x[1], 0, -1):
                if res[k] is None:
                    res[k] = x
                    p_maxim += x[2]
                    break
        
        with open("proiecte.out", 'w') as g:
            g.write(f"Profitul maxim este: {p_maxim}\nIar proiectele sunt programate astfel:\n")
            for key, val in res.items():
                if val is not None:
                    g.write(f"Ziua {key}: proiectul {val[0]}\n")
    except FileNotFoundError:
        print("Fisierul nu exista!")

# aici greedy-ul e optim (proof by exchange argument) dar implementarea nu e O(n**2)
# pentru implementare optima O(nlog2n) vezi in cursuri, curs 10 
if __name__ == "__main__":
    main()
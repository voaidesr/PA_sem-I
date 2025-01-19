# pbinfo #91

def main():
    file_in = "masini.in"
    file_out = "masini.out"
    try: 
        with open(file_in) as f:
            n, c = [int(x) for x in f.readline().split()]
            timpi = [int(x) for x in f.readline().split()]
            timpi.sort()
            counter = 0
            for i in range(n):
                if timpi[i] <= c:
                    counter += 1
                    c -= timpi[i]
                else:
                    break
        with open(file_out, 'w') as g:
            g.write(str(counter))
    except FileNotFoundError:
        print("NU")
if __name__ == "__main__":
    main()
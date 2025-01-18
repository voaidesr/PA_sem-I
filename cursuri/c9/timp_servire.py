def main():
    file_in = "input.txt"
    file_out = "output.txt"
    try:
        with open(file_in) as f:
            lsp = [] # memoram spectacolele in ordine (index, begin_time, end_time)
            i = 1
            line = f.readline()
            while line != "":
                beg, end = line.split("-")
                lsp.append((i, beg.strip(), end.strip()))
                line = f.readline()
                i += 1
            # sortam spectacolele dupa end_time
            lsp = sorted(lsp, key = lambda x : x[2])

            prog_spect = [] # aici mentinem programarea optima a spectacolelor
            prog_spect.append(lsp[0])

            for spect in lsp[1:]: # parcurgem restul spectacolelor
                if spect[1] > prog_spect[-1][2]: # vedem daca spectacolul spect incepe dupa terminarea ultimului spectacol programat
                    prog_spect.append(spect)

            g = open(file_out, 'w')
            g.write(f"Se pot programa maxim {len(prog_spect)} spectacole\n")
            for s in prog_spect:
                g.write(f"{s[1]}-{s[2]} Spectacolul {s[0]}\n")
    except FileNotFoundError:
        print(f"Fisierul {file_in} nu exista!")

if __name__ == "__main__":
    main()
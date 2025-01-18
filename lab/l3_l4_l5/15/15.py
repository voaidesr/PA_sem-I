from pprint import pprint

def main():
    file = "persoane.in"
    date = []
    try:
        with open(file) as f:
            line = f.readline()
            while line != "":
                pers = {}
                nume, prenume, adresa = line.strip().split(",", 2)
                
                for item in [nume, prenume]:
                    key, val = item.split(":")
                    pers[key.strip()] = val.strip()
                
                key, val = adresa.split(":{")
                key = key.strip()
                val = val.strip("}\n")
                dict2 = {a.strip(): b.strip() for a, b in (x.split(":") for x in val.split(","))}
                pers[key] = dict2
                
                date.append(pers)
                line = f.readline()
            pprint(date)
            orase = {}
            for pers in date:
                if pers["adresa"]["oras"] not in orase:
                    orase[pers["adresa"]["oras"]] = [pers["nume"]+ " " + pers["prenume"]]
                else: 
                    orase[pers["adresa"]["oras"]] += [pers["nume"] + " " + pers["prenume"]]
            pprint(orase)
    except FileNotFoundError:
        print(f"Fisierul {file} nu exista!")

if __name__ == "__main__":
    main()
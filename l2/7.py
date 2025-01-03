def bisect(an):
    if an % 4 != 0:
        return False
    elif an % 100 == 0 and an % 400 != 0:
        return False
    else:
        return True

def zi(data):
    zile_saptamana = [
        "duminica",
        "luni",
        "marti",
        "miercuri",
        "joi",
        "vineri",
        "sambata"
    ]

    zi, luna, an = map(int, data.split())

    zile_luni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(bisect(an)):
        zile_luni[1] = 29
    
    # total zile de la 1 ian 1702
    total = 0

    for year in range(1702, an):
        total += 366 if bisect(year) else 365

    for month in range(1, luna):
        total += zile_luni[month - 1]

    total += zi - 1

    zi_sapt = total % 7

    return zile_saptamana[zi_sapt]

data = input()
print(zi(data))
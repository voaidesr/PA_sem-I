def perechi_suma(list, S):
    rez = []
    i = 0
    j = len(list)-1
    while i < j:
        if list[i]  + list[j] < S:
            i += 1
        elif list[i] + list[j] > S:
            j -= 1
        if list[i] + list[j] == S:
            rez.append((list[i], list[j]))
            i += 1
            j -= 1
    return rez

def main():
    v = [2, 5, 7, 8, 10, 12, 15, 17, 25]  
    s = 20
    print(*perechi_suma(v, s))

if __name__ == "__main__":
    main()
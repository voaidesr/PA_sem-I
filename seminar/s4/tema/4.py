def functie_len(n, *siruri):
    rez = ()
    for s in siruri:
        if len(s) == n:
            rez += (s,)
    return rez

def generator(n, *siruri):
    for s in siruri:
        if len(s) == n:
            yield s

def main():
    siruri = ["ab", "abcd", "mals", "ilom", "abcdef", "abcdefgh", "abcdefghij"]
    result = functie_len(4, *siruri)
    print(result)
    print()
    f = generator(4, *siruri)
    n = next(f, None)
    if n is None:
        print(f"Nu exista")
    else:
        while n is not None:
            print(n, end=" ")
            n = next(f, None)

if __name__ == "__main__":
    main()

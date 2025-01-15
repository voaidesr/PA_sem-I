"""
Scrieți o funcție care verifică dacă două șiruri de caractere sunt anagrame sau nu
utilizând un singur vector de frecvențe.

Parametri:
- s1 (str): Primul șir de caractere.
- s2 (str): Al doilea șir de caractere.

Returnează:
- bool: True dacă șirurile de caractere sunt anagrame, False în caz contrar.

"""
def anagrame(s1, s2):
    f = [0] * 26
    for l in s1:
        f[ord(l) - ord("a")] += 1
    for l in s2:
        f[ord(l) - ord("a")] += -1
    for i in f:
        if i != 0:
            return False
    return True

def main():
    s1 = input().strip()
    s2 = input().strip()
    print(anagrame(s1, s2))

if __name__ == "__main__":
    main()
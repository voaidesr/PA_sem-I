"""
Verifică dacă două șiruri de caractere formate doar din litere mici sunt anagrame sau nu.

Două șiruri sunt anagrame dacă sunt formate din aceleași litere, dar așezate în altă ordine 
(sau, echivalent, unul dintre șiruri se poate obține din celălalt printr-o permutare a caracterelor sale).

De exemplu, șirurile "emerit" și "treime" sunt anagrame, dar șirurile "emerit" și "treimi" nu sunt.

"""
def anagrame(a, b):
    if set(a) != set(b):
        print(f"{a} si {b} nu sunt anagrame")
        return()
    else:
        litere_a = {}
        litere_b = {}
        for l in a:
            if l in litere_a: # O(1)
                litere_a[l] += 1 # O(1) - dar depinde de performanta functiei de dispersie, nu e cea mai stabila varianta
            else:
                litere_a[l] = 1
        for l in b:
            if l in litere_b:
                litere_b[l] += 1
            else:
                litere_b[l] = 1
        if litere_a == litere_b:
            print(f"{a} si {b} sunt anagrame")
        else:
            print(f"{a} si {b} nu sunt anagrame")
        # Complexitatea de timp este O(max(len(a), len(b))) - adica O(n)
        # Complexitatea de spatiu este O(len(a) + len(b))

def main():
    a = input()
    b = input()
    anagrame(a, b)

if __name__ == "__main__":
    main()
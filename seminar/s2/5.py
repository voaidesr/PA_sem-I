"""
Se citește un șir de caractere 𝑠. Să se verifice dacă există un șir 𝑠', diferit de 𝑠, astfel încât
șirul 𝑠 să se poată obține prin concatenarea de un număr arbitrar de ori 𝑘 a șirului 𝑠'.
De exemplu, pentru 𝑠 = "𝑎𝑎𝑏𝑎𝑎𝑏𝑎𝑎𝑏" avem 𝑠' = "𝑎𝑎𝑏" și 𝑘 = 3.

"""
def subsir(s):
    # sirul va fi intotdeauna un prefix
    # lungimea sirului va fi intotdeauna un divizor al sirului s
    # va fi mereu <= len(s)//2
    for i in range(1, len(s)//2 + 1):
        if len(s) % i == 0:
            t = s[:i]
            if t*(len(s)//i) == s:
                return t, len(s)//i
        else:
            continue
    return "", 0

s = input()
a, b = subsir(s)
print(a, b)
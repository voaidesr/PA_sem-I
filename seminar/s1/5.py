"""
Se citește un șir format din cel puțin 3 numere naturale cu proprietatea că fiecare
valoare distinctă apare de exact două ori în șir, mai puțin una care apare o singură dată.
Să se afișeze valoarea care apare o singură dată în șir. De exemplu, în șirul 100, -7, 20, 20,
1, -7, 1, 3, 100 valoarea 3 apare o singură dată.
"""
def single_element(v):
    x = 0
    for i in v:
        x ^= i
        # parcurge tot - complexitatea este O(n)
    return x
v = [int(x) for x in input().split()]
print(single_element(v))
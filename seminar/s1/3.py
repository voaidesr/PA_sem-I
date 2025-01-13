# sa se determine numarul de biti nenuli
def nenul(n):
    k = 0
    while n:
        n = n & (n-1)
        k += 1
        # maxim, daca toti bitii sunt 1, are complexitate O(log2n)
    return k
a = 1024
print(f"Numarul {a} are {nenul(a)} biti nenuli")
# sa se verifice daca un numear n este de forma 2^k si sa se returneze exponentul k
# simplu
def putere2(n):
    k = 0
    while n & 1 == 0:
        # lungimea lui n in binar e 1 + [log2n]
        # algoritmul are complexitate O(log2n)
        n = n >> 1
        k += 1
    if n == 1:
        print("Este putere a lui 2")
        return k
    else:
        print("Nu este putere")
        return
a = putere2(24)
print(a)
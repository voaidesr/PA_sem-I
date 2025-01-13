import math
def putere2(n):
    if n & (n-1) == 0:
        print(f"{n} este 2**{int(math.log2(n))}")
        # logaritmul este foarte rapid in limbajele moderne
        # se considera solutia de complexitate O(1)
    else:
        print(f"{n} nu este o putere a lui 2")
putere2(24)

# sa se gaseasca secventa maxima a unei secvente de biti egali cu 1
# 0b01011101101000
# 0b10111011010000 shift left o data
# 0b00011001000000 and - din fiecare secventa de biti este eliminat un 1 
def longest_bit_seq(n):
    k = 0
    while n:
        n = n & (n << 1)
        k += 1
    return k
    # complexitate data de lungimea maxima
    # maxim in O(log2n)
a = 40
print(f"Cea mai lunga secventa de biti de 1 ai lui {a} este {longest_bit_seq(a)}")
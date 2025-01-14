"""
Fie k un număr natural. Să se determine cea mai mică putere a lui 2 mai mare sau egală
decât numărul k.

"""
def putere2(k):
    # 0b0100000   
    # 0b0011111
    # 000000000
    # 111111111
    if k & (k - 1) == 0:
        return k
    p = 1
    while p < k:
        p = p << 1
    return p
k = int(input("k = "))
print(putere2(k))



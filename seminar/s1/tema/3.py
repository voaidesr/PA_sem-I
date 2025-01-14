"""
Calculate the number of bits in the binary representation of a number `x` that need to be flipped to obtain the number `y`.

Args:
    x (int): A non-zero natural number.
    y (int): Another non-zero natural number.

Returns:
    int: The number of bits that need to be flipped.

Example:
    x = 29 (11101 in binary)
    y = 15 (01111 in binary)
    The number of bits that need to be flipped is 2.

Note:
    The solution involves calculating the number of set bits (1s) in the number `t = x ^ y`.
"""
x = int(input("x = "))
y = int(input("y = "))
x_xor_y = x ^ y
n = 0
# daca un numar are 101100
# nr - are 101011 - operatorul si imi elimina cate un bit
while x_xor_y:
    x_xor_y &= (x_xor_y - 1)
    n += 1
print(f"Trebuie comutati {n} biti din {x} pentru a-l obtine pe {y}")
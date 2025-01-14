"""
Determine efficiently the number of zero bits in the binary representation of a non-zero natural number.
For example, the binary representation of the number 600 is 0b1001011000 and contains 6 zero bits.

Args:
    num (int): A non-zero natural number.

Returns:
    int: The number of zero bits in the binary representation of the input number.
"""
import math
def nr_biti_0(n):
    k = math.floor(math.log2(n)) + 1
    mb = (1 << k) - 1
    n ^= mb
    # we flipped the bits of n
    number = 0
    while n:
        n &= (n-1)
        number += 1
    return number

print(nr_biti_0(600))
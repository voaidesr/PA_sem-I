"""
Reads n - 2 distinct natural numbers from the first k natural numbers.
Displays the missing numbers x and x'.

"""
n = int(input("n = "))
v = [int(x) for x in input("Values: ").split()]
x_xor_y = 0
for i in v:
    x_xor_y ^= i
for i in range(1, n+1):
    x_xor_y ^= i
# at this point x_xor_y = x^y 
# x != y, deci x^y != 0 deci x^y va avea un bit nenul ---> exista cel putin un bit care e diferit la x fata de y
# mb - masca binara
mb = x_xor_y & (~(x_xor_y-1))
# ex: 
#   x_xor_y = 0b1011000
#  x_xor_y_1= 0b1010111
# ~x_xor_y-1= 0b0101000
# and =       0b0001000 masca binara tine doar primul bit din numar care este setat 
x = 0
for i in range(1, n+1):
    if i & mb:
        x ^= i
for i in v:
    if i & mb:
        x ^= i
print(f"Numerele lipsa sunt {min(x_xor_y^x, x)} si {max(x_xor_y^x, x)}")
    
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import random 
# ascii_lowerase = "abcd...z"

def gen_password():
    digits = "0123456789"
    password = ""
    password += uc[random.randint(0, len(uc)-1)]
    for _ in range(3):
        password += lc[random.randint(0, len(lc) - 1)]
    for _ in range(4):
        password += digits[random.randint(0, len(digits)-1)]
    return password

f = open("date.in")
g = open("date.out", 'w')
s = f.readline()
while s != "":
    linie = s.split()
    mail = f"{linie[1].lower()}.{linie[0].lower()}@email.com"
    linie = f"{mail}, {gen_password()}\n"
    g.write(linie)
    s = f.readline()
f.close()
g.close()
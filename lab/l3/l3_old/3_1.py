from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import random
def gen_password():
    digits = "0123456789"
    parola = ""
    parola += uc[random.randint(0, len(uc)-1)]
    for i in range(3):
        parola += lc[random.randint(0, len(lc)-1)]
    for i in range (4):
        parola += random.choice(digits)
    return parola
out_file = open ("l3/date.out", "w")
with open("l3/date.in", "r") as in_file:
    for line in in_file:
        nume, prenume = line.strip().split()
        email = f"{prenume.lower()}.{nume.lower()}@myfmi.unibuc.ro"
        parola = gen_password()
        out_file.write(f"{email},{parola}\n")
out_file.close
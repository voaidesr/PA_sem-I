# Din numărul 4 se poate obține orice număr natural nenul aplicând în mod repetat următoarele operații:
# 1. împărțirea numărului la 2;
# 2. adăugarea cifrei 4 la sfârșitul numărului;
# 3. adăugarea cifrei 0 la sfârșitul numărului.

# ca sa obtinem operatiile, aplicam operatii inverse
def step_back(n):
    if n != 4:
        if n % 10 == 4 or n % 10 == 0:
            step_back(n//10)
        else:
            step_back(n*2)
        print (" -> ", n, end=" ")
    else:
        print("4", end = " ")

step_back(133)
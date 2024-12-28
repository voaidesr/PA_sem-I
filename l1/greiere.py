x = int(input("Lungimea initiala = "))
n = int(input("Numarul de sarituri  = "))
p = int(input("Procentul cu care scade dupa n sarituri = "))
m = int(input("Numarul total de sarituri = "))
distance = 0
counter = 0
for _ in range(m):
    distance += x
    counter += 1
    if counter == n:
        counter = 0
        x *= (1 - p/100)
print(distance)
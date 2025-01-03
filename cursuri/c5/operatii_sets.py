a = set([1, 2, 3, 3, 3, 4, 2, 1, 1])
b = {x%6 for x in range(8, 100)}

print(a < b) # incluziune, <= inclus egal
print(a | b) # reuniune
print(a & b) # intersectie
print(a ^ b) # diferenta simetrica
print(b - a) # diferenta
print(a)
print(b)
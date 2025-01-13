# 1. Să se interschimbe valorile a două variabile de tip întreg folosind operatorul ^ (XOR/"sau exclusiv" pe biți).
x = 15
y = 20
x = x^y
y = x^y
x = x^y
print(x, y)

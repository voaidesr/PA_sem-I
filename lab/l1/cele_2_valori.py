n = int(input())
x1 = "not_found"
x2 = "not_found"
for _ in range(n):
    a = int(input())
    if x1 == "not_found":
        x1 = a
    elif a > x1:
        x1, x2 = a, x1
    elif x2 == "not_found" and a != x1:
        x2 = a
if(x1 == "not_found" or x2 == "not_found"):
    print("Impossible")
else:
    print(x2, x1)
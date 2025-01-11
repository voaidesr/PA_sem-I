cifre = list(input().strip())
cifre.sort(reverse=True)
max = "".join(cifre)
cifre.sort()
# eliminam toate zero-urile 
while True:
    if '0' in cifre:
        cifre.remove('0')
    else:
        break
min = "".join(cifre)
print(min, max)
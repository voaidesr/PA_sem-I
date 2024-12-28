def palindrom(n):
    n.strip()
    if n == n[::-1]:
        return True
    else:
        return False
f = open("palindrom.in")
g = open("palindrom.out", 'w')
n = int(f.readline().strip())
for _ in range(n):
    word = f.readline().strip()
    if palindrom(word):
        g.write('1\n')
    else:
        g.write('0\n')
f.close()
g.close()
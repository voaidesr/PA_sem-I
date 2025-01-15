
def anagrame(s1, s2):
    f = [0] * 26
    for l in s1:
        f[ord(l) - ord("a")] += 1
    for l in s2:
        f[ord(l) - ord("a")] += -1
    for i in f:
        if i != 0:
            return False
    return True

def permutare(s1, s2):
    p = {}
    for i in range(len(s1)):
        index = s2.find(s1[i])
        p[i+1] = index+1
        s2 = s2[:index] + " " + s2[index+1:]
    return p

def print_permutare(p):
    for i in p:
        print(i, end=" ")
    print()
    for i in p:
        print(p[i], end=" ")

def main():
    s1 = input().strip()
    s2 = input().strip()
    if anagrame(s1, s2):
        p = permutare(s1, s2)
        print_permutare(p)
    else:
        print(f"{s1} si {s2} nu sunt anagrame")

if __name__ == "__main__":
    main()
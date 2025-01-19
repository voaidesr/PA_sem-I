# algoritmul Boyer-Moore
def castigator(v):
    majoritar = 0
    avantaj = 0
    for i in v: 
        if avantaj == 0 and majoritar != i:
            majoritar = i
            avantaj = 1
        elif majoritar != i:
            avantaj -= 1
        elif majoritar == i:
            avantaj +=1 
    count = 0
    for i in v:
        if i == majoritar:
            count += 1
    if count >= len(v)//2 + 1:
        return majoritar
    else:
        return 0

# rezolva problema in O(n) fara sa ocupe spatiu 

def main():
    v = [1, 5, 5, 1, 1, 5]
    print(castigator(v))

if __name__ == "__main__":
    main()
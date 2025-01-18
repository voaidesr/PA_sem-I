def find_position(list, property):
    res = []
    for i in range(len(list)):
        if property(list[i]):
            res.append(i)
    return res

def checkanagrame(s):
    def anagrame(x):
        if sorted(x.lower()) == sorted(s.lower()):
            return True
        else:
            return False
    return anagrame

def checknat(n, s):
    def nat(x):
        if len(str(x)) != n:
            return False
        elif sum([int(i) for i in str(x)]) != s:
            return False
        else:
            return True
    return nat

def main():
    list = [1, -2, 3, -4, 5, 6]
    print(find_position(list, lambda x: True if x > 0 else False))
    prop = "Num, ini! F?"
    print(find_position(prop, lambda x: True if x in ",.?;:!" else False))
    prop = "Cal pe lac in alc de cal".split()
    print(find_position(prop, checkanagrame("cal")))
    list =[321, 1890, 800, 600, 809, 114]
    print(find_position(list, checknat(3, 6)))

if __name__ == "__main__":
    main()
        
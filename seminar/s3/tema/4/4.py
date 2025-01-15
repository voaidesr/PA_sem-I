def largest_num(dict):
    dict_copy = dict.copy()
    num = 0
    for i in sorted(dict, reverse=True):
        while dict_copy[i]:
            num *= 10
            num += int(i)
            dict_copy[i] -= 1
    return num

def smallest_num(dict):
    dict_copy = dict.copy()
    indices = sorted(dict_copy)
    num = 0
    if indices[0] == "0":
        num = int(indices[1])
        dict_copy[indices[1]] -= 1
    else:
        num = int(indices[0])
        dict_copy[indices[0]] -= 1
    for i in indices:
        while dict[i]:
            num *= 10
            num += int(i)
            dict[i] -= 1
    return num
    
def main():
    try:
        with open('numere.txt') as f:
            cifre = {}
            for i in f.read().strip():
                if not i.isdigit():
                    continue
                if i in cifre:
                    cifre[i] += 1
                else:
                    cifre[i] = 1
        print(largest_num(cifre))
        print(smallest_num(cifre))
    except FileNotFoundError:
        print("Fisierul nu exista!")

if __name__ == "__main__":
    main()
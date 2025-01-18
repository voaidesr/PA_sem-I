def ieftinire(carti):
    updated_carti = carti.copy()
    for carte in updated_carti:
        if carte[2]  < 2000:
            carte[3] *= 0.8
    return updated_carti

def print_l(list):
    for i in list:
        print(*i, sep=" ")

def key1(x):
    return -x[2], x[0]

def key2(x):
    return len(x[1]) -x[3]

def key3(x):
    return x[1][0][1], x[1][0][0], x[0], x[2]

def main():
    list = [["Ana", [("Andrei", "Popescu"), ("Liviu", "Rebreanu")], 2001, 16],
            ["Ion", [("Liviu", "Rebreanu")], 1920, 30],
            ["Faust", [("Johann", "Goethe")], 1920, 40],
            ["Mara", [("Ioan", "Slavici"), ("Johann", "Goethe"), ("Johann", "Goethe")], 1920, 25],
            ["Enigma Otiliei", [("George", "Calinescu")], 1938, 35],
            ["Morometii", [("Aarin", "Popescu")], 1955, 45],
            ["Harry Potter", [("J.K.", "Rowling"), ("John", "Doe")], 2010, 50],
            ["Game of Thrones", [("George", "Martin"), ("Jane", "Smith")], 2007, 60]]
    print_l(sorted(ieftinire(list), key=key3))

if __name__ == '__main__':
    main()
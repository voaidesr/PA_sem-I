def op(string1, string2):
    if string1 == "" or string2 == "":
        return string1 + string2
    elif string1[-1] != string2[0]:
        return string1 + string2
    else:
        chr = string1[-1]
        string1 = string1.rstrip(chr)
        string2 = string2.lstrip(chr)
        return op(string1, string2)

sir1 = input().strip()
sir2 = sir1[::-1]

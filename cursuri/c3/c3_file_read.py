try:
    f = open("input.txt", "r")
    s = f.read()
    print(s)
except:
    print("file not found")
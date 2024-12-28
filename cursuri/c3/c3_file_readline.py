try: 
    f = open("input.txt")
    s = f.readline()
    while s != "":
        print(s, end = "")
        s = f.readline()
except:
    print("file not found")
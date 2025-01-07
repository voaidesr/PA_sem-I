with open("cheltuieli.txt") as f:
    text = f.read().split()
    numbers = []
    for word in text:
        if word[0].isdecimal() and '.' not in word:
            numbers.append(int(word))
        elif word[0].isdecimal():
            intr, dec = word.split('.')
            leng = len(dec)
            nr = int(intr)
            nr += (int(dec))*10**-leng
            numbers.append(nr)
    value = []
    for i in range(0,len(numbers),2):
        value.append(numbers[i]*numbers[i+1])
    print(sum(value))


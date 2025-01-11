num = input().strip().split()
num = [int(x) for x in num]
num = sorted (num, reverse=True)
print (num[0])
for i in range(len(num)):
    if(num[i] != num[0]):
        print(num[i])
        break
else:
    print("nu exista doua valori nedistincte")
fraza = input().strip().split()
numere = [int(x) for x in fraza if x.isnumeric()]
print(sum(numere))
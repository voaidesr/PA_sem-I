# https://cses.fi/problemset/task/1090 - Ferris Wheel
n, x = (int(x) for x in input().split())
weight = list(map(int, input().split()))
weight.sort()
numar_minim = 0
i = 0
j = n-1
# scriem conditia cand pozitiile sunt disjuncte
while(i < j):
    if(weight[i] + weight[j] <= x):
        numar_minim += 1
        i += 1
        j -= 1
    else:
        j -=1 
        numar_minim += 1
# verificam cazul cand sunt pe aceeasi pozitie
if(i == j):
    numar_minim += 1
print(numar_minim)
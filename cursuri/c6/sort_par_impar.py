def parity_sort(n):
    if n % 2 == 0:
        return 0, n
    else:
        return 1, -n
a = [0, 9, 3, 2, 1, 0, 7, 8, 4, 2]
print(sorted(a, key=parity_sort))
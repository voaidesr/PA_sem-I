import numpy as np
a = [[3, 7, -2], [8, 5, 9], [2, -4, 6]]
b = np.linalg.inv(a)
for i in a:
    for j in a[i]:
        print(a[i][j])
        print(" ")
    print("\n")
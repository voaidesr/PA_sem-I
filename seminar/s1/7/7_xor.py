"""
This function reads k-1 distinct natural numbers from the first k natural numbers and returns the missing number x.

Examples:
    - If the numbers read are 5, 1, 4, 2, then the missing number is x = 3.
    - If the numbers read are 1, 2, 3, 4, then the missing number is x = 5.
    - If the numbers read are 2, 3, 4, 5, then the missing number is x = 1.
"""
def missing_number(v, k):
    x = 0
    for i in range(1, k+1):
        x ^= i
    for i in v:
        x ^= i
    # complexitate de timp O(n)
    # complexitate de spatiu O(n) - s-ar putea implementa in O(1) daca nu am folosi vector 7
    return x
k = int(input())
v = [int(x) for x in input().split()]
print(f"The missing number is {missing_number(v,k)}")
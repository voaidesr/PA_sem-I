def shift(c, k):
    return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
text = input("text: ").strip()
k = int(input().strip())
result = ""
for c in text:
    if c == " ":
        result = result + c
    else:
        result += shift(c, k)
print(result)
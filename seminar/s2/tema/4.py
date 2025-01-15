# Implementati cifrul lui Cezar

def encrypt_letter(l, key):
    return chr((ord(l) - ord('a') + key) % 26 + ord('a'))

def encrypt_word(word, key):
    encrypted = ""
    for l in word:
        encrypted += encrypt_letter(l, key)
    return encrypted

a = "Robert"
k = 6
b = encrypt_word(a, k)
a = encrypt_word(b, -k)
print(a, b)
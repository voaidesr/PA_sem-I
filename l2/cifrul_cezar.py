def shift(c, k):
    return chr((ord(c) - ord('a') + k) % 26 + ord('a'))

def encrypt(word, k):
    encrypted_word = ""
    for letter in word:
        encrypted_word += shift(letter, k)
    return encrypted_word

def decrypt(encrypted_word, k):
    word = ""
    for letter in encrypted_word:
        word += shift(letter, -k)
    return word

word = input().strip()
k = int(input())
enc = encrypt(word, k)
print(enc)
word = decrypt(enc, k)
print(word)
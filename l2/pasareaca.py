import re # split cu mai multe chestii 
def pasareasca(text):
    vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    text_nou = ""
    for char in text:
        if char in vocale:
            text_nou += (char + 'p' + char.lower())
        else:
            text_nou += char
    return text_nou

def decrypt_pasareaca(text):
    vocale = "aeiouAEIOU"
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in vocale:
            i += 2
        i += 1
    return result

    # punctul b

def pasareasca_cratime(text):
    text = text.split("-")
    result = [word + 'p' + word[-1].lower() for word in text]
    result = "-".join(result)

    text = result.split(" ")
    result = [text[i] + 'p' + text[i][-1].lower() for i in range(len(text) - 1)]
    result.append(text[-1])
    result = " ".join(result)
    return result

def decrypt_cratime(text):
    text = text.split("-")
    result = []
    for word in text:
        result.append(word[-len(word):-2])
    text = "-".join(result)
    text = text.split()
    for i in range (len(text) - 1):
        text[i] = text[i][-len(text[i]):-2]
    text = " ".join(text)
    return text
    
text = input().strip()
text = pasareasca_cratime(text)
print(text)
text = decrypt_cratime(text)
print(text)
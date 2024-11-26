in_file = open("l4/input.txt", "r")
words = []
for line in in_file:
    words += line.strip().split()
dic = {}
for word in words:
    word_set = set(word)
    if word_set in dic:
        dic(word_set) += word
    else:
        dic(word_set) = [word]
print(dic)
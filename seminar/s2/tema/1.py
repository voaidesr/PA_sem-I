"""
Reads a word `w` and a sequence of `n` words. Displays all distinct words that have the same length as `w`.
For example, for `w = "mere"` and the words "pere", "teste", and "mure" (thus `n = 3`), the words "pere" and "mure" should be displayed.

"""
word = input("cuvantul test: ")
words = set(x.lower() for x in input("Cuvinte: ").split())
words_same_lenght = []
for i in words:
    if len(i) == len(word):
        words_same_lenght.append(i)
if len(words_same_lenght):
    print(f"Cuvintele de aceeasi lungime cu {word} sunt: {', '.join(words_same_lenght)}")
else:
    print(f"Nu exista cuvinte de aceeasi lungime ca {word}")
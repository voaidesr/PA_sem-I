"""
În fișierul text numar_lipsa.txt se găsesc pe prima linie 𝑛 − 1 numere naturale distincte
dintre primele 𝑛 numere naturale nenule. Să se afișeze numărul lipsă. De exemplu, dacă
prima linie din fișier este 2 1 5 4, numărul lipsă este 3.

"""
try:
    with open("numar_lipsa.txt") as f:
        numbers = [int(x) for x in f.readline().split()]
        x = 0
        for n in numbers:
            x ^= n
        for i in range(1, len(numbers) + 2):
            x ^= i
        print(f"Numarul lipsa este {x}")
except FileNotFoundError:
    print("Fisierul nu exista!")
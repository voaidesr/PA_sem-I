# Se citește un cuvânt w, un număr natural nenul p și un șir format din n cuvinte.
# Să se afișeze toate cuvintele care sunt p-rime cu w, respectiv ultimele p caractere ale sale
# coincid cu ultimele p caractere ale lui w.
# De exemplu, pentru w = "mere", p = 2 și cuvintele "pere", "teste" și "programare" (deci n = 3),
# trebuie să fie afișate cuvintele "pere" și "programare".

def p_rima(*words, mainword, p):
    rima = mainword[-p:]
    for w in words:
        if w[-p:] == rima: # slicing de la p incolo - ultimele 2 litere
        # sau se poate folosi 
        # if w.endswith(rima) - complexitate O(p) unde p este lungimea sufixului
            print(w, end=" ")

cuvant = input("Cuvantul: ")
n = int(input("N = "))
cuvinte = input("Cuvintele: ").split()
p_rima(*cuvinte, mainword=cuvant, p=n)

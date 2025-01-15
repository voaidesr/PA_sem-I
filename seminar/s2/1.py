s = input("s = ")
"""
This script takes two input strings, `s` and `t`, and finds all occurrences of `t` within `s`.
It prints the index of each occurrence of `t` in `s`. If `t` is not found in `s`, it prints a message indicating so.
Time Complexity of find method: O(n*m) where n is the length of the string and m is the length of the substring.
"""
t = input("t = ")
p = s.find(t)


if p == -1:
    print(f"Sirul {t} nu apare in sirul {s}")
else:
    i = 0
    while p != -1:
        print(f"Aparitia {i} la indexul {p}")
        p = s.find(t, p + len(t)) # cautam mai incolo decat secventa deja gasita
        i += 1
# find returneaza index-ul sau -1, daca nu este gasit 
# are si parametrul start si stop
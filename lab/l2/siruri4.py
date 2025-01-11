s = input("Primul cuvant: ").strip()
t = input("Al doilea cuvant: ").strip()
s_sorted = sorted(s)
t_sorted = sorted(t)
if s_sorted == t_sorted:
    print("anagrame")
else:
    print("nu anagrame")
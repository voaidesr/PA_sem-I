fraza = input("Introduceti fraza: ").strip()
c_seq = input("Introduceti secventa corecta: ").strip()
w_seq = input("Introduceti secventa gresita: ").strip()

fraza_corecta = fraza.replace(w_seq, c_seq)

print(fraza_corecta)
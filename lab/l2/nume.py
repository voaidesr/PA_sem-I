
def is_name(nume):
    if nume.count('-') > 1:
        return False
    for chr in nume:
        if not chr.isalpha() and chr != "-":
            return False
    parts = nume.split("-")
    for part in parts:
        if len(part) < 3:
            return False
        if not part[0].isupper():
            return False
    return True

nume = input().strip()
print(is_name(nume))
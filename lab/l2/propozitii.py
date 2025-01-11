import re # regex
def propozitii_wrong(text):
    propozitii = text.split(".")
    return propozitii

def propozitii_complext(text):
    pattern = r'(?<!\w)(?<=[.!?])\s+(?=[A-Z])'
    propozitii = re.split(pattern, text)
    return propozitii

text = input().strip()
propozitii = propozitii_complext(text)
for i in range(len(propozitii)):
    print(f"Propozitia {i+1} este {propozitii[i]}")
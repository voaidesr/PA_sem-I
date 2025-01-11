n = int(input().strip())
precedent_value = float(input().strip())
max = 0
max_value_1 = 0
max_value_2 = 0
for i in range(n-1):
    current_value = float(input().strip())
    if abs(current_value - precedent_value) > max:
        max = abs(current_value - precedent_value)
        max_value_1 = i+1
        max_value_2 = i
    precedent_value = current_value
print(f"Cea mai mare crestere a fost intre zilele {max_value_2} si {max_value_1}")
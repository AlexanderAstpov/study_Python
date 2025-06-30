s = input("Введите любую строку: ")
chars = 0
digits = 0
for ch in s:
    if ch.isalpha():
        chars += 1
    elif ch.isdigit():
        digits += 1

print(f"Количестово букв в строке: {chars} ")
print(f"Количестово цифр в строке: {digits} ")


# Мама мыла раму. Дочка не мыла раму, потому что дочка плохо моет раму, а мама моет раму хорошо, а не плохо.
text = input("Введите текст:   ").split()
text = [t.lower().strip(" ,.:;!?") for t in text]
print(*text)
print(len(set(text)))



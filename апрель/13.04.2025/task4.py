fruit = ("apple", "banana", "orange", "lemon", "apple", "apple", "lemon")

user_choise = input("Введите название фрукта:   ")
count = fruit.count(user_choise)

if count:
    print(f"{user_choise} встречается в кортеже {count} раз ")
else:
    print("Этого у нас нет к сожалению (")

fruit = ("apple", "banana", "orange", "lemon", "apple", "apple", "lemon", "bananamango")

user_choise = input("Введите название фрукта:   ")
count = len(tuple(filter(lambda x: user_choise in x ,fruit)))

if count:
    print(f"{user_choise} встречается в кортеже {count} раз ")
else:
    print("Этого у нас нет к сожалению (")
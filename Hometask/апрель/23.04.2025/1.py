# fruit = ("apple", "banana", "orange", "lemon", "apple", "apple", "lemon")

# user_choise = input("Введите название фрукта:   ")
# count = fruit.count(user_choise)

# if count:
#     print(f"{user_choise} встречается в кортеже {count} раз ")
# else:
#     print("Этого у нас нет к сожалению (")

tup_1 = (1, 2, 3, 8, 91, 12)
tup_2 = (0, 2, 13, 18, 91, 12)
tup_3 = (10, 22, 31, 8, 91, 120)
res = tuple(set(tup_1) & set(tup_2) & set(tup_3))
print(res)

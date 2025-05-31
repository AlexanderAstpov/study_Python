autos = ('bmw', 'audi', 'ford', 'tesla')

user_choise, rename = input("Введите что заменить и на что:  ").split()
count = autos.count(user_choise)

if count:
    autos = tuple(map(lambda x: rename if x==user_choise else x ,autos))

print(autos)


# def is_equal(x):
#     if x == user_choise:
#         return rename
#     else:
#         return x

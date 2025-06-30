# генератор списка

a = input("Введите список целых чисел через пробел  ")

ls1 = [int(i) for i in a.split()]
print(ls1)
print()
# получаем 10 нулей или все что захотим
ls0 = [0 for i in range(10)]
print(ls0)

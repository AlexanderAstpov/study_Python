# генератор списка

a = input("Введите список целых чисел через пробел  ")

ls1 = sum([int(i) for i in a.split() if int(i) < 0])
print(ls1)
print()
 
ls1 = [int(i) for i in a.split() if int(i) < 0]
ls1 = sum(ls1)
print(ls1)

ls1 = []
for i in a.split():
    if int(i) < 0:
        ls1.append(int(i))
ls1 = sum(ls1)
 
print(ls1)
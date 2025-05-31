
ls1 = input("Введите список целых чисел через пробел  ")
# ls1 = ls1.split()
# for i in range(len(ls1)):
#     ls1[i] = int(ls1[i])
# print(ls1)

s = 0

for i in ls1:
    if i < 0:
        s += i
print(s)
print()
# найти сумму отрицательный чисел


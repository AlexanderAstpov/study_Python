random = (input("Введите слечайные отрицательные и положительные числа  через пробел:   "))
random2 = (input("Введите слечайные отрицательные и положительные числа  через пробел:   "))
ran = ([int(i) for i in random.split()])
ran2 = ([int(i) for i in random2.split()])
print("список - содержащий элементы обоих списков ")
ran3 = ran + ran2
print(ran3)
print("список - содержащий элементы обоих списков без повторений")
ran3 = []
for elem in ran:
    if elem not in ran3:
        ran3.append(elem)

for elem in ran2:
    if elem not in ran3:
        ran3.append(elem)

print(ran3)
print("список - содержащий элементы общие для двух списков")
ran3 = []
for elem in ran:
    if elem in ran2:
        ran3.append(elem)

print(ran3)
print("список - содержащий только уникальные элементы каждого из списков")
ran3 = []
for elem in ran:
    if elem not in ran2:
        ran3.append(elem)

for elem in ran2:
    if elem not in ran:
        ran3.append(elem)

print(ran3)
print("список - содержащий только минимальное и максимальное значение каждого из списков.")
ran3 = ran + ran2

print([max(ran3), min(ran3)])
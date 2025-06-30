# методы множества (операции на множетелеми)  изменяют исходные множества

st1 = {0,1,2,3,4,5,6}
st2 = {5,6,7,8,9}
print(st1)
print(st2)

# изменяющее пересечение
# print("изменяющее пересечение")

# st1.intersection_update(st2)
# print(st1)
# st1 &= st2
# print(st1)


# print("изменяющее объединение")
# st1 = {0,1,2,3,4,5,6}
# st2 = {5,6,7,8,9}
# print(st1)
# print(st2)

# st1.update(st2)
# print(st1)

# st1 |= st2
# print(st1)

# print("Изменяющая разность")
# st1 = {0,1,2,3,4,5,6}
# st2 = {5,6,7,8,9}
# print(st1)
# print(st2)
# st1.difference_update(st2)
# print(st1)

# st1 -= st2
# print(st1)


print("Изменяющая симетричная разность")
st1 = {0,1,2,3,4,5,6}
st2 = {5,6,7,8,9}
print(st1)
print(st2)
# st1.symmetric_difference_update(st2)
# print(st1)
st1 ^= st2
print(st1)



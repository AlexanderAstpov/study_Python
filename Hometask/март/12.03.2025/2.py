start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
print("Все числа диапазона:")

for i in range(start, end+1):
    print(i, end=" ")
print()

print("Все числа диапазона в убывающем порядке:")

for i in range(end, start-1, -1):
    print(i, end=" ")
print()

print("Все числа, кратные 7:")

for i in range(start, end+1):
    if i % 7 == 0:
        print(i, end=" ")
print()

count = 0
for i in range(start, end+1):
    if i % 5 == 0:
        count += 1
print("Количество чисел, кратных 5:", count)


start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
for i in range(start, end+1):
    if i % 3 == 0:
        print("Fizz", end=" ")
print()

for i in range(start, end+1):
    if i % 5 == 0:
        print("Buzz", end=" ")
print()

for i in range(start, end+1):
    if  i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz ", end=" ")
print()




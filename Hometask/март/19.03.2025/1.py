
sum = int(input("Введите количество рядов: "))
for i in range(sum):
    print(" " * i * 2, end="")
    print("* " *  (sum - i))
   
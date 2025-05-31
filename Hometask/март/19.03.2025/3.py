
sum = int(input("Введите количество рядов: "))
for i in range(sum):
    print(" " * i, end="")
    print("* " *  (sum - i))
   
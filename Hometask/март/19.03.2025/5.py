
sum = int(input("Введите количество рядов: "))
for i in range(sum):
    print(" " * i, end=" ")
    print("* " *  (sum - i))
sum+= 1
for i in range(1, sum):
    print(" " * (sum - i), end="")
    print("* " *   i)
   
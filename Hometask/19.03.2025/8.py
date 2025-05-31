
sum = int(input("Введите количество рядов: "))
for i in range(sum):
    print(" " * (sum * 2), end="")
    print(" " * ((sum - i) * 2), end="")
    print("* " * i)
   
for i in range(sum):
    print(" " * (sum * 2), end="")
    print(" " * (i * 2), end="")
    print("* " * (sum - i))
   
   
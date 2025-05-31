
sum = int(input("Введите количество рядов: "))
for i in range(sum):
    print("* " * i, end="")
    print(" " * ((sum - i) * 4), end="")
    print("* " * i)

for i in range(sum):
    print("* " * (sum - i), end="")
    print(" " * (i * 4), end="")
    print("* " * (sum - i))
   
   
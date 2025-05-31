
sum = int(input("Введите количество рядов: "))
sum = sum + 1
for i in range(sum):
    print(" " * ((sum - i )  ), end=" ")
    print("*" * i)
    
  
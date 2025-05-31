num1 = int(input("Введите первое число начало диапозона - "))
num2 = int(input("Введите второе число конец диапозона - "))
while num1 <= num2:
    num1 += 1
    if num1 % 7 == 0:
        print(num1)




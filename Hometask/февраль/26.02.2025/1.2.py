num = int(input("Введите четырех значное число "))
num1 = num // 1000
num2 = (num - (num1 * 1000)) // 100
num4 = num % 10
num3 = (num - num4) /10 % 10
result = num1  * num2 * num3 * num4
print( result)

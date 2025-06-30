num1 = int(input("Введите число для вычисления факториала "))
result = 1  
for i in range(1, num1 + 1): #range - задает количество повторений 
    result = result * i
print(result)
    
    
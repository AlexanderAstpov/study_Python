num = int(input("Введите натуральное число n:   "))
n = 0
for i in range(1, num + 1):
        if num % i == 0:
            n = i
            print(n)
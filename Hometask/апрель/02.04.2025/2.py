num = (input("Введите слечайные целые числа  через пробел:   "))
n = [int(i) for i in num.split()]
n.sort()
print(n)
print(sorted(n, reverse=True))

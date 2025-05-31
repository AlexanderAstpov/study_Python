def exponentiation(x, y):
    a = []
    for i in y:
        a.append(i ** x)
    return a


x = 3
y = [1, 2, 3, 4]
a = exponentiation(x, y)
print(a)
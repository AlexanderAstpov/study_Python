def multiplication_num(x1, x2):
    if x1 < x2:
        result = 1
        ls = [i for i in range(x1, x2+1)]
        for i in ls:
            result = result * i
        return result
    elif x1 > x2:
        result = 1
        ls = [i for i in range(x2, x1+1)]
        for i in ls:
            result = result * i
        return result
    elif x1 == x2:
        return('Числа одинаковые для создания диапазона')

a= multiplication_num(3,6)
print(a)
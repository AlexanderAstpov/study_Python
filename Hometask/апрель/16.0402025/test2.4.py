


def divide_by_2(num):
    if num % 3 != 0:
        return False
    return True

lst = [10, 15, 21, 30, 44, 14, 7]
lst_2 = list(filter(divide_by_2, lst))
print(lst_2)




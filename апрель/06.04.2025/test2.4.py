# lst = [10, 15, 21, 30, 44, 14, 7]


def divide_by_2(num):
    if num % 3 != 0:
        return num
    return False

lst = [10, 15, 21, 30, 44, 14, 7]
lst = list(map(divide_by_2, lst))
print(lst)




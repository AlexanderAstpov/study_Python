def is_simple_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True    

lst = [23, 7, 13, 4, 55, 7567, 435, 565, 3, 9]
lst_2 = list(filter(is_simple_number, lst))
print(lst_2)
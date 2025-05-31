def is_simple_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True   

lst = [3, 65, 7, 3]
lst_2 = list(filter(is_simple_number, lst))
print(lst_2)
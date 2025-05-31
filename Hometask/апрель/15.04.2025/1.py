
def is_even_namber(num):
    if num % 2 == 0:
        return True
    return False

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_2 = list(filter(is_even_namber, lst))
print(lst_2)
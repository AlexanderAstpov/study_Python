
def is_simple_namber(num):
    if num > 0:
        return True
    return False

lst =  [-5, 10, -3, 20, 0, 7]
lst_2 = list(filter(is_simple_namber, lst))
lst_3 = list(map(lambda x: x * 2, lst_2))
print(lst_3)

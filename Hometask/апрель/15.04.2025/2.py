def square(num):
    return num ** 2
    

lst = [2, 4, 6, 8, 10]
lst_2 = list(map(square, lst))
print(lst_2)

def divide_by_2(num):
    return num / 2

lst = [234, 541, 745, 566]
lst = list(map(divide_by_2, lst))
print(lst)


# lst = [234, 541, 745, 566]
# lst = list(map(lambda num: num / 2, lst))
# print(lst)

# my_fanc = lambda x: x / 2

# print(my_fanc(1200))
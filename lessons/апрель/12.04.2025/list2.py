lst = [10, 12, 13, "apple", 15, True, 34]
print(lst)
lst[3] = 14
print(lst)

lst.insert(1,11) # вставляет элемент на нужную позиции двигая другие эл.
print(lst)

lst.extend([16, 17]) # расширяет список добовляя значения в конец списка
print(lst)

lst.remove(True)
print(lst)

lst.pop(6) # удоляет эл по индексу
print(lst)

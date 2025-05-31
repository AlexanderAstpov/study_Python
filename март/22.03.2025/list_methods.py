ls = [12,22, 44, 54, 9]
ns = [0,0,7]
print(ls)

print(len(ls))
print(max(ls))
print(min(ls))
m = min(ls)
print(m)
print(sum(ls)) # сумма всех элементов
print(sorted(ls)) 
print(sorted(ls, reverse=True)) 

print()
print(ls + ns)
print(ls * 2)

print()

# Методы списка
# метод добавления значения в сисок
ls.append(55) # добавляет элемент в конец списка
print(ls)
ls.append(ns)
print(ls)
print(ls[-1])
print(ls[-1][2])

print()
print(ls)
ls.insert(1, 123) # записываем значение в индекс
print(ls)
print()

ls.remove(123) # передаем значение а не индекс удаляет первае входящее значение
print(ls)
print()

x = ls.pop()
print(x)
ls.pop() # удаляут последний элемент из списка
print(ls)

ls.pop(1) # удаляут указанный индекс  из списка
print(ls)
print()
ls.append(12)
print(ls)

print(ls.index(12))
print()

print(ls.count(12))
print()

ls.sort()
print(ls)

ls.reverse() # разворачивает задом на перед
print(ls)
print()

# ls.clear()
# print(ls)
print()

# оператор принадлежности in
print(ls)
print(54 in ls)
print(55 in ls)
print()

ls =[]
ls = [1,2,3]
ls = list()
print()

s= "мама мыла раму"
ls = list(s)
print(ls)
ls = s.split()
print(ls)
l= "яблока,персик,банан"
ls = l.split()
print(ls)
ls = l.split(',')
print(ls)
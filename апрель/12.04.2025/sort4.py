# lst = [ 456, 34, 35, 1, 235, 346, 33, 78]
# lst.sort()
# print(lst)

# lst.sort(reverse=True) # от большего к меньшему
# print(lst)

employers = [
    ['Иван', "Иванов", 1000, 20],
    ['Сергей', "Сергеев", 800, 35],
    ['Светлана', "Иванова", 1500, 15],
    ['Анатольй', "Червяк", 2000, 1],
    ['Арнольд', "Шварцнегер", 3000, 0],
    ['Сильвестр', "Сталоне", 300, 60] 
    ]

for i in employers:
    print(i)

employers.sort()
print('='*35)
for i in employers:
    print(i)


employers.sort(key=lambda x: x[2])
print('='*35)
for i in employers:
    print(i)

employers.sort(key=lambda x: x[2], reverse=True)
print('='*35)
for i in employers:
    print(i)

employers.sort(key=lambda x: x[2]* x[3], reverse=True)
print('='*35)
for i in employers:
    print(i)
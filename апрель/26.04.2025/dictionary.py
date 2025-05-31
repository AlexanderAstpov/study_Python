capitals = {"Russia":"Moscow", "Great Britan":"London", "Spain":"Madrid"}
print(capitals)
print(f"Столицей России является - {capitals['Russia']}")

print("создание словаря через встроенныю функцию")
capitals = dict(Russia="Moscow", Great_Britan="London", Spain="Madrid" ) # создание словаря через встроенныю функцию
print(capitals)

print("вариант скиска картежей")
capitals = dict([("Russia","Moscow"), ("Great Britan","London"), ("Spain","Madrid")]) # вариант скиска картежей
print(capitals)

print("посмотреть все ключи в словаре")
for key in capitals: # посмотреть все ключи в словаре
    print(key)

print("посмотреть все значения в словаре")
for key in capitals: # посмотреть все значения в словаре
    print(capitals[key])

print("вывести запись как кортеж")
for key in capitals: # вывести запись как кортеж
    print(key, capitals[key])

print(" метод ключи")
for key in capitals.keys(): # метод ключи
    print(key)


for value in capitals.values(): # метод ключи
    print(value)

for item in capitals.items(): # ключ - значение в кортеже
    print(item)

for key, value in capitals.items(): # ключ - значение в кортеже - распакован
    print(key, value)
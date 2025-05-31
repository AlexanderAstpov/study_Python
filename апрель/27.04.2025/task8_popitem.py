worker = {
    "name": "Иван",
    "fname": "Иванов",
    "profession": "Баскетболист",
    "salary": 500_000
}

name = worker.popitem() # удаляет последнюю запись ключа
print(f"удалили из словаря {name}")
print(worker)
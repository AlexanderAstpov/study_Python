worker = {
    "name": "Иван",
    "fname": "Иванов",
    "profession": "Баскетболист",
    "salary": 500_000
}

worker1 = worker.copy() # создает новый словарь а не ссылку
print(worker1)
worker1["age"] = 100 # добавляет ключ и значение
print(worker)
print(worker1)
worker = {
    "name": "Иван",
    "fname": "Иванов",
    "profession": "Баскетболист",
    "salary": 500_000
}

worker.setdefault("age", 0) # Если ключа нет то добавляет, а если есть то просто пропустит.
worker.setdefault("age", 30) # Если ключа нет то добавляет, а если есть то просто пропустит.
print(worker)

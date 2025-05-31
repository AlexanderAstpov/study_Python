worker = {
    "name": "Иван",
    "fname": "Иванов",
    "profession": "Баскетболист",
    "salary": 500_000
}

name = worker.pop("name")
print(f"удалили из словаря имя {name}")
print(worker)
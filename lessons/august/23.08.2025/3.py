import sqlite3

connection = sqlite3.connect(r"lessons\august\23.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall() # получить все- список кортежей
columns = [desc[0] for desc in cursor.description] # получили название колонок
data = [dict(zip(columns, row)) for row in rows] # приобразовываем в словарь с ключем zip склеивает название колонок и описание

for d in data :
    print(d)


cursor.close()
import sqlite3

connection = sqlite3.connect(r"lessons\august\24.08.2025\school.db")
connection.row_factory = sqlite3.Row  # для кортежей ключь значение упрощает вывод в словарь [dict]
cursor = connection.cursor()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
data  = [dict(row) for row in rows]

for d in data: # выведет как список словарей [dict]
    print(d)

# for row in rows:
#     print(row[1]) # print(row['title']) или любой индекс или название колонки


cursor.close()
import sqlite3

connection = sqlite3.connect(r"lessons\august\23.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall() # получить все
for row in rows:
    print(row)


cursor.close()
import sqlite3

connection = sqlite3.connect(r"lessons\august\23.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute('''
DELETE FROM workers
WHERE id = 2
''')

connection.commit()

cursor.execute("SELECT * FROM workers")

rows = cursor.fetchall() # получить все
for row in rows:
    print(row)


cursor.close()
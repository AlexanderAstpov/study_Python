import sqlite3

connection = sqlite3.connect(r"lessons\august\23.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

new_worker = ('Павел', 55, 'сварщик')
cursor.execute('''
INSERT INTO workers (name, age, profession)
VALUES (?,?,?)

''', new_worker)

connection.commit()

cursor.execute("SELECT * FROM workers")

rows = cursor.fetchall() # получить все
for row in rows:
    print(row)


cursor.close()
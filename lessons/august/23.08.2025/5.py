import sqlite3

connection = sqlite3.connect(r"lessons\august\23.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM workers")
rows = cursor.fetchall() # получить все
columns = [desc[0] for desc in cursor.description] # получили название колонок

print(columns)


cursor.close()
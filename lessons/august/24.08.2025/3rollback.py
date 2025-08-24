import sqlite3

connection = sqlite3.connect(r"lessons\august\24.08.2025\school.db")
cursor = connection.cursor()

cursor.execute('''
INSERT INTO books ('title', 'author', 'publish_date', 'page_value') 
VALUES ('Кубок огня', 'Джоан Роулинг', '2005-12-12', 650)            
''')

print(cursor.lastrowid) # показывает последний индекс строка, в данном случае он равен id

connection.rollback() # отмена операции

cursor.close()
connection.close() # закрывает всю базу данных
# не забываем делать commit
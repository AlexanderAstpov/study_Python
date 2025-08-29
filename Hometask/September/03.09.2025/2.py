import sqlite3

connection = sqlite3.connect('cinema.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS halls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(500),
    capacity INTEGER NOT NULL
    )
''')

connection.commit()
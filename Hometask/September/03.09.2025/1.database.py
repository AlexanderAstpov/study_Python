import sqlite3

connection = sqlite3.connect('cinema.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(500),
    genre VARCHAR(50),
    duration INTEGER NOT NULL
    )
    ''')

connection.commit()




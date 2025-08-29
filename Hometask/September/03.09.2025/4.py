import sqlite3

connection = sqlite3.connect('cinema.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreing_keys = ON")


cursor.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
    buyer_name VARCHAR(100),
    price  INTEGER,
    FOREIGN KEY (session_id) REFERENCES sessions (id))
''')

connection.commit() # применить изменения


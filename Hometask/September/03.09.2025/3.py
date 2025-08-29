import sqlite3

connection = sqlite3.connect('cinema.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreing_keys = ON")


cursor.execute('''
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER,
    hall_id INTEGER,
    start_time  DATETIME DEFAULT 'YYYY-MM-DD HH:MM:SS',
    FOREIGN KEY (movie_id) REFERENCES movie (id),
    FOREIGN KEY (hall_id) REFERENCES halls (id))
''')

connection.commit() # применить изменения



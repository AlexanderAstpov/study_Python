import sqlite3

connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

new_sessions = [
    (1, 1, '2025-09-01 18:00'),
    (2, 2, '2025-09-01 20:00'),
    (3, 3, '2025-09-02 19:00'),
    (4, 4, '2025-09-02 21:30'),
    (5, 5, '2025-09-03 18:15'),
    (6, 6, '2025-09-03 19:00'),
    (7, 7, '2025-09-03 21:00'),
    (8, 8, '2025-09-04 17:45'),
    (9, 9, '2025-09-04 20:10'),
    (10, 10, '2025-09-05 19:40'),
    
]

cursor.executemany('''
INSERT INTO sessions ('movie_id', 'hall_id', 'start_time') 
VALUES (?, ?, ?)          
''', new_sessions)

connection.commit()

cursor.execute("SELECT * FROM sessions")

rows = cursor.fetchall() 
for row in rows:
    print(row)


cursor.close()



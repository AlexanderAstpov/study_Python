import sqlite3

connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

new_halls = [
    ('Зал 1', 100),
    ('Зал 2', 80),
    ('Зал 3', 50),
    ('Зал 4', 120),
    ('Зал 5', 60),
    ('Зал 6', 90),
    ('VIP 1', 30),
    ('VIP 2', 25),
    ('IMAX', 200),
    ('4DX', 110),
    
]

cursor.executemany('''
INSERT INTO halls ('name', 'capacity') 
VALUES (?, ?)          
''', new_halls)

connection.commit()

cursor.execute("SELECT * FROM halls")

rows = cursor.fetchall() 
for row in rows:
    print(row)


cursor.close()



import sqlite3

connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

cursor.execute('''
    SELECT SUM(t.price)
    FROM movies AS m
    JOIN sessions AS s ON m.id = s.movie_id
    JOIN tickets AS t ON s.id = t.session_id
    JOIN halls AS h ON h.id = s.hall_id
    WHERE t.price > 0
               
''')

rows = cursor.fetchall() # получить все
for row in rows:
    print(row)


cursor.close()
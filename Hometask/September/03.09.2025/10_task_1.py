import sqlite3

connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

cursor.execute('''
    SELECT m.title, h.name, t.buyer_name
    FROM movies AS m
    JOIN sessions AS s ON m.id = s.movie_id
    JOIN tickets AS t ON s.id = t.session_id
    JOIN halls AS h ON h.id = s.hall_id
               
''')

rows = cursor.fetchall() # получить все
for row in rows:
    print(row)


cursor.close()
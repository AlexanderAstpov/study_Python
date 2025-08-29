import sqlite3

connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

new_movies = [
    ('Интерстеллар', 'фантастика',	169),
    ('Начало', 'боевик', 148),
    ('Матрица',	'фантастика', 136),
    ('Джокер',	'драма', 122),
    ('Паразиты', 'триллер',	132),
    ('Зелёная книга', 'драма', 130),
    ('Безумный Макс: Дорога ярости', 'боевик',	120),
    ('Гран Торино',	'драма', 116),
    ('Дюна', 'фантастика', 155),
    ('Варкрафт', 'фэнтези',	123),
]

cursor.executemany('''
INSERT INTO movies ('title', 'genre', 'duration') 
VALUES (?, ?, ?)          
''', new_movies)

connection.commit()

cursor.execute("SELECT * FROM movies")

rows = cursor.fetchall() 
for row in rows:
    print(row)


cursor.close()



import sqlite3

connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

new_tickets = [
    (1 , 'Иванов Иван',	500),
    (2 , 'Петров Пётр',	450),
    (3 , 'Сидоров Сидор',	500),
    (4 , 'Смирнова Мария',	400),
    (5 , 'Петрова Анна',	550),
    (6 , 'Кузнецов Алексей',	480),
    (7 , 'Васильева Ольга',	600),
    (8 , 'Орлов Дмитрий',	420),
    (9 , 'Миронова Екатерина',	650),
    (10 , 'Соколов Андрей',	700),
    
]

cursor.executemany('''
INSERT INTO tickets ('session_id', 'buyer_name', 'price') 
VALUES (?, ?, ?)          
''', new_tickets)

connection.commit()

cursor.execute("SELECT * FROM tickets")

rows = cursor.fetchall() 
for row in rows:
    print(row)


cursor.close()



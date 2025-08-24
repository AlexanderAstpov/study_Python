import sqlite3

with sqlite3.connect(r"lessons\august\24.08.2025\school.db") as connection:
    cursor = connection.cursor()
    cursor.execute('''
    SELECT author, COUNT(id)
    FROM books 
    GROUP BY author
    ORDER BY COUNT (id) DESC
    ''')

    rows = cursor.fetchall()
    for row in rows:
        print(*row)


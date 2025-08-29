import sqlite3

connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM movies")
d = cursor.description

for i in d:
    print(i[0]) # получаем имена колонок (хронятся в нулевом индексе)

name_list = [i[0] for i in d]
print(name_list)
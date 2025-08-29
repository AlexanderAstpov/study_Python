import sqlite3
import json

def safe_to_json(db_file, table_name, json_file):
    
    
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    data = [dict(row) for row in rows]

    conn.close()

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False) 

    print(f"Данные из таблицы '{table_name}' успешно экспортированы в '{json_file}'")

    

safe_to_json("school.db ", "books", "books.txt" ) # открывал только одну папку, поэтому такой короткий путь к базе данных.

import csv
with open("students.csv", 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f'Имя: {row["name"]}, Возраст: {row["age"]}, Оценка: {row["grade"]}') 
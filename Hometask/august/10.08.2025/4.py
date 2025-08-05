import csv
with open("students.csv", 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    av_age = []
    for row in reader:
        if row["grade"] == "A":
            print(f'Имя: {row["name"]}, Возраст: {row["age"]}, Оценка: {row["grade"]}') 
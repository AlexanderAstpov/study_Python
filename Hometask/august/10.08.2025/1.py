import csv
with open('students.csv','w') as csvfile:
    fieldnames = ["name",  "age", "grade"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([
                        {"name": "Alice", "age": 15, "grade": "A"},
                        {"name": "Bob", "age": 14, "grade": "B"},
                        {"name": "Charlie", "age": 15, "grade": "C"},
                        {"name": "Diana", "age": 14, "grade": "A"},
                        {"name": "Edward", "age": 15, "grade": "B"},
                        ])
    
print("writing complete")


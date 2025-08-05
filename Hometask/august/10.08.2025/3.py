import csv
with open("students.csv", 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    av_age = []
    for row in reader:
        av_age.append(int(row['age']))
    print(f"Средний возраст всех учеников составляет - {round(sum(av_age)/ len(av_age), 2)}")    
    
        
    
       

grades = ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'D']
d ={}

for i in grades:
    d[i] = d.get(i, 0) + 1
    
print(d)
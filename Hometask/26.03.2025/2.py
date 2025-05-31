random = (input("Введите слечайные отрицательные и положительные числа  через запятую:   "))

max_sum = 0
min_sum = 0
neg_value_count = 0
pos_value_count = 0
zero_count = 0
for sum in random:
    if sum > max_sum:
        max_sum = sum
    if sum < min_sum:
        min_sum = sum
    if sum > 0:
        pos_value_count += 1
    if sum < 0:
        neg_value_count += 1
    else:
        zero_count += 1

print(int(random))
print(int(max_sum))





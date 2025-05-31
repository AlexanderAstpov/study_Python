num = (input("Введите слечайные целые числа  через пробел:   "))
n = [int(i) for i in num.split()]
ind_max = (n.index(max(n)))
ind_min = (n.index(min(n)))
n[ind_min], n[ind_max] = n[ind_max], n[ind_min]

print(*n)

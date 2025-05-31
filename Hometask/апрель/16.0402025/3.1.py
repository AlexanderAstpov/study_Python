lst = "a1b2c3d4eee"
a = list(lst)
lst_2 = []
for i in range(len(a)):
    if a[i].isdigit() == True:
        lst_2.append(a[i])
        lst_3 = ([int(i) for i in lst_2])
print(lst_3)


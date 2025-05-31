
lst = ["apple", "Cat", "Banana", "cherry", "123", "dog"]
lst_2 = []
for i in range(len(lst)):
    if lst[i].isalpha() == True and len(lst[i]) > 3 and lst[i].istitle() == True:
        lst_2.append(lst[i])
print(lst_2)
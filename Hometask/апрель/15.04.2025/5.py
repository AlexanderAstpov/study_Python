def new_list(lst):
    for i in range(len(lst)):
        if lst[i].isdigit() == True or lst[i].startswith("+") == True or lst[i].startswith(" ") == True:
            return True
        return False

lst = ["8-912-123-45-67", "+79162345678", "abc", "4951234567", " +7 999 123-45-67 "]

lst_2 = list(filter(new_list, lst))
lst_3 = list(map(lambda x: x.lstrip("+ 7 8 - ") , lst_2))
lst_4 = [''.join(filter(str.isdigit, tel)) for tel in lst_3]
lst_5 = list(map(lambda x: f'+7 ({x[0:3]}) {x[3:6]}-{x[6:8]}-{x[8:12]}', lst_4))
print(lst_5)

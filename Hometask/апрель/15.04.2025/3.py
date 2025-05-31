
def new_list(lst):
    for i in range(len(lst)):
        if lst[i].startswith("a") == True:
            return True
        return False

lst = ["apple", "banana", "cherry", "avocado", "orange"]

lst_2 = list(filter(new_list, lst))
lst_3 = list(map(lambda x: str(x.upper()), lst_2))
    
print(lst_3)
         
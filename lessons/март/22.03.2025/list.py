print()

ls = ["Петя","Вяся", "Коля", "женя"]
print(ls[0])
print()
name = ls[0]
print(name)
print()

print(ls)
ls[2] = " Света"
print(ls)
print()

s = "Првет"
print(s[0])
print()
# s[0] = "Б"
print()

# ls1 = [10, 'Петя', 11.5, False]
# print(ls1)
# print()

# new_ls = ls1
# new_ls[-1] = True
# print(ls1)
# print()
# print(new_ls)

# ls1 = [10, 'Петя', 11.5, False]
# print(ls1)
# print()

# new_ls = ls1[:]
# new_ls[-1] = True
# print(ls1)
# print()
# print(new_ls)

# ls1 = [10, 'Петя', 11.5, False]
# print(ls1)
# print()

# new_ls = ls1.copy() # копирует строку с данными, а не ссылку
# new_ls[-1] = True
# print(ls1)
# print()
# print(new_ls)

# print()
# ls1 = [10, 'Петя', 11.5, False]
# print(type(ls1))

s = "Привет"
ls = list(s)
print(ls)

print("" .join(ls))
print("=" .join(ls))
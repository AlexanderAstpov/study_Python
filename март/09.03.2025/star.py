#print("*")

# print("*")
# print("*" * 2)
# print("*" * 3)
star = int(input("Введите число звезд "))
for i in range(1, star + 1):
    print(" " * (star - i), end="")
    print("* " * i)
for i in range(star - 1, 0, -1):
    print(" " * (star - i), end="")
    print("* " * i)
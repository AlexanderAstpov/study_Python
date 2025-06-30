h = int(input("введите высоту: "))
w = int(input("введите ширину: "))
for i in range(h):
    if i == 0 or i == h-1:
        print('* ' * w, end="")
    else:
        print('* ', end="")
        for j in range(w - 2):
            print('0 ', end="")
        print("* ", end="")
    print()

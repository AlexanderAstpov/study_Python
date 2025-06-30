h = int(input("введите высоту: "))
w = int(input("введите ширину: "))
for i in range(h):
    for j in range(h):
        if h - 1 - i== j or i == j:
            print("0 ", end="")
        else:
            print("* ", end="")
    print()
   

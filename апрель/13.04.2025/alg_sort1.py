lst = [6, 456, 564, 32, 75, 123, 2, 464, 5, 66]

n = len(lst)

for i in range(n):
    for j in range(n - 1):
        if lst[j] > lst[j +1]:
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j +1 ] = temp
    print(lst)


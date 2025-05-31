def show_even_numbers(a ,b):
    e = 0
    if b > a:
        for i in range(a + 1, b + 1):
            if i % 2 == 0:
                e = i
                print (e, end=" ")
    if a > b:
        for i in range(b + 1, a + 1):
            if i % 2 == 0:
                e = i
                print (e, end=" ")

show_even_numbers(18, 12)
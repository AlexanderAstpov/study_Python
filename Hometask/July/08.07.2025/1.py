def split_even_odd(lst):
    even_number = []
    odd_number = []
    for number in lst:
        if number % 2 == 0:
            even_number.append(number)
        else:
            odd_number.append(number)
    return even_number, odd_number


lst = [1, 2, 3, 4, 5, 6, 13]
print(split_even_odd(lst))


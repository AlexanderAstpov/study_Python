def is_simple_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True    

lst = [3, 65, 7, 3]
for i in lst:
    print(is_simple_number(i))
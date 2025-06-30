def is_simple_num(number):
    for delitel in range(2, number):
        if number % delitel == 0:
            return False
    return True

print(is_simple_num(7))
print(is_simple_num(6))

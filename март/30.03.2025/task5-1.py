def is_lucky_num(num):
    left  = num // 1000
    right = num % 1000
    sun_left = (left // 100) + ((left//10) % 10) + (left % 10) 
    sun_right = (right // 100) + ((right//10) % 10) + (right % 10)

    return sun_left == sun_right # спавнение выдает булевое значение либо True либо False

print(is_lucky_num(123456))
print(is_lucky_num(123420))


def is_lucky_num(num):
    ls = [int(i) for i in str(num)]
    return sum(ls[:3]) == sum(ls[3:])
     
print(is_lucky_num(123456))
print(is_lucky_num(123420))
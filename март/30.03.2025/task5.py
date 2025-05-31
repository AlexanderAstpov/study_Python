def is_lucky_num(num):
    left  = num // 1000
    right = num % 1000
    sun_left = (left // 100) + ((left//10) % 10) + (left % 10) 
    sun_right = (right // 100) + ((right//10) % 10) + (right % 10)
    if sun_left == sun_right:
        return True
    else:
        return False
print(is_lucky_num(123456))
print(is_lucky_num(123420))


def is_lucky_num(num):
    num = str(num)
    ls = [int(i) for i in num]
    if sum(ls[:3]) == sum(ls[3:]):
        return True
    else:
        return False
print(is_lucky_num(123456))
print(is_lucky_num(123420))
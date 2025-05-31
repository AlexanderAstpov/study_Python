def is_palindrome_num(num):
    ls = [int(i) for i in str(num)]
    l = int(len(ls)/2)
    a = (ls[:l])
    b = (ls[l:])
    b1 = b[::-1]
    if l % 2 == 0:
       l = l
    if str(a) == str(b1):
        print(" Это число 'Палиндром'")
    else:
        print(" Это число не 'Палиндром'")
    

is_palindrome_num(12344321)
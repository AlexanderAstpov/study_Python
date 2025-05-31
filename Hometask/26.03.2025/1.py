s = (input("Введите арифметическое вырожение:   "))
if '+' in s:
    a, b = s.split('+')
    print(int(a) + int(b))
elif '-' in s:
    a, b = s.split('-')
    print(int(a) - int(b))
elif '*' in s:
    a, b = s.split('*')
    print(int(a) * int(b))
elif '/' in s:
    a, b = s.split('/')
    print(int(a) / int(b))
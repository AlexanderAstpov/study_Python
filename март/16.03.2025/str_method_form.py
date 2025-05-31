s = "Hello World"

print(s.center(20))
print(s.center(20,"*"))
print(s.center(3,"*"))
print()

ss = "\tHello World"
print(ss.expandtabs())# 8 пробелов
print(ss.expandtabs(tabsize=1)) # один пробел
print(s)
print()

print(s.ljust(20))
print(s.ljust(20,"*"))
print()

print(s.rjust(20))
print(s.rjust(20,"*"))
print()

sss = "   Hello!!!"
s1 = "!!!Hello   "
print(sss)
print(sss.lstrip()) # убирает пробелы
print(sss.lstrip()) # убирает пробелы
print(s1)
print(s1.lstrip("!")) # убирает пробелы
print(sss.rstrip("!"))

print()
s2 = "!!!Hello!!!"
print(s2)
print(s2.strip("!"))
print()

a = "123"
a1 = "+123"
print(a)
print(a.zfill(8)) # заполняет нулями все пустое пространство
print(a1.zfill(8)) # заполняет нулями все пустое пространство
print(a1)
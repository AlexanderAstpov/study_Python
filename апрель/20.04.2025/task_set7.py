s = "Мама мыла раму и пила пиво"
st = {i[1:2] for i in s.split() if i[1:2] != ''}
print(st)


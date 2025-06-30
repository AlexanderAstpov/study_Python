# методы множества (операции на множетелеми) не изменяют исходные множества

st1 = {0,1,2,3,4,5,6}
st2 = {5,6,7,8,9}

# объединение
st3 = st1.union(st2)
print(st3)
st4 = st1 | (st2)
print(st4)

print('объединение')

# пепесечение
st3 = st1.intersection(st2)
print(st3)

st4 = st1 & st2
print(st4)

print('пепесечение')

# разность
st3 = st1.difference(st2)
st5 = st1 - st2
print(st1)
print(st2)
print(st3)
print(st5)
print('разность')

st4 = st2.difference(st1)
st5 = st2 - st1
print(st1)
print(st2)
print(st4)
print(st5)
print('разность')

# симетричная разность

st3 = st1.symmetric_difference(st2)
print(st3)
st4 = st1 ^ st2
print(st4)
print('симетричная разность')
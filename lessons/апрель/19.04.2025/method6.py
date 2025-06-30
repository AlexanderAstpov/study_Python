# методы множества (операции принадлежности)
st0 = {0,1,2,3,4,5,6,7,8,9}
st1 = {0,1,2,3,4,5,6}
st2 = {5,6,7,8,9}
st3 = {3,4}
print(st0)
print(st1)
print(st2)

print("определение подмножества")
print(st1.issubset(st0))
print(st2.issubset(st0))
print(st1.issubset(st2))

print(st1 < st0)


print("определение надмножества")

print(st0.issuperset(st1))
print(st2.issuperset(st1))
print(st0 > st1)

print("определение наличия общих элементов множества")
print(st1.isdisjoint(st3)) # False когда есть общие элементы и True когда нет
print(st2.isdisjoint(st3))
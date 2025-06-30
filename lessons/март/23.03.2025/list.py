
ls1 = [1, 22, -12, -4, -27, 5, 108, 45, 34, 98]
s = 0

for i in ls1:
    if i < 0:
        s += i
print(s)
print()

a = 0
for i in ls1:
    if i%2 == 0:
        a += i
print(a)
print()

a = 0
for i in ls1:
    if i%2 != 0:
        a += i
print(a)
print()

a = 1
for i in range(len(ls1)):
    if i %3 == 0:
        a *= ls1[i]   
print(a)
print()

a = 1
for i in range(len(ls1)):
    if i %3 == 0:
        a *= ls1[i]   
print(a)
print()
ls1_max = max(ls1)
ls1_min = min(ls1)
print(ls1_max * ls1_min)
print()

d = ls1.index(ls1_min)
g = ls1.index(ls1_max)
ls2 = ls1[d:g]
print(sum(ls2))
print()

q = 0
for i in range(len(ls1)):
    if ls1[i] > 0:
        q = i
        break
w = 0
for i in range(len(ls1)):
    if ls1[i] > 0:
        w = i
       
ls3 = ls1[q + 1:w]
print(sum(ls3))



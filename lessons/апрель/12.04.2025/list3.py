import math
import time
big_lst = [i for i in range(10_000_000)]

# (i/100**8)**0.5
# первый вариант
start = time.time()
new_lst = []
for elem in big_lst:
    a = math.tan((elem / 100 **8 )**0.5)
    new_lst.append(a)

end = time.time()
print("первый вариант : ", start - end)

# второй вариант

start = time.time()

for i in range(10_000_000):
    big_lst[i] = math.tan((big_lst[i] / 100 **8 )**0.5)
   
    
end = time.time()
print("второй вариант:  ", start - end)

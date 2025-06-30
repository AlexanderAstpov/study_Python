w = 15
h = 4

for i in range(h):
    for j in range(w):
            print("* ", end='')
    print()
print()


for i in range(h):
    print(*['*' for j in range(w)])
    
   
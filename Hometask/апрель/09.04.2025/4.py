def delete_number(x,a):
    ls = [int(i) for i in str(x)]
    ls_a = [int(i) for i in str(a)]
    b = 0
    y = []
    for i in ls:
        for j in ls_a:
            if i == j:
                b += 1 
            if i not in ls_a:
                y.append(i)
    return b
  

c = delete_number(12345,12)
print(c)
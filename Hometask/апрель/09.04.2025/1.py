def multiply(x):
    product_of_num = 1
    for elem in x:
        if product_of_num != 0:
            product_of_num *= elem
    return product_of_num

a = [1,2,3,4]
print(multiply(a))
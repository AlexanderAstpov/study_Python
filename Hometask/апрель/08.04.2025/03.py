def square(sym,n,fill):
    line=n*sym
    if fill:
        for i in range(n):
            print(line)
    else:
        print(line)
        for i in range(n-2):
            print(sym+"  "*(n-2)+sym)
        print(line)    
        
        
square("* ",3,True)

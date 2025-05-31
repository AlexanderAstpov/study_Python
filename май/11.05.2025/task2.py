fl = open("_writelines.txt", "r", encoding="utf-8")

lst = fl.readlines()

fl.close()

fl = open("task2.txt", "w", encoding="utf-8")

fl.write(lst[-2])

fl.close()
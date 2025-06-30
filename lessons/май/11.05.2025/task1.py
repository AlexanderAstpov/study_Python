fl = open("_writelines.txt", "r", encoding="utf-8")

lst = fl.readlines()[::-1]

fl.close()

fl = open("task.1.txt", "w", encoding="utf-8")

fl.writelines(lst)

fl.close()

import os
def ans(somh):
    path = somh
    glist = []
    n = int(input("Введите кол-во значений: "))
    for i in range(n):
        tt = input()
        glist.append(tt)
    f = open(path, "w")
    print("Добавление данных элементов: ")
    print(glist)
    for i in glist:
        f.write(str(i) + " ")
    f.close()

    f = open(path, "r")
    print(f.read())

s = input()
ans(s)
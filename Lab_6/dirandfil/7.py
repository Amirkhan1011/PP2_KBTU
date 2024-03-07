def ans(somh, somh2):
    path = somh
    path2 = somh2
    f = open(path, "r")
    f2 = open(path2, "w")
    for i in f:
        f2.write(str(i))
    f2.close()
    f.close()

    f2 = open(path2, "r")
    for i in f2:
        print(i)

s = input()
s2 = input()
ans(s,s2)
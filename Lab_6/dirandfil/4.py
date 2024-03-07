import os
def ans(somh):
    path = somh
    f = open(path, "r")
    count = 0
    for i in f:
        if(i != "\n"):
            count += 1
    print(count)

s = input()
ans(s)
import os
def ans(somh):
    path = somh
    if os.access(path, os.F_OK):
        print("Your path exists")
        x = os.path.split(path)
        print("The directory of the file:", x[0])
        print("The name of file:", x[1])
    else:
        print("Your path does not exist")

s = input()
ans(s)
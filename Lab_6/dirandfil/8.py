import os
def ans(somh):
    path = somh
    if(os.access(path, os.F_OK)):
        print("Your path exist")
        os.remove(path)
        print("Deleted")
    else:
        print("Your path does not exist")

s = input()
ans(s)

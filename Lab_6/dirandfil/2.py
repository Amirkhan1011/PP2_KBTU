import os
def ans():
    path = r"C:\Users\ospan\Documents\github\PP2_KBTU\Lab_6"
    path1 = os.access(path, os.F_OK)
    if(path1 == True):
        print("Your file exists")
    else:
        print("Your file does not exist")
    path2 = os.access(path, os.R_OK)
    if(path2 == True):
        print("I can read your file")
    else:
        print("I can not read your file")
    path3 = os.access(path, os.W_OK)
    if(path3 == True):
        print("I can write something in your file")
    else:
        print("I can not write anything in your file")
    path4 = os.access(path, os.X_OK)
    if(path4 == True):
        print("I can execute your file")
    else:
        print("I can not execute your file")

ans()
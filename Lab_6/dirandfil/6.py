import os
def ans():
    path = r"C:\Users\ospan\Documents\github\PP2_KBTU\Lab_6\dirandfil\a-z"
    for i in range(65, 91):
        name = os.path.join(path, chr(i) +".txt")
        f = open(name, "a")
    for i in os.listdir(path):
        print(i, end = ", ")

ans()
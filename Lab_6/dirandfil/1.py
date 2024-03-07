import os


def ans():
    print("All folders in this path: ")
    for i in os.listdir(r"C:\Users\ospan\Documents\github\PP2_KBTU"):
        if os.path.isdir(os.path.join(r"C:\Users\ospan\Documents\github\PP2_KBTU", i)):
            print(i)
    print("\nAll files in this path: ")
    for i in os.listdir(r"C:\Users\ospan\Documents\github\PP2_KBTU"):
        if os.path.isfile(os.path.join(r"C:\Users\ospan\Documents\github\PP2_KBTU", i)):
            print(i)
    print("\nAll files and folders: ")
    for i in os.listdir(r"C:\Users\ospan\Documents\github\PP2_KBTU"):
        print(i)

ans()
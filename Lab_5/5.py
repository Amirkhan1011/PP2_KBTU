import re
def ans():
    txt = input()
    x = re.findall("^a.*b$", txt)
    print(x)
ans()
import re

def ans():
    txt = input()
    x = re.findall("ab", txt)
    print(x)
ans()
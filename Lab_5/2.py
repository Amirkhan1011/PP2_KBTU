import re
def ans():
    txt = input()
    x = re.findall("ab{2,3}", txt)
    print(x)

ans()
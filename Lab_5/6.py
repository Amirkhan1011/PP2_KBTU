import re
def ans():
    txt = input()
    x = re.sub("\s", ":", txt)
    x = re.sub("[.]", ":", x)
    x = re.sub(",", ":", x)
    print(x)
ans()
import re
def ans():
    txt = input()
    x = re.findall("^a.*b$", txt)
    print(x)
ans()


def splitUpper():
    txt = input()
    x = txt
    for i in range(0, len(x)):
        if x[i].isupper():
            x1 = x[:i]
            x2 = x[i + 1:]
            x = x1 + ' ' + x2
    # l = x.split(' ')
    l = re.split("\s", x)
    l2 = []
    for i in l:
        if len(i) != 0:
            l2.append(i)
    print(l) # if AskarOralkhan [ [], 'skar', 'ralkhan' ]
    print(l2)
# splitUpper()

def splitUpper2():
    txt = input()
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    print(x)
# splitUpper2()

def camelToSnake():
    txt = input()    
    x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
    # camelCase
    # print(x)
    # camel Case
    x = x.split(' ')
    s = ''
    for i in range(0, len(x)):
        s += x[i].lower() + '_'
    print(s[:-1]) # deleting last character
# camelToSnake()
def ans(s):
    x = 0
    y = 0
    for i in s:
        if i.islower() and i != ' ':
            x += 1
        elif i.isupper() and i != ' ':
            y += 1
    print(f"Number of upper case letters: {y}")
    print(f"Number of lower case letters: {x}")


u = "sdfkdksf KKKK"
ans(u)
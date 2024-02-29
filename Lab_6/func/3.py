def ans(s):
    pal = ''.join(reversed(s))
    if pal == s:
        print("Palindorme")
    else:
        print("Not palindrome")



u = "kbbk"
ans(u)
tt = (1, 0, 1, 2, "Olz", True, "True")

def ans(t):
    security = True
    for i in t:
        if i == False:
            security = False
    print(security)

ans(tt)
zakonoslyzhnyi = (1,1,1,True,True,True)
ans(zakonoslyzhnyi)
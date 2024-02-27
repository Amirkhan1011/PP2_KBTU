def squares():
    a = int(input())
    b = int(input())
    x = (i**2 for i in range(a, b +1))
    for i in range((b - a) + 1):
        print(next(x), end = ' ')

squares()
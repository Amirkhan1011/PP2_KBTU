def ans():
    n=int(input())
    a=(i for i in range(n, -1, -1))
    for i in range(n+1):
        print(next(a), end = ' ')

ans()
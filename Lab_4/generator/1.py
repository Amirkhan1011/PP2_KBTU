def ans():
    n=int(input())
    a=(i**2 for i in range(1, n))
    for i in range(n-1):
        print(next(a), end = ' ')

ans()
def ans():
    n=int(input())
    a=(i for i in range(0, n))
    for i in range(n):
        num = next(a)
        if num % 3 == 0 and num % 4 == 0:
            print(num, end = ' ')
ans()
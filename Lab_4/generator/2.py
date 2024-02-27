def ans():
    n=int(input())
    a=(i for i in range(0, n))
    for i in range(n):
        num = next(a)
        if num % 2 == 0 and i != n - 1:
            print(num, end = ', ')
        elif num % 2 == 0 and i == n - 1:
            print(num, end ='.')
ans()
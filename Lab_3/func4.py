def prime_check(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

inp = input("Введите числа, разделенные пробелами: ")
numbers = [int(x) for x in inp.split()]

res = [prime_check(num) for num in numbers]

print(res)

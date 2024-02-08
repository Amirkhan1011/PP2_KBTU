from itertools import permutations

def ans(strr):
    perms = permutations(strr)
    res = ' '.join([''.join(perm) for perm in perms])
    print(res)

x = input("Enter a string: ")

ans(x)

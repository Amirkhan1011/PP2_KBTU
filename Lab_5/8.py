import re

def ans(somh):
    result = re.sub('([a-z])([A-Z])', r'\1 \2', somh)
    return result

s = input()
res = ans(s)

print("Original String:", s)
print("Split Result:", res)

import re

def ans(somh):
    result = re.sub('([a-z])([A-Z])', r'\1_\2', somh)
    return result

s = "ThisSplitStringAtUppercaseLetters"
output_result = ans(s)

print("Original String:", s)
print("Split Result:", output_result)

import re

def ans(input_string):
    result = re.sub('([a-z])([A-Z])', r'\1_\2', input_string)
    return result

input_string = "ThisSplitStringAtUppercaseLetters"
output_result = ans(input_string)

print("Original String:", input_string)
print("Split Result:", output_result)

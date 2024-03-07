import re

def split_at_uppercase(input_string):
    result = re.sub('([a-z])([A-Z])', r'\1 \2', input_string)
    return result

# Example usage:
input_string = "SplitThisString At UppercaseLetters"
output_result = split_at_uppercase(input_string)

print("Original String:", input_string)
print("Split Result:", output_result)

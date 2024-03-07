import re

def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+'

    matches = re.findall(pattern, text)

    return matches

input_text = "This is_a sample_string with_multiple sequences_of_lowercase_letters_joined_with_underscore."
result = find_sequences(input_text)

print("Sequences found:", result)

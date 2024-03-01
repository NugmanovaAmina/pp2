import re

def match_string(pattern, text):
    # Use re.match() to see if the pattern matches the beginning of the string
    match = re.match(pattern, text)
    
    if match:
        print("Match found:", match.group())
    else:
        print("No match found")

# Pattern to match 'a' followed by zero or more 'b's
pattern = r'a*b*'

# Test strings
test_strings = ["ab", "abb", "aab", "a", "b", "bb", "abbb"]

# Match each test string against the pattern
for text in test_strings:
    print("Testing:", text)
    match_string(pattern, text)

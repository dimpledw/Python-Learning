'''Index - Each character has a position number, we call that index. 
Accessing a single element from a sequence using its position(Index).
Slicing - Extracting a portion (multiple elements) from a sequence using a start, stop and optional step.
'''

string1 = "hello"
print(string1[0])

# String Slicing [start:end]
print(string1[0:4])
print(string1[-5:-1])

# Open Ended slicing - [start:end] - Here start is included and end is not included.

print(string1[0:])
print(string1[:4])

print(string1[-3:])
print(string1[-1:])
print(string1[:-4])

# [start:end:step]

print(string1[0:5:2])

# Some more Examples

text = 'Python'

# Extract the first character
print(text[0]) 
print(text[-6])

# Extract the last character
print(text[5])
print(text[-1])

# Extract h
print(text[3])
print(text[-3])

# Extract year
date = "2026-09-20"
print(date[0:4])
print(date[:4])
print(date[:-6])

# Extract the Month
print(date[5:7])
print(date[-5:-3])

# Extract the day
print(date[8:])
print(date[-2:])

# Data Cleansing - Remove Spaces (Whitespace cleanup) 
# It removes tabs and multiple spaces

text = " Engineering"
print(text.lstrip())            # To remove space from left side

text = "Engineering "
print(text.rstrip())            # To remove space from right side

text = " Engineering "
print(text.strip())             # To remove space from both the sides

text = "Data Engineering"
print(text.strip())             # It won't remove spaces from the middle or anything inside the text

text = "Data Engineering"
print(text.replace(" ",""))     # This will remove the space from the middle

text = "###Data Engineering###"
print(text.strip("#"))          # This will remove the '#'

# Use Case - Detect Extra Spaces
text = " Engineering"
print(len(text))
print(len(text.strip()))
no_of_spaces = len(text) - len(text.strip())
print("Number of Spaces are", no_of_spaces)
is_clean = len(text) == len(text.strip())
print("Is your data clean?", is_clean)






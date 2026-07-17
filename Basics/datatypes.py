'''
Data Types
Strings - "Hello"
Integer - 2
Float - 2.48
Boolean - True of False
'''

# Subscripting - To get any letters (individual character) from the string. Below output will be o.
print("Hello"[4])
print("Hello"[-1]) # This will give o as well

print("Hello"[0]) # Output will be H

print("1234" + "2345") # This will just concat the strings

# Integer - Whole Number
print(123+345) # Output will be 468

# When we write large number integer, usually we put commas between large integers to easy to understand but 
# in python we put underscore
print(123,456,789) # Output will be 123 456 789
print(123_456_789) # Output will be 123456789

# Float - Numbers with decimal
print(3.14)

# Boolean - True or False
print(True)
print(False)

# Coding Exercise
street_name = "Abbey Road"
print(street_name[4] + street_name[7]) # Output will be yo

'''
Type Error, Type Checking and Type Conversion
'''

#print(len(123)) # This will give a type error as len doesn't work with integer

# In order it to work
print(len("123")) # len work with certain datatypes

# To check datatype of an object, we use type function

print(type("Hello")) # Output will be string

# Coding Exercise - Write out 4 type checks to print all 4 data types
print(type("Reader"))
print(type(1234))
print(type(12.28))
print(type(True))

# Type Conversion or Type Casting

#print(int("abc") + int("234")) # This will give a ValueError means it doesn't make sense to convert abc to int

# Coding Exercise 
# Make the below code work
# print("Number of letters in your name: " + len(input("Enter your name")))

print("Number of letters in your name: " + str(len(input("Enter your name?\n"))))






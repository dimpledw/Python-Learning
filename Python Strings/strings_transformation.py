# String Transformations

name = "Alexa"
age = 24

print(type(age))
print("Your age is:", age) # This will work because python automatically converts age (an integer) into a displayable form.
#print("Your age is:" + age) # This won't work because it can only concat string with string
print("You age is:" + str(age)) # This will work


# len() counts everything even spaces

text = """
Python is easy to learn.
Python is powerful.
Many people love python
"""
print(text.count("Python")) # Here count is a string method. It counts how many times substring("Python") appears.
# It is also case-sensitive.

# Data Transformations

date1 = "2026/05/10"
print(date1.replace("/","-")) # Replace is a method. It will replace any value. It needs two arguments(old value and new value)

price = "1234,56"
print(price.replace(",","."))

phone = "916-197-1892"
print(phone.replace("-","/"))

phone = "916-197-1892"
print(phone.replace("-","")) # Here replace will remove the -

price = "$1,299.99"
print(price.replace("$","").replace(",","")) # We can chain as many replaces we want

'''
Coding Challenge - Convert the messy phone number into a clean number format with only digits
"+89 (104) 123-4567" -> 00891041234567
'''

number = "+89 (104) 123-4567"
print(number.replace("+", "00").replace(" ","").replace("(","").replace(")","").replace("-",""))

# Join Strings
folder = "C:/Users/report_final/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)

# f-strings - here f is formatted string. It easily lets us put variables and expressions directly inside string value

name = "Alexa"
age = 34
is_student = False

print(f"My name is {name}. I am {age} years old and student status is {is_student}.")

print(f"2+3 = {2+3}")

# String Split - It splits the value in multiple values. It gives result in list

stamp = "2026-09-20 14:30"
print(stamp.split(" ")) # Output will be ['2026-09-20', '14:30']

stamp = "2026-09-20"
print(stamp.split("-")) # Output will be ['2026', '09', '20']

csv_file = "1234,Maxi,USA,1970-10-05,F"
print(csv_file.split(","))

# String Repetation

print("ha" * 3)
print("-" * 10)
print("-" * 10)






# String Functions - Searching

# It checks if the string starts with a specific word
phone = "+89-176-12345"
print(phone.startswith("+89"))

# It checks if the string ends with a specific word
email = "python@gmail.com"
print(email.endswith("gmail.com"))

file = "data_backup.csv"
print(file.endswith(".csv"))

# It checks if the word exists in the string
email = "python@gmail.com"
print("@" in email)

url = "https://api.company.com/v1/data"
print("//api" in url)

# Find - find() is great when combined with other methods to add dynamics

# Example - We are trying to find the phone number excluding the country code
phone1 = "+89-176-12345"
phone2 = "89-654-15248"
phone3 = "0089-342-29182"
print(phone1[4:])
print(phone2[3:]) # Hardcoding the position doesn't work when the country code length changes. It's not the ideal approach
print(phone3[5:])

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

# String Functions - Validation
# Use Case - Prevent invalid or garbage data from entering our system

country = "USA"
print(country.isalpha())  # isalpha() will check if our string contains only alphabets

country = "USA1"
print(country.isalpha())  # This will print False

phone = "01232124514"
print(phone.isnumeric())  # isnumeric() will check if our string contains only numbers

phone = "01a32124514"
print(phone.isnumeric())  # This will print False

# This will print False as it just accepts numbers. 
# Not even floating numbers as it considers . as special character

phone = "3.145"
print(phone.isnumeric())  







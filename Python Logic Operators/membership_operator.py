# Membership Operator - Checks if a value inside another value - in or not in

print("o" in "Python")
print("f" in "Python")
print(not "f" in "Python")
print(3 not in [1,2,3])

# Validate that the domain is not on the banned list
domain = "gmail.com"
banned_domain = ["spam.com","fake.org", "bot.net"]
print(domain not in banned_domain)

# identity Operators - Checks if two variable refer to the same object in memory.

a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)      # This will print False

a = 4
b = 4
print(a == b)
print(a is b)      # This will print True

x = ['a','b','c']
y = ['a','b','c']
print(x == y)      # This will print True
print(x is y)      # This will print False

x = ['a','b','c']
y = x
print(x == y)      # This will print True
print(x is y)      # This will print True

x = 'a'
y = 'a'
print(x == y)      # This will print True
print(x is y)      # This will print True

# Validate the email address. It must be filled in and not empty
email = ""
print(email != "")

email = None
print(email != "")

email = None
print(email is not None and email != "")  # Use is instead of == when checking for None

''' Coding Exercise 
1. Check if a user's name is not empty and the age is greater than or equal to 18
2. Check if the password is atleast 8 characters long and doesn't contain spaces
3. Check if a user's email is not empty, contains '@' and ends with '.com'
4. Check if a username is a string, is Not None and is longer than 5 characters
5. Check if the user is either an admin or a moderator, and either they are not banned or they've verified their email.
'''
# Solution 1
user_name = input("Enter your name?\n")
age = int(input("Enter your age?\n"))
print(user_name != "" and age >= 18)

# Solution 2
password = input("Enter a password.\n")
print(len(password) >= 8 and " " not in password)

# Solution 3
user_email = input("Enter your email\n")
print(user_email != "" and '@' in user_email and user_email.endswith(".com"))

# Solution 4 - Attempt 1
user_name = input("Enter your username\n")
# user_name = 1234456
user_name_type = type(user_name)
print(user_name_type == str and user_name is not None and len(user_name) > 5)

# Solution 4 - Attempt 2
user_name = input("Enter your username\n")
print(isinstance(user_name, str) and user_name is not None and len(user_name) > 5)


# Solution 5
# Attempt - 1
# user_job = input("Enter your job\n")
# user_banned = bool(input("Is user banned? Type True or False\n"))
# print(user_banned)
# email_verified = bool(input("Is your email verified\n"))
# print(email_verified)
# print(user_job == ('admin' or 'moderator') or email_verified == True) and user_banned != True

# Attempt -2

user_job = input("Enter your job\n")
user_banned = input("Is user banned? Type True or False\n").lower() == "true"
email_verified = input("Is your email verified? Type True or False\n").lower() == "true"
print((user_job == "admin" or user_job == "moderator") and (not user_banned or email_verified))

# Attempt - 3
user_job = 'admin'
user_banned = True
user_verified = False
print((user_job == 'admin' or user_job == 'moderator') and (user_banned != True or user_verified != False))


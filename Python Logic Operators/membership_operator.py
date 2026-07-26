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
1. Check if a user's name is not empty and the age is greater that or equal to 18
2. Check if the password is atleast 8 characters long and doesn't contain spaces
3. Check if a user's email is not empty, contains '@' and ends with '.com'
4. Check if a username is a string, is Not None and is longer than 5 characters
5. Check if the user is either an admin or a moderator, and either they are not banned or they've verified their email.
'''


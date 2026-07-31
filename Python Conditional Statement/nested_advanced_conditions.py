# Nested If - If statement inside another if "if the first is true, then check the second"

score = 95
submitted_project = False
if score >= 90:
    if submitted_project == True:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail") 

# Connecting Conditions

score = 95
submitted_project = True
if score >= 90 and submitted_project == True:    # We can also write submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail") 


score = 50
submitted_project = True
if score >= 90 and submitted_project == True:    # We can also write submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60 or submitted_project:
    print("Grade D")
else:
    print("Fail") 


# Independent Ifs 
# Each if is checked separately. All conditions are tested - even if one is already true.

score = 50
submitted_project = False
if score >= 90:
    print("High score")
else:
    print("Low score")
if submitted_project == True:
    print("Project is submitted")
else:
    print("Not submitted")

# Inline if statement (Ternary)
# If you have simple logic, use inline-if
# For complex logic, use classical if

score = 100
grade = ("A" if score >= 90 else "F")
print(grade)

score = 80
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)

# Case Match - Evaluate a value against multiple values. Run the code of the first match.
# Convert the full country names into 2-letter abbreviations

country = "India"
if country == "South Korea":
    print("SK")
elif country == "India":
    print("IN")
else:
    print("Unknown Country")


match country:
    case "United States" | "USA":
        print("US")
    case "India":
        print("IN")
    case _:
        print("Unknown Country")

'''Coding Exercise - 1
Validate the quality and correctness of email values
1. Must not be empty
2. Must contain '.' and '@'
3. Must contain exactly one '@' symbol
4. Must end with '.com', '.org' or '.net'
5. Must not be longer than 254 characters
6. Must start and end with a letter or digit 
'''

email = input("Enter your email\n")
email = email.strip()
if email == "":
    print("Email must not be empty")
elif '.' not in email and '@' not in email:
    print("Email must contain . and @")
elif email.count('@') != 1:
    print("Email should contain exactly one @")
elif not email.endswith(('.com', '.org', '.net')):
    print("Must end with '.com', '.org' or '.net'")
elif len(email) > 254:
    print("Email must not be longer than 254 characters")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print(f"Your email is {email}")


'''Coding Exercise - 2
Validate the quality and correctness of email values
1. Must not be empty
2. Must be atleast 8 characters
3. Must include atleast one uppercase
4. Must include atleast one lowercase
5. Must not be same as the email
6. Must not contain any spaces 
'''
# Attempt - 1
password = input("Enter your password\n")
email = input("Enter your email\n")
if password == "":
    print("Pasword must not be empty")
elif not(len(password) >= 8):
    print("Password must be atleast 8 characters")
elif not(password.isupper()):
    print("Password must include atleast one uppercase")
elif not(password.islower()):
    print("Password must include atleast one lowercase")
elif password.lower() == email.lower():
    print("Password must not be same as email")
elif " " in password:
    print("Password must not contain any spaces")
else:
    print("Your password is created")




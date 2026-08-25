# Advanced For Loop
# Break Statements - It stops the loop immediately 

names = ['John','Maria', '', 'Kumari']
for name in names:
    if name == '':
        print("Empty Value Detected")
        break
    print(f"Name - {name}")

# Continue Statement - It skips one loop cycle without stopping the loop
# Use continue to skip bad or empty data without stopping the whole loop

names = ['John','Maria', '', 'Kumari']
for name in names:
    if name == '':
        continue
    print(f"Name - {name}")

# Pass Statement - It is a placeholder where nothing happens - For now, just keep going and do nothing

names = ['John','Maria', '', 'Kumari']
for name in names:
    if name == '':
        print("Empty Value Detected")
        pass                                  # todo: Handle Empty Value
    print(f"Name - {name}")


names = ['John','Maria', '', 'Kumari']
for name in names:
    if name == '':
        name = name.replace('', 'Unknown')                                       
    print(f"Name - {name}")


'''
Coding Exercise - Loop through a list of days and print only the working days, skipping the weekend
'''

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for day in days:
    if day == "Sunday" or day == "Saturday":
        print("Weekend spotted")
        continue
    print(f"Workday - {day}")

# Attempt - 2

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for day in days:
    if day in ["Sunday", "Saturday"]:
        continue
    print(f"Workday - {day}")

'''
Coding Exercise - Scan emails to block unsafe data from entering your system
'''

emails = [
    'data@gmail.com',
    'name@outlook.de',
    'drop table users;',
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print("SQL Injection - Hacker Attack")
        break
    print(f"Emails - {email}")

## For Critical Risk like cost, security, integrity - use break
## For medium risks like bad rows, empty files/data, skip special cases - use continue
## For low risk, if we have something planned for it (put a placeholder) - use pass

items = [2,4,6,8]
for i in items:
    print(i)
else:  # There is no sense to include else here
    print("Loop is completed")

## Use Case - Use else with loops only when there's a break

## Task - Check for even numbers

items = [1, 3, 4, 5, 7]
for i in items:
    if i%2 == 0:
        print("Even Number Found", i)
        break
else:
    print("All numbers are odd")


items = [1, 3, 5, 7]
for i in items:
    if i%2 == 0:
        print("Even Number Found", i)
        break
else:
    print("All numbers are odd")

## Task - Check for Missing names in a list

names = ['Maria', 'Rosie', None, 'Myra']
for name in names:
    if name is None:
        print(f"Missing name found!")
        break
else:
    print("All names are fine")

names = ['Maria', 'Rosie', 'Mira', 'Myra']
for name in names:
    if name is None:
        print(f"Missing name found!")
        break
else:
    print("All names are fine!")

## Task - Check if all files are CSV files

files = ['data1.csv', 'data2.csv', 'report.pdf', 'data3.csv', 'data4.txt']
for file in files:
    if not file.endswith('.csv'):
        print(f"{file} is not a csv")
        break
else:
    print("All files are CSV")



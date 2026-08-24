# For-Else Loop

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

## It makes no sense to use else + continue

'''
Coding Exercise - Check whether any filename appears more than once
'''

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'data.csv'
]
for file in file_list:
    if file_list.count(file) == 2:
        print("Duplicate found")
        break
else:
    print("All files are unique")

## Attempt - 2

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
for file in file_list:
    if file_list.count(file) == 2:
        print("Duplicate found")
        break
else:
    print("All files are unique")

## Nested Loops - Loop inside another loop
for x in (1,2,3):
    for y in (1,2):
        print(x,y)

for x in range(3):
    for y in range(2):
        for z in range(2):
                    print(f"({x}, {y}, {z})")
            

# Use Cases for Nested Loop - Crossing/Cartesan Data or Navigate Hierarchy

# Crossing Data
colors = ['red', 'black', 'purple']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f"({color} - Size {size})")

# Navigate Hierarchy

years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)
for year in years:
    for month in months:
        for day in days:
            print(f"Report_{year}_{month}_{day}.csv")

# Select count(*) from customers where id is NULL;

tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']
for table in tables:
    for column in columns:
        print(f"SELECT count(*) from {table} where {column} is Null;")

        


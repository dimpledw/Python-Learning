'''
Control Flow Statements 
Loops are repeated tasks. They repeat a block of code over and over until a condition is met. 
Types are For and while. To control the flow of our code, we use break pass continue
'''

# For Loops - Go through a list of items one by one to do something for each item - 
# We define loop variable - Variable to assign the current value of the sequence
# Python Iterator - An object that lets you go through items one by one in a sequence. (Remember what's done. Knows what's next)

for i in (1,2,3):
    print(f"Round: {i}")

items = (1,2,3,4,5)
for item in items:
    print(f"Round: {item}")

# Sequences which we can loop - In sequence we can give combination of any datatype (int, str, numbers)
items = (1,2,3,4,"Hello")
for item in items:
    print(f"Round: {item}")

items = " Python "
for item in items:
    print(f"Round: {item}")

for item in range(1, 5):              # 1 is start and 5 is stop. Start is always inclusive and stop is exclusive
    print(f"Round: {item}")


for item in range(0, 10, 2):              # 1 is start and 5 is stop. Start is always inclusive and stop is exclusive
    print(f"Round: {item}")

# For Loop use cases
# Aggregations
scores = [80,50,60,75]
total = 0
for score in scores:
    total += score
    print(f"Current Total is {total}")
print(f"Final Total is {total}")

# Transform data like cleaning data before processing

files = [' Report.csv', 'DATA.csv ', ' final.TXT']
for file in files:
    file = file.strip().lower().replace(".txt",".csv")
    print(f"Processing {file}")

''' Coding Exercise - 1
Print the 7-times table from 1 to 10 using a For Loop '''

# Attempt - 1
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    number *= 7
    print(f"Seven table {number}")

# Attempt - 2
for number in range(1, 11):   
    number *= 7          
    print(f"Seven Table {number}")

# Attempt - 3
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    result = number * 7
    print(f"7 * {number} = {result}")

'''Coding Exercise - 2
Print a left aligned pyramid of stars with 6 rows using a for loop '''

# Attempt - 1
numbers = [1,2,3,4,5,6]
for number in numbers:
    result = number * 1
    print(f"{'*' * result}")

# Attempt - 2
for number in range(1,7):
    print(f"{'*' * number}")
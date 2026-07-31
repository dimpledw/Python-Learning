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



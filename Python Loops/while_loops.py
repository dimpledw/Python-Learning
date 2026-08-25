# WHILE LOOPS - Repeats a block of code over and over again as long as condition is True
# Task - Build a counter from 1 to 5

count = 1
while count <= 10:
    print(count)
    count += 2

# Write a program that keeps asking "Do you agree?" until the user types "yes"

answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ")
print("Thank you")

# While True

while True:
    answer = input("Do you agree?(yes/no): ")
    if answer == "yes":
        break
print("Thank you")

# For v/s While
# For Loop - Loop over a fixed sequence. Predefined condition. No. of iteration is known.
# While Loop - Loop while a condition is True. We define a condition. No of iteration is unknown 

'''
Coding Exercise - 
while True:
    answer = input("Do you agree?(yes/no): ")
    if answer == "yes":
        break
print("Thank you")
1. Allow up to 3 attempts
2. If the user types "yes", print "Glad we are on the same page"
3. Otherwise print, "3 strikes, You are out!"
'''
attempts = 0
while attempts < 3:
    answer = input("Do you agree?(yes/no): ")
    if answer == "yes":
        print("Glad we are on the same page!")
        break
    attempts += 1
else:
    print("3 strikes, You are out!")




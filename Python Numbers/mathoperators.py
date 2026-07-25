# Mathematical Operators

print("My Age" + str(18))
print(123+456) # Addition
print(7-3) # Subtraction
print(2*4) # Multiplication
print(6/3) # This will give us 2.0 (float type). In divisoon, we always get float as result even if number gets divide cleanly. 
#This is called implicit typecasting where python itself typecasts the result into float
print(6//3) # This will give us integer and wipes out any decimal number. This will give 2 (int type)
print(5//3) # This will give us 1 (type int)
print(2**2) # This will give us 4 (type int)

#PEMDAS - (), **, *, /, +, -

#Coding Exercise 1

print(3*3+3/3-3) # Output will be 7.0

#Coding Exercise 2 - Change the above code to get 3 instead of 7

print(3+3*3/3-3)

# Coding Exercise 3: BMI Calculator

'''
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
This is the formula used to calculate it:
bmi is equal to the person's weight divided by the person's height squared.
'''

height = 1.65
weight = 84

bmi = weight/(height**2)

print(bmi)

# Number Manipulation and F strings in Python

# Since bmi is quite a large number, we can round it off using round function 

print(round(bmi))

print(round(bmi, 2))

score = 0
score += 1 # When user scores a point
print(score)

# F-string - With f-string we don't have to type cast the data type

score = 0
height = 5.8
is_winning = True

print(f"Your score is = {score} and {height}. You are winning {is_winning}")

# Coding Exercise 4

# What will be the output of this? 

print(6 + 4 / 2 - (1 * 2)) # Output will be 6.0

# Coding Exercise 5

# What is the data type of the result of the variable a in the following line of code:

a = int("5") / int(2.7)
print(type(a))




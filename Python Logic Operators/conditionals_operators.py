'''
Conditional - If/Else
If condition:
    do this
else:
    do this
'''

# Write a program to find user's height and if user's height is greater than 120cm, they can ride or else they can't

height = int(input("What is your height in cm?\n"))
if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, You can't ride. Height Criteria didn't meet!")


# Comparison Operators - >, <, >=, <=, ==, !=
# = means when we are assigning some value. Example - a = 4 or name = input("Enter your name")
# == means to check equality. To check if value on the left is equals to value on right. Example height == 120
# Modulo Operator % - 10 % 2 = 0(It gives the remainder)

# Write a program to find if a number is even or odd?

number = int(input("Enter any number?\n"))
if number%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")


# Nested if/else
# Write a program to find height. If height is greater than 120, then you can ride or you cannot. 
# Ask for age. If age is under 12 then price is $5, if age is between 12 and 18, price is $7 or else proce is $12.
# Further ask if person wants a photo, if yes, then add $3 to the bill.

height = int(input("What is your height in cm?\n"))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Your ticket price is $5")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Your ticket price is $7")
    else:
        bill = 12
        print("Your ticket price is $12")
    
    photo = (input("Do you want photos? Yes or No \n"))
    
    if photo == "Yes":
        bill += 3
    print(f"You total bill is: ${bill}")

else:
    print("Sorry, You can't ride. Height Criteria didn't meet!")


# Write a program to calculate BMI of a person. If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

height = float(input("Enter your height?\n"))
weight = int(input("Enter your weight?\n"))
bmi = int(weight/(height**2))

print(f"Your BMI is {bmi}")
if bmi < 18.5:
    print("You are underweight")
elif bmi >=18.5 and bmi < 25:
    print("You have Normal Weight")
else:
    print("You are overweight")

# Logical Operators - And, or, Not
# And - Both conditions must be true
# Or - Either condition should be true














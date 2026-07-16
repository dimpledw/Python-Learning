'''
A variable is a name we create to store a value, so we can use it later in our code.
'''

name = input("What is your name? ")
print(name)

# We can change the value of a variable

name = "Rabbit"
print(name)

# To find the length of the string, use len()
 
name = input("What is your name? ")
length = len(name)
print(length)

name = "Rabbit"
print(len(name))

'''
Coding Exercise - We have 2 variables glass1 and glass2. 
glass1 contains milk and glass2 contains juice. 
Write 3 lines of code to switch the contents of the variables. 
You are not allowed to type the words "milk" or "juice". 
You are only allowed to use variables to solve this exercise.
'''

glass1 = 'milk'
glass2 = 'juice'
temp = glass1
glass1 = glass2
glass2 = temp
print("Glass 1 is " + glass1)
print("Glass 2 is " + glass2)

# Another way of solving 

glass1 = "milk"
glass2 = "juice"
(glass1, glass2) = (glass2, glass1)
print(glass1)
print(glass2)


'''
Varible Naming
While naming variable, be mindful as it should make sense even 
after you read it after 6-9 months. Writing meaning variable names 
makes our code more readable. 
Try to avoid giving function name as variable name. It will create confusion.
Name Error is probably because you misspell or mistype the variable name.
'''

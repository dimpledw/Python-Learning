# Data Structures - Ways to store and organize data

# List - List stores multiple items in order and can be changed. Stored in []

states_of_canada = ['Ontario','Nova Scotia','British Columbia']
print(states_of_canada[0]) # This 0th index will print first item in the list which is Ontario

# To change the value of a list
states_of_canada[0] = 'Alberta'
print(states_of_canada[0])

states_of_canada = ['Alberta','Nova Scotia','British Columbia']
print(states_of_canada[0])

states_of_canada.append("lalalandstate") # append is used to add an item at the end of the list
print(states_of_canada) # This will print ['Alberta','Nova Scotia','British Columbia', 'lalalandstate']

# Coding Exercise - Write a program to figure out how to pick a random name from the list of friends.

import random
friends_list = ["April", "June", "Wednesday", "Alexa", "Siri"]
random_friends = random.choice(friends_list)
print(f"Person who will pay the bill is: {random_friends}")


random_index = random.randint(0,4)
print(random_index)

# Here random_index is in square bracket because we are accessing an item 
#from a list using it's index
print(friends_list[random_index]) 

# Index Errors - A list index error happens when we try to access an index that doesn't exist in a list

# Nested Lists
fruits = ["Apple", "Banana", "Cherry", "Pears", "Orange"]
vegetables = ["Spinach", "Kale", "Okra", "Opo Squash"]
food = [fruits, vegetables]
print(food)
print(food[1])
print(food[0][1])  

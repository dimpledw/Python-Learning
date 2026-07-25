'''
Random Module - To generate random whole numbers
random.randint(a,b) To generate whole numbers between a and b. Inclusive of a and b
random.random - To generate float number between 0 and 1 where 0 is inclusive.
random.uniform - To generate float number between a and b where both a and b are inclusive.
Use Case - To generate test data (dummy) for like age, ID or prices
Random Sampling - Picking a smaller, random part of a huge dataset
'''
import random

random_integer = random.randint(1, 100)
print(random_integer)

random_random = random.random()
print(random_random)

random_float = random.uniform(1, 100)
print(random_float)

# Coding Exercise - Write a program to find heads and tail

import random

random_integer = random.randint(1, 1000)
print(random_integer)
if random_integer >= 1 and random_integer <= 500:
    print("Heads")
elif random_integer > 500 and random_integer <= 1000:
    print("Tails")

# Another way
import random

random_integer = random.randint(0, 1)
print(random_integer)
if random_integer == 0:
    print("Heads")
else:
    print("Tails")


# Coding Exercise - Generate a random integer number between 1 and 100, and check if the result is an even number

import random
random_integer = random.randint(1,100)
if random_integer%2 == 0:
    print(f"{random_integer} is an even number")
else:
    print(f"{random_integer} is an odd number")
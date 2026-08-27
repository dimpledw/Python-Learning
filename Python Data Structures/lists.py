# Data Structure - Way of organizing and storing data so it can be used efficiently.
# list[]
# tuple()
# set{}
# dict{}

# Function - A resuable block of code that performs a task and is called independently. function(variable) e.g - len(variable)
# Method - A method belongs to an object (such as list, string, dictionary etc). variable.method e.g - variable.append()

# Lists - is ordered collection of items. It can be changeable, allows duplicates
# Create Lists
empty = []
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
mixed = [1, 'a', True, None]  # In list, we can store different data type
print(mixed)
print(type(mixed))


empty = list()
print(empty)

letters = list('Python')
print(letters)

numbers = list(range(5))
print(numbers)

# Nested Lists Matrix - List inside a list

matrix = [['a', 'b', 'c'], ['d', 'e', 'f']]
mixed_matrix = [['a','b','c'], [1,2,3,4], [True]]
print(mixed_matrix)
print(type(mixed_matrix))

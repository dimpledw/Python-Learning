
''' Number Functions - Rounding Numbers
Sometimes numbers are messy, so we round them to make results easier to read and work with
Flooring means round to the lower number like 1.2 to 1, 1.7 to 1
Ceiling means round to the higher number like 1.7 to 2, 1.8 to 2 1.1 to 2
Rounding means rounding to the close number like 1.7 to 2, 1.1 to 1, 1.3 to 1 and 1.5 to 2
ties (like 1.5) go to the nearest even number - Example - 1.5 to 2, 2.5 to 2 (as 2 is the nearest even number)
'''

import math
price = 272.36272
print(round(price))
print(round(price, 2))     # This will print 272.36 (rounding to 2 places)

# Floor() is not a built-in function. Floor() belongs to math module. We need to import it before using it.

print(math.floor(price))    # This will print 272

# Ceil() - Perfect for Data Engineering - like splitting data into pages or batches
print(math.ceil(price))     # This will print 273

# trunc() cuts off the decimal part and keeps the whole number(no rounding)
print(math.trunc(price))    # This will print 272

# We can also use int() to do the same
print(int(price))           # This will also print 272

# int() vs trunc()
# if you are not using math module, just use int(), it's simple and built-in
# If you already imported the math module, use trunc() it makes your intent clearer

# Number Functions - Validation
# is_integer() - Checks if a float has no decimal part (is a whole number)

x = 7.0
print(x.is_integer())

y = 8.2
print(y.is_integer())

# isinstance(value, type) - built in function - Checks if a value belongs to a certain data type
x = 80
print(isinstance(x, int))
print(isinstance(x, float))

y = 80.80
print(isinstance(y, float))

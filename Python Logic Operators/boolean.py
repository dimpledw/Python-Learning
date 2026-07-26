''' Boolean Expressions'''

print(True)
print(False)
print(type(True))

# bool(value) is true if the value is non-empty or non-zero 
# bool(value) is false if the value is empty or zero
print(bool(123))    # This will print True
print(bool())       # This will print False
print(bool(""))     # This will print False
print(bool(None))   # This will print False

# any - Returns True if atleast one value is True
# all - Returns True if all values are True

email = ""
phone = "026-372717"
username = ""

# Let's allow registration in our website if any one of the field is filled
print(any([email, phone, username]))      # This will print True

# Let's allow registration in our website if all of the field is filled
print(all([email, phone, username]))      # This will print False as only phone is filled

# isinstance checks for the value and it's datatype. Based on that it gives True or False
print(isinstance(123, int))       # This will print True
print(isinstance(True, int))      # This will print True as bool is a subclass of int
# type() will give the exact datatype and isinstance() checks whether an object is an instance of a class or any of it's parent classes

print("Hello".startswith("H"))    # This method will also print True or False
print("Hello".endswith("o"))






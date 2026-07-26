''' Boolean Expressions 
Comparison Operators - It compares two values and return True or False based on the result. == != < > >= <=
'''

print(10 == 10)
print(7> 4)
print(4 != 4)
print( 4 >= 8)
print( 4 <= 8)

# Strings can be compared too. We can compare strings too alphabetically, not just numbers
print("a" > "b")     # This will print False
print("a" < "b")     # True
print("ab" == "ab")  # True
print("a" == "A")    # False

# Chained Comparison - Check multiple conditions in one line, just like in math. It evaluates it from left to right,
# checking each condition one by one.

print(1 < 4 < 6)    # This will print True
print(5 < 4 < 6)    # This will print False. If any one condition is false, it will print False 

# Is age between 18 and 30?
age = 20
print(18 <= 20 <= 30)

''' Logical Operators - Use to combine multiple boolean expressions - and or not '''
print(3>2 and 5<1)     # This will print False
print(3>2 or 4 < 2)    # This will print True as one condition is true

# Check if the system is under pressure
cpu_usage = 70 
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)    # This will print True

# Checking user credentials before login
email = True
password = False
print(email and password)      # This will print False

# NOT Operator - It reverses the truth. It turns True into False and False into True

print(not 4 > 2)
print(not True)
print(not False)
print(not not True)

name = ""
print(not name)
print(not 0)

# Control Mixed Conditions - and has higher priority than or operator. Use () to control the order

print(4 == 4 or 2>4 and 5 < 6)
print((4 == 4 or 2>4) and 5 < 6)         # Here or will execute first as it in parenthesis
print((4 != 4 or 2>4) and 5 < 6)         # This will print False

# Allow access only if the user is logged in or they are a guest, but they must not be banned

is_logged_in = True
is_guest = False
is_banned = False

print((is_logged_in or is_guest )and not is_banned)

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest )and not is_banned)








# Conditional Statements - Checkpoints that check a condition - True? Run the code or false? - skip it
# If statement - Defines the first condition - If this is true, do this, otherwise, do nothing

score = 100
if score >= 90:
    print("A") 

# Two way Decision using else statement - Runs only if all previous conditions are false. 
# If nothing was true, do this instead

score = 90
if score >= 90:
    print("Pass")
else:
    print("Fail") 

# Multiple Conditions - Elif
# Elif statement - Asks a follow-up question. Only runs if previous conditions were false

score = 86
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Fail") 


score = 75
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail") 


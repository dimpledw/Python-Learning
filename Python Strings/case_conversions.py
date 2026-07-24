# Case Conversion
# Use Case - Standardize Text Case

text = "python PROGRAMMING"
print(text.lower())  # lower() makes all letters lowercase
print(text.upper())  # Upper() makes all letters uppercase

# Use Case - Clean Data for matching

search = 'Email'
data = "emAil"
print(search == data) # This will print False as python is case sensitive

search = 'Email'.lower()
data = "emAil".lower()
print(search == data) # This will print True 

search = ' Email'.lower()
data = "emAil".lower()
print(search == data) # This will print False 

search = ' Email'.lower().strip()
data = "emAil".lower()
print(search == data) # This will print True

'''
Coding Challenge
Turn the messy string into a single clean summary with name, role and age.
"968-Maria, ( D@t@ Engineer );; 27y  "
Clean the string to the below -
"name: maria | role: data engineer | age: 27
'''

text = "968-Maria, ( D@t@ Engineer );; 27y  "

text_replace = (text.replace("968", "name").replace("-", ": ").replace("(", "| role:").replace(")", "| age: ").replace(",","").replace("@", "a").replace(";",""))
text_strip = text_replace.strip()
print(text_strip.lower())
'''
Tip Calculator
Write a program to create tip Calculator. Ask user the total bill, how much tip they like to give? 10, 12 or 15? 
and how many people to split the bill? Then at the end print each person's share 
'''

print("Welcome to the tip Calculator")
total_bill = int(input("What was the Total Bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
total_people = int(input("How many people to split the bill?\n"))
#print(type(total_bill))
#print(type(tip))
#print(type(total_people))
each_person_share = (total_bill + total_bill * (tip/100))/total_people
final_bill = round(each_person_share, 2)

print(f"Each person should pay: ${final_bill}")


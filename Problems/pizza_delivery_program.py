print("Welcome to Pizza Shop!")
pizza_size = input("Which pizza size you want? Small, Medium or Large\n")
bill = 0
if pizza_size == "Small":
    bill = 15
    pepproni = input("Do you want Pepproni? Yes or No\n")
    if pepproni == "Yes":
        bill = bill + 2 # We can also write bill += 2
    cheese = input("Do you want to add extra cheese? Yes or No\n")
    if cheese == "Yes":
        bill = bill + 1 
    print(f"Your total bill is ${bill}")
elif pizza_size == "Medium":
    bill = 20
    pepproni = input("Do you want Pepproni? Yes or No\n")
    if pepproni == "Yes":
        bill = bill + 3 # We can also write bill += 3
    cheese = input("Do you want to add extra cheese? Yes or No\n")
    if cheese == "Yes":
        bill = bill + 1 
    print(f"Your total bill is ${bill}")
elif pizza_size == "Large":
    bill = 25
    pepproni = input("Do you want Pepproni? Yes or No\n")
    if pepproni == "Yes":
        bill = bill + 3 # We can also write bill += 3
    cheese = input("Do you want to add extra cheese? Yes or No\n")
    if cheese == "Yes":
        bill = bill + 1 
    print(f"Your total bill is ${bill}")
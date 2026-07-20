print("Welcome to Treasure Island! Your mission is to find the treasure.")
turn = input("You're at a cross road. Where do you want to go? Type 'Left' or 'Right'\n")
if turn == "Left":
    lake = input("You have come to a lake. There is an island in the middle of the lake.\n" \
    "Type 'Wait' to wait for a boat. Type 'Swim' to swim across.\n")
    if lake == "Wait":
        door = input("You have arrived at the island unharmed. There is a house with 3 doors.\n" \
        "One Red, One Yellow and one Blue. Which color do you choose?\n")
        if door == "Red":
            print("Burned by Fire. Game Over!")
        elif door == "Yellow":
            print("Congratulations! You win")
        elif door == "Blue":
            print("You have been eaten by beasts. Game Over!")
    else:
        print(" You have been attacked by a trout. Game Over!")

else:
    print("You have fallen into a hole. Game Over!")



print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
direction = input('You\'re at the cross road. Where do you want to go? \n Type "left" or "right"')

if direction == "left":
    choice = input("Choose one: swim or wait")
    if choice == "wait":
        door = input("Choose a door: red or blue or yellow")
        if door == "red":
            print("Burned by Fire. Game over.")
        elif door == "blue":
            print("Eaten by beasts. Game over.")
        elif door == "yellow":
            print("Treasure found. You won!")
        else:
            print("Game over.")
    else:
        print("You were attacked by a trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")








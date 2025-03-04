# import sys
# import random

# print("")

# playerChoice = input("Choose the One you like\n 1. For Rock🪨\n 2. For Scissors ✂️\n 3. For Paper📃\n\n")
# player = int(playerChoice)

# if player < 1 | player > 3:
#     sys.exit("You need to choose a number between 1 to 3")

# computer = random.randint(1,3)

# print(f"You choose {playerChoice} and Computer choose {computer}")

# if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
#     print("You won!")
# elif player == computer:
#     print("A Tie Happen")
# else:
#     print("You Lose")


import random

while True:
    print("\nRock-Paper-Scissors Game!")
    print("")

    playerChoice = input("Choose the One you like\n 1. For Rock🪨\n 2. For Scissors ✂️\n 3. For Paper📃\n 4. To Exit ❌\n\n")
    
    if playerChoice == "4":
        print("Thanks for playing! Goodbye! 👋")
        break  # Exits the loop
    
    if playerChoice not in ["1", "2", "3"]:
        print("Invalid choice! Please enter a number between 1 and 3.")
        continue  # Restart the loop

    player = int(playerChoice)
    computer = random.randint(1, 3)

    print(f"You chose {playerChoice} and the Computer chose {computer}")

    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("You won! 🎉")
    elif player == computer:
        print("A Tie Happened! 🤝")
    else:
        print("You Lose! 😢")


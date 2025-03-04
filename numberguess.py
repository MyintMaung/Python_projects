# import random

# computer = random.randint(1,100)


# attempts = 0

# while True:
#     guess_num = int(input("Enter a number between (1 to 100): "))
#     attempts += 1

#     if guess_num > computer:
#         print("The number is higher, try again")
#         print('')
#     elif guess_num < computer:
#         print("The number is lower, try again")
#         print('')
#     else:
#         print(f"You guess the correct number and the time you guess is {attempts} times.")
#         break












import random 

# computer_guess = random.randint(0, 100)

# attempts = 0

# while True:

#     guess = int(input("Guess the Number: "))
#     attempts += 1

#     if guess > computer_guess:
#         print("The number is higher, try again!")
#     elif guess < computer_guess:
#         print("The number is lower, try again")
#     else:
#         print(f"You choose the right number in {attempts} times, Good Job")
#         break
# print("\n")        


import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    attempt = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # When low == high, we know the number

        attempt += 1
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f'The computer guessed your number {guess} correctly in {attempt} attempts!')
            break  # Exit when correct
        else:
            print("Invalid input! Please enter 'H', 'L', or 'C'.")

computer_guess(1000)

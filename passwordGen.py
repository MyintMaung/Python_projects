import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

def generate_password():
    passwordLength = int(input("Enter the length of the password: "))

    random.shuffle(characters)

    password = []

    for x in range(passwordLength):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


option = input("Do you want to generate a password? (y/n): ")

if option == "y":
    generate_password()
elif option == "n":
    print("Goodbye!")
    option.quit()   
else:
    print("Invalid input!, Please try again")
    option.quit()   

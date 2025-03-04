
# First version
# while True:
    
#     num1 = float(input("Enter the first number you want: "))
#     num2 = float(input("Enter the second number you want: "))

#     print("Choose Operation")
#     print("1. Addition ")
#     print("2. Subtract ")
#     print("3. Multiply ")
#     print("4. Divide ")

#     choose = input("You can choose: 1, 2, 3, 4: ")

#     def add(x,y):
#         return x + y

#     def sub(x,y):
#         return x - y

#     def multiply(x,y):
#         return x * y

#     def division(x,y):
#         if y == 0:
#             return "Cannot divide by zero"
#         return x/y


#     if choose == "1":
#         print(f"Result: {add(num1, num2)}")
#     elif choose == "2":
#         print(f"Result: {sub(num1, num2)}")
#     elif choose == "3":
#         print(f"Result: {multiply(num1, num2)}")
#     elif choose == "4":
#         print(f"Result: {division(num1, num2)}")
#     else:
#         print("You can only chose from 1 to 4")

#     print("\n")




#Second Version

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    if y == 0:
        return "Cannot divide by zero"
    return x/y

while True:
    print("\nBasic Calculator")

    start = input("Enter \'A\' to start the program or \'B\'to quit: ").strip().upper()
    if start == 'B':
        print("\nThank you for using this calculator!")
        break
    elif start != 'A':
        print("\n❌ Invalid input! Please enter 'A' to start or 'B' to quit.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ you can only enter number, please try again!")

    print("Choose Operation")
    print("1. Addition ")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")

    choose = input("You can choose: 1, 2, 3, 4: ")

    

    if choose == "1":
        print(f"Result: {add(num1, num2)}")
    elif choose == "2":
        print(f"Result: {sub(num1, num2)}")
    elif choose == "3":
        print(f"Result: {multiply(num1, num2)}")
    elif choose == "4":
        print(f"Result: {division(num1, num2)}")
    else:
        print("You can only chose from 1 to 4")

    print("\n")
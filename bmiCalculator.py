while True:
    print("Pleas chosse from one!")
    a = input("Enter 'g' to start the calculator and 'q' to quit the calculator: ")

    if a == 'q':
        print("Thanks you for using this calculator!")
        break
    elif a != 'g':
        print("Invalid error you need to choose between 'g' and 'q'")
        continue
    
    def bmi_calculator(weight, height):
        bmi = (weight * 703) / (height * height)
        return bmi

    # Get user input and convert to float
    name = input("Enter Your name: ")
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))


    bmi = round(bmi_calculator(weight, height), 2)  # Limits to 2 decimal places


    if bmi < 18.5:
        print (f"{name}, the result is {bmi} you are underweight and health risk is minimal")
    elif bmi > 18.5 and bmi < 24.9:
        print(f"{name}, the result is {bmi} you are normal weight and health risk is minimal")
    elif bmi > 25 and bmi < 29.9:
        print(f"{name}, the result is {bmi} you are overweight and health risk is increased")
    elif bmi > 30 and bmi < 34.9:
        print(f"{name}, the result is {bmi} you are obese and health risk is high")
    elif bmi > 35 and bmi < 39.9:
        print(f"{name}, the result is {bmi} you are severely obese  and health risk is very heigh")
    elif bmi > 40:
        print(f"{name}, the result is {bmi} you are morbidly obese and health risk is extremely high")
    else:
        print("Invalid error, please Try again")
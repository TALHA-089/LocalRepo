def ValidateMainInput(choice):
    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
        return True
    else:
        print("\nInvalid Input. Please choose a valid operation.")
        return False

def ValidateOperandInput(operand):
    try:
        float(operand)  # Try converting to a number
        return True
    except ValueError:
        return False

def MainMenu():
    print("\nWelcome to Python Calculator Module\n")
    print("---- Choose an Operation ----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    MainMenu()
    choice = input("\nEnter choice (1-4): ")
    if ValidateMainInput(choice):
        if choice == "1":
            num1 = input("\nEnter first number: ")
            if ValidateOperandInput(num1):
                num1 = float(num1)
            else:
                print("\nInvalid input for first number.")
                continue
            num2 = input("\nEnter second number: ")
            if ValidateOperandInput(num2):
                num2 = float(num2)
            else:
                print("\nInvalid input for second number.")
                continue
            print("\nResult:")
            print(f"\n{num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            num1 = input("\nEnter first number: ")
            if ValidateOperandInput(num1):
                num1 = float(num1)
            else:
                print("\nInvalid input for first number.")
                continue
            num2 = input("\nEnter second number: ")
            if ValidateOperandInput(num2):
                num2 = float(num2)
            else:
                print("\nInvalid input for second number.")
                continue
            print("\nResult:")
            print(f"\n{num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            num1 = input("\nEnter first number: ")
            if ValidateOperandInput(num1):
                num1 = float(num1)
            else:
                print("\nInvalid input for first number.")
                continue
            num2 = input("\nEnter second number: ")
            if ValidateOperandInput(num2):
                num2 = float(num2)
            else:
                print("\nInvalid input for second number.")
                continue
            print("\nResult:")
            print(f"\n{num1} * {num2} = {num1 * num2}")
        elif choice == "4":  
            num1 = input("\nEnter first number: ")
            if ValidateOperandInput(num1):
                num1 = float(num1)
            else:
                print("\nInvalid input for first number.")
                continue
            num2 = input("\nEnter second number: ")
            if ValidateOperandInput(num2):
                num2 = float(num2)
            else:
                print("\nInvalid input for second number.")
                continue
            if num2 != 0:
                print("\nResult:")
                print(f"\n{num1} / {num2} = {num1 / num2}")
            else:
                print("\nError! Division by zero.")
        else:
            print("\nExiting the calculator. Goodbye!\n")
            break
    else:
        continue
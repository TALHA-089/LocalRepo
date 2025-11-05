print("Welcome to Python Calculator Module")
firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = firstNumber + secondNumber
elif operation == '-':
    result = firstNumber - secondNumber
elif operation == '*':
    result = firstNumber * secondNumber
elif operation == '/':
    if secondNumber != 0:
        result = firstNumber / secondNumber
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"
print(f"The result is: {result}")
print("Calculator.py execution completed.")
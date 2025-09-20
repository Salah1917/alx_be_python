num1 = int(input("Enter the first number:"))
num1 = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

if operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(num1 / num2)
elif operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
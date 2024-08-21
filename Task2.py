# Task - 2

# Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the calculation and display the result.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    operations = {
        '1': 'Addition',
        '2': 'Subtraction',
        '3': 'Multiplication',
        '4': 'Division'
    }

    print("\nSelect operation:")
    for key, value in operations.items():
        print(f"{key}. {value}")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in operations:
            return choice
        else:
            print("Invalid choice. Please select a valid operation.")

def calculate(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)

def main():
    print("Welcome to the Simple Calculator!")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()

        result = calculate(operation, num1, num2)

        print(f"\nThe result is: {result}\n")

        if input("Do you want to perform another calculation? (y/n): ").lower() != 'y':
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()

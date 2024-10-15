def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def calculator():
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Perform a calculation")
        print("2. Exit the program")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                operation = input("Enter the operation (+, -, *, /): ")

                if operation == '+':
                    print("Result:", add(num1, num2))
                elif operation == '-':
                    print("Result:", subtract(num1, num2))
                elif operation == '*':
                    print("Result:", multiply(num1, num2))
                elif operation == '/':
                    print("Result:", divide(num1, num2))
                else:
                    print("Error: Invalid operation.")
            except ValueError:
                print("Error: Invalid input.")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    calculator()

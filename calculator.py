def get_user_input():
    """Get user input for two numbers and an operation."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("\nAvailable operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = int(input("\nChoose an operation (1, 2, 3, 4): "))
        
        return num1, num2, operation
    
    except ValueError:
        print("Invalid input. Please enter a number or a valid operation choice.")
        return get_user_input()

def perform_operation(num1, num2, operation):
    """Perform the chosen mathematical operation."""
    if operation == 1:
        return num1 + num2, "+"
    elif operation == 2:
        return num1 - num2, "-"
    elif operation == 3:
        return num1 * num2, "*"
    elif operation == 4:
        if num2 != 0:
            return num1 / num2, "/"
        else:
            raise ZeroDivisionError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation choice.")

def main():
    num1, num2, operation = get_user_input()
    
    try:
        result, operator = perform_operation(num1, num2, operation)
        print(f"\n{num1} {operator} {num2} = {result}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()

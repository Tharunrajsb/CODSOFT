def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Simple Calculator")
    print("=================")
    
    try:
        num1 = float(input("Enter the first number: "))
        
        num2 = float(input("Enter the second number: "))
        
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = input("Enter the number of the operation (1/2/3/4): ").strip()
        
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        else:
            result = "Invalid choice. Please select a valid operation."
        
        print(f"\nResult: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numerical values only.")

if __name__ == "__main__":
    main()

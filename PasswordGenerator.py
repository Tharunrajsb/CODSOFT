import random
import string

def generate_password(length, complexity):
    if length < 1:
        return "Error: Password length must be at least 1."
    
    if complexity == 'low':
        characters = string.ascii_letters
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Error: Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    print("==================")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Length must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    while True:
        complexity = input("Choose complexity (low, medium, high): ").strip().lower()
        if complexity in {'low', 'medium', 'high'}:
            break
        print("Invalid choice. Please enter 'low', 'medium', or 'high'.")
    
    password = generate_password(length, complexity)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()

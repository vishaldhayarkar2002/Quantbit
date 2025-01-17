def validate_input():
    user_input = input("Enter a number: ")  

    try:
        number = int(user_input)  
        print(f"You entered: {number}")
    except ValueError:
        print("Invalid input. Please enter a number.")  # Handle invalid input

# Example usage
validate_input()

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def test_factorial():
    try:
        n = int(input("Enter the number to calculate the factorial: "))
        expected = int(input(f"Enter the expected factorial value for {n}: "))
        
        actual = factorial(n)
        if actual == expected:
            print(f"Test Passed for input {n}")
        else:
            print(f"Test Failed for input {n}. Expected: {expected}, Got: {actual}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the test
test_factorial()

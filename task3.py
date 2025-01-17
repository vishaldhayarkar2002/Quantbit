def find_second_largest(numbers):
    if len(numbers) < 2:
        return "The list must contain at least two distinct numbers."
    
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest  # Update second largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num  # Update second largest

    if second_largest == float('-inf'):
        return "There is no second largest number in the list."
    
    return second_largest

numbers = [10, 20, 4, 45, 99]
result = find_second_largest(numbers)
print("Second largest number:", result)

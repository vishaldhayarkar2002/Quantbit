def optimized_code(numbers):
    result = ""
    max_num = max(numbers)  # Get the maximum number in the list
    count_dict = {}  # Dictionary to store the counts of numbers

    for num in numbers:
        if num % 2 == 0:
            square = num * num
            result += f"Square of {num} is {square}\n"
        
        # Count occurrences of each number
        count_dict[num] = count_dict.get(num, 0) + 1

    result += f"\nMax number is {max_num}\n"
    result += "Number counts:\n"

    for num, count in count_dict.items():
        result += f"{num}: {count}\n"

    return result

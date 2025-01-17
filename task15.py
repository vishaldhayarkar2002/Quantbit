def optimized_code(numbers):
    result = []
    max_num = float('-inf')
    count_dict = {}

    for num in numbers:
        if num % 2 == 0:
            result.append(f"Square of {num} is {num * num}")
        
        max_num = max(max_num, num)  # Update max number
        count_dict[num] = count_dict.get(num, 0) + 1  # Count frequencies

    result.append(f"\nMax number is {max_num}")
    result.append("Number counts:")
    for num, count in count_dict.items():
        result.append(f"{num}: {count}")

    return "\n".join(result)

# Example usage
numbers = [1, 2, 2, 3, 4]
print(optimized_code(numbers))

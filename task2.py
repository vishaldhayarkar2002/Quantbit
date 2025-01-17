def sum_numbers_from_file(filename):
    total_sum = 0

    with open(filename, 'r') as file:
        for line in file:
            total_sum += int(line.strip())  # Add the integer value of each line

    return total_sum

# Example usage
filename = 'numbers.txt'
print("Sumof the numbers = ", sum_numbers_from_file(filename))  


def calculate_statistics(data):
    mean = sum(data) / len(data)  # Calculate mean
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    median = (sorted_data[n // 2] if n % 2 == 1 
              else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2)  # Calculate median
    
    frequency = {num: data.count(num) for num in set(data)}  # Count occurrences
    mode = max(frequency, key=frequency.get)  # Find mode

    return mean, median, mode

# Example usage
data = [1, 2, 2, 3, 4]
mean, median, mode = calculate_statistics(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # middle index
        
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Target not found


arr = [1, 3, 5, 7, 9]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")

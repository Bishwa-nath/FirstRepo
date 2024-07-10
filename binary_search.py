def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Target not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Target {target} found at index {result}")

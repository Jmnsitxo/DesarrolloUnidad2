def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
    
    
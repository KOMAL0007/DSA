def binary_search_first_occurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1  
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid  
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    return result

# Example usage:
arr = [3,6,4,8,8,16,13,4,4]
key = 4

result = binary_search_first_occurrence(arr, key)

if result != -1:
    print("First occurrence of element at index", result)
else:
    print("Element not found")

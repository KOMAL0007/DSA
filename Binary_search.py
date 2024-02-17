def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid  
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # if match is not found
  
arr = [2, 4, 6, 8, 10, 12]
key = 8

result = binary_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

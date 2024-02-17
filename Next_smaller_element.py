def find_next_smaller_element(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1  
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            result = mid  
            high = mid - 1
            
    return arr[result] if result != -1 else None

arr = [10,22,33,44,55,56]
target = 33

next_smaller = find_next_smaller_element(arr, target)

if next_smaller is not None:
    print("Next smaller element greater than", target, "is", next_smaller)
else:
    print("No smaller element greater than", target, "found in the array")

def find_next_greater_element(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1  
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            result = mid  
            high = mid - 1
        else:
            low = mid + 1
            
    return arr[result] if result != -1 else None

arr = [11,12,13,14,16,17]
target = 12

next_greater = find_next_greater_element(arr, target)

if next_greater is not None:
    print("Next greater element greater than", target, "is", next_greater)
else:
    print("No greater element greater than", target, "found in the array")

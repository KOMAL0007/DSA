def find_last_repetition(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

arr = [2, 4, 6, 8, 10, 10, 10, 12]
target = 10

index = find_last_repetition(arr, target)

if index != -1:
    print(f"The last repetition of target is at index {index}")
else:
    print(f"Repetition of target target not found in the list")

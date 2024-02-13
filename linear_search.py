def linear_search(arr, key):
    index = 0
    while index < len(arr):
        if arr[index] == key:
            return index 
        index += 1
    return -1  

arr = [2,4,6,7,13,16]
key = 7

result = linear_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

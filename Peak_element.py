def peak_element(arr):
    n = len(arr)
    if n == 1: 
        return arr[0]

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]  
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

arr = [6, 13, 7, -5, 4, 3, 19]
peak_element = find_peak_element(arr)
print("Peak element in the array is:", peak_element)

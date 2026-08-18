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
    return -1 
n = int(input("Enter number of elements: ")) 
arr = [] 
for i in range(n): 
    arr.append(int(input("Enter element: "))) 
key = int(input("Enter element to search: ")) 
if arr == sorted(arr): 
    print("Array is sorted.")     
    result = binary_search(arr, key) 
    if result != -1: 
        print("Element found at index", result) 
    else: 
        print("Element not found.") 
else: 
    print("Array is unsorted.") 
    print("Binary search cannot be performed correctly on an unsorted array.")     
    arr.sort() 
    print("Sorted array:", arr) 
    result = binary_search(arr, key) 
    if result != -1: 
        print("Element found at index", result, "after sorting.") 
    else: 
        print("Element not found.") 

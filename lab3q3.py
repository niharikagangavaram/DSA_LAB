def selection_sort(arr): 
    n = len(arr) 
    for i in range(n): 
        min_idx = i 
        for j in range(i + 1, n): 
            if arr[j] < arr[min_idx]: 
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
user_input = input("Enter numbers separated by spaces: ") 
data = [int(x) for x in user_input.split()] 
print("\nOriginal array:", data) 
selection_sort(data) 
print("Sorted array in ascending order:", data) 

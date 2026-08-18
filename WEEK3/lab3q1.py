def bubble_sort(arr): 
    n = len(arr)
    for i in range(n): 
        swapped = False 
        for j in range(0, n - i - 1): 
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                swapped = True 
        if not swapped: 
            break 
user_input = input("Enter numbers separated by spaces: ") 
numbers_list = [int(x) for x in user_input.split()]
print(f"\nOriginal list: {numbers_list}")
bubble_sort(numbers_list) 
print(f"Sorted list:   {numbers_list}") 

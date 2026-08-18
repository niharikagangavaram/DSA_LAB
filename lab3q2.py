def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i - 1 
        while j >= 0 and arr[j] > key: 
            arr[j + 1] = arr[j] 
            j -= 1 
        arr[j + 1] = key 
if __name__ == "__main__": 
    user_input = input("Enter the elements to sort (separated by spaces): ") 
    numbers = [int(x) for x in user_input.split()] 
    print("\nOriginal array:", numbers) 
    insertion_sort(numbers) 
    print("Sorted array:  ", numbers) 

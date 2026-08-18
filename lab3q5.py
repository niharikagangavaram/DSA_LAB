def quick_sort(arr): 
    if len(arr) <= 1: 
        return arr 
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 
    return quick_sort(left) + middle + quick_sort(right) 
if __name__ == "__main__": 
    print("--- Quick Sort Program ---") 
    user_input = input("Enter elements separated by spaces: ") 
    try: 
        elements = [int(item) for item in user_input.split()]  
        print(f"\nOriginal List: {elements}") 
        sorted_elements = quick_sort(elements) 
        print(f"Sorted List:   {sorted_elements}") 
    except ValueError: 
        print("Error: Please ensure you only enter numbers separated by spaces.") 

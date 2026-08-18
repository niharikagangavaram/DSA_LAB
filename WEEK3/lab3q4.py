def merge_sort(arr): 
    if len(arr) <= 1: 
        return arr 
    mid = len(arr) // 2 
    left_half = arr[:mid] 
    right_half = arr[mid:] 
    left_sorted = merge_sort(left_half) 
    right_sorted = merge_sort(right_half) 
    return merge(left_sorted, right_sorted) 
def merge(left, right): 
    sorted_list = [] 
    i = j = 0 
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            sorted_list.append(left[i]) 
            i += 1 
        else: 
            sorted_list.append(right[j]) 
            j += 1 
    sorted_list.extend(left[i:]) 
    sorted_list.extend(right[j:])     
    return sorted_list 
if __name__ == "__main__": 
    print("--- Merge Sort Program ---") 
    try: 
        user_input = input("Enter the elements separated by spaces: ") 
        elements = [float(x) if '.' in x else int(x) for x in user_input.split()] 
        if not elements: 
            print("The list is empty. Nothing to sort.") 
        else: 
            print(f"\nOriginal List: {elements}") 
            sorted_elements = merge_sort(elements) 
            print(f"Sorted List:   {sorted_elements}") 
    except ValueError: 
        print("Invalid input! Please enter only valid integers or numbers separated by spaces.") 

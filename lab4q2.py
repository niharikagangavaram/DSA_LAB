def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                p = i + 1
                quick_sort(arr, low, p - 1)
                quick_sort(arr, p + 1, high)
# Input from user
arr = list(map(int, input("Enter elements separated by spaces: ").split()))
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

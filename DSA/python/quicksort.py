def quicksort(arr):
    if len(arr) <= 1:
        return arr  
    
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    numbers = [33, 10, 55, 71, 29, 3, 18]
    print("Original array:", numbers)
    sorted_numbers = quicksort(numbers)
    print("Sorted array:", sorted_numbers)

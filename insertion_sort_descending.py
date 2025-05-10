def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1        
        # Move elements that are smaller than key forward
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
if __name__ == "__main__":
    numbers = [12, 4, 5, 3, 8, 7]
    print("Original array:", numbers)
    insertion_sort_descending(numbers)
    print("Sorted array in decreasing order:", numbers)

# the following is output we get after running the codes above. 
    
# Original array: [12, 4, 5, 3, 8, 7]
# Sorted array in decreasing order: [12, 8, 7, 5, 4, 3]

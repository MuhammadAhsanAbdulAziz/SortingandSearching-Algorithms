def bubbleSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        no_of_swaps = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # Swapping positions
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # Update the swap counter
                no_of_swaps += 1

        # Zero swaps mean array is now sorted           
        if no_of_swaps == 0:
            return arr
        else:
            return bubbleSort(arr)


print(bubbleSort([9,88,77,66,55,44,33,22,11]))
        

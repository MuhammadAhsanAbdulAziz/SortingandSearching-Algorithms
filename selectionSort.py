def selectionSort(arr):
    length = len(arr)
    # Base case
    if length <= 1:
        return arr
    else:
        # Assume first num is the lowest
        lowest = arr[0]
        for i in range(length-1):
            # Set new lowest if found in further nums
            if arr[i+1] > lowest:
                lowest = arr[i+1]

        arr.remove(lowest)
        # Find lowest in remaining unsorted arr
        return [lowest] + selectionSort(arr)
        
    
            
print(selectionSort([3, 5, 8, 4, 1, 9, -2]))

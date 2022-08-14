def quickSort(arr):
     # Base Case
     if len(arr) <= 1:
        return arr
     else:
        # Choosing last num as pivot and removing it from arr
        pivot = arr.pop()
        # Lower and Higher sublists
        lower_arr = []
        higher_arr = []
                            
        for num in arr:
            if num < pivot:
                lower_arr.append(num)
            else:
                higher_arr.append(num)

        # Applying quick sort on both sublists
        # and returning it with pivot
        return quickSort(lower_arr) + [pivot] + quickSort(higher_arr)
     

print(quickSort([2, 1, 6, 10, 4, 1, 3, 9, 7]))

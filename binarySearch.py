def binarySearch(num, arr, start, end):
    if end >= start:
        mid = (end + start)//2
        if num == arr[mid]:
            return mid
        if num > arr[mid]:
            start = mid+1
            return binarySearch(num, arr, start, end)
        else:
            end = mid-1
            return binarySearch(num, arr, start, end)

    else:
        return -1

lst = [1,3,4,6,7,8,9]
print(binarySearch(-1, lst, 0, len(lst)-1))

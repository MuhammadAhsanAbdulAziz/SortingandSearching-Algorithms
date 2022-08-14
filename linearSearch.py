def linearSearch(num, arr):
    for i in range(len(arr)):
        if arr[i] == num:
            return i

    return -1


print(linearSearch(0, [0,2,0,9,4,5,1]))

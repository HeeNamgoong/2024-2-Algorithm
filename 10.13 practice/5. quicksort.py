def quicksort(arr, l, r):
    if l+1 >= r:
        return
    
    p = partition(arr, l, r)

    quicksort(arr, l, p)
    quicksort(arr, p+1, r)

    return arr


def partition(arr, l, r):
    p = arr[r-1]
    i = l
    for j in range(l, r):
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i - 1


print(quicksort([4, 3, 9, 8, 7, 2, 5, 6], 0, 8))
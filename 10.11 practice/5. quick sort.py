def quick_sort(arr, l, r):
    if l+1 >= r:
        return
    
    p = partition(arr, l, r)

    quick_sort(arr, l, p)
    quick_sort(arr, p+1, r)

    return arr


def partition(arr, l, r):
    p = arr[r-1] # pivot

    i = l
    for j in range(l, r):
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    return i - 1




print(quick_sort([4, 3, 9, 8, 7, 6, 5, 2], 0, 8))

def quickselect(arr, l, r, i):
    if l+1 >= r:
        return arr[l]
    
    p = partition(arr, l, r)
    
    if i == p:
        return arr[p]
    elif i < p:
        return quickselect(arr, l, p, i)
    elif i > p:
        return quickselect(arr, p+1, r, i)


def partition(arr, l, r):
    p = arr[r-1]
    i = l
    for j in range(l, r):
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i - 1


print(quickselect([11, 1, 9, 2, 7, 13, 12, 8, 6, 3, 10], 0, 11, 3))

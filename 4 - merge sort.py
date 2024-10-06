def mergesort(arr, l, r):
    if l + 1 >= r:
        return
    m = (l + r) // 2
    mergesort(arr, l, m)
    mergesort(arr, m, r)
    merge(arr, l, m, r)

    print(arr)

def merge(arr, l, m, r):
    tmp = arr[l:r]
    i, j, k = 0, m-l, l
    while i < (m-l) and j < (r-l):
        if tmp[i] < tmp[j]:
            arr[k] = tmp[i]
            i += 1
        else:
            arr[k] = tmp[j]
            j += 1
        k += 1
    
    while i < (m-l):
        arr[k] = tmp[i]
        i += 1
        k += 1
    while j < (r-l):
        arr[k] = tmp[j]
        j += 1
        k += 1
        
mergesort([3, 2, 4, 1], 0, 4)

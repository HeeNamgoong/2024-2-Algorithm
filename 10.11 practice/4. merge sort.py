def merge_sort(arr, l, r):
    if l + 1 >= r:
        return
    
    m = (l+r) // 2

    merge_sort(arr, l, m)
    merge_sort(arr, m, r)
    merge(arr, l, m, r)

    return arr

def merge(arr, l, m, r):
    tmp = arr[l:r]

    i, j, k = 0, m-l, l

    while i < (m-l) and j < (r-l): # 매번 j 범위 (r-l)을 (r-m)이라고 한다. 조심하자
        if tmp[i] < tmp[j]:
            arr[k] = tmp[i]
            i += 1; k += 1
        else:
            arr[k] = tmp[j]
            j += 1; k += 1

    while i < (m-l):
        arr[k] = tmp[i]
        i += 1; k += 1

    while j < (r-l):
        arr[k] = tmp[j]
        j += 1; k += 1


    



print(merge_sort([4, 3, 9, 8, 7, 6, 5, 2], 0, 8))

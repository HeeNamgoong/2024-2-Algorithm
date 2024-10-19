def merge_sort(arr, l, r):
    if l + 1 >= r:
        return
    
    m = (l+r) // 2
    print(arr[l:m], "(l, m)", (l, m))
    print(arr[m:r], "(m, r)", (m, r))
    print()
    merge_sort(arr, l, m)
    merge_sort(arr, m, r)
    merge(arr, l, m, r)
    return arr

def merge(arr, l, m, r):
    tmp = arr[l:r]

    i, j, k = 0, m-l, l
    while i < (m-l) and j < (r-l):
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
    print("before merge", tmp)
    print("*after merge", arr[l:r])
    print()


print(merge_sort([4, 3, 8, 7, 6, 5, 2, 1], 0, 8))

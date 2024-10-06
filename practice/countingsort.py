def counting_sort(arr, r):
    cnts = [0] * r
    n = len(arr)

    for x in arr:
        cnts[x] += 1
    
    for i in range(1, r):
        cnts[i] += cnts[i-1]
    
    sorted = [0] * n
    for x in reversed(arr):
        cnts[x] -= 1
        sorted[cnts[x]] = x
    arr[:] = sorted

    return arr


print(counting_sort([5, 1, 5, 1, 0, 4, 1, 2, 4, 5], 6))
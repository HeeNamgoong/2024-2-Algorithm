def quick_sort(arr, l, r):
    if l+1 >= r:
        return
    
    p = partition(arr, l, r)
    quick_sort(arr, l, p)
    quick_sort(arr, p+1, r)

    return arr
    


def partition(arr, l, r):
    p = arr[r-1]

    i = l # 0부터라 했는데 0이 아니라 partition 처음 시작하는 부분은 l 입니다!!!
    for j in range(l, r): # 아 범위 좀 조심하랑께?? -> len(arr) 이랬음;; ㅋㅋ
        if arr[j] <= p: # = 꼭 붙여야합니다. pivot이랑 같으면 어쨌든 큰 수들보단 작은 수라 앞으로 가기위해 swap 되어야함.
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i - 1 # pivot return 해줍시다



print(quick_sort([4, 3, 9, 8, 7, 2, 5, 6], 0, 8))
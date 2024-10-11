def heap_sort(arr):
    n = len(arr)
    build_heap(arr, n)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(0, arr, i) ### 다시

    return arr

def sift_down(i, arr, n):
    c = 2*i + 1

    while c < n:
        if c+1 < n and arr[c] < arr[c+1]:
            c = c + 1
        if arr[i] > arr[c]:
            break # best case의 최적 시간 복잡도를 위해 break를 해주자!! 까먹고 안 함
        arr[i], arr[c] = arr[c], arr[i]
        i = c
        c = 2*i + 1

def build_heap(arr, n):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        sift_down(i, arr, n)

print(heap_sort([4, 3, 9, 8, 7, 6, 5, 2]))
